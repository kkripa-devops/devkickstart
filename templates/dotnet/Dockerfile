FROM mcr.microsoft.com/dotnet/sdk:7.0

WORKDIR /src
COPY . .
RUN dotnet restore
RUN dotnet build

CMD ["dotnet", "run"]
