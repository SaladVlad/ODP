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

def pokupi_informacije_sastojci_za_slanje():
    sastojci = input("Sastojci (odvojeni zarezom) -> ").split(',')
    return pickle.dumps(sastojci)

def pokupi_informaciju_za_lokaciju_fajla():
    return input("Putanja fajla -> ").encode()

def main():
    kanal_server_primarni = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    kanal_server_primarni.connect(('localhost', 6000))
    print("Veza sa primarnim serverom je uspostavljena.")

    kanal_server_sekundarni = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    kanal_server_sekundarni.connect(('localhost', 7000))
    print("Veza sa sekundardnim serverom je uspostavljena.")

    while True: 
        operacija = input("Odaberite operaciju: \n1.Dodaj lek \n2.Izmeni lek \n3.Obrisi lek\n4.Procitaj lek\n5.Dodaj sastojke\n6.Repliciraj podatke putem fajla\n7.Repliciraj podatke\n") 
        if not operacija : break         
        if operacija == "1": # Dodaj lek   
            kanal_server_primarni.send(("ADD").encode())  
            kanal_server_primarni.send(pokupi_informacije_leka_za_slanje())
            print(kanal_server_primarni.recv(1024).decode())
        elif operacija == "2": # Izmeni lek 
            kanal_server_primarni.send(("UPDATE").encode())
            kanal_server_primarni.send(pokupi_informacije_leka_za_slanje())
            print(kanal_server_primarni.recv(1024).decode())
        elif operacija == "3": # Obrisi lek 
            kanal_server_primarni.send(("DELETE").encode())
            kanal_server_primarni.send(pokupi_informaciju_id_leka_za_slanje())
            print(kanal_server_primarni.recv(1024).decode())     
        elif operacija == "4": # Procitaj lek 
            kanal_server_primarni.send(("READ").encode())
            kanal_server_primarni.send(pokupi_informaciju_id_leka_za_slanje())
            iscitaj_lek(kanal_server_primarni.recv(1024))
        elif operacija == "5": # Dodaj sastojke 
            kanal_server_primarni.send(("ADD_INGR").encode())
            kanal_server_primarni.send(pokupi_informaciju_id_leka_za_slanje())        
            kanal_server_primarni.send(pokupi_informacije_sastojci_za_slanje())
            print(kanal_server_primarni.recv(1024).decode())
        elif operacija == "6" :
            kanal_server_primarni.send(("BACKUP").encode())
            print(kanal_server_primarni.recv(1024).decode()) 
            kanal_server_primarni.send(("REPLICATE").encode())            
            kanal_server_primarni.send(pokupi_informaciju_za_lokaciju_fajla())   
            print(kanal_server_primarni.recv(1024).decode())    
        elif operacija == "7": # Repliciraj podatke 
            kanal_server_primarni.send(("READ_ALL").encode())
            kanal_server_sekundarni.send(("WRITE_ALL").encode())
            kanal_server_sekundarni.send(kanal_server_primarni.recv(1024))
            print(kanal_server_primarni.recv(1024).decode())
            print(kanal_server_sekundarni.recv(1024).decode())    
        else:
            print("Molimo unesite validnu operaciju.")
            continue

    kanal_server_primarni.close() 
    print("Zatvaranje konekcije.")
    
main()