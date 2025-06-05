# Dockerfile
# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies first (for Docker caching efficiency)
# This layer will only be rebuilt if requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code and tests
# This layer will be rebuilt if any of your code files change
COPY . .

# (Optional) You can define a default command, but TeamCity will override this
# CMD ["pytest"]
