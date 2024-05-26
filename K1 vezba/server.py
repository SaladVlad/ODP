
import socket, pickle

lekovi = {}

def dodaj_lek():
    pass

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',7000))
server.listen()
print("Slusam ja sad sve...")

kanal,adresa = server.accept()
while True:
    opcija = kanal.recv(1024).decode()
    if not opcija : break
    if opcija == 'ADD':
        odgovor = dodaj_lek()
    elif opcija == 'LIST':
        odgovor = pickle.dumps(lekovi)
        kanal.send(odgovor)
    else:
        pass

server.close()



