import requests
import json

url = "https://api-basketball.p.rapidapi.com/teams"

headers = {
    'x-rapidapi-host': "api-basketball.p.rapidapi.com",
    'x-rapidapi-key': "9e80ccaa30msh32897036341e644p104614jsnc53b7209b1cd"
}


def get_all_teams():
    querystring = {"league": "12", "season": "2019-2020"}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    responseJson = response.json()
    responseJson = json.dumps(responseJson, indent=4)

    print(responseJson)


def get_all_teams_stats():
    url = "https://api-basketball.p.rapidapi.com/statistics"

    querystring = {"league": "12", "season": "2019-2020", "team": "133"}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    responseJson = response.json()
    print(responseJson['response']['team'])
    # if responseJson["errors"]["team"] != "The Team field do not exist.":
    responseJson = json.dumps(responseJson, indent=4)
    # print(responseJson["errors"]["teams"])

    #        if responseJson["errors"]["teams"] != "The Team field do not exist.":
    print(responseJson)


get_all_teams_stats()
