import socket
import threading
from db import init_db, save_message, get_user

HOST = '0.0.0.0'
PORT = 5000

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message)

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    try:
        auth_msg = client_socket.recv(1024).decode()
        if not auth_msg:
            client_socket.close()
            return
            
        parts = auth_msg.split(":")
        if len(parts) == 2:
            username, password = parts
            if get_user(username, password):
                client_socket.send("AUTH_OK".encode())
                clients.append(client_socket)
            else:
                client_socket.send("AUTH_FAIL".encode())
                client_socket.close()
                return
        else:
            client_socket.send("AUTH_FAIL".encode())
            client_socket.close()
            return

        while True:
            message = client_socket.recv(1024)
            if not message:
                break

            decoded = message.decode()
            print(f"[{addr}] {decoded}")

            save_message(username, decoded)
            broadcast(message, client_socket)

    except:
        pass
    finally:
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()
        print(f"[DISCONNECTED] {addr}")

def start_server():
    init_db()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[STARTED] Server running on port {PORT}")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
