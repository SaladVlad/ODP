import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7000))
server.listen()
print("Server je pokrenut.")

kanal, adresa = server.accept()
print(f"Prihvacena je konekcija sa adrese: {adresa}")

while True: 
    izraz = kanal.recv(1024).decode()
    if not izraz : break
    print(f"Primljeni zadatak: {izraz}")
    rezultat = str(eval(izraz))
    print(f"Rešenje: {rezultat}")
    kanal.send(rezultat.encode())
print("Server se gasi.")
server.close()