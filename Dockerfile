FROM python:3.8-alpine3.14

WORKDIR /app/webapp

COPY requirements.txt /app/webapp/requirements.txt

RUN apk --update add --no-cache g++ && pip install --upgrade pip && pip install -r requirements.txt && rm -rf /var/cache/apk/*

COPY ./data /app/data
COPY ./webapp /app/webapp

ENTRYPOINT ["python"]
CMD ["app.py"]
