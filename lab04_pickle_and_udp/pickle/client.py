import socket
import pickle

sock = socket.socket()
sock.connect(('localhost', 9090))
data = {"name": "alice", "n": 42, "hobbies": ["reading", "swimming"]}
print("Sending:", data)
sock.send(pickle.dumps(data))
received = sock.recv(4096)
result = pickle.loads(received)
print("echo:", result)
sock.close()
