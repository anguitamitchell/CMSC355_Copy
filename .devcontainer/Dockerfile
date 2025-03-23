FROM python:3.10-slim

# Set the working directory to the 'backend' folder where app.py and requirements.txt are located
WORKDIR /app/backend

# Install Python dependencies from requirements.txt
COPY Sprint\ 1/AI\ Fitness\ Project/backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY Sprint\ 1/AI\ Fitness\ Project/backend/ ./

# Expose port 5000 (common port for Flask apps)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
