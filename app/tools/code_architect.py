import os
import shutil
from typing import Optional, Dict, Any
from langchain_core.tools import tool

CRITICAL_FILES = {"app/main.py", "app/core/graph.py", ".env", "docker-compose.yml"}

@tool
def write_project_file(file_path: str, content: str, reason: str) -> Dict[str, Any]:
    """
    Creates or updates a file in the project. 
    It automatically creates backups for critical system files.
    """
    try:
        # Security: Prevent escaping the workspace
        abs_path = os.path.abspath(file_path)
        if not abs_path.startswith(os.getcwd()):
            return {"status": "error", "message": "Cannot write files outside project directory."}

        # Backup for critical files
        if file_path in CRITICAL_FILES and os.path.exists(file_path):
            backup_path = f"{file_path}.bak"
            shutil.copy2(file_path, backup_path)
            backup_msg = f" Backup created at {backup_path}."
        else:
            backup_msg = ""

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "success",
            "message": f"File {file_path} written successfully.{backup_msg}",
            "reason": reason
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@tool
def read_project_file(file_path: str) -> str:
    """Reads the content of a project file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"
