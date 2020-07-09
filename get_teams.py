import requests
import json

url = "https://api-basketball.p.rapidapi.com/teams"

querystring = {"league": "12", "season": "2019-2020"}

headers = {
    'x-rapidapi-host': "api-basketball.p.rapidapi.com",
    'x-rapidapi-key': "9e80ccaa30msh32897036341e644p104614jsnc53b7209b1cd"
}

response = requests.request("GET", url, headers=headers, params=querystring)

responseJson = response.json()
responseJson = json.dumps(responseJson, indent=4)

print(responseJson)
