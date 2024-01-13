FROM arm64v8/python:3.9-slim

RUN mkdir /app
WORKDIR /app
COPY ./app .
RUN ls -l

RUN pip install -r requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
