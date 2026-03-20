import subprocess
import os
from typing import Dict, Any
from langchain_core.tools import tool

@tool
def run_project_tests(path: str = "app/tests") -> Dict[str, Any]:
    """
    Executes pytest on the specified path and returns the results.
    Useful for validating generated code.
    """
    try:
        # Prepare environment with PYTHONPATH
        env = os.environ.copy()
        env["PYTHONPATH"] = f".{os.pathsep}{env.get('PYTHONPATH', '')}"

        # Run pytest via subprocess
        result = subprocess.run(
            ["pytest", path, "-v", "--tb=short"],
            capture_output=True,
            text=True,
            timeout=60,
            env=env
        )
        
        return {
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "passed": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "Tests timed out."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
