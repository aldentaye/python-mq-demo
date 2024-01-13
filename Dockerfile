# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY ./app /app

RUN ls -l

RUN pip install -r requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
