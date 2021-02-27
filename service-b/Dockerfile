FROM python:3.8.8-alpine
COPY ./service-b /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","service-b.py"]