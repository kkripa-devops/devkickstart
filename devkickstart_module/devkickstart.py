# Copyright (c) 2025 Radhakrishnan Krishna Kripa
# Licensed under the MIT License

import os
import sys
from .utils import detect_project_type, generate_setup

def main():
    print("Welcome to DevKickstart!")
    project_path = os.getcwd()

    project_type = detect_project_type(project_path)
    if not project_type:
        print("Could not detect project type. Supported: Node, Python, .NET, C++, CMake.")
        sys.exit(1)

    print(f"Detected project type: {project_type}")
    generate_setup(project_type, project_path)
    print("Dev environment setup generated successfully!")
