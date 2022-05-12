# Nome
# Senha
# Repetir senha
# Email 

def cadastrar():
    print("Tela de Cadastro:")
    nome = input("Nome: ")
    senha = input("Senha:")
    print(nome)
    print(senha)

def escolha():
    if c == '1':
        print("cadastrar()")
    elif c == '2':
        print('consultar()')
    elif c == '0':
        print("Sair")
    else:
        print("Comando inválido")

def interface():
    print("Banco de Dados")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("0 - Sair\n")
    c = input("> ")
    print(c)
    
interface()