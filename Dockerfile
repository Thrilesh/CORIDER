# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container at /app
COPY . /app/

# Install any dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 
EXPOSE 5000

# Run the Python script
CMD ["python", "app.py"]
