import socket

HOST = "127.0.0.1"  # Same as server
PORT = 65432        # Same as server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        client_socket.sendall(message.encode())  # Send to server
        data = client_socket.recv(1024)  # Receive echo
        print("Server:", data.decode())
