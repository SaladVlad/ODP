import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 6000))

server.listen()
print("Server je pokrenut.")

kanal, adresa = server.accept()
print(f"Prihvacena je konekcija sa adrese: {adresa}")
while True:
    poruka = kanal.recv(1024).decode()
    if not poruka : break

    answer = str(eval(poruka)) #very very dangerous but works!

    kanal.send(answer.encode())
print("Server se gasi.")
server.close() 