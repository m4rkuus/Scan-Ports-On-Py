#Autor @mmunoz28
import sys
import socket

objetivo = socket.gethostbyname(input("Inserte La Dirección IP: "))

print("Escaneando Objetivo: " + objetivo)

try:
    for port in range(1 , 150):
        s = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo , port))
        if resultado == 0:
            print("El Puerto {} está abierto".format(port))
            s.close
except:
    print("\n Saliendo...")
    sys.exit(0)