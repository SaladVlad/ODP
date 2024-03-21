import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

klijent.connect(('localhost', 6000))
print("Veza sa serverom je uspostavljena.")
while True: 
    izbor = input("Sta zelis da radis? \n1.Napravi novog studenta\n2.Izmeni postojeceg\n3.Listaj")
    if not izbor : break

    if izbor == "1":
        poruka = ""
        poruka += input("Broj Indeksa: ") + " "
        poruka += input("Ime: ") + " "
        poruka += input("Prezime: ") + " "
        poruka += input("Prosek: ")

        klijent.send(poruka.encode())
        if klijent.recv(1024).decode() == "success":
            print("Added new student")

    if izbor == "2":
        poruka = ""
        poruka += input("Broj Indeksa: ") + " "
        poruka += input("Ime: ") + " "
        poruka += input("Prezime: ") + " "
        poruka += input("Prosek: ")

        klijent.send(poruka.encode())
        if klijent.recv(1024).decode() == "success":
            print("Izmenjen student")
    
    if izbor == "3":
        poruka = input("Unesi broj indeksa: ")
        klijent.send(poruka.encode())
        odgovor = klijent.recv(1024).decode()
        print("Informacije: ", odgovor)

print("Konekcija se zatvara.")
klijent.close()