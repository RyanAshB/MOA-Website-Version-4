# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app  

# Cpoy porject requirements
COPY  requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt  

# Copy project files into the container
COPY . .  

# Expose port 5000 for Flask
EXPOSE 5000  

# Command to run the app
CMD []
