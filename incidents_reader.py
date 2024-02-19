import stomp
import json
import xmltodict
from pymongo import MongoClient
from pykafka import KafkaClient

file = open("config.cfg","r")
cred = json.load(file)

user = cred["cfg_user"]
password = cred["cfg_password"]
live_feed_topic=cred["cfg_live_feed_topic"]
status_message_topic=cred["cfg_status_messages_topic"]
messaging_host=cred["cfg_messaging_host"]
stomp_port=cred["cfg_stomp_port"]
openwire_port=cred["cfg_openwire_port"]
mpass=cred["mongo_password"]
muser=cred["mongo_user"]

def connect_mongo():
    client = MongoClient('localhost', 27017,username=muser, password=mpass)
    return client

ct = connect_mongo()
db = ct['nationalrail']
collection = db['incidents_test_real']

#kafka
client = KafkaClient(hosts="localhost:9092")
topic = client.topics[b'nationalrail']
producer = topic.get_sync_producer()

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)
    def on_message(self, frame):
        xml_data = frame.body.replace("uk.co.nationalrail.xml.incident.PtIncidentStructure","PtIncident") #https://wiki.openraildata.com/KnowledgeBase
        xml_dict = xmltodict.parse(xml_data)
        collection.insert_one(xml_dict)
        producer.produce(xml_dict)
    def on_connected(self, frame):
        print("CONNECTED")

c = stomp.Connection12([(messaging_host, stomp_port)])
c.connect(user, password)
c.set_listener('', MyListener())
c.subscribe(destination="/topic/"+live_feed_topic, id=1, ack='auto')