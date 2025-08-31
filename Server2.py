import socket
from _thread import *
import json
from prometheus_client import start_http_server, Gauge

HOST = "127.0.0.1"
port = 8080

g = Gauge('my_cpu_percents', 'Description of the amount of percentage of cpu usage in gauge', ['method', 'endpoint'])

def Main(connectto):
    with conn:
            print(f"Connect Through {addr}")
            while True:
                recievedData = connectto.recv(2048)
                if not recievedData:
                    break
                i = DataTojson(recievedData)
                UseOfCpuPercentage(i, connectto)
                connectto.sendall(recievedData.upper())

def UseOfCpuPercentage(a, connectto):
    i = str(connectto.getpeername())
    g.labels(' ', i).set(a)

def DataTojson(recievedData):
    i = recievedData.decode('utf-8')
    jsons = json.loads(i)
    return jsons["The Perecentage Of CPU USAGE"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as Socket1:
    Socket1.bind((HOST, port))
    Socket1.listen()
    start_http_server(8000)
    while True:
        conn, addr=Socket1.accept()
        start_new_thread(Main,(conn,))
        
