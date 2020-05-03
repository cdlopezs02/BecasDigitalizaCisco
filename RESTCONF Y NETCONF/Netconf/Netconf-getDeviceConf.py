from ncclient import manager
import xml.dom.minidom as xml

#Establece la conexion
con=manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

#Pedimos los datos
reply= con.get_config(source="running")

#Mostramos los datos 
print(xml.parseString(reply.xml).toprettyxml())