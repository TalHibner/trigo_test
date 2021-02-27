FROM python:3.8.8-alpine
COPY ./multi-env-config /app
COPY ./svc-config /app/svc-config
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","multi-env-config.py"]