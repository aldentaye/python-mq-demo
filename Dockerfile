FROM python:3.9-alpine

WORKDIR /app
COPY ./app .
RUN ls -l

RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

