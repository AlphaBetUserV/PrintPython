import requests

response = requests.get("https://api.ipify.org/?format=json")
return response
