import socket, pickle
from datetime import date
from lek import Lek

from direktorijum_korisnika import hesiranje

def pokupi_informacije_leka_za_slanje():
    id = input("ID leka -> ")
    naziv = input("Naziv leka -> ")
    godina, mesec, dan = input("Godina, mesec, dan proizvodnje u obliku YYYY-MM-DD -> ").split('-')
    lek = Lek(id, naziv, date(int(godina), int(mesec), int(dan)))
    return pickle.dumps(lek)

def pokupi_informaciju_id_leka_za_slanje():
    return input("ID leka -> ").encode()

def iscitaj_lek(odgovor):
    try:
        lek = pickle.loads(odgovor)
        print(lek)
    except:
        print(odgovor.decode())

def popupi_informacije_sastojci_za_slanje():
    sastojci = input("Sastojci (odvojeni zarezom) -> ").split(',')
    return pickle.dumps(sastojci)

def main():
    klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klijent.connect(('localhost', 6000))
    print("Veza sa serverom je uspostavljena.")

    while(True):
        uname = input("Unesite korisnicko ime: ")
        passwd = input("Unesite lozinku: ")
        klijent.send(("AUTH").encode())
        klijent.send((uname+","+hesiranje(passwd)).encode())
        if(klijent.recv(1024).decode() == "OK"):
            print("Logovanje uspesno!")
            break
        else:
            print("Pokusajte ponovo.")

    while True: 
        operacija = input("Odaberite operaciju: \n1.Dodaj lek \n2.Izmeni lek \n3.Obrisi lek\n4.Procitaj lek\n5.Dodaj sastojke\n") 
        if not operacija : break         
        if operacija == "1": # Dodaj lek   
            klijent.send(("ADD").encode())  
            klijent.send(pokupi_informacije_leka_za_slanje())
            print(klijent.recv(1024).decode())
        elif operacija == "2": # Izmeni lek 
            klijent.send(("UPDATE").encode())
            klijent.send(pokupi_informacije_leka_za_slanje())
            print(klijent.recv(1024).decode())
        elif operacija == "3": # Obrisi lek 
            klijent.send(("DELETE").encode())
            klijent.send(pokupi_informaciju_id_leka_za_slanje())
            print(klijent.recv(1024).decode())     
        elif operacija == "4": # Procitaj lek 
            klijent.send(("READ").encode())
            klijent.send(pokupi_informaciju_id_leka_za_slanje())
            iscitaj_lek(klijent.recv(1024))
        elif operacija == "5": # Dodaj sastojke 
            klijent.send(("ADD_INGR").encode())
            klijent.send(pokupi_informaciju_id_leka_za_slanje())        
            klijent.send(popupi_informacije_sastojci_za_slanje())
            print(klijent.recv(1024).decode())    
        else:
            print("Molimo unesite validnu operaciju.")
            continue

    klijent.close() 
    print("Zatvaranje konekcije.")
    
main()