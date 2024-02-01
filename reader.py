import stomp
import json
import gzip
import xmltodict

file = open("/Users/lucianonieto/repo/Kafka-stream/config.cfg","r")
cred = json.load(file)

user = cred["cfg_user"]
password = cred["cfg_password"]
live_feed_topic=cred["cfg_live_feed_topic"]
status_message_topic=cred["cfg_status_messages_topic"]
messaging_host=cred["cfg_messaging_host"]
stomp_port=cred["cfg_stomp_port"]
openwire_port=cred["cfg_openwire_port"]

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)
    def on_message(self, frame):
        #msg = gzip.decompress(frame.body)
        #print('received a message "%s"' % msg.decode())
        xml_data = frame.body.replace("uk.co.nationalrail.xml.incident.PtIncidentStructure","PtIncident") #https://wiki.openraildata.com/KnowledgeBase
        xml_dict = xmltodict.parse(xml_data)
        print("Message ",xml_dict) 
    def on_connected(self, frame):
        print("CONNECTED")
    def on_connecting(self, host_and_port):
        print("connecting..")

c = stomp.Connection([(messaging_host, stomp_port)])
c.connect(user, password)
c.set_listener('', MyListener())
c.subscribe(destination="/topic/"+live_feed_topic, id=1, ack='auto')