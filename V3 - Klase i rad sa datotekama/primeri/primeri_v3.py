# KLASE

# Primer 89
class Trougao:
   boja = "plava"

trougao = Trougao()
print(trougao.boja) # Ispisuje 'plava'

# Primer 90
class Trougao:
   boja = "plava"
   a = b = 1

   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
      
trougao = Trougao(3, 4, 5)
print(trougao.boja, trougao.a, trougao.b, trougao.c) # Ispisuje 'plava 3 4 5'

# Primer 91
class Trougao:
    boja = "plava"
    a = b = 1

    def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c

    def __str__(self):
       return f"Trougao, boja: {self.boja}, stranice: {self.a}, {self.b}, {self.c}"
    
    def obim(self):
       return self.a+self.b+self.c
      
      
trougao = Trougao(3, 4, 5)
print(trougao.boja, trougao.a, trougao.b, trougao.c) # Ispisuje 'plava 3 4 5'
print(trougao) # Ispisuje 'Trougao, boja: plava, stranice: 3, 4, 5'
print(trougao.obim()) # Ispisuje 12

# OPSEZI I MODULI
                                       
# Primer 92
def funkcija():
   x = 10 # Lokalna promenljiva
   print(x)

funkcija() # Ispisuje 10
try:
  print(x) # Greška! 'x' nije definisano - NameError: name 'x' is not defined 
except Exception as e:
  print(e)
  
# Primer 93
x = 10 # Globalna promenljiva
def dupliraj():
    print(x*2) # Upotreba globalne promenljive u lokalnom opsegu

dupliraj() # Ispisuje 20

# Primer 94
x = 300 # Globalno x
def myfunc():
  x = 200 # Lokalno x
  print(x) # Ispisuje lokalno x

myfunc() # Ispisuje 200
print(x) # Ispisuje 300

# Primer 95
x = 10 # Globalna promenljiva
def dupliraj():
    global x
    x = x*2

dupliraj()
print(x) # Ispisuje 20

# DATETIME
# Primer 96
from datetime import date

datum = date(2000, 1, 1)
print(datum) # Ispisuje '2000-01-01'

danas = date.today()
print(danas) # Ispisuje '2023-08-23'

print("Trenutna godina: ", danas.year) # Ispisuje 'Trenutna godina:  2023'
print("Trenutni mesec: ", danas.month) # Ispisuje 'Trenutni mesec:  8'
print("Trenutni dan u mesecu: ", danas.day) # Ispisuje 'Trenutni dan u mesecu:  23'

# Primer 97
from datetime import time

vreme1 = time()
print(vreme1) # Ispisuje '00:00:00'

vreme2 = time(hour=14)
print(vreme2) # Ispisuje '14:00:00'

vreme3 = time(second=30)
print(vreme3) # Ispisuje '00:00:30'

vreme4 = time(17, 42, 15, 500)
print(vreme4) # Ispisuje '17:42:15.000500'

print("Sati ima", vreme4.hour) # Ispisuje 'Sati ima 17'
print("Minuta ima", vreme4.minute) # Ispisuje 'Minuta ima 42'
print("Sekundi ima", vreme4.second) # Ispisuje 'Sekundi ima 15'
print("Mikrosekundi ima", vreme4.microsecond) # Ispisuje 'Mikrosekundi ima 500'

# Primer 98
from datetime import datetime

dt1 = datetime(1999, 12, 12)
print(dt1) # Ispisuje '1999-12-12 00:00:00'

dt2 = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(dt2) # Ispisuje '1999-12-12 12:12:12.342380'

print("Godina: ", dt2.year) # Ispisuje 'Godina:  1999'
print("Mesec: ", dt2.month) # Ispisuje 'Mesec:  12'
print("Dan: ", dt2.day) # Ispisuje 'Dan:  12'
print("Sati: ", dt2.hour) # Ispisuje 'Sati:  12'
print("Minute: ", dt2.minute) # Ispisuje 'Minute:  12'
print("Sekunde: ", dt2.second) # Ispisuje 'Sekunde:  12'
print("Mikrosekunde: ", dt2.microsecond) # Ispisuje 'Mikrosekunde:  342380'

# Primer 99
from datetime import datetime

sadasnji_trenutak = datetime.now()
print(sadasnji_trenutak) # Ispisuje 2023-08-25 14:18:41.076007

# RAD SA DATOTEKAMA

# Primer 100

