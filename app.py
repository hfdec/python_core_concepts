import os # faz import da lib para limpar o terminal...
def exibir_menu():  
    print("=========================")
    print(" \n  SABOR EXPRESS \n ")
    print("=========================")

def exibir_opcoes():
    print("=========================")
    print("1. Cadastrar Restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair ")
    print("=========================")

def encerrar_programa(): 
    print("=========================")
    os.system("clear")
    print("\n\nEncerrando programa...")

def escolher_opcao():
    op_escolhida = int(input("Escolha uma opção: \n"))
    print(f"você escolheu a opção: {op_escolhida}!\n")
    if op_escolhida == 1:
        print("Cadastrar restaurante")
    elif op_escolhida == 2:
        print("Listar restaurante")
    elif op_escolhida == 3:
        print("Ativar restaurante")
    else:   
     encerrar_programa()




def main():
    exibir_menu()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__" : 
    main()