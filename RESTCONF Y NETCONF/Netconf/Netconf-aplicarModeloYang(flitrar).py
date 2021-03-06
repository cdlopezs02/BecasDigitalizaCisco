from ncclient import manager
import xml.dom.minidom as xml

#Establece la conexion
con=manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

#Creamos el cambio/filtro
change="""
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""

#Pedimos los datos o los modificamos
reply= con.get(filter=change)

#Mostramos los datos 
print(xml.parseString(reply.xml).toprettyxml())