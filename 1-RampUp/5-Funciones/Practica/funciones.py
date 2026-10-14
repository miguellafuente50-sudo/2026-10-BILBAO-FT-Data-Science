def dias_semanas(numero):
    dias_ = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    if 1 <= numero <= 7:
        if numero == 1:
            return dias_[0]
        elif numero == 2:
            return dias_[1]
        elif numero == 3:
            return dias_[2]
        elif numero == 4:
            return dias_[3]
        elif numero == 5:
            return dias_[4]
        elif numero == 6:
            return dias_[5]
        elif numero == 7:
           return dias_[6]
    else:
        return "Número no válido. Introduce un número del 1 al 7."


def piramides(filas):
    for i in range(filas, 0, -1):
        print(str(i)*i)
    




def comp(num1,num2):
    if num1 == num2:
        return "Son iguales"
    elif num1 > num2:
        return "El primero es mayor"
    elif num2 > num1:
        return "El segudo es mayor"



def contador(palabra,letras):
    contador = 0
    for letra in palabra:
        if letra == letras:
            contador +=1
    return contador


def dic(texto):
    diccionario = {}

    for letra in texto:
        if letra in diccionario:
            diccionario[letra] +=1
        else:
            diccionario[letra] = 1
    



def editor(lista,comando,elemento:None):
    if comando == "Add":
        lista.append(elemento)
    elif comando == "Remove":
        lista.remove(elemento)
    else:
        print("Comando erronio ")
    print(lista)


def num(palabra):
    frase = " ".join(palabra)
    return frase    


def fibo(num:int):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)



def cuadrado(lado):
    area = lado **2
    return area

def triangulo(base,altura):
    area = (base * altura)/2
    return area

def circulo(radio):
    area = math.pi * radio **2
    return area

import math


