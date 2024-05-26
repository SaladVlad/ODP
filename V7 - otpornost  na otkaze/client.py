import socket, pickle
from datetime import date
from lek import Lek

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
    try:
        klijentP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        klijentP.connect(('localhost', 6000))
        print("Veza sa serverom na portu 6000 je uspostavljena.")
    except Exception as ex:
        print(ex)

    try:
        klijentS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        klijentS.connect(('localhost', 7000))
        print("Veza sa serverom na portu 7000 je uspostavljena.")
    except Exception as ex:
        print(ex)

    while True:             
        operacija = input("Odaberite operaciju: \n1.Dodaj lek \n2.Izmeni lek \n3.Obrisi lek\n4.Procitaj lek\n5.Dodaj sastojke\n") 
        if not operacija : break         
        if operacija == "1": # Dodaj lek
            try:   
                klijentP.send(("ADD").encode())  
                klijentP.send(pokupi_informacije_leka_za_slanje())
                print(klijentP.recv(1024).decode())
            except Exception as ex:
                print(ex)
                try:   
                    klijentS.send(("ADD").encode())  
                    klijentS.send(pokupi_informacije_leka_za_slanje())
                    print(klijentS.recv(1024).decode())
                except Exception as ex:
                    print(ex)
        elif operacija == "2": # Izmeni lek 
            try:   
                klijentP.send(("UPDATE").encode())
                klijentP.send(pokupi_informacije_leka_za_slanje())
                print(klijentP.recv(1024).decode())
            except Exception as ex:
                print(ex)
                try:   
                    klijentS.send(("UPDATE").encode())
                    klijentS.send(pokupi_informacije_leka_za_slanje())
                    print(klijentS.recv(1024).decode())
                except Exception as ex:
                    print(ex)
        elif operacija == "3": # Obrisi lek 
            klijentP.send(("DELETE").encode())
            klijentP.send(pokupi_informaciju_id_leka_za_slanje())
            print(klijentP.recv(1024).decode())     
        elif operacija == "4": # Procitaj lek 
            klijentP.send(("READ").encode())
            klijentP.send(pokupi_informaciju_id_leka_za_slanje())
            iscitaj_lek(klijentP.recv(1024))
        elif operacija == "5": # Dodaj sastojke 
            klijentP.send(("ADD_INGR").encode())
            klijentP.send(pokupi_informaciju_id_leka_za_slanje())        
            klijentP.send(popupi_informacije_sastojci_za_slanje())
            print(klijentP.recv(1024).decode())    
        else:
            print("Molimo unesite validnu operaciju.")
            continue

    klijentP.close() 
    print("Zatvaranje konekcije.")
    
main()