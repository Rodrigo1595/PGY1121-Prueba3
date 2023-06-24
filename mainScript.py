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
        fp.limpiarPantalla()
    elif respuesta == 3:
        fp.limpiarPantalla()
        data = fp.imprimirCertificado(lista)
        fp.limpiarPantalla()
    elif respuesta == 4:
        menu = False
        print("¡Hasta Pronto!")
    #Herramienta seleccion para debuggear lista
    elif respuesta == 999: 
        print(lista)   
        input("Presionar Tecla")
        fp.limpiarPantalla()