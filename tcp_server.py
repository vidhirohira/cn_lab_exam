import socket

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)
    print("TCP Server listening on port 12345")

    while True:
        client_socket, client_addr = server_socket.accept()
        print("Connection from", client_addr)
        data = client_socket.recv(1024)
        if data:
            print("Received:", data.decode())
            client_socket.sendall(b"Hello from TCP Server")
        client_socket.close()

if __name__ == "__main__":
    tcp_server()
