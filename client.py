import socket
import threading
from datetime import datetime

# Prompt user for their nickname
nickname = input("Choose your nickname: ")

# Configuration
HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Could not connect to the server. Is server.py running?")
    exit()

def receive_messages():
    """Continuously listens for messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                print("\nDisconnected from server.")
                client.close()
                break
        except:
            print("\nAn error occurred. Disconnecting...")
            client.close()
            break

def send_messages():
    """Continuously waits for user input to send messages."""
    while True:
        try:
            text = input("")
            if text.lower() == 'exit':
                print("Disconnecting gracefully...")
                client.close()
                break
            
            # Format: [HH:MM] Nickname: Message
            timestamp = datetime.now().strftime("%H:%M")
            formatted_message = f"[{timestamp}] {nickname}: {text}"
            
            client.send(formatted_message.encode('utf-8'))
        except:
            break

# Create and start threads for sending and receiving concurrently
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()