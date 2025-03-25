# Use the official Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies including build tools and MariaDB development files
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    python3-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip (optional but recommended)
RUN pip install --upgrade pip

# Copy the requirements.txt file from the correct relative path into the container
COPY Sprint_1/AI_Fitness_Project/requirements.txt /app/requirements.txt

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of your application code into the container
COPY Sprint_1/AI_Fitness_Project /app

# Set environment variables (using the recommended syntax)
ENV PYTHONUNBUFFERED=1

# Expose the port your app uses (adjust if needed)
EXPOSE 5000

# Run the application
CMD ["python", "/app/app.py"]
