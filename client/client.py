import socket
import threading

HOST = '127.0.0.1' # cambiar cuando se use en red
PORT = 5000

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            print(message)
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    username = input("Username: ")
    password = input("Password: ")
    client.send(f"{username}:{password}".encode())
    
    response = client.recv(1024).decode()
    if response == "AUTH_OK":
        print("Login successful")
    elif response == "AUTH_FAIL":
        print("Invalid credentials")
        client.close()
        return

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        client.send(msg.encode())

if __name__ == "__main__":
    start_client()
