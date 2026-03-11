import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = b"hello udp"
sock.sendto(message, ('localhost', 9091))
print("Sent:", message.decode())
data, addr = sock.recvfrom(1024)
print("echo:", data.decode())
sock.close()
