from pathlib import Path
import shutil
import platform

def get_host_os():
    os_name = platform.system().lower()
    if "windows" in os_name:
        return "windows"
    elif "linux" in os_name or "darwin" in os_name:
        return "linux"
    return "unknown"

def generate_setup(project_type, dest_path):
    os_type = get_host_os()

    # Get the installed path of this file
    base_dir = Path(__file__).resolve().parent
    template_path = base_dir / "templates" / project_type / os_type

    print(f"Looking for templates in: {template_path}")

    if not template_path.exists():
        print(f"No templates found for '{project_type}' on '{os_type}'.")
        return

    for file in template_path.iterdir():
        if file.is_file():
            shutil.copy(file, dest_path)
