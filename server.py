import socket

HOST = "127.0.0.1"  # Localhost (change to your LAN IP for others to connect)
PORT = 65432        # Any free port - Set to 1024

# TCP Socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT)) 
    server_socket.listen()           
    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()  
    with conn:
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)  
            if not data:
                break  
            print(f"Client says: {data.decode()}")
            conn.sendall(data)  # Step 5: Send data back (echo)
