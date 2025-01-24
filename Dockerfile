# Use the official Python 3.10 slim image as the base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY ./app /app/app

# Copy the requirements file to the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port your app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
