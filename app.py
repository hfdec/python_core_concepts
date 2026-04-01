import os # faz import da lib para limpar o terminal...
print(" \n  Sabor Express \n ")
print("1. Cadastrar Restaurante")
print("2. Listar restaurante")
print("3. Ativar restaurante")
print("4. Sair\n")

op_escolhida = int(input("Escolha uma opção: \n"))
# op_escolhida = int(op_escolhida) é valido tmb
print(f"você escolheu a opção: {op_escolhida}!\n")


def encerrar_programa():
    os.system("clear")
    print("\n\nEncerrando programa...")





if op_escolhida == 1:
    print("Cadastrar restaurante")
elif op_escolhida == 2:
    print("Listar restaurante")
elif op_escolhida == 3:
    print("Ativar restaurante")
else:
    encerrar_programa()