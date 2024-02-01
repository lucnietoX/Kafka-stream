import xmltodict
import json


xml_data="""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><PtIncident xmlns:ns2="http://nationalrail.co.uk/xml/common" xmlns:ns3="http://nationalrail.co.uk/xml/incident"><ns3:CreationTime>2024-02-01T17:13:30.141Z</ns3:CreationTime><ns3:ChangeHistory><ns2:ChangedBy>NRE CMS Editor</ns2:ChangedBy><ns2:LastChangedDate>2024-02-01T18:10:26.793Z</ns2:LastChangedDate></ns3:ChangeHistory><ns3:ParticipantRef>130527</ns3:ParticipantRef><ns3:IncidentNumber>AAEDF32AF6C74E47B4B12E3B78054AE5</ns3:IncidentNumber><ns3:Version>20240201181026</ns3:Version><ns3:Source><ns3:TwitterHashtag>Ockley</ns3:TwitterHashtag></ns3:Source><ns3:ValidityPeriod><ns2:StartTime>2024-02-01T17:13:00.000Z</ns2:StartTime><ns2:EndTime>2024-02-01T18:04:00.000Z</ns2:EndTime></ns3:ValidityPeriod><ns3:Planned>false</ns3:Planned><ns3:Summary>Delays between Dorking and Horsham</ns3:Summary><ns3:Description>&lt;p&gt;Disruption caused by a fire next to the track between Dorking and Horsham has now ended.
&lt;/p&gt;&lt;p&gt;&lt;/p&gt;</ns3:Description><ns3:InfoLinks><ns3:InfoLink><ns3:Uri>https://www.nationalrail.co.uk/service-disruptions/ockley-20240201/</ns3:Uri><ns3:Label>Incident detail page</ns3:Label></ns3:InfoLink></ns3:InfoLinks><ns3:Affects><ns3:Operators><ns3:AffectedOperator><ns3:OperatorRef>SN</ns3:OperatorRef><ns3:OperatorName>Southern</ns3:OperatorName></ns3:AffectedOperator></ns3:Operators><ns3:RoutesAffected>&lt;p&gt;between London Victoria and Horsham&lt;/p&gt;</ns3:RoutesAffected></ns3:Affects><ns3:ClearedIncident>true</ns3:ClearedIncident><ns3:IncidentPriority>2</ns3:IncidentPriority></PtIncident>"""

xml_dict = xmltodict.parse(xml_data)

json_data = json.dumps(xml_dict)

print(json_data)
