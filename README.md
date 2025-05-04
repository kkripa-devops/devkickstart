# DevKickstart

**Instant dev container setup for any project.**  

DevKickstart is a lightweight CLI tool that auto-generates `Dockerfile` and `.devcontainer.json` configurations so you can launch VS Code dev containers in seconds without writing setup scripts or YAML.

Dev containers are powerful, but building them from scratch isn't. DevKickstart skips the main writing config file steps so you can start coding right away.


## Why DevKickstart?

Dev containers require you to manually create:
- A working `Dockerfile`
- A properly configured `.devcontainer.json`

Even though the extension handles launching, **you still need to learn and configure it all first**.

DevKickstart handles that setup for you:
- Detects the project type (Node, Python, .NET, C++, CMake)
- Detects your operating system (Windows/Linux)
- Generates ready-to-use Docker and devcontainer files
- Lets you open in VSCode’s dev container instantly

# Installation

pip install devkickstart

# Or using github repo

git clone https://github.com/kkripa-devops/devkickstart.git

cd devkickstart

pip install .

# Uninstall

pip uninstall devkickstart -y

# Usage

Inside any project folder (Node, Python, .NET, etc.):

# Auto-detect
devkickstart

# Force node + Linux

devkickstart --stack dotnet --os linux

# Force node + Windows

devkickstart --stack dotnet --os windows

# Dry run to preview without writing files

devkickstart --dry-run

# Example:

cd my-net-app

devkickstart

# You’ll now see:

Welcome to DevKickstart!

Detected project type: dotnet

Looking for templates in: C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\devkickstart_module\templates\dotnet\windows

Dev environment setup generated successfully!


# Supported Project Types:

 Node.js (package.json)

 Python (requirements.txt or pyproject.toml)

 .NET (.csproj, .sln)

 C++ (.cpp, .h)

 CMake (CMakeLists.txt)

Supports both Linux and Windows environments.
