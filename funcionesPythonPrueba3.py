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

#Modulo 3 Imprimir Certificado:
def imprimirCertificado(listaUsuarios):
    listaUsuariosMemoria = listaUsuarios
    limpiarPantalla()
    NIF = input("Ingrese NIF a buscar : ")
    for i in range(len(listaUsuariosMemoria)):
        if(listaUsuariosMemoria[i][0] == NIF ):
            switch = True
            while(switch):
                limpiarPantalla()
                seleccion = input("Que certificado desea obtener? : \n1)Certificado Nacimiento \n 2) Certificado Conyugal \n 3) Certificado UE Española \n Opc:")
                if seleccion == "1":
                    certNacimiento = input("Ingrese su fecha de nacimiento : ")
                    print("-"*15 , "CERTIFICADO NACIMIENTO" , "-" * 15)
                    print("NIF: ", listaUsuariosMemoria[i][0])
                    print("NOMBRE :",listaUsuariosMemoria[i][1])
                    print("FECHA NACIMIENTO : " , certNacimiento)
                    input("Presione enter para continuar...")
                    print("-"*15 , "*****************************" , "-" * 15)
                    return
                elif seleccion == "2":
                    certConyugal = input("Ingrese su estado conyugal : ")
                    print("-"*15 , "CERTIFICADO CONYUGAL" , "-" * 15)
                    print("NIF: ", listaUsuariosMemoria[i][0])
                    print("NOMBRE :",listaUsuariosMemoria[i][1])
                    print("ESTADO CONYUGAL : " , certConyugal)
                    input("Presione enter para continuar...")
                    print("-"*15 , "*****************************" , "-" * 15)
                    return
                elif seleccion == "3":
                    certUEE = listaUsuariosMemoria[i][3]
                    print("-"*15 , "CERTIFICADO UNION EUROPEA ESPAÑOLA" , "-" * 15)
                    print("NIF: ", listaUsuariosMemoria[i][0])
                    print("NOMBRE :",listaUsuariosMemoria[i][1])
                    print("¿Pertenece a la UEE? : " , certUEE)
                    print("-"*15 , "*****************************" , "-" * 15)
                    input("Presione enter para continuar...")
                    return
                else:
                    input("Elegir una opcion válida ... Presione enter para continuar")
    #Si llega a este punto , es porque no encontro al usuario ingresando su NIF en la lista , por lo tanto se aborta el proceso.
    print("Vaya... Parece que ese usuario no está registrado en el sistema , abortando proceso de impresión ")
    input("Presione Enter para continuar ...")
    return False
            