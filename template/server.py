import socket, pickle
from user import *
import json

lekovi = dict()

korisnici = {}
korisnici["pera"] =  User("pera","peric")
korisnici["mika"] =  User("mika","miric",["ADD,DELETE"])
korisnici["admin"] = User("admin","admin",["ADD","UPDATE","DELETE","READ","READ_ALL","WRITE_ALL"])

trenutni = ""

def dodaj_lek(poruka):
    lek = pickle.loads(poruka)
    if lek.id in lekovi:
        odgovor = f"Lek sa id-em: {lek.id} vec postoji u bazi!"
    else:
        lekovi[lek.id] = lek
        odgovor = f"Lek sa id-em: {lek.id} uspesno upisan u bazu."
    print(odgovor)
    return odgovor.encode()

def izmeni_lek(poruka):
    lek = pickle.loads(poruka)
    if lek.id not in lekovi:
        odgovor = f"Lek sa id-em: {lek.id} ne postoji u bazi!"
    else:
        lekovi[lek.id] = lek
        odgovor = f"Lek sa id-em: {lek.id} uspesno izmenjen."
    print(odgovor)
    return odgovor.encode()
    
def izbrisi_lek(id):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
    else:
        del lekovi[id]
        odgovor = f"Lek sa id-em: {id} uspesno obrisan."
    print(odgovor)
    return odgovor.encode()

def procitaj_lek(id):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
        print(odgovor)
        return odgovor.encode()
    else:
        print(f"Uspesno procitan lek sa id-em: {id}.")
        odgovor = pickle.dumps(lekovi[id])
        return odgovor

def log_info(info):
    log = open("log.txt","a+")
    log.write(info + "\n")
    log.close()

def login(kanal):
    
    username = kanal.recv(1024).decode()
    password = kanal.recv(1024).decode()
    if username in korisnici.keys():
        if korisnici[username].password == hashlib.sha256(password.encode()).hexdigest():
            print("Uspesno logovanje, pisem u fajl...")
            log_info(f"Uspesno logovanje: korisnik {username}.")
            global trenutni
            trenutni = username
            return True
        else:
            print("Neuspesno logovanje, pisem u fajl...")
            log_info(f"Pokusaj logovanja sa username '{username}': LOSA SIFRA!")
            return False
    print("Neuspesno logovanje, pisem u fajl...")
    log_info(f"Neuspesno logovanje: korisnik {username} ne postoji!")
    return False

stanje = "nepoznato"

port = 0

def main():
    global port
    global lekovi

    port = int(input("Unesi broj porta: "))

    

    while True:

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', port))
        server.listen()
        print("Server je pokrenut.")

        kanal, adresa = server.accept()
        print(f"Prihvacena je konekcija sa adrese: {adresa}")

        while True:
            if(login(kanal)):
                kanal.send("Uspeh".encode())
                break
            else:
                kanal.send("Greska".encode())

        while True: 
            opcija = kanal.recv(1024).decode()
            
            if not opcija : break
            print(f"Opcija pristigla: {opcija}")
            if opcija == "ADD" and "ADD" in korisnici[trenutni].permissions: # Dodaj lek
                odgovor = dodaj_lek(kanal.recv(1024))
                fajl = open("lekovi.json","a+")
                json.dump(lekovi,fajl)
                fajl.close()
            elif opcija == "UPDATE" and "UPDATE" in korisnici[trenutni].permissions: # Izmeni lek
                odgovor = izmeni_lek(kanal.recv(1024))
            elif opcija == "DELETE" and "DELETE" in korisnici[trenutni].permissions: # Obrisi lek
                odgovor = izbrisi_lek(kanal.recv(1024).decode())
            elif opcija == "READ" and "READ" in korisnici[trenutni].permissions: # Procitaj lek
                odgovor = procitaj_lek(kanal.recv(1024).decode())            
            elif opcija == "READ_ALL" and "READ_ALL" in korisnici[trenutni].permissions: # Pročitaj sve za replikaciju
                odgovor = pickle.dumps(lekovi)
            elif opcija == "WRITE_ALL" and "WRITE_ALL" in korisnici[trenutni].permissions: # Pročitaj sve za replikaciju
                lekovi = pickle.loads(kanal.recv(1024))
                log_info(f"Uspesna replikacija na server sa portom '{port}'")
            elif opcija == "SET_STATE":
                global stanje
                stanje = kanal.recv(1024).decode()
                print(f"Promenjeno stanje servera na {stanje}")
                odgovor = stanje.encode()

            

            else:
                odgovor = "Nemate pravo za ovu akciju!".encode()
            try:
                kanal.send(odgovor)
            except Exception as ex:
                print(ex)
        
        print("Server zavrsio sa radom.")
        server.close()

main()

    
