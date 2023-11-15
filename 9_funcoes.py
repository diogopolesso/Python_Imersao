# Funções são Blocos reutilizaveis de codigo que utilizam tarefas especificas

# codigo sem função #

fluxo_caixa = []
print("---------")
print("@ Fluxo caixa")
printt
"---------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para acessar #\n")

while True:

    opcao = int( input("Digite a opção: ") )

    if opcao == 1:
        nome = input("nome: ")
        valor = float(input("Valor: "))
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
    elif opcao == 2:
        nome = input("nome: ")
        valor = float(input("Valor: "))
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
    else:
        break

# Nota Fiscal

total = 0
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", Valor: R$", fc['valar'])
    total = total + fc['valor']

    print("Saldo atual: R$", total)



______________________________________________________________________________




# codigo com função #

fluxo_caixa = []
print("---------")
print("@ Fluxo caixa")
print("---------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para acessar #\n")

def adicionar_transacao()
    nome = input("nome: ")
    valor = float(input("Valor: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })
while True:

    opcao = int( input("Digite a opção: ") )

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

# Nota Fiscal

total = 0
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", Valor: R$", fc['valar'])
    total = total + fc['valor']

    print("Saldo atual: R$", total)
    
