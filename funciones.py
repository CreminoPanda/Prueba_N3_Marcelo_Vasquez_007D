import numpy
import os
import msvcrt
import time

lista_rut=[]
lista_nombre=[]
id_unico=[]
lista_mascotas=[]
lista_fila=[]
lista_columna=[]
valor_dia=15000
lista_dias=0

cajitas=numpy.zeros((2,5),int)

def ver_opciones():
    print("""Bienvenido a la guardería Mascota Segura, Seleccione la opción que desea:
    1. Grabar
    2. Buscar mascota
    3. Retirarse
    4. Salir
    """)

def mostrar_habitaciones():
    print("Habitacion:      1 2 3 4 5")
    for x in range(2):
        print("\tFila",[x+1],end=" ")
        for i in range(5):
            print(cajitas[x][i],end=" ")
        print()

def validar_opcion():
    while True:
        try:
            opcion=int(input("Ingrese la opción que desea: "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! DEBE INGRESAR UNA OPCIÓN VALIDA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su rut(Sin puntos ni digito verificador): "))
            if rut>1000000 and rut<=99999999:
                return rut
            else:
                print("ERROR! RUT INGRESADO NO ES VALIDO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_nombre():
    while True:
        nombre=input("Ingrese su nombre: ")
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE MAYOR A 3 LETRAS!")

def validar_nombre_mascota():
    while True:
        nombre_mascota=input("Ingrese el nombre de su mascota: ")
        if len(nombre_mascota.strip())>=3 and nombre_mascota.isalpha():
            return nombre_mascota
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE MAYOR A 3 LETRAS!")

def cantidad_dias():
    while True:
        try:
            dias=int(input("Ingrese la cantidad de días a hospedar a la mascota: "))
            if dias>=1 and dias<=100:
                lista_dias=lista_dias+dias
                return dias
            else:
                print("ERROR! DEBE INGRESAR UNA CANTIDAD DE DIAS ENTRE 1 Y 100 DIAS")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def piso_arra():
    while True:
        try:
            fila=int(input("Ingrese la fila que desea: "))
            if fila in(1,2):
                return fila
            else:
                print("ERROR! DEBE INGRESAR UNA FILA ENTRE 1 Y 2")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def columna_array():
    while True:
        try:
            columna=int(input("Ingrese la habitación que desea: "))
            if columna in(1,2,3,4,5):
                return columna
                
            else:
                print("ERROR! DEBE INGRESAR UNA HABITACIÓN ENTRE 1 Y 5")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def grabar():
    cant_dias=0
    rut=validar_rut() 
    nombre=validar_nombre()
    nombre_mascota=validar_nombre_mascota()
    dias=cantidad_dias()
    mostrar_habitaciones()
    
    fila=piso_arra()
    columna=columna_array()

    if 0 not in cajitas:
        print("NO HAY HABITACIÓNES DISPONIBLES!")

    if cajitas[fila-1][columna-1]==0:
        cajitas[fila-1][columna-1]=1
        print("REGISTRO EXITOSO!")
    else:
        print("TODAS LAS HABITACIÓNES ESTAN OCUPADAS!")
    

    lista_rut.append(rut)
    lista_nombre.append(nombre)
    lista_mascotas.append(nombre_mascota)
    lista_fila.append(fila)
    lista_columna.append(columna)
    lista_dias=+dias
    time.sleep(3)



def buscar_dueño():
    rut=validar_rut()
    if rut in lista_rut:
        mostrar_habitaciones()
        print(f"Su mascota se encuentra en la fila{lista_fila} y en la habitacion{lista_columna}")
        time.sleep(3)

def retirarse():
    rut=validar_rut()
    total=lista_dias*valor_dia
    print("Su total a pagar es:",total)
    time.sleep(3)
    

