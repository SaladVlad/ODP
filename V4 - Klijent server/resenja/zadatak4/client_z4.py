import socket, pickle
from student import Student

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(('localhost', 6000))
print("Veza sa serverom je uspostavljena.")

while True: 
    operacija = int(input("Odaberite operaciju: \n1.Dodavanje \n2.Izmena \n3.Čitanje \n")) 
    if not operacija : break 
    if operacija == 1 or operacija == 2: # DODAJ ili IZMENI      
        br_indeksa = input("Broj indeksa -> ")
        ime = input("Ime -> ")
        prezime = input("Prezime -> ")
        prosek = input("Prosek -> ")
        student = Student(ime, prezime, br_indeksa, prosek)
        klijent.send(pickle.dumps(student))
        print(klijent.recv(1024).decode())
    elif operacija == 3: # PROCITAJ
        br_indeksa = input("Broj indeksa -> ")
        klijent.send(br_indeksa.encode())
        print(klijent.recv(1024).decode())        
    else:
        print("Molimo unesite validnu opciju.")
        continue

klijent.close() 
print("Zatvaranje konekcije.")