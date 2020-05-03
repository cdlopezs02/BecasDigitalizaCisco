from ncclient import manager

#Establece la conexion
con=manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

#Pintamos las capabilities que son las cosas que es capaz de hacer el router
for capability in con.server_capabilities:
    print(capability)
