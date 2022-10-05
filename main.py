import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = user
TOKEN = token
GRAPH_ID = ID

user_parameters = {
    "token": token,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text) - created user so no need for it now

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# (https://pixe.la/v1/users/claudiaacchurch/graphs/hgsbjhfurieo87.html)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now() # can specify year, month and day in parentheses

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5",
}


pixel_response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)

# updating pixels:
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "5.5"
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# delete:
# delete_endpoint = update_endpoint
# requests.delete(url=delete_endpoint, headers=headers)
