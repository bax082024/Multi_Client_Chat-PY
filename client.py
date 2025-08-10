import socket
import threading
import sys

SERVER_HOST = "127.0.0.1"  # change to server IP if connecting over LAN
SERVER_PORT = 65432

def listen(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                print("\n[Disconnected]")
                break
            print(data.decode("utf-8"), end="")
    except Exception:
        pass
    finally:
        try:
            sock.close()
        except:
            pass
        os._exit(0)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        threading.Thread(target=listen, args=(s,), daemon=True).start()

        try:
            for line in sys.stdin:
                s.sendall(line.encode("utf-8"))
                if line.strip().lower() == "/quit":
                    break
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
