import requests
import json
URL = "http://127.0.0.1:3456/stucreate/"

data={
    'name':'Sj',
    'roll':101,
    'city':'Ranchi'
}

json_data = json.dumps(data)
r = requests.post(url = URL,json = json_data)
data = r.json()
print(data)
