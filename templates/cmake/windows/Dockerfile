FROM mcr.microsoft.com/windows/servercore:ltsc2022

SHELL ["powershell", "-Command"]

WORKDIR C:/app
COPY . C:/app

# NOTE: Assumes CMake and Build Tools are pre-installed
CMD ["cmd.exe"]
