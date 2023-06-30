import funciones as fn
import os

while True:
    os.system("cls")
    fn.ver_opciones()
    opcion=fn.validar_opcion()
    
    if opcion==1:
        fn.grabar()
    
    elif opcion==2:
        fn.buscar_dueño()
    
    elif opcion==3:
        fn.retirarse()

    else:
        break

