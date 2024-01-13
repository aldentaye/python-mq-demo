# Use an official Python runtime as a parent image
FROM python:3.9-slim

COPY ./app /app

WORKDIR /app

RUN ls -l

RUN pip install -r requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
