import socket, pickle
from direktorijum_korisnika import *

lekovi = {}

def log_info(message):
    # Log
    log = open("log.txt", "a")
    log.write(message + "\n")
    log.close()

def dodaj_lek(poruka):
    lek = pickle.loads(poruka)
    if lek.id in lekovi:
        odgovor = f"Lek sa id-em: {lek.id} vec postoji u bazi!"
    else:
        lekovi[lek.id] = lek
        odgovor = f"Lek sa id-em: {lek.id} uspesno upisan u bazu."
    log_info(odgovor)
    return odgovor.encode()

def izmeni_lek(poruka):
    lek = pickle.loads(poruka)
    if lek.id not in lekovi:
        odgovor = f"Lek sa id-em: {lek.id} ne postoji u bazi!"
    else:
        lekovi[lek.id] = lek
        odgovor = f"Lek sa id-em: {lek.id} uspesno izmenjen."
    log_info(odgovor)
    return odgovor.encode()
    
def izbrisi_lek(id):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
    else:
        del lekovi[id]
        odgovor = f"Lek sa id-em: {id} uspesno obrisan."
    log_info(odgovor)
    return odgovor.encode()

def procitaj_lek(id):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
        log_info(odgovor)
        return odgovor.encode()
    else:
        odgovor = pickle.dumps(lekovi[id])
        return odgovor
    

def dodaj_sastojke(id, podaci):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
    else:
        sastojci = pickle.loads(podaci)
        lekovi[id].sastojci.extend(sastojci)
        odgovor = f"Uspesno dodati sastojci za lek sa id-em: {id}."
        print(odgovor)
    log_info(odgovor)
    return odgovor.encode()

def inicijalizuj_korisnike():
    dodaj_korisnika("test", "test")
    dodaj_korisnika("pera", "p3r@", ["READ", "ADD", "ADD_INGR"])
    dodaj_korisnika("admin", "Adm1n", ["READ", "ADD", "ADD_INGR", "UPDATE", "DELETE"])

def kreiraj_poruku(pravo_pristupa):
    return f"Niste se uspesno autorizovali nemate pravo pristupa {pravo_pristupa}".encode()

def main():
    inicijalizuj_korisnike()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 6000))
    server.listen()
    print("Server je pokrenut.")

    kanal, adresa = server.accept()
    print(f"Prihvacena je konekcija sa adrese: {adresa}")
    
    while True:
        korisnicko_ime = kanal.recv(1024).decode()
        lozinka = kanal.recv(1024).decode()
        if autentifikacija(korisnicko_ime, lozinka):
            kanal.send(("Uspesna autentifikacija!").encode())
            break
        else:
            kanal.send(("Neuspesna autentifikacija!").encode())

    while True: 
        opcija = kanal.recv(1024).decode()
        if not opcija : break
        elif opcija == "ADD": # Dodaj lek
            lek = kanal.recv(1024)
            if korisnik_autorizovan(korisnicko_ime, opcija):
                odgovor = dodaj_lek(lek)
            else:
                odgovor = kreiraj_poruku(opcija)
        elif opcija == "UPDATE": # Izmeni lek
            lek = kanal.recv(1024)
            if korisnik_autorizovan(korisnicko_ime, opcija):
                odgovor = izmeni_lek(lek)
            else:
                odgovor = kreiraj_poruku(opcija) 
        elif opcija == "DELETE" : # Obrisi lek
            id = kanal.recv(1024).decode()
            if korisnik_autorizovan(korisnicko_ime, opcija):
                odgovor = izbrisi_lek(id)
            else:
                odgovor = kreiraj_poruku(opcija)
        elif opcija == "READ": # Procitaj lek
            id = kanal.recv(1024).decode()
            if korisnik_autorizovan(korisnicko_ime, opcija):
                odgovor = procitaj_lek(id)
            else:
                odgovor = kreiraj_poruku(opcija)          
        elif opcija == "ADD_INGR": # Dodaj sastojke
            id = kanal.recv(1024).decode()
            sastojci = kanal.recv(1024)
            if korisnik_autorizovan(korisnicko_ime, opcija):
                odgovor = dodaj_sastojke(id, sastojci) 
            else:
                odgovor = kreiraj_poruku(opcija)                            
        kanal.send(odgovor)
    
    print("Server se gasi.")
    server.close()


main()

    
