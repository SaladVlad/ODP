import socket,pickle

from datetime import date
from profesor import Profesor

recnik = {}
recnik["1"] = Profesor("1","Profa","Profic",date(int(2020),int(10),int(9)),["Algebra","Analiza","Diskretna matematika"])
recnik["2"] = Profesor("2","Rade","Doroslovacki",date(int(1214),int(1),int(7)),["Algebra","Osnove elektrotehnike","Teorija zivota"])

def add_professor(data):

    prof = pickle.loads(data)

    print("Received professor object:", str(prof))

    if prof.jmbg in recnik.keys():
        return "Professor already exists!"
    else:
        recnik[prof.jmbg] = prof
        return "Successfully added professor."

def modify_professor(data):

    prof = pickle.loads(data)

    if prof.jmbg not in recnik.keys():
        return "Professor doesn't exists!"
    else:
        recnik[prof.jmbg] = prof
        return "Successfully modified professor."

def delete_professor(jmbg):

    if jmbg in recnik.keys():
        deleted = recnik.pop(jmbg)
        return f"Successful deletion of [{str(deleted)}]."
    else:
        return "Professor doesn't exist!"

def read_professor(jmbg):
    if jmbg not in recnik.keys():
        return "Professor doesn't exist!"
    else:
        print(f"Found professor with jmbg:[{jmbg}]")
        return str(recnik[jmbg])

def add_things(jmbg,data):
    new_predmeti = pickle.loads(data)
    recnik[jmbg].predmeti.extend(new_predmeti)
    return "Successfully added new stuff"

def get_sorted_items(jmbg):

    if jmbg in recnik.keys():
        items = recnik[jmbg].predmeti.sort()
        string = "Items: \n"
        for item in items:
            string+=item+"\n"
        return string
    else:
        return "Professor doesn't exist"

def get_20yr_profs():
    response = ""

    today = date.today()
    for prof in recnik.values():
        if (today-prof.datum_izbora).days >= 365*20:
            response+=str(prof)+"/n"

    return response

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind(('localhost',8080))
    server.listen()
    print("Listening for new connections...")

    channel,address = server.accept()
    print(f"Accepted connection from: {address};")

    while True:
        option = channel.recv(1024).decode()

        if not option:
            break

        #CRUD operations, responses are of string type
        if option == "1":
            data = channel.recv(1024) #these are serialized bytes, no need to decode
            response = add_professor(data)
            channel.send(response.encode())
            print("Sent response for add option")
        elif option == "2":
            data = channel.recv(1024) #these are serialized bytes, no need to decode
            response = modify_professor(data)
            channel.send(response.encode())
            print("Sent response for modify option")
        elif option == "3":
            data = channel.recv(1024).decode() #decoding data into a readable string
            response = delete_professor(data)
            channel.send(response.encode())
            print("Sent response for delete option")
        elif option == "4":
            data = channel.recv(1024).decode() #decoding data into a readable string
            response = read_professor(data)
            channel.send(response.encode())
            print("Sent response for read option")

        #special operations
        elif option == "5":
            jmbg = channel.recv(1024).decode() #decoding data into a readable string
            if jmbg in recnik.keys(): #if jmbg exists, continue and send confirmation 
                response = "OK"
                channel.send(response.encode())

                data = channel.recv(1024)
                response = add_things(jmbg,data)
                channel.send(response.encode())
            else:
                response = "BAD"
                channel.send(response.encode())

            print("Sent response for adding stuff option")

        elif option == "6":
            jmbg = channel.recv(1024).decode() #decoding data into a readable string
            response = get_sorted_items(jmbg)
            channel.send(response.encode())
            print("Sent response to listing all items")
        elif option == "7":
            response = get_20yr_profs()
            channel.send(response.encode())
            print("Sent response to listing 20 year old profs")

    print("server shutting down.")
    server.close()



#calling main function
try:
    main()
except KeyboardInterrupt:
    print("Keyboard interrupt! Shutting down server...")