# server.py
from socket import socket, AF_INET, SOCK_STREAM
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(("", 3000)) # 주소를 묶다, 튜플로 주어야함
serverSock.listen(1) # 기다려라!
connectionSock, addr = serverSock.accept() # 커넥션 소켓과, 접속자의 주소를 받아옴
print(str(addr), "님이 이미 접속했습니다.")
data = connectionSock.recv(1024) # 받겠다, 1Kb
print("받은메시지 :", data.decode("utf-8"))
connectionSock.send("I am a Server".encode("utf-8")) 
print("메시지를 보냈습니다.")