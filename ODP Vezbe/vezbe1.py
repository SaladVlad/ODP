'''
# 1
x = 5**2 + 3/4
print(x)

#2
a,b = 17,3
kol = a//b
ost = a%b

#3
rez = kol//2
rez*=3

#4
a = 10
if(a in [5,6,7,8,9,10]):
    print("U opsegu je")
#5
if(a>-10 or a<10):
    print("Tacno")

#6
if(a not in [5,6,7,8,9,10]):
    print("This is true")

if(a <-10 or a>10):
    print("Tacno")

#1
r1 = float(input("unesti broj 1:"))
r2 = float(input("unesti broj 2:"))
print(r1+r2)

#2
dan = int(input("dan:"))
mesec = int(input("mesec:"))
godina = int(input("godina:"))
print(dan,"/",mesec,"/",godina,sep="")

#3
tekst = input("unesite neki tekst")
lista = tekst.lower().strip().split(" ")

#4
txt = input("unesi neki tekst: ")
txt = txt.replace("cao","zdravo")
print(txt)

#5
text = input("tekst za proveru:")
if("je" in text):
    print("contains \'je\'")
if("sam" not in text):
    print("does not contain \'sam\'")
if(text[1]=="A"):
    print("First letter is A")
if(len(text) == 0):
    print("len = 0")

#6
ime,prezime,godine = input("unesite ime prezime i godine").strip().split(',')
print(ime,prezime,"ima",godine,"godina",sep=" ")
'''
####################################################

lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
print(lista[1])
lista[2]="kupine"
lista.append("narandze")
lista.insert(1,"limun")
lista.remove("mandarine")
print(lista[2:5])
print(lista[-1])
print(len(lista))
print(lista.sort())
lista.clear()
del lista

#2
recnik = {
 "marka": "Ford",
"model": "Mustang",
"godina": 1964
}

print(recnik["model"])
print(recnik.get("model"))

recnik.update({"godina",2003})

recnik["boja"] = "zuta"
del recnik["marka"]



