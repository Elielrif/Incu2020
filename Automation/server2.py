from ncclient import manager
import xml.dom.minidom
import socket

node = "127.0.0.1"

def connect(node):
    try:
        device_connection = manager.connect(host = node, port = '2200', username = 'admin', password = 'Cisco.123', hostkey_verify = False, device_params={'name':'nexus'})
        return device_connection
    except:
        print("Unable to connect " + node)

def getHostname(node):
    device_connection = connect(node)
    hostname = """
               <show xmlns="http://www.cisco.com/nxos:1.0">
                   <hostname>
                   </hostname>
               </show>
               """
    netconf_output = device_connection.get(('subtree', hostname))
    xml_doc = xml.dom.minidom.parseString(netconf_output.xml)
    hostname = xml_doc.getElementsByTagName("mod:hostname")
    return "Hostname: "+str(hostname[0].firstChild.nodeValue)

def getVersion(node):
    device_connection = connect(node)
    version = """
                <show xmlns="http://www.cisco.com/nxos:1.0">
                   <version>
                   </version>
                </show>
    
            """
    try:
        netconf_output = device_connection.get(('subtree', version))
        xml_doc = xml.dom.minidom.parseString(netconf_output.xml)
        version = xml_doc.getElementsByTagName("mod:version")
        return "Version: " + str(version[0].firstChild.nodeValue)
    except:
        print("Unable to get this node version")



def changeHostname(node):
    device_connection = connect(node)
    
    update_interface_config_string = '''
            <configure xmlns="http://www.cisco.com/nxos:1.0">
                <__XML__MODE__exec_configure>
                <hostname>
                    <name>NXOS</name>
                </hostname>
                </__XML__MODE__exec_configure>
            </configure>
'''
    
    configuration = ''

    try:
        configuration += '<config>'
        configuration += update_interface_config_string
        configuration += '</config>'
        print(configuration)
        device_connection.edit_config(target='running', config=configuration)
        print("Config pushed successfuly!")
    except:
        print("Unable to change this node hostname")

    
def Main():
    host = "127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(5)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        message = conn.recv(1024).decode()
        if message == "show hostname":
                message = getHostname(node)
        elif message == "show version":
                message = getVersion()
        else:
                message = "I do not understand"
        conn.send(message.encode())
    conn.close()

if __name__ == '__main__':
        Main()
