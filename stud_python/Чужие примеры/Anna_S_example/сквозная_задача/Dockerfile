FROM python:3.8-alpine
RUN apk update && apk upgrade && apk add bash
WORKDIR /opt/api
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "3000"]
