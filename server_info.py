import platform
import socket

print("Hostname:", socket.gethostname())
print("OS:", platform.system())
print("OS VER:", platform.release())
