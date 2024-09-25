import http.server as server
import socketserver as socket
import os
import json

with open('ServerConfig.json', "r") as ReadJsonConfig:
    data = json.load(ReadJsonConfig)

host = data["hostIP"]
port = data["port"]
adress = (host, port)

handler = server.SimpleHTTPRequestHandler

httpd = socket.TCPServer(adress, handler)

print(f"Le server tourne sur le port : {port}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Le serveur est arrêté !')