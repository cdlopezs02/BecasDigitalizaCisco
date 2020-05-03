import json, requests

requests.packages.urllib3.disable_warnings()

#Connection address
url="https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback77"

#headers
headers={"Accept":"application/yang-data+json","Content-type":"application/yang-data+json"}
#Authentification
basic_auth=("cisco","cisco123!")
#data
conf ={    
    "ietf-interfaces:interface": {
        "name": "Loopback77",
        "description": "b",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip":"77.77.77.77",
                    "netmask":"255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

#sending
resp=requests.put(url,data=json.dumps(conf),headers=headers,auth=basic_auth,verify=False)

if resp.status_code>=200 and resp.status_code<=299:
    print(resp.status_code)
else:
    print("Error code:{},reply{}".format(resp.status_code,resp.json()))
#resp_json=resp.json()

#print(json.dumps(resp_json,indent=4))