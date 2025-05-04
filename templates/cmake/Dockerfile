FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y build-essential cmake

WORKDIR /app
COPY . /app
RUN cmake . && make

CMD ["./main"]
