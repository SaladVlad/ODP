#1
f1 = open("zadatak1.txt","w")
f1.write("Vladislav Petkovic PR40-2021")
f1.close()

#2
f2 = open("zadatak2.txt","w")
x = 0
##while(x<5):
##    string = input("Enter text: ")
##    string = "\n"+string
##    f2.write(string)
##    x+=1

f2.close()

f2 = open("zadatak2.txt","r")
print(f2.read())
f2.close()

#3
import pickle

class Student:
    def __init__(self, ime, prezime, broj_indeksa, prosek):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa
        self.prosek = prosek

    def __str__(self) -> str:
        return f"{self.broj_indeksa} {self.prezime} {self.ime}, prosek: {self.prosek}"


lista_studenata = []
f3 = open("S:\\ODP Vezbe\\V3 - Klase i rad sa datotekama\\zadaci\\zadatak3.txt","r")
for line in f3:
    words = line.split("|")
    s = Student(words[0],words[1],words[2],words[3])
    lista_studenata.append(s)
f3.close()

for l in lista_studenata:
    print(l)

#4
f4 = open("zadatak4.txt","wb")
for s in lista_studenata:
    pickle.dump(s,f4)

#5
import datetime
import json
class Ispit:
    
    def __init__(self,datum,brUc,naziv):
        self.datum = datum
        self.brUc = brUc
        self.naziv = naziv

p1 = Ispit(datetime.date(2024,7,14),109,"Osnove distribuiranog programiranja")
f5 = open("zadatak5.json","w")
json.dump(p1.__dict__,f5)
f5.close()
