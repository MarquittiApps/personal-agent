import os
import ast
from typing import List, Dict, Any
from langchain_core.tools import tool

@tool
def map_project_structure(root_dir: str = ".") -> Dict[str, Any]:
    """
    Scans the project directory and returns a structured map of folders, files, 
    classes, and functions to help the agent understand the codebase layout.
    """
    project_map = {
        "directories": {},
        "files": []
    }
    
    exclude_dirs = {".git", "__pycache__", "node_modules", "venv", ".venv", "dist", "build"}
    
    for root, dirs, files in os.walk(root_dir):
        # Filter excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == ".":
            current_level = project_map["directories"]
        else:
            path_parts = rel_path.split(os.sep)
            temp = project_map["directories"]
            for part in path_parts:
                if part not in temp:
                    temp[part] = {"files": [], "subdirs": {}}
                temp = temp[part]["subdirs"]
            current_level = temp # This is slightly flawed for direct file access, let's simplify
            
    # Simplified approach for better clarity
    simple_map = {"structure": {}}
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        rel_path = os.path.relpath(root, root_dir)
        
        py_files = [f for f in files if f.endswith(".py")]
        ts_files = [f for f in files if f.endswith(".tsx") or f.endswith(".ts")]
        
        file_info = []
        for f in py_files:
            file_path = os.path.join(root, f)
            info = {"name": f, "type": "python", "definitions": _parse_python_file(file_path)}
            file_info.append(info)
            
        for f in ts_files:
            file_info.append({"name": f, "type": "typescript"})
            
        if rel_path == ".":
            simple_map["structure"]["root"] = file_info
        else:
            simple_map["structure"][rel_path.replace(os.sep, "/")] = file_info
            
    return simple_map

def _parse_python_file(file_path: str) -> List[Dict[str, Any]]:
    """Extracts function and class names from a Python file using AST."""
    definitions = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
            
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                definitions.append({"type": "function", "name": node.name})
            elif isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                definitions.append({"type": "class", "name": node.name, "methods": methods})
    except Exception as e:
        definitions.append({"type": "error", "message": str(e)})
        
    return definitions
