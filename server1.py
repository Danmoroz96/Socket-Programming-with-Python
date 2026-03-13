import socket

def start_server():
    # Define host and port
    HOST = '0.0.0.0'  # Listens on all available interfaces
    PORT = 65432      # Non-privileged port

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server started. Listening on {HOST}:{PORT}...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_server()