import socket
import json

def send_request(request):
     sock = socket.socket()
     try:
         sock.connect(('localhost', 9092))
         sock.send(json.dumps(request).encode())
         data = sock.recv(1024).decode()
         return json.loads(data)
    except ConnectionRefusedError:
         return {"ok": False, "error": "Server not running"}
    finally:
sock.close()

# Интерактивный клиент
while True:
    print("\n--- Bank Client ---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose action (1-4): ").strip()

    if choice == "1":
        response = send_request({"action": "balance"})
        if response.get("ok"):
            print(f"Current balance: {response['balance']}")
        else:
            print(f"Error: {response.get('error')}")

    elif choice == "2":
        try:
            amount = int(input("Enter amount to deposit: "))
            response = send_request({"action": "deposit", "amount": amount})
            if response.get("ok"):
                print(f"New balance: {response['balance']}")
            else:
                print(f"Error: {response.get('error')}")
        except ValueError:
            print("Invalid amount")

    elif choice == "3":
        try:
            amount = int(input("Enter amount to withdraw: "))
            response = send_request({"action": "withdraw", "amount": amount})
            if response.get("ok"):
                print(f"New balance: {response['balance']}")
            else:
                print(f"Error: {response.get('error')}")
        except ValueError:
            print("Invalid amount")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
     
print("Invalid choice")
EOF
