FROM python:3.8.8-alpine
COPY ./service-a /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","service-a.py"]