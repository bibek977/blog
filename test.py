import requests
import json

url = "http://127.0.0.1:8000/accounts/api/user_login/"


def post_data():
    data = {
        "username":"Bibek",
        "password" : "Django"
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.post(url=url,headers=headers,data=json_data)
    print(r.json())

    # {
    #     "username":"Bibek99",
    #     "email" : "bibek@gmail.com",
    #     "first_name" : "bibek",
    #     "last_name" : "bhattarai",
    #     "password" : "user@123"
    # }