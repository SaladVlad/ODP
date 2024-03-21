import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

klijent.connect(('localhost', 6000))
print("Veza sa serverom je uspostavljena.")
while True: 
    poruka = input("Unesite poruku: ")
    if not poruka : break
    klijent.send(poruka.encode())
    odgovor = klijent.recv(1024).decode()
    print("Odgovor: ", odgovor)
print("Konekcija se zatvara.")
klijent.close()