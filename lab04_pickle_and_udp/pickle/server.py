import socket
import pickle

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
print("Pickle server listening on port 9090")
conn, addr = sock.accept()
print("Client connected", addr)
data = conn.recv(4096)
print("Received pickle data")
conn.send(data)
conn.close()
sock.close()
print("Server finished")
