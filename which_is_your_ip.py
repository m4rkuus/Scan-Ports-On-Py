#Autor @mmunoz28
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El Nombre de tu pc es : " + hostname)
print("Tu dirección IP es : " + ip)