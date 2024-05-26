# KLASE (str. 37)

# Zadatak 1
# Napisati klasu za studente FTNa. 
# Neka atribut fakultet bude zajednički za sve instance ove klase, 
# a neka se kroz konstruktor inicijalizuju ime, prezime i broj indeksa. 
# Definisati metodu koja će prilikom ispisa objekta ispisivati vrednosti 
# ova četiri atributa. 
# Instancirati barem dva studenta i ispisati ih.
class Student:
    fakultet = "FTN"
    def __init__(self, ime, prezime, br_indeksa):
      self.ime = ime
      self.prezime = prezime
      self.br_indeksa = br_indeksa
    
    def __str__(self):
       return f"{self.fakultet} {self.br_indeksa} {self.ime} {self.prezime}"

student1 = Student("Marko", "Markovic", "PR1/2020")
student2 = Student(ime ="Jovan", prezime = "Jovanovic", br_indeksa ="PR2/2020")
student3 = Student(prezime = "Petrovic", ime ="Petra", br_indeksa="PR3/2020")
student4 = Student(br_indeksa="PR4/2020", prezime = "Ivanovic", ime ="Ivana")

print("Studenti:")
print(student1)
print(student2)
print(student3)
print(student4)

# Zadatak 2
# Napisati klasu koja opisuje merenja visine po gradovima u Srbiji. 
# Potrebni atributi su: grad, drzava i kolekcija izmerenih vrednosti. 
# Pored metoda za inicijalizaciju i tekstualni prikaz objekata, 
# dodati i metodu koja računa prosečnu visinu za svaki grad. 
# Instancirati barem tri grada i za svaki ispisati prosečnu visinu. 
class Merenje:
    drzava = "Srbija"
    def __init__(self, grad, merenja):
       self.grad = grad
       self.merenja = merenja

    def __str__(self):
       return f"{self.drzava}, {self.grad}, {self.merenja}"
    
    def prosek(self):
       try:
         return sum(self.merenja)/len(self.merenja)
       except Exception as e:
          print("Greska:", e)
          return 0

novi_sad = Merenje("Novi Sad", [1.75, 1.80, 1.65, 2.02, 1.90, 1.68, 1.73])
sombor = Merenje("Sombor", [1.85, 1.80, 1.75, 2.02, 1.95, 1.78, 1.83])
zrenjanin = Merenje("Zrenjanin", [1.75, 1.70, 1.67, 2.00, 1.80, 1.78, 1.73])

print("Prosecna visina po gradu:")
print(f"{novi_sad}, prosečna visina: {novi_sad.prosek()}")
print(f"{sombor}, prosečna visina: {sombor.prosek()}")
print(f"{zrenjanin}, prosečna visina: {zrenjanin.prosek()}")

# Zadatak 3
# Napisati klasu Ucenik sa poljima: ime, prezime, ocene. 
# Ocene su rečnik, pri čemu je ključ naziv predmeta, a vrednost lista 
# ocena iz tog predmeta. 
# Konstruktor kao parametre prihvata samo ime i prezime, 
# dok se rečnik popunjava metodom za upis ocena, kojoj se prosleđuje 
# predmet i ocena koja se upisuje. 
# Pored ove metode, potrebno je definisati metodu koja spram 
# prosleđenog naziva predmeta računa zaključnu ocenu za taj predmet 
# i smešta je u novi recnik – zakljucene_ocene. 
# Treća metoda računa prosek učenika spram svih zaključenih ocena.
class Ucenik:
    def __init__(self, ime, prezime):
      self.ime = ime
      self.prezime = prezime
      self.ocene = {}
      self.zakljucene_ocene = {}

    def upisi_ocenu(self, predmet, ocena):
       if predmet in self.ocene.keys():
        self.ocene[predmet].append(ocena)
       else:
         self.ocene[predmet] = [ocena]

    def zakljuci_ocenu(self, predmet):
      if predmet in self.ocene.keys():
         try:
            zakljucna = round(sum(self.ocene[predmet])/len(self.ocene[predmet]))
            self.zakljucene_ocene[predmet] = zakljucna
            return zakljucna
         except Exception as e:
            print("Greska:", e)
      return None

    def prosek(self):
       try:
         return sum(self.zakljucene_ocene.values())/len(self.zakljucene_ocene.values())
       except Exception as e:
         print("Greska:", e)
    
    def __str__(self):
      return f"{self.ime} {self.prezime} ocene : {self.ocene}"
    
