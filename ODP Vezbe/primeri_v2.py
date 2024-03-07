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

# OBRADA IZUZETAKA
    
# Primer 77
try:
  print(x)
except:
  print("Greska!")

try:
  print(x)
except NameError as ex:
  print("Greska: ", ex)
except:
   print("Neka druga greska!")

try:
  print(x)
except NameError as ex:
  print("Greska: ", ex)
except Exception as err:
   print(err)

try:
  print(x)
except (NameError, TypeError, SyntaxError):
  print("Greska!")
except:
   print("Neka druga greska!")

# Primer 78
try:
  print("Zdravo")
except:
  print("Greska!")
else:
  print("Nema greske!")

try:
  print(x)
except:
  print("Greska!")
finally:
  print("Kraj try-except bloka.")

# Primer 79
x = int(input("Unesite nenegativan broj: "))

if type(x) is not int:
   raise TypeError("Greska! Niste uneli ceo broj.")

if x < 0:
  raise Exception("Greska! Broj je manji od 0.")

# FUNKCIJE

# def naziv_funkcije(parametri):
#    naredbe

# Primer 80
# Definicija
def funkcija():
   print("Ovo je funkcija.")

# Poziv
funkcija() # Ispisuje 'Ovo je funkcija.'

# Primer 81
def predstavi_se(ime, prezime):
  print("Ja sam {} {}".format(ime, prezime))
  #print("Ja sam " + ime + " " + prezime)

predstavi_se("Petar", "Petrović") # Ispisuje 'Ja sam Petar Petrović'
predstavi_se("Marko", "Marković") # Ispisuje 'Ja sam Marko Marković'
predstavi_se("Jovan", "Jovanović") # Ispisuje 'Ja sam Jovan Jovanović'

predstavi_se(ime = "Milan", prezime = "Milanović") # Ispisuje 'Ja sam Milan Milanović'
predstavi_se(prezime = "Milošević", ime = "Miloš") # Ispisuje 'Ja sam Miloš Milošević'

# Primer 82
def funkcija_parametri(*args):
    for arg in args:
        print(arg)

funkcija_parametri("Prvi parametar", "Drugi parametar")
funkcija_parametri("Prvi parametar", "Drugi parametar", "Treći parametar")
funkcija_parametri("Prvi parametar")

# Primer 83
def funkcija_imenovani_parametri(**kwargs):
    for key, value in kwargs.items():
        print("%s -> %s" % (key, value))
 
funkcija_imenovani_parametri(prvi='Prvi parametar', drugi='Drugi parametar', treći='Treći parametar')
funkcija_imenovani_parametri(prvi='Prvi parametar', drugi='Drugi parametar')
funkcija_imenovani_parametri(prvi='Prvi parametar', drugi='Drugi parametar', treći='Treći parametar', četvrti="Četvrti parametar")

# Primer 84
def stepenovanje(x, y = 2):
   print(x**y)

stepenovanje(2, 3) # Ispisuje 8
stepenovanje(2) # Ispisuje 4

# Primer 85
def stepenovanje(x: int, y: int):
    print(x**y)

stepenovanje(2, 3) # Ispisuje 8
stepenovanje("tekst", 4) # Greska!

def izmena(x):
   x[0] = 5

x = [1, 4, 3, 2, 1]
izmena(x)
print(x) # Ispisuje [5, 4, 3, 2, 1]

def dodela(x):
   x = [1, 2, 3, 4, 5]

x = [5, 4, 3, 2, 1]
dodela(x)
print(x) # Ispisuje [5, 4, 3, 2, 1]

# Primer 86
def stepenovanje(x: int, y: int) -> int:
    return x**y

z = stepenovanje(2, 3) 
print(z) # Ispisuje 8

def veci_broj(x, y):
    if x > y:
       return x
    elif y > x:
       return y
    return None

print(veci_broj(2, 5)) # Ispisuje 5
print(veci_broj(20, 5)) # Ispisuje 20
print(veci_broj(2, 2)) # Ispisuje None

# Primer 87
mnozenje = lambda a, b, c : a * b * c
print(mnozenje(5, 6, 2)) # Ispisuje 60

par_nepar = lambda broj: "Paran broj" if broj % 2 == 0 else "Neparan broj"
print(par_nepar(20)) # Ispisuje 'Paran broj'

lista = ["1", "2", "9", "0", "-1", "-2"]
print("Pozitivni parni brojevi:",
      list(filter(lambda x: (int(x) % 2 == 0 and int(x) > 0), lista))) # Ispisuje 'Pozitivni parni brojevi: ['2']'

# Primer 88
def faktorijel(n):
   if n>0:
      return n*faktorijel(n-1)
   else:
      return 1
   
f = faktorijel(5)
print("5! = ", f) # Ispisuje '5! = 120'