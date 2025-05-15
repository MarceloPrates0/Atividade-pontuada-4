from dataclasses import dataclass
import time
import os
os.system("cls || clear")

listFuncionarios = []
arquivo = "dadosFuncionarios.csv"
# Classes 
@dataclass
class Funcionario:
    nome: str
    cpf: str
    cargo: str
    salario: float
    


# Função para validar a lista.
def validarLista(lista):
    if not lista:     
        print("\n Lista está vazia.")
        return True
    return False 

#Adicionando os dados dos funcionarios.
def adicionarFuncionario(lista):
    funcionario = Funcionario(input("Insira o nome que deseja adicionar: "),
                              input("Insira o CPF: "),
                              input("Insira o respectivo cargo: "),
                              float(input("Insira o salário para cadastro: ")))
    lista.append(f"Nome: {funcionario.nome}")
    lista.append(f"CPF: {funcionario.cpf}")
    lista.append(f"Cargo: {funcionario.cargo}")
    lista.append(f"Salario: {funcionario.salario}")
    print("Dados adicionados com sucesso.")
    

#Função para remover os dados adicionados e selecionar qual dado especifico remover.
def remover(lista):
    if validarLista(listFuncionarios):
        return
    
    mostrarFuncionarios(listFuncionarios)
    dadoRemover = input("Insira o dado que deseja remover: ")
    if dadoRemover in listFuncionarios:
        lista.remove(dadoRemover)
        print(f"O dado {dadoRemover} foi removido.")

    else:
        print("Dado não encontrado")

#Função para mostrar os dados adicionados na lista.
def mostrarFuncionarios(lista):
    if validarLista(listFuncionarios):
        return
    
    print(" - LIsta de Funcionarios - ")
    for funcionario in lista:
        print(f"- {funcionario}- ")

#Função para atualizar os dados adicionados e espeficicar qual quer remover.
def atualizarFuncionario(lista):
    if validarLista(lista):
        return
    
    mostrarFuncionarios(lista)
    dadoAntigo = input("Digite o Dado deseja atualizar: ")
    if dadoAntigo in lista:
        novodado = input(f" Digite o novo Dado: ")
        indice = lista.index(dadoAntigo)
        lista[indice] = novodado
        print(f"{dadoAntigo} foi atualizad para {novodado}.")
    else:
        print(f"\n O dado {dadoAntigo} não foi encontrado.")

#Função para gravar dados inseridos na lista em formato CSV.
def gravaDadoCsv(lista):
    if validarLista(listFuncionarios):
        return
    
    with open(arquivo, "w") as gravaDado:
        for funcionario in lista:
            gravaDado.write(f"{funcionario}\n")

#Função para exibir a lista guardada na memoria do arquivo.
def exibeDadoCsv(arquivo):
    with open(arquivo, 'r') as exibeDado:
        linhas = exibeDado.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")

#Menu interativo sendo exibido com seus respectivos comandos sendo executados com funções
while True:
    print("""
===CADASTRO DE FUNCIONÁRIOS===
1 - Adicionar funcionário
2 - Listar funcionários cadastrados
3 - Remover funcionário
4 - Atualizar dados
5 - Gravar dados no banco de dados
6 - Exibir dados cadastrados
7 - Encerrar programa
""")
    comando = int(input("Insira a ação que deseja executar: "))
    match comando:
        case 1:
            adicionarFuncionario(listFuncionarios)
        case 2:
            mostrarFuncionarios(listFuncionarios)
        case 3:
            remover(listFuncionarios)
        case 4:
            atualizarFuncionario(listFuncionarios)
        case 5:
            gravaDadoCsv(listFuncionarios)
        case 6:
            exibeDadoCsv(arquivo)
        case 7:
            print("Encerrando programa...")
            break
        case _:
            print("Opção inválida\nTente Novamente.")
    time.sleep(2) 
    os.system("cls || clear)
