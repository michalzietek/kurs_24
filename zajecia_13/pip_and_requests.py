import requests

response = requests.get(url="https://www.onet.pl")
print(response.text)
