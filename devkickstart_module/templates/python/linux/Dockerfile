FROM python:3.11

RUN apt-get update && apt-get install -y \
    git \
    cmake \
    nodejs \
    npm \
    p7zip-full \
    curl \
    build-essential \
    pipx

# Optional: install yarn
RUN npm install -g yarn

WORKDIR /app
COPY . .

CMD ["bash"]
