#1
print("=================1=================")
class Student:
    fakultet = "FTN"

    def __init__(self,ime,prezime,brInd):
        self.ime = ime
        self.prezime = prezime
        self.brInd = brInd
    
    def __str__(self):
        return f"Ime:{self.ime} Prezime: {self.prezime} BrIndeksa:{self.brInd} Fakultet: {self.fakultet}"


s1 = Student("pera","peric","pr999")
s2 = Student("marko","markovic","pr007")

print(s1)
print(s2)

#2
print("=================2=================")
class Measurement:

    def __init__(self,grad,drzava,merenja):
        self.grad = grad
        self.drzava = drzava
        self.merenja = merenja
    
    def __str__(self):
        return f"Grad: {self.grad}, Drzava: {self.drzava}, Merenja: [{self.merenja}], Prosek: {self.prosek()}"

    def prosek(self):
        suma = 0
        try:
            for x in self.merenja:
                suma+=x
            return suma/len(self.merenja)
        except:
            return -1

m1 = [200,300,230,260,420]
m2 = [500,600,530,390]
m3 = []

mer1 = Measurement("Novi Sad","Srbija",m1)
mer2 = Measurement("Kairo","Egipat",m2)
mer3 = Measurement("Mesec","Svemir",m3)

print("M1: \n",mer1,"\nM2: \n",mer2,"\nM3: \n",mer3)

#3
print("================3===================")
class Ucenik:

    def __init__(self,ime,prezime):
        self.ime = ime
        self.prezime = prezime
        self.ocene = dict()
        self.zakljucene_ocene = dict()

    def __str__(self):
        return f"Ime: {self.ime}, Prezime: {self.prezime}\nOcene: {self.ocene}"

    def upisOcena(self,input):
        for kvp in input:
            if kvp in self.ocene.keys():
                self.ocene[kvp]+=input[kvp]
            else:
                self.ocene[kvp]=input[kvp]
    
    def zakljuci(self,predmet):
        if predmet in self.ocene.keys():
            suma = 0
            for x in self.ocene[predmet]:
                suma+=x
            zak = round(suma/len(self.ocene[predmet]))
            self.zakljucene_ocene.update({predmet:zak})
        else:
            print("Ne postoji taj predmet!!")

    def konacno_zakljucivanje(self):
        try:
            suma = sum(self.zakljucene_ocene.values())
            return suma/len(self.zakljucene_ocene.values())
        except:
            pass

        
u1 = Ucenik("Imenko","Prezimic")
u1.upisOcena({"Matematika":[3,5,5,4],"Informatika":[4,5,5]})
print(u1)
u1.upisOcena({"Matematika":[1]})
print(u1)
u1.zakljuci("Matematika")
print("Zakljucena ocena iz svih predmeta: ",u1.konacno_zakljucivanje())


