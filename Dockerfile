FROM python:3.9-slim

# Metadata
LABEL maintainer="Bhanu Reddy <2022bcd0026>"
LABEL description="ML Model Deployment - Bhanu Reddy (2022bcd0026)"

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY train.py .
COPY model.pkl .

# Set environment variables
ENV NAME="Bhanu Reddy"
ENV REGISTER="2022bcd0026"

# Run the application
CMD ["python", "train.py"]
