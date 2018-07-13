import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000))
print("已连接到服务端")
while True:
    re_data = input()
    if re_data == "exit":
        client.close()
    client.send(re_data.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode("utf-8"))
    # sock.send("hello {}".format(data.decode("utf-8")).encode("utf-8"))
