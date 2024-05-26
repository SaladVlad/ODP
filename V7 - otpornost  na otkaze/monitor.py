import socket
import time

def povezi_se_sa_serverom(port, stanje) :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        server.connect(('localhost', port))
        print(f"Veza sa {stanje} serverom je uspostavljena.")
        azuriraj_stanje(server, stanje)
        return server
    except Exception as ex:
        print(ex)
        return

def azuriraj_stanje(socket, stanje):
    socket.send(("SET_STATE").encode())
    socket.send(stanje.encode())
    print(socket.recv(1024).decode())

def proveri_stanje(socket):
    try:
        socket.send(("GET_STATE").encode())  
        return socket.recv(1024).decode()
    except Exception as ex:
        print(ex)
        return "nepoznato"

def main():
    server_jedan = povezi_se_sa_serverom(6000, 'primarni')
    server_dva = povezi_se_sa_serverom(7000, 'sekundarni')

    while True: 
        stanje_servera_jedan = proveri_stanje(server_jedan)
        stanje_servera_dva = proveri_stanje(server_dva)

        print(f"Stanje prvog servera je: {stanje_servera_jedan}")
        print(f"Stanje drugog servera je: {stanje_servera_dva}")
        
        #ukoliko je doslo do ispada prvog servera
        if stanje_servera_jedan == "nepoznato" and stanje_servera_dva == "sekundarni":            
            print("Podesiti stanje na primarni:")
            azuriraj_stanje(server_dva, "primarni")                
            stanje_servera_dva = proveri_stanje(server_dva)
        
        #ukoliko su ispala oba servera        
        if stanje_servera_jedan == "nepoznato" and stanje_servera_dva == "nepoznato": 
            print("Oba servisa su van funkcije.")
            server_jedan.close()
            server_dva.close()
            print("Zatvaranje konekcije.")
            break
        time.sleep(5)
    
main()