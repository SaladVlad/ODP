import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(('localhost', 7000))
print("Veza sa serverom je uspostavljena.")

while True: 
    izraz = input("Unesite neki matematički izraz:")
    if not izraz : break 
    klijent.send(izraz.encode()) 
    rezultat = klijent.recv(1024).decode()
    print(f"Server je vratio sledeće rešenje: {rezultat}")
print("Konekcija se zatvara.")
klijent.close()