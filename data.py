import requests

quiz_url = "https://opentdb.com/api.php"

parameters = {"amount":10,
             "category": 17,
              "type": "boolean"}

question_data = requests.get(url=quiz_url, params=parameters)
question_data.raise_for_status()
question_data = question_data.json()["results"]
