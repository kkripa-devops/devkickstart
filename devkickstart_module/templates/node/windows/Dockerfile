FROM mcr.microsoft.com/windows/servercore:ltsc2022

SHELL ["powershell", "-Command"]

# Install Chocolatey
RUN Set-ExecutionPolicy Bypass -Scope Process -Force ; \
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install essential tools
RUN choco install -y; \
    git ; \
    nodejs ; \
    cmake ; \
    python ; \
    7zip ; \
    yarn

WORKDIR C:/app
COPY . .

CMD ["cmd.exe"]
