#Primer 1
jezik = 'python'
 
if jezik == 'python':
    print('Ucimo python!')
else:
    print('Pogresan jezik.')
print('Gotovo ucenje!')

#Primer 2
j = 1
while(j <= 5):
    print(j)
    j = j + 1

#Primer 3
# Ovo je komentar
print("Komentar")

#Primer 4
a, b = 1, 3  # Deklarisanje dve promenljive
sum = a + b  # Sabiranje dve promenljive
print(sum)  # Ispis rezultata

#Primer 5
#print("Zdravo, svete!")
print("Ćao, druže!")

#Primer 6
# Ovo je primer
# viselinijskog
# komentara

"""
Ovo je primer
viselinijskog
komentara
"""

#Primer 7 - operatori identiteta
x=5
y=5
x is y # Vraca True
list1 = []
list2 = []
list1 is list2 # Vraca False
list1 = list2
list1 is list2 # Vraca True

#Primer 8 - operatori pripadnosti
"a" in "Ana" # Vraca True
"b" in "Ana" # Vraca False
"b" not in "Ana" #Vraca True
1 in [1, 2, 3] # Vraca True
4 not in [1, 2, 3] # Vraca True

#Primer 9 - operatori bita
a = 2   # 00000010
b = 3   # 00000011
a&b # 00000010 - Vraca 2
a|b # 00000011 - Vraca 3
a^b # 00000001 - Vraca 1
~a  # 11111101 - Vraca –3
a << 2  # 0001000 - Vraca 8
a >> 2  # 0000000 - Vraca 0

#Primer 10
x = 5
print(type(x)) # Ispisuje <class 'int'>

# Primer 11
# U praktikumu (str. 13)

# Primer 12
x = str("Zdravo")
x = int(20)
x = list(("jabuka", "banana", "limun"))
x = dict(name="John", age=36)

# LOGIČKI TIP

# Primer 13
bool("abc") # True
bool(123) # True
bool(["apple", "cherry", "banana"]) # True

# Primer 14
bool(False) # False
bool(None) # False
bool(0) # False
bool("") # False
bool(()) # False
bool([]) # False
bool({}) # False

# Primer 15
x = int(1)   # x ce biti 1
y = int(2.8) # y ce biti 2
z = int("3") # z ce biti 3
x = float(1)     # x ce biti 1.0
y = float(2.8)   # y ce biti 2.8
z = float("3")   # z ce biti 3.0
w = float("4.2") # w ce biti 4.2
x = str("s1") # x ce biti 's1'
y = str(2)    # y ce biti '2'
z = str(3.0)  # z ce biti '3.0'

#Primer 16
tekst = input("Unesite neki tekst: ")
print(tekst)

#Primer 17
broj = int(input("Unesite neki broj: "))
print(broj, " ", type(broj))

#Primer 18
x, y = input("Unesite dve vrednosti: ").split()
print("Prva vrednost: ", x)
print("Druga vrednost: ", y)
x, y = input("Unesite dve vrednosti: ").split(',')
print("Prva vrednost: ", x)
print("Druga vrednost: ", y)

#Primer 19
print("Neki tekst") # Ispisuje 'Neki tekst'
print(5) # Ispisuje '5'
x = 2.4
print(x) # Ispisuje '2.4'
print("x = ", x) # Ispisuje 'x = 2.4'
a = 2
b = 3
print("a + b =", a+b) # Ispisuje 'a + b = 5'

#Primer 20
a=12
b=12
c=2022
print(a,b,c,sep="-") # Ispisuje '12-12-2022'
print('jabuke', 'narandze', 'banane', sep=', ') # Ispisuje jabuke, narandze, banane
print('jabuke', 'narandze', 'banane', sep=' i ') # Ispisuje jabuke i narandze i banane
print('A', 'B', 'C', sep='') # Ispisuje 'ABC' (bez sep: A B C)


# Primer 21
tekst = 'Neki tekst'
slovo = "A"

# Primer 22
dugacakTekst = """Važno je, možda, i to da znamo
Čovek je željan tek ako želi
I ako sebe celoga damo
Tek tada i možemo biti celi.
Saznaćemo tek ako kažemo
Reči iskrene, istovatne
I samo onda kad i mi tražimo
Moći će neko i nas da sretne"""

# Primer 23
a = "Zdravo!"
print(len(a)) # Ispisuje 7

