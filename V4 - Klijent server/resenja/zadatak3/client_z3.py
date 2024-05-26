import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(('localhost', 6000))
print("Veza sa serverom je uspostavljena.")

while True: 
    broj_indeksa = input("Unesite broj indeksa studenta čije podatke želite:")
    if not broj_indeksa : break 
    klijent.send(broj_indeksa.encode()) 
    student = klijent.recv(1024).decode()
    print(f"Podaci o traženom studentu: {student}")
print("Konekcija se zatvara.")
klijent.close()