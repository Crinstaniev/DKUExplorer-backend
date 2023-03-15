FROM python:3.9-slim-buster

# Install dependencies
WORKDIR /app
COPY requirements.txt .
