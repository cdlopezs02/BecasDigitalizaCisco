from ncclient import manager
import xml.dom.minidom as xml

#Establece la conexion
con=manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

#Creamos el cambio/filtro
change="""
<config><native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
        <Loopback>
            <name>88</name>
            <description>interfaz_Creada</description>
            <ip>
                <address>
                    <primary>
                        <address>88.88.88.88</address>
                        <mask>255.255.255.0</mask>
                    </primary>
                </address>
            </ip>
        </Loopback>
    </interface>
</native></config>
"""

#Pedimos los datos o los modificamos
reply= con.edit_config(target="running",config=change)

#Mostramos los datos 
print(xml.parseString(reply.xml).toprettyxml())