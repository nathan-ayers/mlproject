# Use a minimal, official Python runtime
FROM python:3.8-slim

# Set and create working directory
WORKDIR /app

# 1) Copy only requirements.txt first for better layer caching
COPY requirements.txt .

# 2) Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copy the rest of your application code
COPY . .

# (Optional) Set Flask env vars if you ever run flask directly
ENV FLASK_APP=application.py \
    FLASK_ENV=production

# 4) Expose the port your app listens on
EXPOSE 5000

# 5) Start Gunicorn with 2 workers and a 120 s timeout
CMD ["gunicorn", "application:application", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120"]

