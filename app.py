print(" \n  Sabor Express \n ")
print("1. Cadastrar Restaurante")
print("2. Listar restaurante")
print("3. Ativar restaurante")
print("4. Sair\n")

op_escolhida = input("Escolha uma opção: \n")
print(f"você escolheu a opção: {op_escolhida}!")

if op_escolhida == 1:
    print("Cadastrar restaurante")
elif op_escolhida == 2:
    print("Listar restaurante")
elif op_escolhida == 3:
    print("Ativar restaurante")
else:
    print("Encerrando programa...")