ucenik1 = Ucenik("Marko", "Markovic")
ucenik1.upisi_ocenu("matematika", 5)
ucenik1.upisi_ocenu("matematika", 4)
ucenik1.upisi_ocenu("matematika", 5)
ucenik1.upisi_ocenu("matematika", 5)

print(ucenik1)
print("Ocene: ", ucenik1.ocene)
print("Zakljucna ocena iz matematike: ",ucenik1.zakljuci_ocenu("matematika"))
print("Zakljucna ocena iz srpskog: ", ucenik1.zakljuci_ocenu("srpski"))

ucenik1.upisi_ocenu("srpski", 5)
ucenik1.upisi_ocenu("srpski", 4)
ucenik1.upisi_ocenu("srpski", 3)
ucenik1.upisi_ocenu("srpski", 5)

print("Ocene: ", ucenik1.ocene)
print("Zakljucna ocena iz srpskog: ", ucenik1.zakljuci_ocenu("srpski"))
print("Prosek ucenika", ucenik1.prosek())

# RAD SA DATOTEKAMA (str. )

# Zadatak 1
# Kreirati datoteku naziva „zadatak1.txt“ i u nju upisati svoj broj indeksa, ime i prezime.

f = open("zadatak1.txt", "w")
f.write("PR15/2015 Petar Petrovic")
f.close()

# Zadatak 2
# Kreirati datoteku naziva „zadatak2.txt“ i upotrebom while petlje u nju upisivati korisnički unos sa terminala. 
# Ručno izmeniti datoteku, zatim pročitati ceo sadržaj i ispisati ga.

f = open("zadatak2.txt", "w")
while True:
   unos = input("Unesite novi red:")
   if not unos: break
   f.write(unos + "\n")
f.close()

f = open("zadatak2.txt")
print(f.read())
f.close()


# Zadatak 3
# Čitati sadržaj datoteke „zadatak3.txt“ liniju po liniju i 
# za svaki pročitani red instancirati po jedan objekat klase Student iz datoteke student.py 
# i dodati ga u listu studenata. Nakon završenog čitanja, ispisati sve studente iz liste.

from student import Student

studenti = []

f = open("zadatak3.txt")
for red in f:
  reci = red.split("|")
  student = Student(reci[0], reci[1], reci[2], reci[3])
  studenti.append(student)
f.close()

for s in studenti: print(s)

# Zadatak 4
# Serijalizovati listu iz prethodnog zadatka i upisati je u datoteku „zadatak4.txt“.

import pickle

f = open("zadatak4.txt", "wb")
pickle.dump(studenti, f)
f.close()

# Zadatak 5
# Napisati klasu Ispit, koja sadrži sledeća polja: listu učionica u kojima se ispit održava, naziv predmeta i ime profesora. 
# Kreirati objekat tipa Ispit za predmet Osnove distribuiranog programiranja, 
# koji će se održati u učionicama 109, 109a i 108 kod prof. Lendak. 
# Kreirani objekat upisati u datoteku „zadatak5.json“.

import json

class Ispit:
   def __init__(self, ucionice, predmet, profesor):
      self.ucionice = ucionice
      self.predmet = predmet
      self.profesor = profesor

ODP = Ispit([109, '109a', 108], 'Osnove distribuiranog programiranja', "prof. Imre Lendak")
f = open("zadatak5.json", "w")
json.dump(ODP.__dict__, f)
f.close()

# Zadatak 6
# Učitati sadržaj „zadatak6.json“ datoteke. 
# Pročitano ispisati u formatu ključ : vrednost.

import json

f = open("zadatak6.json")
recnik = json.load(f)
for key,value in recnik.items():
   print(key, value, sep=": ")
f.close()