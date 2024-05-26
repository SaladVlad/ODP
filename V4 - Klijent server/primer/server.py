# Uvoz potrebnog modula
import socket

# Kreiranje soketa -> 
# AF_INET označava IPv4 familiju adresa, 
# SOCK_STREAM definiše da će se komunikacija odvijati po TCP protokolu
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Konfiguracija adrese ->
# Soket se povezuje na lokalnu adresu i proizvoljan port (od 1024 pa naviše)
# Napomena: parametar bind funkcije je uređeni par (adresa, port) tj. torka (tuple)
server.bind(('localhost', 6000))

# Funkcijom listen server se otvara za klijentske konekcije;
# kreira se tzv. "slušajući" soket
server.listen()
print("Server je pokrenut.")

# Funkcija accept blokira izvršavanje programa dok god ne stigne zahtev za povezivanje od strane nekog klijenta
# Povratne vrednosti su novi socket objekat koji predstavlja samu konekciju i adresa klijenta
kanal, adresa = server.accept()
print(f"Prihvacena je konekcija sa adrese: {adresa}")
while True: # Dok god stižu poruke
    poruka = kanal.recv(1024).decode() # Prihvati niz bajtova koji je klijent poslao i dekodiraj ga nazad u string
    if not poruka : break # Ako nije ništa stiglo, prekini petlju
    print(f"Primljena poruka: {poruka}") # Ispiši primljenu poruku
print("Server se gasi.")
server.close() # Zatvaranje komunikacionog kanala sa serverske strane