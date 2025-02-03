# Use the official Python image (you can use the latest stable version)
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy all project files including requirements.txt and setup.py
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask (if needed)
ENV FLASK_APP=application.py
ENV FLASK_ENV=production

# Expose port 5000
EXPOSE 5000

# Run Gunicorn as the production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "application:application"]
