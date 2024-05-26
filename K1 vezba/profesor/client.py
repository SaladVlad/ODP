import socket,pickle
import json

from datetime import date
from profesor import Profesor

f = open("E:\Faks\ODP\K1 vezba\profesor\profs.json","r")
profs_list = json.load(f)

profs = {prof["jmbg"]:Profesor(**prof) for prof in profs_list}

def printMenu():
    print("\tMenu")
    print("1. Add prof from a file")
    print("2. Modify prof from a file")
    print("3. Delete prof with jmbg")
    print("4. Read prof with jmbg")
    print("5. Add predmets to a professor")
    print("6. Read predmets from a professor with jmbg")
    print("7. Get file with profs teaching for over 20 years")

def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",8080))
    print("Connected to the server.")

    while True:
        printMenu()
        option = input("Enter option: ")

        if option == "1":
            client.send(option.encode())
            for prof in profs.values():
                print(prof.__str__())
            jmbg = input("Enter jmbg of the prof you want to add: ")
            client.send(pickle.dumps(profs[jmbg]))

            response = client.recv(1024).decode()
            print(response)

        elif option == "2":
            client.send(option.encode())
            for prof in profs.values():
                print(prof.__str__())
            jmbg = input("Enter jmbg of the prof you want to modify: ")
            client.send(pickle.dumps(profs[jmbg]))

            response = client.recv(1024).decode()
            print(response)

        elif option == "3":
            client.send(option.encode())
            jmbg = input("Enter jmbg of the prof you want to delete: ")
            client.send(jmbg.encode())

            response = client.recv(1024).decode()
            print(response)

        elif option == "4":
            client.send(option.encode())
            jmbg = input("Enter jmbg of the prof you want to read: ")
            client.send(jmbg.encode())

            response = client.recv(1024).decode()
            print(response)

        elif option == "5":
            client.send(option.encode())
            
            #first send the jmbg
            jmbg = input("Enter jmbg you want to add to: ")
            client.send(jmbg.encode())

            response = client.recv(1024).decode()
            if response == "OK": #if jmbg is ok, then continue with the adding
                adding = []
                while True:
                    course = input("Add one: ")
                    if not course : break
                    adding.append(course)
                client.send(pickle.dumps(adding))

                response = client.recv(1024).decode()
                print(response)

            else:
                print("This professor doesn't exist!")

        elif option == "6":
            client.send(option.encode())
            jmbg = input("Enter jmbg you want to read from: ")
            client.send(jmbg.encode())

            response = client.recv(1024).decode()
            print(response)

        elif option == "7":
            client.send(option.encode())

            response = client.recv(1024) #this should be a stream, we should dump it to a file

            f = open("result.txt","wb")
            pickle.dump(response,f)
            f.close()

            print("Results are in, let's see what we got")

            f = open("result.txt","r")
            for line in f:
                print(line)
        else:
            print("Invalid option. Please enter a number from 1 to 7.")


try:
    main()
except KeyboardInterrupt:
    print("Closing client...")