#Primer 24
tekst = "Najbolje stvari u životu su besplatne!"
print("besplatne" in tekst) # Ispisuje True
tekst = "Najbolje stvari u životu su besplatne!"
print("skupe" not in tekst) # Ispisuje True

# Primer 25
pozdrav = "Zdravo svima!"
print(pozdrav[7:10]) # Ispisuje 'svi'
print(pozdrav[:6]) # Ispisuje 'Zdravo'
print(pozdrav[7:]) # Ispisuje 'svima!'

# Prebacivanje u velika slova – upper()
a = "Zdravo!"
print(a.upper()) # Ispisuje 'ZDRAVO!'

# Prebacivanje u mala slova – lower()
a = "Zdravo, Marko!"
print(a.lower()) # Ispisuje 'zdravo, marko!'

# Uklanjanje razmaka – strip()
a = " Zdravo!  "
print(a.strip()) # Ispisuje 'Zdravo!'

# Zamena – replace()
a = "Cao svima!"
print(a.replace("Cao", "Zdravo")) # Ispisuje 'Zdravo svima!'

#Podela stringa na podnizove – split()
a = "Zdravo, Marko"
print(a.split(",")) # Ispisuje ['Zdravo', ' Marko']

# Konkatenacija stringova
a = "Zdravo"
b = "Marko"
c = a + b
print(c) # Ispisuje 'ZdravoMarko'
a = "Zdravo"
b = "Marko"
c = a + ", " + b
print(c) # Ispisuje 'Zdravo, Marko'

# Formatiranje stringova
godine = 23
tekst = "Moje ime je Marko i ja imam {} godine."
print(tekst.format(godine)) # Ispisuje 'Moje ime je Marko i ja imam 23 godine.'

kolicina = 3
idProizvoda = 567
cena = 50
porudzbina = "Želim {} komada proizvoda {} za {} dinara."
print(porudzbina.format(kolicina, idProizvoda, cena)) # Ispisuje Želim 3 komada proizvoda 567 za 50 dinara.'

# Primeri 26 i 27
tekst = "Ovo je \"citat\""
print(tekst) # Ispisuje 'Ovo je "citat"'

# Primer 28
tekst = "Ispis obrnute kose crte: \\" 
print(tekst) # Ispisuje 'Ispis obrnute kose crte: \'

#LISTE

# Primer 29
lista = ["jabuke", "banane", "kivi"]
print(lista) # Ispisuje ['jabuke', 'banane', 'kivi']

# Primer 30
duzina = len(lista)
print(duzina) # Ispisuje 3

# Primer 31
lista1 = ["jabuke", "banane", "kivi"]
lista2 = [1, 5, 7, 9, 3]
lista3 = [True, False, False]
lista4 = ["abc", 34, True, 40]
print(type(lista1)) # Ispisuje <class 'list'>
print(type(lista2)) # Ispisuje <class 'list'>
print(type(lista3)) # Ispisuje <class 'list'>
print(type(lista4)) # Ispisuje <class 'list'>

# Primer 32
lista = list((1, 2, 3))
print(lista) # Ispisuje [1, 2, 3]

# Primer 33
lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
print(lista[2]) # Ispisuje 'kivi'
print(lista[2:5]) # Ispisuje ['kivi', 'mandarine', 'grozdje']
print(lista[:3]) # Ispisuje ['jabuke', 'banane', 'kivi']
print(lista[3:]) # Ispisuje ['mandarine', 'grozdje', 'mango']

print(lista[-1]) # Ispisuje 'mango'
print(lista[-4:-1]) # Ispisuje ['kivi', 'mandarine', 'grozdje']
print(lista[:-2]) # Ispisuje ['jabuke', 'banane', 'kivi', 'mandarine']
print(lista[-4:]) # Ispisuje ['kivi', 'mandarine', 'grozdje', 'mango']

# Primer 34
lista = ["jabuke", "banane", "kivi"]
lista.append("mango")
print(lista) # Ispisuje ['jabuke', 'banane', 'kivi', 'mango']
lista.insert(1, "kruska")
print(lista) # Ispisuje ['jabuke', 'kruska', 'banane', 'kivi', 'mango']
lista2 = ["maline", "kupine", "jagode"]
lista.extend(lista2)
print(lista) # Ispisuje ['jabuke', 'kruska', 'banane', 'kivi', 'mango', 'maline', 'kupine', 'jagode']

