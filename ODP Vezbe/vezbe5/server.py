import socket, pickle
from korisnik import Korisnik
import direktorijum_korisnika as dk

lekovi = {}

k1 = Korisnik("Veljko","12345",[2,4])
k2 = Korisnik("Pera","admin123",[1,2,3,4,5])

korisnici = {}

trenutni = ""

dk.dodaj_korisnika(k1,korisnici)
dk.dodaj_korisnika(k2,korisnici)

def autorizuj(user,pwd):
    if(dk.autentifikacija(user,pwd,korisnici)):
        pass
    else:
        return "ERROR".encode()
    
    trenutni = user
    return "OK".encode()


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

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 6000))
    server.listen()
    print("Server je pokrenut.")

    kanal, adresa = server.accept()
    print(f"Prihvacena je konekcija sa adrese: {adresa}")

    while True: 
        opcija = kanal.recv(1024).decode()
        if not opcija : break

        if opcija == "AUTH":
            parts = kanal.recv(1024).decode().split(',')
            odgovor = autorizuj(parts[0],parts[1])

            
        elif opcija == "ADD": # Dodaj lek

            if(1 in korisnici[trenutni].roles):
                odgovor = dodaj_lek(kanal.recv(1024))
            else:
                odgovor = "Error".encode()


        elif opcija == "UPDATE": # Izmeni lek
            odgovor = izmeni_lek(kanal.recv(1024))


        elif opcija == "DELETE": # Obrisi lek
            odgovor = izbrisi_lek(kanal.recv(1024).decode())


        elif opcija == "READ": # Procitaj lek
            odgovor = procitaj_lek(kanal.recv(1024).decode())   


        elif opcija == "ADD_INGR": # Dodaj sastojke
            id = kanal.recv(1024).decode()
            sastojci = kanal.recv(1024)
            odgovor = dodaj_sastojke(id, sastojci) 


        kanal.send(odgovor)
    
    print("Server se gasi.")
    server.close()


main()

    
