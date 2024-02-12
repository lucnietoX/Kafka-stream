import requests
import xmltodict
import json
from pymongo import MongoClient
 
url="https://publicdatafeeds.networkrail.co.uk/ntrod/SupportingFileAuthenticate?type=CORPUS"

api_auth = "https://opendata.nationalrail.co.uk/authenticate"
username="luciano.nieto@gmail.com"
password=""

response = requests.post(api_auth,data={"username":username,"password":password})
tokenv=response.json()["token"]

response = requests.get(url,headers={"X-Auth-Token":tokenv})
xml_data=response.content
xml_dict = xmltodict.parse(xml_data)
json_data = json.dumps(xml_dict)
json_data = json.loads(json_data)["StationList"]["Station"]

def connect_mongo():
    client = MongoClient('localhost', 27017,username="root", password="example")
    return client
ct = connect_mongo()
db = ct['nationalrail']
collection = db['stations']
collection.insert_one(xml_dict)


for i in json_data:
    collection.insert_one(i)

ct.close()