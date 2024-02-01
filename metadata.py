import requests

incidents="https://opendata.nationalrail.co.uk/api/staticfeeds/5.0/incidents"
api_auth = "https://opendata.nationalrail.co.uk/authenticate"
username="luciano.nieto@gmail.com"
password=""


response = requests.post(api_auth,data={"username":username,"password":password})
tokenv=response.json()["token"]

response = requests.get(incidents,headers={"X-Auth-Token":tokenv})
response.content