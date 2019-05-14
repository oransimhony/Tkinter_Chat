import socket

server_host = ('127.0.0.1', 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_host)

clients = []

while True:
    try:
        data, addr = sock.recvfrom(4096)
        if data:
            if addr not in clients:
                clients.append(addr)
            if len(data.strip()):
                for client_addr in clients:
                    sock.sendto(data, client_addr)
    except OSError:
        continue
