import hashlib
from korisnik import Korisnik

def hesiranje(str):
    return hashlib.sha256(str.encode()).hexdigest()

def dodaj_korisnika(korisnik,recnik):
    recnik[korisnik.user] = korisnik
    recnik[korisnik.user].passwd = hesiranje(korisnik.passwd)

def autentifikacija(user,passwd,recnik):
    if(user in recnik):
        print("Found user")
        if(recnik[user].passwd == passwd):
            recnik[user].auth = True
            return True
    return False
