class Lek:
    def __init__(self, id, naziv, datum):
        self.id = id
        self.naziv = naziv
        self.datum = datum
        self.sastojci = []

    def __str__(self) -> str:
        return f"{self.id} - {self.naziv} - {self.datum}, sastojci: {self.sastojci}"

