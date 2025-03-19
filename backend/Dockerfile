# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for psycopg2 (PostgreSQL libraries)
RUN apk update && apk add --no-cache \
    build-base \
    libpq-dev \
    gcc \
    libffi-dev

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on (Flask runs on port 5000 by default)
EXPOSE 5000

# Define the environment variable for Flask
ENV FLASK_APP=app.py

# Start the Flask application when the container runs
CMD ["flask", "run", "--host=0.0.0.0"]
