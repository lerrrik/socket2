import socket
import json
balance = 1000 # начальный баланс

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 9092))
sock.listen(5)
print("Bank server listening on port 9092")

while True:
    try:
        conn, addr = sock.accept()
        print(f"Client connected from {addr}")
        data = conn.recv(1024).decode()
    if not data:
        conn.close()
        continue

    request = json.loads(data)
    print(f"Request: {request}")

    response = {"ok": True}

    if request["action"] == "balance":
        response["balance"] = balance

    elif request["action"] == "deposit":
        amount = request.get("amount", 0)
        if amount > 0:
            balance += amount
            response["balance"] = balance
         else:
            response["ok"] = False
            response["error"] = "Invalid amount"

    elif request["action"] == "withdraw":
         amount = request.get("amount", 0)
         if 0 < amount <= balance:
             balance -= amount
             response["balance"] = balance
         else:
             response["ok"] = False
             response["error"] = "Insufficient funds or invalid amount"
    else:
        response["ok"] = False
        response["error"] = "Unknown action"

    conn.send(json.dumps(response).encode())
    conn.close()
    print(f"Response sent: {response}")

    except KeyboardInterrupt:
        print("Server shutting down...")
        break
    except Exception as e:
        print(f"Error: {e}")
        conn.close()

sock.close()
EOF
