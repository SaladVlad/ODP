class Lek:
    def __init__(self,id,naziv,datum_proizvodnje,sastojci):
        self.id = id
        self.naziv = naziv
        self.datum_proizvodnje = datum_proizvodnje
        self.sastojci = sastojci

    def __str__(self):
        return f"id: {self.id} naziv: {self.naziv} datum_proizvodnje: {self.datum_proizvodnje} sastojci: {self.sastojci}"


s1 = Lek(11,"Cedevita","",7.4)
studenti = {
    s1.id:s1
}

import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 6000))
server.listen()
print("Server je pokrenut.")

kanal, adresa = server.accept()
print(f"Prihvacena je konekcija sa adrese: {adresa}")

while True:
    poruka = kanal.recv(1024).decode()
    print(poruka)
    if not poruka : break
    parts = poruka.split(" ")
    if len(parts)==1 and poruka in studenti:

        kanal.send(str(studenti[poruka]).encode())
    else:
        kanal.send("Ne postoji lik sa tim indeksom".encode())
    
    if len(parts)==4:
        s = Student(parts[1],parts[2],parts[0],float(parts[3]))
        studenti.update({s.brInd:s})
    else:
        kanal.send("Ne postoji ovaj student!".encode())
print("Server se gasi.")
server.close() 

