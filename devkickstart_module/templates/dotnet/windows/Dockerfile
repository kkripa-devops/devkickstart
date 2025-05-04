FROM mcr.microsoft.com/dotnet/sdk:7.0-windowsservercore-ltsc2022

SHELL ["powershell", "-Command"]

# Install Chocolatey
RUN Set-ExecutionPolicy Bypass -Scope Process -Force ; \
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12 ; \
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install required tools via Chocolatey
RUN choco install -y ; \
    visualstudio2022buildtools ; \
    cmake ; \
    git ; \
    python ; \
    7zip ; \
    nuget.commandline ; \
    powershell-core ; \
    nodejs

# Add Python to PATH (optional but helpful)
RUN setx PATH "$env:PATH;C:\Python311\;C:\Python311\Scripts"

WORKDIR C:/app
COPY . .

CMD ["cmd.exe"]
