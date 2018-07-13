import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()

def handle_socket(sock, addr):
    while True:
        data = sock.recv(1024)
        if data == "exit":
            sock.close()
        print(data.decode("utf-8"))
        # sock.send("hello {}".format(data.decode("utf-8")).encode("utf-8"))
        re_data = input()
        sock.send(re_data.encode("utf-8"))

# 获取客户端发送的数据# 一次获取1k的数据
while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_socket, args=(sock, addr))
    client_thread.start()