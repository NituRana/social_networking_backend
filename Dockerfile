# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the working directory in the container
WORKDIR /socialnetworking

# Copy the current directory contents into the container at /socialnetworking
COPY . /socialnetworking/

# Install dependencies
COPY requirements.txt /socialnetworking/
RUN pip install --no-cache-dir -r requirements.txt

# Run migrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
