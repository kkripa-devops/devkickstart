FROM mcr.microsoft.com/windows/servercore:ltsc2022

SHELL ["powershell", "-Command"]

WORKDIR C:/app
COPY . C:/app

# Assume Visual Studio Build Tools are preinstalled or use a custom base image
CMD ["cmd.exe"]
