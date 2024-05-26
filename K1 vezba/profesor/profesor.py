class Profesor:

    def __init__(self,jmbg,ime,prezime,datum_izbora,predmeti=[]):
        self.jmbg = jmbg
        self.ime = ime
        self.prezime = prezime
        self.datum_izbora = datum_izbora
        self.predmeti = predmeti

    def __str__(self) -> str:
        return f"[{self.jmbg}] {self.ime} {self.prezime} : {self.datum_izbora}\n---Predmeti----\n{self.predmeti}\n-------------"
