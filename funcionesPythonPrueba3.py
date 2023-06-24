import os


def limpiarPantalla():
    os.system('cls')

def grabarDatosUsuario():
    errorDato = False
    while( not errorDato):
        NIF = input("Ingrese su NIF : ")
        if(len(NIF) < 8):
            print("Porfavor ingrese un NIF válido (Mín 8 caracteres)")
        else:
            nombreUsuario = input("Ingrese su nombre : ")
            errorEdad = True
            while (errorEdad):
                edadUsuario = input("Ingrese su edad : ")
                #Castear edad para forzar edades enteras
                edadUsuario = int(edadUsuario)
                if (edadUsuario <= 0 ):
                    print("Porfavor ingrese una edad válida (Mayor a 0)")
                else:
                    print("El usuario ha sido grabado satisfactoriamente en el sistema . ")
                    input("Presione una tecla para continuar")
                    limpiarPantalla()
                    return [NIF,nombreUsuario,edadUsuario]
        

            