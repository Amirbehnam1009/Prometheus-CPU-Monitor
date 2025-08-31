import socket
import json
import psutil

port = 8080
HOST = "127.0.0.1"

def EstablishConnection(Socket1):
    Socket1.connect((HOST, port))
    print("YOU HAVE BEEN CONNECTED")
    while True:   
        UsageUse = cpu_percentofuse()
        data2 = {"The Perecentage Of CPU USAGE" : UsageUse}
        normalform=json.dumps(data2)
        Socket1.sendall(normalform.encode())
        data = Socket1.recv(1024).decode()
        print(f"{data}")    

def cpu_percentofuse(): 
    return psutil.cpu_percent(1)
    
if __name__ == '__main__':    
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as Socket1:
                EstablishConnection(Socket1)
        except:
            print("Server Is Not Working")
