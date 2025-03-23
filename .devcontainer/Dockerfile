# Use a Python 3.10 base image (Debian-based)
FROM python:3.10-bullseye

# Set the working directory inside the container
WORKDIR /app

# Install Node.js and npm (latest LTS) from NodeSource
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs

# Install additional dependencies (if needed)
RUN apt-get install -y git

# Copy the application files into the container
COPY . .

# Expose necessary ports (adjust if needed)
EXPOSE 5000 3000  

# Set the default command (adjust based on your project setup)
CMD ["bash"]
