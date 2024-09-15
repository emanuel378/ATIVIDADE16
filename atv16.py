# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso =float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura"))
imc= peso/altura

if imc<18.5:
    print("Abaixo do peso")
elif imc <25:
    print("Peso normal")

elif imc<30:
    print("Sobrepeso")

elif imc>=30:
    print("Obsidade")
