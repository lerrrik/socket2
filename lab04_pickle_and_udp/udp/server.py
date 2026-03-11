import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9091))
print("UDP server listening on port 9091")
while True:
    try:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        sock.sendto(data, addr)
    except KeyboardInterrupt:
        print("Server stopped")
        break
sock.close()
