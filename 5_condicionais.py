salario = float(input("Informe seu Ultimo Salário: "))

if salario <= 3000:
    print("Programador Júnior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador Senior")
else:
    print("Gerente de Projetos")
