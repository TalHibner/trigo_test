FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./ /app/
COPY ./svc-config /app/svc-config
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt