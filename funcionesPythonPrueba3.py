import os
# Limpiar pantalla
def limpiarPantalla():
    os.system('cls')

#Modulo 1 Grabar Datos
def grabarDatosUsuario():
    errorDato = False
    while(not errorDato):
        NIF = input("Ingrese su NIF : ")
        if(NIF.find("-") == -1):
            limpiarPantalla()
            print("Porfavor ingrese un NIF válido (Formato : 99999999-XXX)")
        else:
            listaNIF = NIF.split("-")
            if(len(listaNIF[0]) < 9) :
                print("Porfavor ingrese un NIF válido (Formato : 99999999-XXX)")
            else:
                errorNombre = True
                while(errorNombre):
                    nombreUsuario = input("Ingrese su nombre : ")
                    if(len(nombreUsuario) < 8):
                        print("Porfavor ingrese un nombre válido (Mín 8 caracteres)")
                    else:
                        errorNombre = False
                        errorEdad = True
                        while (errorEdad):
                            edadUsuario = input("Ingrese su edad : ")
                            #Castear edad para forzar edades enteras
                            edadUsuario = int(edadUsuario)
                            if (edadUsuario <= 0 ):
                                limpiarPantalla()
                                print("Porfavor ingrese una edad válida (Mayor a 0)")
                            else:
                                if(listaNIF[1].upper() == 'RTX' or listaNIF[1].upper() == 'XXY' or listaNIF[1].upper() == 'CCU' or listaNIF[1].upper() == '03F'):
                                    perteneceUE = "Pertenece a la Unión Europea Española"
                                else:
                                    perteneceUE = "No pertenece a la Unión Europea Española"
                                print("El usuario ha sido grabado satisfactoriamente en el sistema . ")
                                input("Presione una tecla para continuar")
                                limpiarPantalla()
                                return [NIF,nombreUsuario,edadUsuario,perteneceUE]
        
#Modulo 2 Buscar Usuario:
def buscarUsuario(listaUsuarios):
    listaUsuariosMemoria = listaUsuarios
    encontrado = True
    while(encontrado):
        limpiarPantalla()
        NIF = input("Ingrese NIF a buscar : ")
        for i in range(len(listaUsuariosMemoria)):
            if(listaUsuariosMemoria[i][0] == NIF ):
                for j in range(len(listaUsuariosMemoria[i])):
                    print(listaUsuariosMemoria[i][j])
                input("Presione enter para continuar...")
                return
        encontrado = False
        if (not encontrado):
            respuesta = input("Vaya... Parece que ese usuario no está registrado en el sistema \n ¿Desea buscar nuevamente? S/N :  ")
            if(respuesta.upper() == "N"):
                return
            else:
                encontrado = True
    

            