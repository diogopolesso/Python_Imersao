for #Loop que percorre sequencias, repetindo ações para cada elemento.

while #Loop que executa ações enquanto a condição for verdadeira.

# Exemplo 1 = Loop que se repita 5 vezes:

for x in range(5):
  print(x)

# o X é uma variavel temporaria, enquanto range é uma função que cria uma sequencia de numeros range(5)=[0, 1, 2, 3, 4]

# Exemplo 2 = Definir a nota de uma prova para 100 alunos:

notas  = []

for x in range(100):
    codigo_aluno = input("UR: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    print( "Quantidade de notas", len(notas))

    for n in notas:
        codigo_aluno = n[0]
        nota = n[1]
        print("O UR ", codigo_aluno, "Tirou a nota: ", nota)

# Exemplo 3 = Definir a nota de uma prova para 100 alunos usando "while":

notas = []

contador = 1 # para o nosso while executar o bloco de repetição enquanto a variavel não atigir o numero 5

while contador <= 5:
    codigo_aluno = input("UR: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador = contador + 1 # alternativa: contador += 1

    print("Quantidade de notas", len(notas))
  
