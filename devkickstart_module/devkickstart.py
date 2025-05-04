# Copyright (c) 2025 Radhakrishnan Krishna Kripa
# Licensed under the MIT License

import os
import argparse
from .utils import detect_project_type, generate_setup, get_host_os

def main():
    parser = argparse.ArgumentParser(description="DevKickstart - Generate devcontainer files")
    parser.add_argument('--stack', type=str, help="Override detected project type (e.g., node, python, dotnet, cpp, cmake)")
    parser.add_argument('--os', type=str, choices=['windows', 'linux'], help="Override host OS")
    parser.add_argument('--dry-run', action='store_true', help="Preview actions without writing files")

    args = parser.parse_args()

    print("Welcome to DevKickstart!")

    project_path = os.getcwd()

    # Determine stack
    if args.stack:
        project_type = args.stack
        print(f"Using overridden stack: {project_type}")
    else:
        project_type = detect_project_type(project_path)
        if not project_type:
            print("Could not detect project type. Use --stack to override.")
            return
        print(f"Detected project type: {project_type}")

    # Determine OS
    os_type = args.os if args.os else get_host_os()
    print(f"Target OS: {os_type}")

    # Generate setup
    generate_setup(project_type, project_path, os_type, dry_run=args.dry_run)

    if not args.dry_run:
        print("Dev environment setup generated successfully!")

