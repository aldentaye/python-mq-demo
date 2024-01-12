# Use an official Python runtime as a parent image
FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN ls -l

RUN pip install -r ./app/requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
