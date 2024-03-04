# import requests
# import json

# URL = "http://127.0.0.1:8000/studentapi/"

# def get_data(id=None):
#     param = {}
#     if id is not None:
#         param = {'id':id}
#     # json_data = json.dumps(data)
#     print(param)
#     r = requests.get(url = URL,params=param)
#     data = r.json()
    
#     print(data)

# get_data(2)
    


# import requests
# import json

# URL = "http://127.0.0.1:8000/studentapi/"

# def post_data():
#     data = {
#         'name': 'ajay',
#         'roll': 76,
#         'city': 'Dhanbad'
#     }

#     r = requests.post(url=URL, json=data)
#     data = r.json()
#     print(data)
        
# post_data()



# import requests

# URL = "http://127.0.0.1:8000/studentapi/"

# def update_data():
#     data = {
#         'id': 21,
#         'name': 'Rohit',
#         'city': 'Ranchi'
#     }
    
#     r = requests.put(url=URL, json=data)
    
#     if r.status_code == 200:  
#         print("Data successfully updated!")
#     else:
#         print("Failed to update data")

# update_data()
        
import requests

URL = "http://127.0.0.1:8000/studentapi/"

def delete_data():
    data = {
        'id': 9
    }
    
    r = requests.delete(url=URL, json=data)
    
    print(r)
    if r.status_code == 200:  
        print("Data successfully deleted!")
    else:
        print("Failed to delete data")

delete_data()


