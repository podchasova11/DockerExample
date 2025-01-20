
import requests

response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

print(response.json()["insult"])

# def test_data():
#     url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
#     lang = en
#
#     response = requests.get(url)
#     body = response.json()
#     data = body["data"]
#
#     assert data["id"] == id
#     assert data["email"] == email


