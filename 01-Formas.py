def num_input(text):
    while True:
        a = input(text)
        try:
            return float(a)
        except ValueError:
            print("erro ao processar entrada")

def circulo():
    raio = num_input("insira o raio do circulo: ")
    
    area = raio * 3.14
    print(f"a area do seu circulo é {area:.2f}")

def triangulo():
    base = num_input("insira a largura do triângulo: ")
    altura = num_input("insira a altura do triângulo: ")
    
    area = base*altura/2
    print(f"a area do seu triângulo: {area}")

def quadrado():
    altura = num_input("insira a altura do quadrado: ")
    
    area = altura**2
    print(f"a area do seu quadrado: {area}")

def retangulo():
    base = num_input("insira a largura do retângulo: ")
    altura = num_input("insira a altura do retâgulo: ")
    
    area = base*altura
    print(f"a area do seu reângudo: {area}")

while True:
    print("1 - Circulo")
    print("2 - Triângulo")
    print("3 - Quadrado")
    print("4 - Retângulo")
    print("5 - Paralelograma")
    print("6 - Losango")
    print("7 - Trapésio")
    print("0 - Sair do Programa")

    opcao = input("selecione a forma que você deseja calcular: ")

    if opcao == "1":
        circulo()
    elif opcao == "2":
        triangulo()
    elif opcao == "3":
        quadrado()
    elif opcao == "4":
        retangulo()
    elif opcao == "5":
        print("calculando")
    elif opcao == "6":
        print("calculando")
    elif opcao == "7":
        print("calculando")
    elif opcao == "0":
        break
    else:
        print("Opção invalida")