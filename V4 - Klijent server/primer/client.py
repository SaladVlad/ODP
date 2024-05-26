# Uvoz potrebnog modula
import socket

# Kreiranje soketa -> 
# AF_INET označava IPv4 familiju adresa, 
# SOCK_STREAM definiše da će se komunikacija odvijati po TCP protokolu
klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Klijent inicira uspostavljanje konekcije sa serverom
# Napomena: parametar connect funkcije je uređeni par (adresa, port) tj. torka (tuple)
klijent.connect(('localhost', 6000))
print("Veza sa serverom je uspostavljena.")
while True: 
    poruka = input("Unesite poruku:") # Traži se unos od korisnika
    if not poruka : break # Ukoliko korisnik ne unese ništa (pritisne Enter), petlja se prekida
    klijent.send(poruka.encode()) # Pomoću encode metode se string pretvara u niz bajtova i poruka se kao takva šalje
print("Konekcija se zatvara.")
klijent.close() # Zatvaranje komunikacionog kanala sa klijentske strane