def run():
    import math
    # diccionario = {}
    # for i in range(1,101):        
    #     if i%3 != 0:
    #         diccionario[i] = i**3

    # print(diccionario)
    
    # diccionario = {i: i**3 for i in range(1,101) if i%3 != 0}
    # print(diccionario)

    # Reto: 1000 primeros numeros con su raiz cuadrada
    #numeros = {i: round(math.sqrt(i),2) for i in range(1, 1001)}
    numeros = {i: round(i**0.5, 2) for i in range(1, 1001)}
    print(numeros)


if __name__ == '__main__':
    run()