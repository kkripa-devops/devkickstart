# Copyright (c) 2025 Radhakrishnan Krishna Kripa
# Licensed under the MIT License

import os
import shutil
from pathlib import Path
import platform

def get_host_os():
    os_name = platform.system().lower()
    if "windows" in os_name:
        return "windows"
    elif "linux" in os_name or "darwin" in os_name:
        return "linux"
    return "unknown"

def detect_project_type(path):
    files = os.listdir(path)
    if "package.json" in files:
        return "node"
    elif "requirements.txt" in files or "pyproject.toml" in files:
        return "python"
    elif any(f.endswith(".csproj") or f.endswith(".sln") for f in files):
        return "dotnet"
    elif any(f.endswith(".cpp") or f.endswith(".h") for f in files):
        return "cpp"
    elif "CMakeLists.txt" in files:
        return "cmake"
    else:
        return None

def generate_setup(project_type, dest_path, os_type, dry_run=False):
    base_dir = Path(__file__).resolve().parent
    template_path = base_dir / "templates" / project_type / os_type

    print(f"Looking for templates in: {template_path}")
    if not template_path.exists():
        print(f"No templates found for '{project_type}' on '{os_type}'.")
        return

    # Always write into a .devcontainer folder at the project root
    dest_root = Path(dest_path)
    target_dir = dest_root / ".devcontainer"
    if dry_run:
        print(f"Would create: {target_dir}")
    else:
        target_dir.mkdir(parents=True, exist_ok=True)
    print(f"Writing to: {target_dir}")

    for file in template_path.iterdir():
        if file.is_file():
            dst = target_dir / file.name
            if dry_run:
                print(f"Would copy: {file.name} → {dst}")
            else:
                # copy2 preserves mtime where available
                shutil.copy2(file, dst)
                # Log path relative to project root so it reads as ".devcontainer/…"
                try:
                    rel = dst.relative_to(dest_root)
                except ValueError:
                    rel = dst
                print(f"Copied: {rel}")
