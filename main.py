from Cliente import Cliente
from Produto import Produto
import xlrd
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

cont = 100
obj = []
objcli = []
prodatb = []

while(cont != 0):
    print("1 - Cliente")
    print("2 - Produto")
    print("0 - Sair")
    print("Escolhida: ")
    x = int(input())

    if(x == 1):


        print("--Informe o Metodo de Inserção Cliente--")
        print("1 - Manual")
        print("2 - Listar Manual e inserir no MongoDB")
        print("3 - Planilha")
        print("4 - Listar Planilha e inserir no MongoDB")
        print("Escolhida: ")
        y = int(input())

        if (y == 1):

            print("---Informe os Dados---")

            print("ID: ")
            a = input()

            print("Nome: ")
            b = input()

            print("Telefone: ")
            c = input()

            print("Endereço: ")
            d = input()

            print("Cidade: ")
            e = input()

            print("Estado: ")
            f = input()

            print("Nascimento:")
            g = input()

            print("-----------------------------")

            z = Cliente(a, b, c, d, e, f, g)

            obj.append(z)

        elif (y == 2):
            i = 0
            while i < len(obj):
                print("-----------------------------")
                print((" ID : {} \n Nome : {} \n Telefone : {} \n Endereço : {} \n Cidade : {} \n Estado : {} \n Nascimento : {} \n").format(obj[i].getID(), 
                    obj[i].getNome(), obj[i].getTelefone(), obj[i].getEndereco(), obj[i].getCidade(), obj[i].getEstado(), obj[i].getNasc()))
                print("-----------------------------")
                i += 1

        elif (y == 3):
            book = xlrd.open_workbook("cliente.xls")

            sh = book.sheet_by_index(0)

            print("-----------------------------")
            print("A Planilha Foi Lida !")

        elif (y == 4):
            i = 1
            while i < 6:
                x = mycol.insert_one({"ID" : (sh.cell_value(rowx=0, colx=i)),
                "Nome" : (sh.cell_value(rowx=1, colx=i)),
                "Telefone" : (sh.cell_value(rowx=2, colx=i)),
                "Endereco" : (sh.cell_value(rowx=3, colx=i)),
                "Cidade" : (sh.cell_value(rowx=4, colx=i)),
                "Estado" : (sh.cell_value(rowx=5, colx=i)),
                "Nascimento" : (sh.cell_value(rowx=6, colx=i))})

                print(x.inserted_id)
                
                i += 1

        elif (y == 0):
            break

    elif(x == 2):
        print("--Informe o Metodo de Inserção PRODUTO--")
        print("1 - Manual")
        print("2 - Listar Manual e inserir no MongoDB")
        print("3 - Planilha")
        print("4 - Listar Planilha e inserir no MongoDB")
        print("3 - Ler Site Extra")
        print("4 - Listar e inserir Site no MongoDB")
        print("Escolhida: ")
        y = int(input())

        if (y == 1):

            print("---Informe os Dados---")

            print("ID: ")
            a = input()

            print("Nome: ")
            b = input()

            print("Preço: ")
            c = input()

            print("Entrada: ")
            d = input()

            print("Saida: ")
            e = input()

            print("-----------------------------")

            z = Cliente(a, b, c, d, e)

            objcli.append(z)

        elif (y == 2):
            i = 0
            while i < len(obj):
                print("-----------------------------")
                print((" ID : {} \n Nome : {} \n Preço : {} \n Entrada : {} \n Saída : {} \n").format(obj[i].getID(), 
                    obj[i].getNome(), obj[i].getTelefone(), obj[i].getEndereco(), obj[i].getCidade(), obj[i].getEstado(), obj[i].getNasc()))
                print("-----------------------------")
                i += 1

        elif (y == 3):
            book = xlrd.open_workbook("clientes.xls")

            sh = book.sheet_by_index(0)

            print("-----------------------------")
            print("A Planilha Foi Lida !")

        elif (y == 4):
            i = 1 
            while i < 6:
                sh.cell_value(rowx=0, colx=i)
                sh.cell_value(rowx=1, colx=i)
                sh.cell_value(rowx=2, colx=i)
                sh.cell_value(rowx=3, colx=i)
                sh.cell_value(rowx=4, colx=i)
                sh.cell_value(rowx=5, colx=i)
                sh.cell_value(rowx=6, colx=i)
                
                i += 1

        elif (y == 0):
            break

    elif(x == 0):
        break