# Primer 35
lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
lista[0] = "kruske"
print(lista) # Ispisuje ['kruske', 'banane', 'kivi', 'mandarine', 'grozdje', 'mango']
lista[2:4] = ["jagode", "maline"]
print(lista) # Ispisuje ['kruske', 'banane', 'jagode', 'maline', 'grozdje', 'mango']
lista[2:4] = ["kupine"]
print(lista) # Ispisuje ['kruske', 'banane', 'kupine', 'grozdje', 'mango']
lista[2:4] = ["borovnice", "ribizle", "narandza"]
print(lista) # Ispisuje ['kruske', 'banane', 'borovnice', 'ribizle', 'narandza', 'mango']

# Primer 36
lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
lista.remove("kivi")
print(lista) # Ispisuje ['jabuke', 'banane', 'mandarine', 'grozdje', 'mango']
lista.pop()
print(lista) # Ispisuje ['jabuke', 'banane', 'mandarine', 'grozdje']
lista.pop(0)
print(lista) # Ispisuje ['banane', 'mandarine', 'grozdje']
lista.clear()
print(lista) # Ispisuje []

lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
del lista[0]
print(lista) # Ispisuje ['banane', 'kivi', 'mandarine', 'grozdje', 'mango']
del lista[1:3]
print(lista) # Ispisuje ['banane', 'grozdje', 'mango']
del lista
print(lista) # Greska! NameError: name 'lista' is not defined.

# Primer 37
lista1 = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
lista2 = [1, 5, 7, 9, 3]
lista1.sort()
lista2.sort()
print(lista1) # Ispisuje ['banane', 'grozdje', 'jabuke', 'kivi', 'mandarine', 'mango']
print(lista2) # Ispisuje [1, 3, 5, 7, 9]

lista1.sort(reverse=True)
lista2.sort(reverse=True)
print(lista1) # Ispisuje ['mango', 'mandarine', 'kivi', 'jabuke', 'grozdje', 'banane']
print(lista2) # Ispisuje [9, 7, 5, 3, 1]

# Primer 38
lista1 = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
lista2 = [1, 5, 7, 9, 3]
lista1.reverse()
lista2.reverse()
print(lista1) # Ispisuje ['mango', 'grozdje', 'mandarine', 'kivi', 'banane', 'jabuke']
print(lista2) # Ispisuje [3, 9, 7, 5, 1]

# RECNICI

# Primer 39
recnik = {
    "marka": "Ford",
    "model": "Mustang",
    "godina": 1964 
}
print(recnik) # Ispisuje {'marka': 'Ford', 'model': 'Mustang', 'godina': 1964}

# Primer 40
duzina = len(recnik)
print(duzina) # Ispisuje 3

# Primer 41
recnik = {
    "marka": "Ford",
    "model": "Mustang",
    "godina": 1964,
    "boje": ["crvena", "crna", "zuta"] 
}
print(type(recnik)) # Ispisuje <class 'dict'>

# Primer 42
recnik = dict(marka = "Ford", model = "Mustang", godina = 1964)
print(recnik) # Ispisuje {'marka': 'Ford', 'model': 'Mustang', 'godina': 1964}

# Primer 43
recnik = {
    "marka": "Ford",
    "model": "Mustang",
    "godina": 1964,
    "boje": ["crvena", "crna", "zuta"] 
}
print(recnik["godina"]) # Ispisuje 1964
print(recnik.get("model")) # Ispisuje 'Mustang'

# Primer 44
recnik = {
    "marka": "Ford",
    "model": "Mustang",
    "godina": 1964,
    "boje": ["crvena", "crna", "zuta"] 
}

kljucevi = recnik.keys()
print(kljucevi) # Ispisuje dict_keys(['marka', 'model', 'godina', 'boje'])

vrednosti = recnik.values()
print(vrednosti) # Ispisuje dict_values(['Ford', 'Mustang', 1964, ['crvena', 'crna', 'zuta']])

elementi = recnik.items()
print(elementi) # Ispisuje dict_items([('marka', 'Ford'), ('model', 'Mustang'), ('godina', 1964), ('boje', ['crvena', 'crna', 'zuta'])])

