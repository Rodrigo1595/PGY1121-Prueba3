import funcionesPythonPrueba3 as fp
lista = []
menu = True
while(menu):
    print("* Bienvenido al registro civil de Andalucía *")
    respuesta = int(input("Porfavor ingrese opción a utilizar : \n 1)Grabar usuario \n 2)Buscar Usuario \n 3)Imprimir Certificado \n 4)Salir \n Opc :  ")) 
    if respuesta == 1:
        fp.limpiarPantalla()
        data = fp.grabarDatosUsuario()
        lista.append(data)
    elif respuesta == 2:
        fp.limpiarPantalla()
        data = fp.buscarUsuario(lista)
    elif respuesta == 3:
        data
    elif respuesta == 4:
        menu = False
    #Herramienta DEV para debuggear lista
    elif respuesta == 5: 
        print(lista)   
        input("Presionar Tecla")
        fp.limpiarPantalla()