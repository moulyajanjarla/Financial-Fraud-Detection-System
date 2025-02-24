# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy all files from the current directory to /app inside the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]