# Primer 45
recnik = {
    "marka": "Ford",
    "model": "Mustang",
    "godina": 1964 
}
recnik["godina"] = 2000
print(recnik) # Ispisuje {'marka': 'Ford', 'model': 'Mustang', 'godina': 2000}
recnik["boja"] = "crvena"
print(recnik) # Ispisuje {'marka': 'Ford', 'model': 'Mustang', 'godina': 2000, 'boja': 'crvena'}

recnik.update({"godina": 2020})
print(recnik) # Ispisuje {'marka': 'Ford', 'model': 'Mustang', 'godina': 2020, 'boja': 'crvena'}
recnik.update({"cena": 100000})
print(recnik) # Ispisuje {'marka': 'Ford', 'model': 'Mustang', 'godina': 2020, 'boja': 'crvena', 'cena': 100000}

# Primer 46
recnik = {
    "marka": "Ford",
    "model": "Mustang",
    "godina": 1964,
    "boje": ["crvena", "crna", "zuta"] 
}
recnik.pop("marka")
print(recnik) # Ispisuje {'model': 'Mustang', 'godina': 1964, 'boje': ['crvena', 'crna', 'zuta']}
del recnik["model"]
print(recnik) # Ispisuje {'godina': 1964, 'boje': ['crvena', 'crna', 'zuta']}
recnik.popitem()
print(recnik) # Ispisuje {'godina': 1964}
recnik.clear()
print(recnik) # Ispisuje {}
del recnik
print(recnik) # Greska! NameError: name 'recnik' is not defined.

# TORKE
# Primer 47
torka = ("jabuke", "banane", "kivi") 
print(torka) # Ispisuje ('jabuke', 'banane', 'kivi') 

# Primer 48
duzina = len(torka) 
print(duzina) # Ispisuje 3 

# Primer 49
torka1 = ("jabuke", "banane", "kivi") 
torka2 = (1, 5, 7, 9, 3)
torka3 = (True, False, False) 
torka4 = ("abc", 34, True, 40) 

print(type(torka1)) # Ispisuje <class 'tuple'> 
print(type(torka2)) # Ispisuje <class 'tuple'> 
print(type(torka3)) # Ispisuje <class 'tuple'> 
print(type(torka4)) # Ispisuje <class 'tuple'> 

# Primer 50
torka = tuple((1, 2, 3)) 
print(torka) # Ispisuje (1, 2, 3)

# Primer 51
torka = ("jabuke", "banane", "kivi", "mandarine", "grozdje", "mango") 
print(torka[2]) # Ispisuje 'kivi' 
print(torka[2:5]) # Ispisuje ('kivi', 'mandarine', 'grozdje') 
print(torka[:3]) # Ispisuje ('jabuke', 'banane', 'kivi')
print(torka[3:]) # Ispisuje ('mandarine', 'grozdje', 'mango') 
print(torka[-1]) # Ispisuje 'mango' 
print(torka[-4:-1]) # Ispisuje ('kivi', 'mandarine', 'grozdje') 
print(torka[:-2]) # Ispisuje ('jabuke', 'banane', 'kivi', 'mandarine') 
print(torka[-4:]) # Ispisuje ('kivi', 'mandarine', 'grozdje', 'mango') 

# Primer 52
torka = ("jabuke", "banane", "kivi", "mandarine", "grozdje", "mango")
lista = list(torka)
lista.append("kruske")
torka = tuple(lista)
print(torka) # Ispisuje ('jabuke', 'banane', 'kivi', 'mandarine', 'grozdje', 'mango', 'kruske')

# Primer 53
torka1 = ("jabuke", "banane", "kivi")
torka2 = ("mandarine", "grozdje")
torka3 = ("mango",)
torka1 += torka2
print(torka1) # Ispisuje ('jabuke', 'banane', 'kivi', 'mandarine', 'grozdje')
torka1 += torka3
print(torka1) # Ispisuje ('jabuke', 'banane', 'kivi', 'mandarine', 'grozdje', 'mango')

# Primer 54
torka = ("jabuke", "banane", "kivi")
(crveno, zuto, zeleno) = torka
print(crveno) # Ispisuje 'jabuke'
print(zuto) # Ispisuje 'banane'
print(zeleno) # Ispisuje 'kivi'

# Primer 55
torka = ("jabuke", "banane", "kivi", "mandarine", "grozdje", "mango")
(jabuke, *ostalo, mango) = torka
print(jabuke) # Ispisuje 'jabuke'
print(ostalo) # Ispisuje ['banane', 'kivi', 'mandarine', 'grozdje']
print(mango) # Ispisuje 'mango'

