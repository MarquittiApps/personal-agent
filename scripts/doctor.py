import sys
import subprocess
import os
import platform
import socket
import requests

# Requirements settings
MIN_PYTHON_VERSION = (3, 10)
MIN_NODE_VERSION = 18

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_step(message):
    print(f"{Colors.BLUE}==>{Colors.END} {Colors.BOLD}{message}{Colors.END}")

def print_ok(message):
    print(f"  {Colors.GREEN}✓{Colors.END} {message}")

def print_warn(message, suggestion=None):
    print(f"  {Colors.YELLOW}⚠{Colors.END} {message}")
    if suggestion:
        print(f"    {Colors.YELLOW}Suggestion:{Colors.END} {suggestion}")

def print_error(message, suggestion=None):
    print(f"  {Colors.RED}✗{Colors.END} {message}")
    if suggestion:
        print(f"    {Colors.YELLOW}Suggestion:{Colors.END} {suggestion}")

def check_python_version():
    print_step("Checking Python version...")
    current_version = sys.version_info
    if current_version >= MIN_PYTHON_VERSION:
        print_ok(f"Python {current_version.major}.{current_version.minor}.{current_version.micro} detected.")
        return True
    else:
        print_error(
            f"Insufficient Python version ({current_version.major}.{current_version.minor}).",
            f"Please install Python {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} or higher."
        )
        return False

def check_node_version():
    print_step("Checking Node.js version...")
    try:
        output = subprocess.check_output(['node', '--version'], stderr=subprocess.STDOUT).decode().strip()
        version_str = output.lstrip('v')
        major_version = int(version_str.split('.')[0])
        
        if major_version >= MIN_NODE_VERSION:
            print_ok(f"Node.js {output} detected.")
            return True
        else:
            print_error(
                f"Insufficient Node.js version ({output}).",
                f"Please install Node.js v{MIN_NODE_VERSION} or higher."
            )
            return False
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Node.js not found in PATH.", "Install Node.js from https://nodejs.org/")
        return False

def check_directories():
    print_step("Checking directories and dependencies...")
    
    # Check node_modules
    if os.path.isdir("web/node_modules") or os.path.isdir("node_modules"):
        print_ok("node_modules directory found.")
    else:
        print_warn("node_modules directory not found.", "Run 'npm install' in the 'web/' directory to install frontend dependencies.")

    # Check Python venv
    venv_found = False
    for venv_dir in [".venv", "venv", "env"]:
        if os.path.isdir(venv_dir):
            print_ok(f"Python virtual environment detected ({venv_dir}).")
            venv_found = True
            break
    
    if not venv_found:
        print_warn("Python virtual environment (.venv) not found.", "Run 'python -m venv .venv' to create one.")

def check_env_files():
    print_step("Checking configuration files...")
    
    env_exists = os.path.isfile(".env")
    example_exists = os.path.isfile(".env.example")
    
    if env_exists:
        print_ok(".env file found.")
    else:
        if example_exists:
            print_error(".env file missing.", "Copy the .env.example file to .env and fill in the variables.")
        else:
            print_error(".env and .env.example files missing.", "Check the documentation to configure the environment.")
    return env_exists

def check_service_port(port, service_name, suggestion=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect(("localhost", port))
            print_ok(f"{service_name} service detected on port {port}.")
            return True
        except (socket.timeout, ConnectionRefusedError):
            print_error(f"{service_name} service not found on port {port}.", suggestion)
            # Try to start via docker compose if it's postgres
            if port == 5432:
                print_step("Attempting to start the database via Docker Compose...")
                try:
                    subprocess.run(["docker", "compose", "up", "-d"], check=True)
                    print_ok("Docker Compose started successfully.")
                    return True
                except Exception as e:
                    print_error("Failed to start via Docker Compose.", "Make sure Docker is installed and running on your system.")
            return False

def check_ollama_health():
    print_step("Checking Ollama API...")
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            print_ok("Ollama API is responding correctly.")
            return True
        else:
            print_warn(f"Ollama returned status {response.status_code}.")
            return False
    except requests.exceptions.RequestException:
        print_error("Ollama API is not accessible.", "Make sure Ollama is running.")
        return False

def check_db_connection():
    print_step("Testing database connection...")
    try:
        # Try dynamic import to avoid error if psycopg2 is not installed
        try:
            from app.core.database import get_db_connection
        except ImportError:
            # If application module import fails, try generic connection if envs exist
            import psycopg2
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', '5432'),
                dbname=os.getenv('DB_NAME', 'personal_ai_core'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', 'yourpassword')
            )
            conn.close()
            print_ok("PostgreSQL connection established successfully.")
            return True
            
        conn = get_db_connection()
        conn.close()
        print_ok("PostgreSQL connection established successfully.")
        return True
    except Exception as e:
        print_error(f"Database connection failed: {e}", "Check if PostgreSQL is running and if the credentials in .env are correct.")
        return False

def main():
    print(f"{Colors.HEADER}{Colors.BOLD}Personal AI Core - Local Environment Diagnostic{Colors.END}\n")
    
    # 1. Runtimes
    runtime_results = [
        check_python_version(),
        check_node_version()
    ]
    
    # 2. Configs
    env_ok = check_env_files()
    check_directories()
    
    # 3. Services (if basic configs are OK)
    service_results = []
    if env_ok:
        print("\n")
        service_results.append(check_service_port(5432, "PostgreSQL", "Start PostgreSQL or the Docker container."))
        service_results.append(check_ollama_health())
        
        # 4. Deep Connection
        if service_results[0]: # If Postgres port is open
            service_results.append(check_db_connection())
    
    print("\n")
    all_ok = all(runtime_results) and env_ok and all(service_results)
    
    if all_ok:
        print(f"{Colors.GREEN}{Colors.BOLD}All set! Your environment is configured and services are active.{Colors.END}")
        sys.exit(0)
    else:
        print(f"{Colors.RED}{Colors.BOLD}Some issues were detected. Check the messages above.{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
