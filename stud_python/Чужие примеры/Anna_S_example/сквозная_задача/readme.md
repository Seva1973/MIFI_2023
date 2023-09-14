
## Сквозная задача. Сафонова Анна


### Docker
#### Docker image build
* docker build -t asafonova .
#### Docker container run
* docker run -d --name apicontainer -p 3000:3000 asafonova


### Test API calls

1. Ping sweep functionality
#### Curl
```
curl -X GET -G 'http://localhost:3000/scan' -d'ip=192.168.0.1' -d'count=3'
```
or
```
curl -X GET 'http://localhost:3000/scan?ip=192.168.0.1&count=3'
```
#### Python
Please refer to example script:
[`api_call_example.py`](api_call_example.py)

2. Send http request
#### Curl
```
curl -X POST -G 'http://localhost:3000/sendhttp' -d'target=https://www.google.com' -d'method=GET' -d'header=Server' -d'header_value=HTTP'
```
or
```
curl -X POST 'http://localhost:3000/sendhttp?target=https://www.google.com&method=GET&header=Server&header_value=HTTP'
```
#### Python
Please refer to example script:
[`api_call_example.py`](api_call_example.py)
