import json, requests

requests.packages.urllib3.disable_warnings()

#Connection address
url="https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/"

#headers
headers={"Accept":"application/yang-data+json","Content-type":"application/yang-data+json"}
#Authentification
basic_auth=("cisco","cisco123!")

#sending
resp=requests.get(url,headers=headers,auth=basic_auth,verify=False)

resp_json=resp.json()

print(json.dumps(resp_json,indent=4))