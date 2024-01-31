import requests

response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

print(response.json()["insult"])