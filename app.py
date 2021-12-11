from os import name
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

# opening and reading json
json_names = []
with open(r'C:\Users\User\Desktop\fuck\famous.json', 'r') as f:
    json_names = json.loads(f.read())
    
famous_data = []

# getting from api
for i in json_names:
    api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(i)
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv("APIKEY")})
    print(response.text)
    for celebrity in json.loads(response.text):
        keys = celebrity.keys()
        if "nacionality" in keys and "height" in keys and "birthdy" in keys and "age" in keys and "is_alive" in keys:
            famous_object = {
                "name": celebrity["name"],
                "gender": celebrity["gender"],
                "nationality": celebrity["nationality"],
                "occupation": celebrity["occupation"],
                "height": celebrity["height"],
                "birthdy": celebrity["birthdy"],
                "age": celebrity["age"],
                "is_alive": celebrity["is_alive"]
            }
            famous_data.append(famous_object)
    
with open(r'C:\Users\User\Desktop\fuck\data.json', 'w+') as f:
    json.dump(famous_data, f)


    
    
 

#search specific data and save it on json


