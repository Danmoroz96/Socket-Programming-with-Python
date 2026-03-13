# Socket-Programming-with-Python
Learn the basics of TCP socket communication by creating a simple client–server system in Python.


This project consists of two Python scripts:

- **Server:** Listens for incoming TCP connections and prints received sensor data to the console.

- **Client:** Connects to the server, generates a random temperature reading (e.g., "Temperature: 24.5 C"), and sends it every 5 seconds.

## How to Run

### 1. Prerequisites
Ensure you have Python 3.x installed on your machine.

### 2. Running on Localhost
1. Open a terminal and run the server:
   ```bash
   python server1.py

2. Open a second terminal and run the client:

python client1.py

3. Running via Mobile Hotspot / WiFi
Connect both devices to the same hotspot.

Find the Server's IP address (using ipconfig on Windows).

Update the SERVER_IP variable in client.py with that address.

Run the server on the first device and the client on the second.

Test Environment,Status and Notes: 


Localhost - PASS, Successful communication on 192.168.89.175


Mobile Hotspot - PASS,Connected via Samsung Hotspot (Laptop to mobile phone Samsung)

