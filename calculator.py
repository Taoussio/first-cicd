#This is a comment2
#Ceci est une calculatrice en python

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b
