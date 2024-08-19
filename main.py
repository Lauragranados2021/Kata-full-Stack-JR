#e62c3c89eb4095943dfe28ed5cfad7de mi numero en hash numero a trabaja=6
s=6
def challenge_one():
    vectorEntrada=[]
    vectorSalida = []
    s=6
    try:
        n = int(input("Ingrese la cantidad de digitos dentro de su vector (menor a 100): "))
        if(n<=100 and n >0):
            while len(vectorEntrada)<n:
                num = input("Ingrese los digitos:  ")
                if int(num)>0:
                    vectorEntrada.append(num)
                else:
                    print("Debe ingresar valores mayores a 0 ")
##CON EL SEGUNDO FOR SOLO PODEMOS CUADRAR NUMEROS DE A PAREJAS POR ESO ES NECESARIO REPETIR EL PROCESO, EL PRIMER FOR LO QUE HACE ES AYUDARME HACER EL PROCESO CUANTAS VECES NECESITE
            for i in range(len(vectorEntrada) - 1):
                for j in range (0,len(vectorEntrada)-i-1):
                    if vectorEntrada[j]>vectorEntrada[j+1]:
                        vectorEntrada[j],vectorEntrada[j+1]=vectorEntrada[j+1],vectorEntrada[j]
# #ES NECESARIO HACERLO ASI PORQUE CON EL SEGUNDO FOR PUEDO REVISAR PAREJAS CONSECUTIVAS PERO NO PUEDO COMPARAR EL PRIMERO CON EL TERCERO POR EJEMPLO
            for i in range(len(vectorEntrada)):
                separar=str(vectorEntrada[i])
                div = [int(digito) for digito in separar]
                for e in div:
                    if e<s:
                        vectorSalida.append(e)
            print (vectorEntrada)
            print (vectorSalida)
        else:
            print("Usted escribio un numero mayor a 100 o menor a 0 , la entrada no es valida ")
    except Exception as e:
        print('digitaste un valor incorrecto ')

def challenge_two():
    vectorEntrada = []
    vectorSalida = []
    try:
        # pedimos el tamaño del vector y verificamos que no sea vacio
        n = int(input("Ingrese la cantidad de digitos dentro de su vector debe ser mayor a 0 "))
        if (n>0):
            # un ciclo para pedir los digitos
            while len(vectorEntrada) < n:
                num = input("Ingrese los digitos:  ")

                vectorEntrada.append(num)

            print( vectorEntrada)

            for e in vectorEntrada:
                    cuadrado=pow(int(e),2)
                    if cuadrado<=66:
                        vectorSalida.append(cuadrado)
            print(vectorSalida)
            # el primer for comprueba que los numeros esten en la posicion correcta
            for i in range(len(vectorSalida)-1):
                #el segundo comprueba entre dos numeros, primera con segunda, segunda con tercera ... para poner al mayor en la parte izquierda
                for j in range(0,len(vectorSalida)-i-1):
                    if vectorSalida[j]>vectorSalida[j+1]:
                        #cambia los valores de ambas posicones
                        vectorSalida[j],vectorSalida[j+1]=vectorSalida[j+1],vectorSalida[j]

            print(vectorSalida)
        else:
            print("Su vector no debe estar vacio")
    except Exception as e:
        print('digitaste un valor incorrecto ')
def challenge_three():
    vectorEntrada = []
    try:
        n = int(input("Ingrese el tamaño de su matriz: "))
        if (n>0):
            # un ciclo para pedir los digitos
            while len(vectorEntrada) < n:
                num = int(input("Ingrese el valor de sus monedas. Recuerde que deben ser positivos:  "))
                if num>0:
                    vectorEntrada.append(num)
                else:
                    print("usted agrego una moneda negativa, eso no existe")
                    #Primero lo ordeno
            vectorEntrada.sort()
            #la suma minima de dinero
            #el minimo cambio que puedo hacer es 1 pero ira sumando a medida que encuentre mas monedas de otros valores
            cambio=1
            for i in vectorEntrada:
                #compruebo que el cambio sea menor a la moneda que tengo, si llega a ser mayor entonces significa que ese es mi mayor
                if(i<=cambio):
                    cambio=cambio+i
                else:
                    break

            print( vectorEntrada)
            print(cambio)

    except Exception as e:
        print('digitaste un valor incorrecto ')
while True:
    print("\nMenú:")
    print("1. Desafío 1")
    print("2. Desafío 2")
    print("3. Desafío 3")
    print("4. Salir")

    choice = input("Ingrese el número del desafío que desea ejecutar (1-3) presiones 4 para salir: ")

    if choice == '1':
        challenge_one()
    elif choice == '2':
        challenge_two()
    elif choice == '3':
        challenge_three()
    elif choice == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 4.")
