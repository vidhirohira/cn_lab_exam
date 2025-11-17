import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"Hello from UDP Client", ("localhost", 12346))
    data, addr = client_socket.recvfrom(1024)
    print("Received:", data.decode())
    client_socket.close()

if __name__ == "__main__":
    udp_client()
