# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /app
COPY test.py .

# Run echo when the container launches
CMD echo "Hello, World!"
CMD [ "pytest","./test.py" ]
