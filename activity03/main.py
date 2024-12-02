import math

def areaquadrado (a):
    return  a**2
def arearetangulo (a,b):
    return a*b
def areacirculo (a):
    return math.pi*a**2
def pericirculo (a):
    return math.pi*2*(a)
def periretangulo (a,b):
    a+a+b+b
def periquadrado (a):
    a*4

def calcular_areas():
    while True:
        print("\nEsolha uma operação:" )
        print("1. Area de um quadrado")
        print("2. Area de um retangulo")
        print("3. Area de um circulo")
        print("4. Perimetro de um circulo")
        print("5. Perimetro de um retangulo")
        print("6. Perimetro de um quadrado")
        print("7. Sair")

        opcao= input("Digite o número da operação:")

        if opcao == "7":
            print("saindo...")
            break

        if opcao == "1":
            num1= float(input("Digite um lado do quadrado: "))
            print(f"A área do quadrado é: {areaquadrado(num1)}")
        elif opcao == "2": 
            num1= float(input("digite o menor lado do retangulo: "))
            num2= float(input("digite o maior lado do retangulo: "))
            print(f"O resultado da subtração é: {arearetangulo(num1, num2)}")
        elif opcao == '3':
            num1= float(input("digite o raio do circulo: "))
            print(f"O resultado da multiplicação é: {areacirculo(num1)}")
        elif opcao == '4':
            num1= float(input("digite o raio do circulo: "))
            print(f"O resultado da divisão é: {pericirculo (num1)}")
        elif opcao == '5':
            num1= float(input("digite o menor lado do retangulo: "))
            num2= float(input("digite o maior lado do retangulo: "))
            print(f"O resultado da divisão é: {periretangulo(num1, num2)}")
        elif opcao == '6':
            num1= float(input("digite um lado do quadrado: "))
            print(f"O resultado da divisão é: {periquadrado(num1)}")
        else:
            print(f"Opção inválida!")

calcular_areas()