f = open("demo.txt", "r")
print(f.read())
# Ispisuje: 
# Ovo je demo rada sa datotekama u Python-u.
# Ovo je novi red.
f.close()

f = open("demo.txt", "r")
print(f.readline()) # Ispisuje: Ovo je demo rada sa datotekama u Python-u.
f.close()

f = open("demo.txt", "r")
print(f.read(11)) # Ispisuje: Ovo je demo
f.close()

f = open("demo.txt", "r")
for x in f:
  print(x)
# Ispisuje: 
# Ovo je demo rada sa datotekama u Python-u.
# Ovo je novi red.
f.close()

# Primer 101
f = open("demo.txt", "a")
f.write("\nDodali smo još jedan red!")
f.close()

f = open("demo.txt", "r")
print(f.read())
# Ispisuje:
# Ovo je demo rada sa datotekama u Python-u.
# Ovo je novi red.
# Dodali smo još jedan red!
f.close()

# Primer 102
f = open("demo.txt", "w")
f.write("Ovo ce sada biti jedini red!")
f.close()

f = open("demo.txt", "r")
print(f.read()) # Ispisuje: Ovo ce sada biti jedini red!
f.close()

# Primer 103
import os
if os.path.exists("demo.txt"):
  os.remove("demo.txt")
else:
  print("Trazena datoteka ne postoji.")

# SERIJALIZACIJA
# Primer 104

class Student:
    def __init__(self, ime, prezime, broj_indeksa, prosek):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa
        self.prosek = prosek

    def __str__(self) -> str:
        return f"{self.broj_indeksa} {self.prezime} {self.ime}, prosek: {self.prosek}"
    
import pickle

student = Student("Jovan", "Jovanović", "PR23/2023", 9.0)
print(student) # Ispisuje 'PR23/2023 Jovanović Jovan, prosek: 9.0'

b_student = pickle.dumps(student) # Serijalizacija
print(type(b_student)) # Ispisuje '<class 'bytes'>'

student2 = pickle.loads(b_student) # Deserijalizacija
print(student2) # Ispisuje 'PR23/2023 Jovanović Jovan, prosek: 9.0'

# Primer 105
class Student:
    def __init__(self, ime, prezime, broj_indeksa, prosek):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa
        self.prosek = prosek

    def __str__(self) -> str:
        return f"{self.broj_indeksa} {self.prezime} {self.ime}, prosek: {self.prosek}"
    
import pickle

student = Student("Jovan", "Jovanovic", "PR23/2023", 9.0)
print(student) # Ispisuje 'PR23/2023 Jovanović Jovan, prosek: 9.0'

f = open("student.txt", "wb")
pickle.dump(student, f)
f.close()

f = open("student.txt", "rb")
student2 = pickle.load(f) # Deserijalizacija
print(student2) # Ispisuje 'PR23/2023 Jovanović Jovan, prosek: 9.0'
f.close()

# Primer 106
import json

recnik = {
  "ime": "Jovan",
  "godine": 30,
  "student": False,
  "kola": [
    {"model": "BMW 230", "boja": "crna"},
    {"model": "Ford Edge", "boja": "crvena"}
  ]
}

print(recnik)
print(type(recnik)) # Ispisuje: <class 'dict'>

recnik_json = json.dumps(recnik)
print(recnik_json)
print(type(recnik_json)) # Ispisuje: <class 'str'>

nazad_u_recnik = json.loads(recnik_json)
print(nazad_u_recnik)
print(type(nazad_u_recnik)) # Ispisuje: <class 'dict'>

f = open("recnik.json", "w")
json.dump(recnik, f)
f.close()

f = open("recnik.json")
recnik2 = json.load(f)
print(recnik2)
f.close()

# Primer 107
import json

class Student:
    def __init__(self, ime, prezime, broj_indeksa, prosek):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa
        self.prosek = prosek

    def __str__(self) -> str:
        return f"{self.broj_indeksa} {self.prezime} {self.ime}, prosek: {self.prosek}"
    
student = Student("Jovan", "Jovanovic", "PR23/2023", 9.0)
f = open("student.json", "w")    
json.dump(student.__dict__, f)
f.close()

f = open("student.json")
student_json = json.load(f) # Ovo će biti rečnik.
student2 = Student("", "", "", 0)
for key, value in student_json.items(): setattr(student2, key, value)
print(student2) # Ispisuje: PR23/2023 Jovanovic Jovan, prosek: 9.0