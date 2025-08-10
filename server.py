import socket
import threading

HOST = "0.0.0.0"
PORT = 65432

clients = {} 
clients_lock = threading.Lock()

def broadcast(msg, exclude_conn=None):
    """Send msg to all connected clients (optionally excluding one)."""
    with clients_lock:
        dead = []
        for conn in clients:
            if conn is exclude_conn:
                continue
            try:
                conn.sendall(msg.encode("utf-8"))
            except Exception:
                dead.append(conn)
        for d in dead:
            try:
                d.close()
            except:
                pass
            clients.pop(d, None)

def handle_client(conn, addr):
    try:
        conn.sendall("Welcome! Enter your nickname: ".encode("utf-8"))
        nickname = conn.recv(1024).decode("utf-8").strip() or f"user@{addr[0]}"
        with clients_lock:
            clients[conn] = nickname

        broadcast(f"*** {nickname} joined the chat ***\n")
        conn.sendall("Type /quit to leave. Type /list to see users.\n".encode("utf-8"))

        while True:
            data = conn.recv(4096)
            if not data:
                break
            msg = data.decode("utf-8").rstrip("\n")
            if msg.lower() == "/quit":
                break
            if msg.lower() == "/list":
                with clients_lock:
                    names = ", ".join(clients.values())
                conn.sendall(f"Online: {names}\n".encode("utf-8"))
                continue
            broadcast(f"[{nickname}] {msg}\n", exclude_conn=None)
    except Exception:
        pass
    finally:
        with clients_lock:
            nickname = clients.pop(conn, "someone")
        broadcast(f"*** {nickname} left the chat ***\n")
        try:
            conn.close()
        except:
            pass

def main():
    print(f"Chat server listening on {HOST}:{PORT} ...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()
