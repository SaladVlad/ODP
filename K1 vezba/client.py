import socket,pickle
from datetime import date
from lek import Lek

def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",7000))

    print("Connected to the server.")

    while True:
        op = input("Enter the operation you want to do:\n1.List all meds\n2.Add med\n3.Update med\n4.Remove med\n5.Add ingredients\n")

        if op == '1':
            client.send("LIST".encode())
            answer = pickle.loads(client.recv(1024).decode())
            for lek in answer:
                print(lek)
            break
        if op == '2':
            pass
            break
        if op == '3':
            pass
            break
        if op == '4':
            pass
            break
        if op == '5':
            pass
            break

    client.close()

main()