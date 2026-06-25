import socket
import threading

# Configuration
HOST = '127.0.0.1'  # localhost
PORT = 55555

# List to keep track of active client connections
clients = []

def broadcast(message, current_client):
    """Sends a message to all clients except the sender."""
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                # Remove broken connections
                remove(client)

def handle_client(client):
    """Handles communication with a single client."""
    while True:
        try:
            # Receive message from client
            message = client.recv(1024)
            if message:
                print(f"Broadcasting: {message.decode('utf-8')}")
                broadcast(message, client)
            else:
                # If message is empty, client disconnected gracefully
                remove(client)
                break
        except:
            # Handle unexpected disconnections
            remove(client)
            break

def remove(client):
    """Removes a client from the tracking list and closes the socket."""
    if client in clients:
        clients.remove(client)
        client.close()
        print("A client has disconnected. Active clients:", len(clients))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}...")

    while True:
        # Accept incoming client connections
        client_socket, client_address = server.accept()
        print(f"Connected with {str(client_address)}")

        clients.append(client_socket)

        # Start a new thread to handle this specific client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()