class Student:
    def __init__(self, ime, prezime, broj_indeksa, prosek):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa
        self.prosek = prosek

    def __str__(self) -> str:
        return f"{self.broj_indeksa} {self.prezime} {self.ime}, prosek: {self.prosek}"