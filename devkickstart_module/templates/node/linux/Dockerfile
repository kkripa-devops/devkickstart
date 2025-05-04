FROM node:18

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    cmake \
    p7zip-full \
    curl \
    build-essential

# Optional: Install yarn
RUN npm install -g yarn

WORKDIR /app
COPY . .

CMD ["bash"]
