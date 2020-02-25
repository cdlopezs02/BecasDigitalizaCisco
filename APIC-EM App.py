import json
import requests
import tabulate
import time
requests.packages.urllib3.disable_warnings()  #No es necesario pero elimina warnings


def getTicket():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
    "content-type": "application/json"
    }
    body_json = {
  "password": "Xj3BDqbU",
  "username": "devnetuser"
    }

    #json.dumps(body_json) Convierte el diccionario de Python en un Json para la request

    #Envio de la request
    resp=requests.post(url,json.dumps(body_json),headers=headers,verify=False)

    #Using the response:
    print("Ticket request status: ", resp.status_code)

    response_json = resp.json()       # Pasa de json a diccionario de python
    serviceTicket = response_json["response"]["serviceTicket"]  #accedes al valor que quieres y lo guardas en una variable
    return serviceTicket
    
def getHosts(ticket):
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }
    
    resp = requests.get(api_url, headers=headers, verify=False)  #Envia la request
    print("Status of /host request: ", resp.status_code)
    if resp.status_code != 200: #si no es 200 salta error
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json() #pasa a diccionario de python

    host_list = []
    i = 0
    for item in response_json["response"]:
         i+=1
         host = [
                 i,
                 item["hostType"],
                 item["hostIp"] 
                ]
         host_list.append( host )
    table_header = ["Number", "Type", "IP"]
    print( tabulate.tabulate(host_list, table_header) )

def getDevices(ticket):
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)  #Envia la request
    print("Status of devices request: ", resp.status_code)
    if resp.status_code != 200: #si no es 200 salta error
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json() #pasa a diccionario de python

    host_list = []
    i = 0
    for item in response_json["response"]:
         i+=1
         host = [
                 i,
                 item["type"],
                 item["managementIpAddress"] 
                ]
         host_list.append( host )
    table_header = ["Number", "Type", "IP"]
    print( tabulate.tabulate(host_list, table_header) )

def getflowAnalysisId(ticket):
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    print('\n Avaliable Hosts:')
    getHosts(ticket)
    print('\n Avaliable Devices:')
    getDevices(ticket)

    print('No se porque muchas ip de origen/ destino hacen que no funcione. origen 10.1.15.117 y destino 10.1.12.20 funciona seguro.')
    print('creo que es porque solo funciona con algunos tipos de  dispositivos como extremos pero no se cuales.')
    sourceIp= input('Introduce la Ip origen:')
    destinyIp= input('Introduce la Ip destino:')
    #sourceIp='10.1.15.117'
    #destinyIp='10.1.12.20'
    body_json = {
    "destIP": destinyIp,
    "sourceIP": sourceIp
    }

    resp=requests.post(url,json.dumps(body_json),headers=headers,verify=False)
    resp_json=resp.json()

    flowAnalysisId = resp_json["response"]["flowAnalysisId"]
    return flowAnalysisId

def getFlowAnalysis(flowId,ticket):
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    
    resp=requests.get(url,headers=headers,verify=False)
    resp_json=resp.json()
    
    for elem in resp_json['response']:
        if elem['id']==flowId:
            flow=elem
            status=elem['status']
            if status=='INPROGRESS':
                print('Status not clear')
                return 2
            if status== 'FAILED':
                print('There was an error in the flow Analisis')
            if status== 'COMPLETED':
                print('Flow Analisis Completed')
        
    if status =='COMPLETED':
        url+='/'+flowId
        resp=requests.get(url,headers=headers,verify=False)
        result=resp.json()
        host_list=[]
        for elem in result['response']["networkElementsInfo"]:
            host=[elem['ip'],elem['type']]
            host_list.append(host)

        table_header = ["IP","Type"]
        print( tabulate.tabulate(host_list, table_header) )

def FlowAnalysis():
    ticket=getTicket()
    flowId=getflowAnalysisId(ticket)
    if getFlowAnalysis(flowId,ticket)==2:
        print('Dando tiempo al servidor...')
        time.sleep(10)
        getFlowAnalysis(flowId,ticket)


print('Elige una opcion:')
print('''        
1. Obtener Ticket
2. Mostrar Hosts
3. Mostrar Dispositivos de la Red
4. Realizar un Flow Analysis
5. Mostrar Opciones
'''
)

print('Escriba el numero de la opcion elegida o escriba \"exit\" para salir:', end='\n')
o = input()

while o != 'exit':
    if o == '1':
        print('Obteniendo Ticket...')
        t=getTicket()
        print('Su ticket es: '+ t +'\n')
    elif o == '2':
        print('Buscando Hosts...')
        t=getTicket()
        getHosts(t)
        print()
    elif o == '3':
        print('Buscando dispositivos en la red...')
        t=getTicket()
        getDevices(t)
        print()
    elif o == '4':
        print('Realizando un Flow Analysis:')
        FlowAnalysis()
        print()
    elif o == '5':
        print('Elige una opcion:')
        print('''        
1. Obtener Ticket
2. Mostrar Hosts
3. Mostrar Dispositivos de la Red
4. Realizar un Flow Analysis
5. Mostrar Opciones
'''
)
    elif o =='exit':
        break
    print('Escriba el numero de la opcion elegida o escriba \"exit\" para salir:', end='\n')
    o = input()