# SKUPOVI
# Primer 56
skup = {"jabuke", "banane", "kivi"}
print(skup) # Ispisuje {'kivi', 'banane', 'jabuke'} (ili nekim drugim redosledom)

skup = {"jabuke", "banane", "kivi", "kivi"}
print(skup) # Ispisuje {'kivi', 'banane', 'jabuke'} (ili nekim drugim redosledom)

# Primer 57
duzina = len(skup) 
print(duzina) # Ispisuje 3 

# Primer 58
skup1 = {"jabuke", "banane", "kivi"} 
skup2 = {1, 5, 7, 9, 3}
skup3 = {True, False, False} 
skup4 = {"abc", 34, True, 40} 

print(type(skup1)) # Ispisuje <class 'set'> 
print(type(skup2)) # Ispisuje <class 'set'> 
print(type(skup3)) # Ispisuje <class 'set'> 
print(type(skup4)) # Ispisuje <class 'set'> 

# Primer 59
skup = set((1, 2, 3)) 
print(skup) # Ispisuje {1, 2, 3} 

# Primer 60
skup1 = {"jabuke", "banane", "kivi"} 
skup1.add("kruske")
print(skup1) # Ispisuje {'kivi', 'banane', 'kruske', 'jabuke'}

skup2 = {"mandarine", "grozdje", "mango"} 
skup1.update(skup2)
print(skup1) # Ispisuje {'mandarine', 'mango', 'jabuke', 'kivi', 'banane', 'kruske', 'grozdje'}

# Primer 61
skup1 = {"jabuke", "banane", "kivi"} 
skup1.remove("kivi")
print(skup1) # Ispisuje {'banane', 'jabuke'}
skup1.remove("jabuka") # Greska!

skup2 = {"mandarine", "grozdje", "mango"}
skup2.discard("grozdje")
print(skup2) # Ispisuje {'mandarine', 'mango'}
skup2.discard("mandarina") # Nema efekta.
print(skup2) # Ispisuje {'mandarine', 'mango'}

# Primer 62
skup1 = {"jabuke", "banane", "kivi", "mandarine", "grozdje"} 
x = skup1.pop()
print("Obrisani element:", x) #Ispisuje 'Obrisani element: mandarine'

# Primer 63
skup1 = {"jabuke", "banane", "kivi", "mandarine", "grozdje"}
skup1.clear()
print(skup1) # Ispisuje 'set()'

del skup1
print(skup1) # Greska! NameError: name 'skup1' is not defined.

# KONTROLA TOKA
# GRANANJE
# Primer 64
if 2 < 5:
    print("Dva je manje od pet.")

# Primer 65
a = 33
b = 200
if b > a:
    print("b je veće od a")
else:
    print("b nije veće od a")

# Primer 66
a = 33
b = 200
if b > a:
    print("b je veće od a")
elif a > b:
    print("a je veće od b")
else:
    print("a je jednako b")

# Primer 67
if a > b: print("a je veće od b")
print("A") if a > b else print("B")

# Primer 68
x = 41

if x > 10:
  print("x je veće od 10,")
  if x > 20:
    print("a veće je i od 20")
  else:
    print("ali nije veće od 20")

# Primer 69
a = 33
b = 200
if b > a:
    pass
else:
    print("b nije veće od a")

# PETLJE
# Primer 70
lista = ["jabuka", "banana", "visnja"]
for x in lista:
  print(x)

rec = "jabuka"
for slovo in rec:
    print(slovo)

# Primer 71
for x in range(6):
  print(x) # Ispisuje 0 1 2 3 4 5

for x in range(2, 6):
  print(x) # Ispisuje 2 3 4 5

for x in range(2, 30, 3):
  print(x) # Ispisuje 2 5 8 11 14 17 20 23 26 29

# Primer 72
i = 1
while i < 6:
  print(i)
  i += 1

# Primer 73
for i in range(10):
    print(i)
    if i == 5:
        break

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Primer 74
for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

# Primer 75
n = 10
for i in range(n):
  pass

i = 0
while i < 6:
    i += 1
    pass

# Primer 76
for i in range(1, 4):
    print(i)
else:  
    print("Ovo se ispisuje na kraju.")

i = 0
while i < 4:
    i += 1
    print(i)
else:  
    print("Ovo se ispisuje na kraju.")