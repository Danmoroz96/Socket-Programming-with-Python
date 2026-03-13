import socket
import time
import random

def start_client():
    # Use '127.0.0.1' for localhost or the Server's IP for WiFi testing
    SERVER_IP = '192.168.89.175' 
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((SERVER_IP, PORT))
            print(f"Connected to server at {SERVER_IP}")

            while True:
                # Generate random sensor data
                temp = round(random.uniform(20.0, 30.0), 1)
                message = f"Temperature: {temp} C"
                
                # Send data
                s.sendall(message.encode('utf-8'))
                print(f"Sent: {message}")
                
                # Wait for 5 seconds
                time.sleep(5)
        except ConnectionRefusedError:
            print("Error: Could not connect to the server. Is it running?")

if __name__ == "__main__":
    start_client()