import sys
import subprocess
import os
import platform

# Configurações de requisitos
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
        print(f"    {Colors.YELLOW}Sugestão:{Colors.END} {suggestion}")

def print_error(message, suggestion=None):
    print(f"  {Colors.RED}✗{Colors.END} {message}")
    if suggestion:
        print(f"    {Colors.YELLOW}Sugestão:{Colors.END} {suggestion}")

def check_python_version():
    print_step("Verificando versão do Python...")
    current_version = sys.version_info
    if current_version >= MIN_PYTHON_VERSION:
        print_ok(f"Python {current_version.major}.{current_version.minor}.{current_version.micro} detectado.")
        return True
    else:
        print_error(
            f"Versão do Python insuficiente ({current_version.major}.{current_version.minor}).",
            f"Instale o Python {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} ou superior."
        )
        return False

def check_node_version():
    print_step("Verificando versão do Node.js...")
    try:
        output = subprocess.check_output(['node', '--version'], stderr=subprocess.STDOUT).decode().strip()
        version_str = output.lstrip('v')
        major_version = int(version_str.split('.')[0])
        
        if major_version >= MIN_NODE_VERSION:
            print_ok(f"Node.js {output} detectado.")
            return True
        else:
            print_error(
                f"Versão do Node.js insuficiente ({output}).",
                f"Instale o Node.js v{MIN_NODE_VERSION} ou superior."
            )
            return False
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Node.js não encontrado no PATH.", "Instale o Node.js em https://nodejs.org/")
        return False

def check_directories():
    print_step("Verificando diretórios e dependências...")
    
    # Check node_modules
    if os.path.isdir("node_modules"):
        print_ok("Diretório node_modules encontrado.")
    else:
        print_warn("Diretório node_modules não encontrado.", "Execute 'npm install' para instalar as dependências do frontend.")

    # Check Python venv
    venv_found = False
    for venv_dir in [".venv", "venv", "env"]:
        if os.path.isdir(venv_dir):
            print_ok(f"Ambiente virtual Python detectado ({venv_dir}).")
            venv_found = True
            break
    
    if not venv_found:
        print_warn("Ambiente virtual Python (.venv) não encontrado.", "Execute 'python -m venv .venv' para criar um.")

def check_env_files():
    print_step("Verificando arquivos de configuração...")
    
    env_exists = os.path.isfile(".env")
    example_exists = os.path.isfile(".env.example")
    
    if env_exists:
        print_ok("Arquivo .env encontrado.")
    else:
        if example_exists:
            print_error("Arquivo .env ausente.", "Copie o arquivo .env.example para .env e preencha as variáveis.")
        else:
            print_error("Arquivo .env e .env.example ausentes.", "Verifique a documentação para configurar o ambiente.")
    return env_exists

import socket
import requests

def check_service_port(port, service_name, suggestion=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect(("localhost", port))
            print_ok(f"Serviço {service_name} detectado na porta {port}.")
            return True
        except (socket.timeout, ConnectionRefusedError):
            print_error(f"Serviço {service_name} não encontrado na porta {port}.", suggestion)
            # Tenta subir via docker compose se for o postgres
            if port == 5432:
                print_step("Tentando iniciar o banco de dados via Docker Compose...")
                try:
                    subprocess.run(["docker", "compose", "up", "-d"], check=True)
                    print_ok("Docker Compose iniciado com sucesso.")
                    return True
                except Exception as e:
                    print_error("Falha ao iniciar via Docker Compose.", "Certifique-se que o Docker está instalado e em execução no seu sistema.")
            return False

def check_ollama_health():
    print_step("Verificando Ollama API...")
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            print_ok("Ollama API está respondendo corretamente.")
            return True
        else:
            print_warn(f"Ollama retornou status {response.status_code}.")
            return False
    except requests.exceptions.RequestException:
        print_error("Ollama API não está acessível.", "Certifique-se de que o Ollama está rodando.")
        return False

def check_db_connection():
    print_step("Testando conexão com o Banco de Dados...")
    try:
        # Tenta importar dinamicamente para evitar erro se psycopg2 não estiver instalado
        try:
            from app.core.database import get_db_connection
        except ImportError:
            # Se não conseguir importar o módulo do app, tenta conexão genérica se as envs existirem
            import psycopg2
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', '5432'),
                dbname=os.getenv('DB_NAME', 'personal_ai_core'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', 'yourpassword')
            )
            conn.close()
            print_ok("Conexão com PostgreSQL estabelecida com sucesso.")
            return True
            
        conn = get_db_connection()
        conn.close()
        print_ok("Conexão com PostgreSQL estabelecida com sucesso.")
        return True
    except Exception as e:
        print_error(f"Falha na conexão com o banco de dados: {e}", "Verifique se o PostgreSQL está rodando e se as credenciais no .env estão corretas.")
        return False

def main():
    print(f"{Colors.HEADER}{Colors.BOLD}Personal AI Core - Diagnóstico de Ambiente Local{Colors.END}\n")
    
    # 1. Runtimes
    runtime_results = [
        check_python_version(),
        check_node_version()
    ]
    
    # 2. Configs
    env_ok = check_env_files()
    check_directories()
    
    # 3. Services (se as configs básicas estiverem OK)
    service_results = []
    if env_ok:
        print("\n")
        service_results.append(check_service_port(5432, "PostgreSQL", "Inicie o PostgreSQL ou o container Docker."))
        service_results.append(check_ollama_health())
        
        # 4. Deep Connection
        if service_results[0]: # Se a porta do Postgres está aberta
            service_results.append(check_db_connection())
    
    print("\n")
    all_ok = all(runtime_results) and env_ok and all(service_results)
    
    if all_ok:
        print(f"{Colors.GREEN}{Colors.BOLD}Tudo pronto! Seu ambiente está configurado e os serviços estão ativos.{Colors.END}")
        sys.exit(0)
    else:
        print(f"{Colors.RED}{Colors.BOLD}Alguns problemas foram detectados. Verifique as mensagens acima.{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
