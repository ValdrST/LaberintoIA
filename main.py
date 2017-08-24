# -*- coding: utf-8 -*-
"""
Created on Mon May 15 16:20:00 2017

@author: Valdr
"""
import math
import os
vida = 100
trampas = []
pila = []
visitados = []
posibles = []
laberinto=[]

def leerLaberinto():
    archLab=open("Laberinto.txt","r")
    cordMax = archLab.readline()
    cordMax=cordMax.split(',')
    cordMax.pop()
    print(cordMax)
    for line in archLab:
	    line=line.split(',')
	    line.pop()
	    laberinto.append(line)
    archLab.close()
    return laberinto
    
def imprimeLaberinto(x,raton,salida):
    os.system("cls")
    print("+",end="")
    for col in range(0,len(x[0])):
        print("-",end="")
    print("+")
    for ren in range(0,len(x)):
        print("|",end="")
        for col in range(0,len(x[0])):
            if (ren,col)== raton and raton== salida:
                print("#",end="")
            elif raton==(ren,col):
                print("R",end="")
            elif salida==(ren,col):
                print("S",end="")
            else:
                try:
                    pila.index((ren,col))
                    print("*",end="")
                except:
                    print(x[ren][col],end="")
        print("|")
    print("+",end="")
    for col in range(0,len(x[0])):
        print("-",end="")
    print("+")
    print("Trampas tocadas: ",trampas)
    print("salida: ",salida)
    return
def push(pila,p):
    pila.append(p)
    return

def pop(pila):
    try:
        return pila.pop()
    except:
        return()

def tos(pila):
    try:
        return pila[len(pila)-1]
    except:
        return()

def visitado(pos):
    try:
        visitados.index(pos)
        return True
    except:
        return False
    return

def camino(pos):
    (ren,col)=pos
    if ren<0:
        return False
    elif col<0:
        return False
    elif ren>len(laberinto)-1:
        return False
    elif col>len(laberinto[0])-1:
        return False
    elif laberinto[ren][col]!='x':
        return True
    return False

def movimiento(raton, salida):
    global vida
    if raton==():
        return ()
    (ren,col)=raton
    op1=100
    op2=100
    op3=100
    op4=100
    if camino((ren-1,col)) and not visitado((ren-1,col)) and (trampa((ren-1,col)))<vida:
        op1=distancia((ren-1,col),salida)
    if camino((ren+1,col)) and not visitado((ren+1,col)) and (trampa((ren+1,col)))<vida:
        op2=distancia((ren+1,col),salida)
    if camino((ren,col-1)) and not visitado((ren,col-1)) and (trampa((ren,col-1)))<vida:
        op3=distancia((ren,col-1),salida)
    if camino((ren,col+1)) and not visitado((ren,col+1)) and (trampa((ren,col+1)))<vida:
        op4=distancia((ren,col+1),salida)
    if op1<op2 and op1<op3 and op1<op4:
        vida=vida-trampa((ren-1,col))
        visitados.append((ren-1,col))
        return ((ren-1,col))
    if op2<op1 and op2<op3 and op2<op4:
        vida=vida-trampa((ren+1,col))
        visitados.append((ren+1,col))
        return ((ren+1,col))
    if op3<op1 and op3<op2 and op3<op4:
        vida=vida-trampa((ren,col-1))
        visitados.append((ren,col-1))
        return ((ren,col-1))
    if op4<op1 and op4<op2 and op4<op3:
        vida=vida-trampa((ren,col+1))
        visitados.append((ren,col+1))
        return ((ren,col+1))
    return ()
    
def leerPosicion(nombre):
    print("posicion de ", nombre)
    pos=[0,0]
    pos[0],pos[1]=int(input("posicion x: ")),int(input("posicion y: "))
    (ren,col)=pos
    if ren<0:
        print("posicion invalida, fuera de laberinto")
        return exit()
    elif col<0:
        print("posicion invalida, fuera de laberinto")
        return exit()
    elif ren>len(laberinto)-1:
        print("posicion invalida, fuera de laberinto")
        return exit()
    elif col>len(laberinto[0])-1:
        print("posicion invalida, fuera de laberinto")
        return exit()
    elif laberinto[ren][col]=='x':
        print("posicion invalida, esta dentro de una pared")
        return exit()
    pos=tuple(pos)
    return pos

def trampa(pos):
    (ren,col) = pos
    if laberinto[ren][col]== ' ':        
        return 0.2
    if laberinto[ren][col]== 'A':
        trampas.append(pos)        
        return 0.5
    if laberinto[ren][col]== 'F':
        trampas.append(pos)        
        return 0.5
    if laberinto[ren][col]== 'G':
        trampas.append(pos)        
        return 2
    if laberinto[ren][col]== 'L':
        trampas.append(pos)        
        return 3
    return 0.0

def distancia(pos, salida):
    (ren1,col1) = pos
    (ren2,col2) = salida
    x = ren1-ren2
    y = col1-col2 
    lengthy = math.sqrt((x*x)+(y*y))
    return lengthy
    
def main():
    global vida
    laberinto=leerLaberinto()
    raton=[0,0]
    salida=[0,0]
    raton=leerPosicion("raton")
    salida=leerPosicion("salida")
    push(pila,raton)
    while True:
        raton=movimiento(raton,salida)
        if raton==():
            pop(pila)
            raton=tos(pila)
            if raton==():
                print("el raton se murio por jugarle alv")
                break
            imprimeLaberinto(laberinto,raton,salida)
            print(vida)
        else:
            push(pila,raton)
            imprimeLaberinto(laberinto,raton,salida)
            print(vida)
            if salida==raton:
                print("Vidas: ",vida)
                print("el raton llego al queso :)")
                break
        print("posicion actual",raton)
    if pila!=():
        print("ruta de salida del raton: ",pila)  
    return
main()
