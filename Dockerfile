FROM python:3.8.5-alpine3.12

COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV MONGO_HOST=mongo
ENV MONGO_PORT=27017
ENTRYPOINT ["gunicorn","-b","0.0.0.0:8000","app:app"]