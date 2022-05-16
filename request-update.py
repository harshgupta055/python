import requests
import json

URL = "http://127.0.0.1:8000/student_update/"

def update_data(id):
    data = {
        'id':id,
        'name':'Ayushya',
        'roll':100,
        'city':'Lucknow',
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

#update_data(1)


def delete_data(id):
    data = {
        'id':id,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data(1)