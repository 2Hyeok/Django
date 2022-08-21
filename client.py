# client py
from socket import socket, AF_INET, SOCK_STREAM
clientSock = socket(AF_INET, SOCK_STREAM) # 서버와 옵션이 똑같아야함
clientSock.connect(("localhost", 3000)) # 값을 튜플로 주어야함
print("연결했습니다")
clientSock.send("I am a client".encode("utf-8"))
print("메시지를 보냈습니다.")
data = clientSock.recv(1024)
print("받은데이터 :", data.decode("utf-8"))