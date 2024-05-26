import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(('localhost', 7000))
print("Veza sa serverom je uspostavljena.")

while True: 
    poruka = input("Unesite neku poruku:")
    if not poruka : break 
    klijent.send(poruka.encode()) 
    odgovor = klijent.recv(1024).decode()
    print(f"Server je odgovorio: {odgovor}")
print("Konekcija se zatvara.")
klijent.close()