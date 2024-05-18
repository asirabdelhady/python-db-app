# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY app/requirements.txt /app/requirements.txt

# Install Flask
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ./app /app

# Specify the command to run on container start
CMD ["python", "app.py"]
