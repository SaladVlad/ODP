from korisnik import Korisnik
import hashlib

korisnici = {}

def hesiranje(tekst):
    return hashlib.sha256(tekst.encode()).hexdigest()

def dodaj_korisnika(korisnicko_ime, lozinka, prava=[]):
    korisnici[korisnicko_ime] = Korisnik(korisnicko_ime, hesiranje(lozinka), prava)

def autentifikacija(korisnicko_ime, lozinka):
    autentifikovan = False
    if (korisnicko_ime in korisnici) and (hesiranje(lozinka) == korisnici[korisnicko_ime].lozinka):
        autentifikovan = True
    korisnici[korisnicko_ime].autentifikovan = autentifikovan
    return autentifikovan

def korisnik_autentifikovan(korisnicko_ime):
    return korisnicko_ime in korisnici and korisnici[korisnicko_ime].autentifikovan == True 
    
def korisnik_autorizovan(korisnicko_ime, pravo_pristupa):
    return korisnicko_ime in korisnici and pravo_pristupa in korisnici[korisnicko_ime].prava
