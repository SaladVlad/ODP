import socket, pickle
from student import Student

studenti = {}
studenti["PR1/2020"] = Student("Petar", "Petrović", "PR1/2020", 10.0)
studenti["PR2/2020"] = Student("Marko", "Marković", "PR2/2020", 9.0)
studenti["PR3/2020"] = Student("Jovan", "Jovanović", "PR3/2020", 8.0)
studenti["PR4/2020"] = Student("Milan", "Milanović", "PR4/2020", 7.0)
studenti["PR5/2020"] = Student("Mirko", "Mirković", "PR5/2020", 6.0)

def pronadji_studenta(broj_indeksa : str):
    print(f"Traži se student sa brojem indeksa: {broj_indeksa}")
    if broj_indeksa not in studenti: 
        print(f"Student sa brojem indeksa: {broj_indeksa} ne postoji u bazi!")
        return f"Student sa brojem indeksa: {broj_indeksa} ne postoji u bazi!"
    return studenti[broj_indeksa].__str__()

def dodaj_izmeni_studenta(poruka):
    student = pickle.loads(poruka)
    studenti[student.broj_indeksa] = student
    return f"Student sa broj indeksa {student.broj_indeksa} uspesno upisan/izmenjen."
        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 6000))
server.listen()
print("Server je pokrenut.")

kanal, adresa = server.accept()
print(f"Prihvacena je konekcija sa adrese: {adresa}")

while True: 
    poruka = kanal.recv(1024)
    if not poruka : break
    try:
        student = dodaj_izmeni_studenta(poruka)
        kanal.send(student.encode())
    except:
        student = pronadji_studenta(poruka.decode())
        kanal.send(student.encode())
    
print("Server se gasi.")
server.close()


    
