FROM mcr.microsoft.com/dotnet/sdk:7.0

# Install packages
RUN apt-get update && apt-get install -y \
    cmake \
    git \
    python3 \
    python3-pip \
    p7zip-full \
    curl \
    unzip

# Install NuGet CLI manually (as it's not apt-get available)
RUN curl -L https://dist.nuget.org/win-x86-commandline/latest/nuget.exe -o /usr/local/bin/nuget.exe && \
    chmod +x /usr/local/bin/nuget.exe

# Optional: symlink nuget to run with mono if
