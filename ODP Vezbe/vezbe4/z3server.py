class Student:
    def __init__(self,ime,prezime,brInd,prosek):
        self.ime = ime
        self.prezime = prezime
        self.brInd = brInd
        self.prosek = prosek

    def __str__(self):
        return f"Ime: {self.ime} Prezime: {self.prezime} BrIndeksa: {self.brInd} Prosek: {self.prosek}"


s1 = Student("Pera","Peric","Pr99/2020",7.4)
s2 = Student("Veljko","Lukic","Pr1/2021",9.2)
s3 = Student("Aleksa","Milicev","Pr68/2021",6.8)
studenti = {
    s1.brInd:s1,
    s2.brInd:s2,
    s3.brInd:s3
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
    if not poruka : break
    if poruka in studenti:
        kanal.send(str(studenti[poruka]).encode())
    else:
        kanal.send("Ne postoji ovaj student!".encode())
print("Server se gasi.")
server.close() 

