class Korisnik:
    def __init__(self, korisnicko_ime, lozinka, prava=[]):
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.autentifikovan = False
        self.prava = prava