#1
print("=============1=============")
x = int(input("Unesite neki broj:"))
if x<0:
    print("Manji je od 0.")

#2
print("=============2=============")
a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))

print ("Prvi je veci") if a>b else print("Drugi je veci") if a<b else print("Oba su ista")

#3
print("=============3=============")
lista = ["luk","krompir","krastavac"]

if "krompir" in lista: print("Ima krompira.")
elif "grasak" in lista: print("Ima graska.")
else: print("Vreme je za nabavku.")

#4
print("=============4=============")
brojevi = [2,6,4,10,2,3,22]
for b in brojevi:
    print(b,end=" ")
print()

#5
print("=============5=============")
torka = (True,False)
for t in torka:
    print(t)

#6
print("=============6=============")
stringovi = {"jedan","dva","tri"}
for s in stringovi:
    print(s)

#7
print("=============7==============")
recnik = {
    "ime" : "Petar",
    "prezime" : "Petrovic",
    "datum" : "18.12.2021"
}
for r in recnik.keys():
    print(r)

#8
print("=============8==============")
lista = ["jabuke","banane","kivi","mandarine","grozdje","mango"]
for l in lista:
    if l == "kivi":
        continue
    if l == "grozdje":
        break
    print(l)

#9 
print("=============9==============")
i = 5
while i<=10:
    print(i)
    i+=1

#10
print("=============10==============")
i=1
while i<6:
    print(i)
    i+=1
print("i vise nije manje od 6.")


