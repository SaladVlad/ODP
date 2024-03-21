import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

klijent.connect(('localhost', 6000))
print("Veza sa serverom je uspostavljena.")
while True: 
    poruka = input("Unesi izraz za racunanje: ")
    if not poruka : break
    klijent.send(poruka.encode())
    odgovor = klijent.recv(1024).decode()
    print("Resenje: ", odgovor)
print("Konekcija se zatvara.")
klijent.close()