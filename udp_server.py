import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 12346))
    print("UDP Server listening on port 12346")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print("From", addr, ":", data.decode())
        server_socket.sendto(b"Hello from UDP Server", addr)

if __name__ == "__main__":
    udp_server()
