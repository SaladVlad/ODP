import socket, pickle
from lek import Lek
import time

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

both_active = False

def pokupi_informacije_leka_za_slanje():
    id = input("ID leka -> ")
    naziv = input("Naziv leka -> ")
    lek = Lek(id, naziv)
    return pickle.dumps(lek)

def pokupi_informaciju_id_leka_za_slanje():
    return input("ID leka -> ").encode()

def iscitaj_lek(odgovor):
    try:
        lek = pickle.loads(odgovor)
        print(lek)
    except:
        print(odgovor.decode())


def trazi_server(monitor):
    global klijent
    print("Traze se serveri koji su dostupni...")

    monitor.send("CHECK_STATES".encode())
    port1,stanje1 = monitor.recv(1024).decode().split(':')
    port2,stanje2 = monitor.recv(1024).decode().split(':')

    print(f"Stanja servera:\n1.{stanje1}\n2.{stanje2}")

    time.sleep(2)

    print("Pokusaj povezivanja sa primarnim serverom")
    if stanje1 == "Primarni":

        klijent.connect(('localhost', int(port1)))
        print("Veza sa prvim serverom je uspostavljena.")
        return True
    if stanje2 == "Primarni":
        klijent.connect(('localhost', int(port2)))
        print("Veza sa drugim serverom je uspostavljena.")
        return True
    return False

def login(socket):

    uname = input("Unesite username:")
    socket.send(uname.encode())
    pw = input("Unesite lozinku:")
    socket.send(pw.encode())
    odgovor = socket.recv(1024).decode()
    if "Uspeh" in odgovor: return True
    print("Neuspesno logovanje, pokusajte opet.")
    return False


def main():

    monitor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    monitor.connect(('localhost',8000))
    while True:
        global klijent
        try:
            
            if not trazi_server(monitor):
                print("Nije nadjen nijedan server, gasim...")
                break
            print("Nadjen server, pocinjem sa radom...")
            while True:
                if(login(klijent)):
                    break

            while True: 
                operacija = input("Odaberite operaciju: \n1.Dodaj lek \n2.Izmeni lek \n3.Obrisi lek\n4.Procitaj lek\n5.Repliciraj podatke\n") 
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
                elif operacija == "5": # Replikacija nad 2 servera, ako su dostupna
                    if not both_active:
                        
                        print("Oba servera moraju da budu dostupna")

                else:
                    print("Molimo unesite validnu operaciju.")
                    continue
        except Exception as e: #doslo je do greske u konekciji, mora se pozvati monitor da vidi sta je dostupno
            print(e)
            print("Greska sa trenutnim serverom, trazenje drugog...")
            klijent.close()
            klijent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    klijent.close()
    print("Zatvaranje konekcije.")
    
main()