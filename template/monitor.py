import socket
import time
port1 = 6000
port2 = 7000
server1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
kanal = socket.socket()

monitorSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
monitorSocket.bind(('localhost',8000))

def login(server):
    print("Login na sistem...")
    server.send("admin".encode())
    time.sleep(1)
    server.send("admin".encode())
    response = server.recv(1024).decode()
    print(response)

def konektuj_se_na_server(server,port):
    if not server: server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    server.connect(('localhost',port))

def zavrsi_konekciju(server):
    time.sleep(1)
    server.close()
    
def iniciraj_konekciju():
    print("monitor slusa za klijenta")
    monitorSocket.listen()
    global kanal
    kanal,adresa = monitorSocket.accept()

def postavi_i_posalji():
    try:
        print("Pokusaj da se poveze na server 1...")
        konektuj_se_na_server(server1,port1)
        print("Povezan na server 1.")
        login(server1)
        server1.send("SET_STATE".encode())
        server1.send("Primarni".encode())
        response = server1.recv(1024).decode()
        kanal.send(f"{port1}:{response}".encode())
        zavrsi_konekciju(server1)
        print("Server 1 dobio ulogu primarnog.")
    except:
        print("Server 1 nije odgovorio...")
        kanal.send(f"{port1}:Nedostupan".encode())
        try:
            print("Pokusaj da se poveze na server 2...")
            konektuj_se_na_server(server2,port2)
            print("Povezan na server 2.")
            login(server2)
            server2.send("SET_STATE".encode())
            server2.send("Primarni".encode())
            response = server2.recv(1024).decode()
            kanal.send(f"{port2}:{response}".encode())
            zavrsi_konekciju(server2)
            print("Server 2 dobio ulogu primarnog.")
        except:
            print("Server 2 nije odgovorio...")
            kanal.send(f"{port2}:Nedostupan".encode())
            return
    
    try:
        print("Pokusaj da se poveze na server 2...")
        konektuj_se_na_server(server2,port2)
        print("Povezan na server 2.")
        login(server2)
        server2.send("SET_STATE".encode())
        server2.send("Sekundarni".encode())
        response = server2.recv(1024).decode()
        kanal.send(f"{port1}:{response}".encode())
        zavrsi_konekciju(server2)
        print("Server 2 dobio ulogu sekundarnog.")
    except:
        print("Server 2 nije odgovorio...")
        kanal.send(f"{port1}:Nedostupan".encode())

def main():

    iniciraj_konekciju()
    if(kanal):
        print("povezan na klijenta.")
        while True:
            command = kanal.recv(1024).decode()
            if not command: break
            print("\n===Poslata komanda za proveru stanja!==")
            if command == "CHECK_STATES":
                postavi_i_posalji()
            print("=========================================\n")
main()