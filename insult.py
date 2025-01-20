
import requests

response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

print(response.json()["insult"])


# def user_data():
#     url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
#     id = 2
#     email = "pod@gmail.com"
#
#     response = requests.get(url)
#     body = response.json()
#     data = body["data"]
#
#     assert data["id"] == id
#     assert data["email"] == email
