def f1(lista):
    maks = max(lista)
    lista.remove(maks)
    minim = min(lista)
    lista.remove(minim)
    lista.insert(0,maks)
    lista.append(minim)

def f2(*args):
    n = 0
    if len(args) == 3:
        for value in args:
            n+=value
    elif len(args) > 0:
        n=1
        for value in args:
            n*=value
    else:
        raise Exception("Nije dobar broj parametara")
    return n

def f3(a,b):
    result = 0
    try:
        if b==0: raise ZeroDivisionError()
        else: 
            result = int(a)/int(b)
            return result
    except:
        print("Ne mozes deliti sa nulom!")
    finally:
        return result

def f4(lista):
    sortirano = sorted(lista,key=lambda x: int(x))
    return sortirano

anonF = lambda l:(int(l)%2==0 and int(l)<0)

def f5(lista,anonF):
    for l in lista:
        lista = filter(anonF(l),lista)
    return lista

def f6(lista):
    for l in lista:
        print(lista)


print("=============1==============")
lista = [2,5,3,10,4,1,6]
f1(lista)
print(lista)

print("=============2==============")
print("Rezultat: ", f2(3,2,2))
print("Rezultat: ",f2(5,5,5,5))

print("=============3==============")
print("Rezultat: ",f3(5,2))
print("Rezultat: ",f3(2,0))

print("=============4==============")
lista = ["10", "2", "19", "0", "-1", "-20", "5"]
print(f4(lista))

print("=============5==============")
lista = [2, 15, -5, 28, 9, -30, 4, -1] 
print(f5(lista,anonF))

lista = ["10", "2", "19", "0", "-1", "-20", "5"] 
print(f6(lista))