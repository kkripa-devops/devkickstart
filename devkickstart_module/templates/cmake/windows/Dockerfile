FROM mcr.microsoft.com/windows/servercore:ltsc2022

SHELL ["powershell", "-Command"]

# Install Chocolatey
RUN Set-ExecutionPolicy Bypass -Scope Process -Force ; \
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install required tools
RUN choco install -y cmake git python 7zip dotnet nuget.commandline

# Add Python to PATH
RUN setx PATH "$env:PATH;C:\Python311\;C:\Python311\Scripts"

WORKDIR C:/app
COPY . .

CMD ["cmd.exe"]
