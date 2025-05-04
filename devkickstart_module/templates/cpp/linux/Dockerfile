FROM gcc:13

WORKDIR /app
COPY . /app

# Optional: Build if main.cpp exists
RUN if [ -f main.cpp ]; then g++ main.cpp -o main; fi

CMD ["bash"]
