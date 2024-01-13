FROM python:3.9-alpine

WORKDIR /app
COPY ./app .
RUN ls -l

RUN pip install -r requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
