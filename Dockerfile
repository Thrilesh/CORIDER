# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app

# Install any dependencies (if you have a requirements.txt file)
RUN pip install -r requirements.txt

# Expose a port (if your application uses a specific port)
EXPOSE 5000

# Run the Python script
CMD ["python", "app.py"]
