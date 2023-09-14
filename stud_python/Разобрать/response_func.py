import requests

response = requests.get('http://info.cern.ch/')
print(response.text)
