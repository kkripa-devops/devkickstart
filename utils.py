import os
import shutil

def detect_project_type(path):
    files = os.listdir(path)
    if "package.json" in files:
        return "node"
    elif "requirements.txt" in files or "pyproject.toml" in files:
        return "python"
    else:
        return None

def generate_setup(project_type, dest_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # where devkickstart lives
    template_path = os.path.join(base_dir, "templates", project_type)

    if not os.path.exists(template_path):
        print(f"❌ Template path not found: {template_path}")
        return

    for filename in os.listdir(template_path):
        full_file = os.path.join(template_path, filename)
        shutil.copy(full_file, dest_path)
