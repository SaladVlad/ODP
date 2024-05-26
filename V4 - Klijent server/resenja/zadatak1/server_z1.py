import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7000))
server.listen()
print("Server je pokrenut.")

kanal, adresa = server.accept()
print(f"Prihvacena je konekcija sa adrese: {adresa}")

while True: 
    poruka = kanal.recv(1024).decode()
    if not poruka : break

    if poruka == "1":
        odgovor = (str)(random.random()*100)
        kanal.send(odgovor.encode())
    else:
        kanal.send("Nevalidna opcija".encode())
print("Server se gasi.")
server.close()