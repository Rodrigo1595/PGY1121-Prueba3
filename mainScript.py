import funcionesPythonPrueba3 as fp
lista = []
menu = True
while(menu):
    print("* Bienvenido al registro civil de Andalucía *")
    respuesta = int(input("Porfavor ingrese opción a utilizar : ")) 
    if respuesta == 1:
        data = fp.grabarDatosUsuario()
        lista.append(data)
    elif respuesta == 2:
        data
    elif respuesta == 3:
        data
    elif respuesta == 4:
        menu = False
    elif respuesta == 5: 
        print(lista)   