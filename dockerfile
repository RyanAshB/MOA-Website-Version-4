# Use an official lightweight Python image
FROM python:3.13.3-alpine

# Set the working directory
WORKDIR /app  

# Cpoy porject requirements
COPY  requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Copy project files into the container
COPY . .  

# Expose port 5000 for Flask
EXPOSE 5000  

# Command to run the app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
