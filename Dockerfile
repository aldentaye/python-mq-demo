# Use an official Python runtime as a parent image
FROM python:3.8-slim

COPY . /app

RUN ls -l

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
