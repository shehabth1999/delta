# Use the official Python image
FROM python:3.12-slim

# Set environment variables to avoid interactive prompts during install
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the project files into the container
COPY . .

# Collect static files (run this only if you don't need DB access at build time)
RUN python manage.py collectstatic --noinput

# Expose the app port
EXPOSE 8000

# Default command to run Gunicorn with 3 workers
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
