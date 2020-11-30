import requests

url = "https://montanaflynn-fifa-world-cup.p.rapidapi.com/teams"

headers = {
    'accepts': "json",
    'x-rapidapi-key': "51507cb5fcmsh4a3e9775685c3f9p1e9bb3jsnb9e1628e4ed0",
    'x-rapidapi-host': "montanaflynn-fifa-world-cup.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)