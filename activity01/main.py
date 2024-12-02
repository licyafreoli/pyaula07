import infos

def calculadora():
    while True:
        print("\nEsolha uma operação:" )
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao= input("digite o número da operação:")

        if opcao == "5":
            print("saindo...")
            break
        
        num1= float(input("digite o primeiro número: "))
        num2= float(input("digite o segundo número: "))

        if opcao == "1":
            print(f"o resultado da soma é: {infos.soma(num1,num2)}")
        elif opcao == "2": 
            print(f"O resultado da subtração é: {infos.sub(num1, num2)}")
        elif opcao == '3':
            print(f"O resultado da multiplicação é: {infos.mult(num1, num2)}")
        elif opcao == '4':
            print(f"O resultado da divisão é: {infos.div(num1, num2)}")
        else:
            print(f"Opção inválida!")

calculadora()