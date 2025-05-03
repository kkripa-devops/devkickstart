import os
import sys
from utils import detect_project_type, generate_setup

def main():
    print("Welcome to DevKickstart!")
    project_path = os.getcwd()
    
    project_type = detect_project_type(project_path)
    if not project_type:
        print("Could not detect project type. Supported: Python, Node.js.")
        sys.exit(1)

    print(f"Detected project type: {project_type}")
    generate_setup(project_type, project_path)
    print("Dev environment setup generated successfully!")

if __name__ == "__main__":
    main()
