import socket, pickle
from lek import Lek

lekovi = {}
lekovi[1] = Lek(1, "Lek broj jedan", "2024-04-05")
lekovi[2] = Lek(2, "Lek broj dva", "2024-04-08")
lekovi[3] = Lek(3, "Lek broj tri", "2024-04-06")

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

def pisi_u_fajl(naziv_datoteke, rezim_otvaranja, podaci = lekovi):
    f = open(naziv_datoteke, rezim_otvaranja)
    pickle.dump(podaci, f)
    f.close()

def procitaj_iz_fajla(naziv_datoteke, rezim_otvaranja):
    f = open(naziv_datoteke, rezim_otvaranja)
    data = bytes()
    data = pickle.load(f)
    f.close()
    return data


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
        if opcija == "ADD": # Dodaj lek
            odgovor = dodaj_lek(kanal.recv(1024))
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
        elif opcija == "BACKUP": # Upisi sve u fajl backup.txt                 
            pisi_u_fajl("backup.txt", "wb")           
            odgovor = ("Uspesno upisani svi podaci u tekstualni fajl!").encode()
        elif opcija == "REPLICATE": # Kopiraj fajl na drugu lokaciju
            location = kanal.recv(1024).decode()
            data = procitaj_iz_fajla("backup.txt", "rb")
            pisi_u_fajl(location + "/backup.txt", "wb", data) #ocekujemo da folder postoji        
            odgovor = ("Uspesno prekopiran fajl na drugu lokaciju!").encode()
        elif opcija == "READ_ALL": # Pročitaj sve za replikaciju
            global lekovi
            kanal.send(pickle.dumps(lekovi))
            odgovor = ("Uspesno procitani svi podaci!").encode()            
        elif opcija == "WRITE_ALL": # Pročitaj sve za replikaciju
            lekovi = pickle.loads(kanal.recv(1024))
            odgovor = ("Uspesno upisani svi podaci!").encode()
            print("Replicirano:")
            for l in lekovi.values(): print(l)        
        kanal.send(odgovor)
    
    print("Server se gasi.")
    server.close()


main()

    
