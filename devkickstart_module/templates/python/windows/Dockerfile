FROM mcr.microsoft.com/windows/servercore:ltsc2022

SHELL ["powershell", "-Command"]

# Install Chocolatey
RUN Set-ExecutionPolicy Bypass -Scope Process -Force ; \
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install essential tools
RUN choco install -y ; \
    python ; \
    git ; \
    nodejs ; \
    cmake ; \
    7zip ; \
    yarn

# Optional: Add Python to PATH if needed
RUN setx PATH "$env:PATH;C:\Python311\;C:\Python311\Scripts"

WORKDIR C:/app
COPY . .

CMD ["cmd.exe"]
