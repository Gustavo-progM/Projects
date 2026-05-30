#APRESENTAÇÃO
nome = str(input("Eae,qual seu nome? ")).capitalize()

#DIA DO NASCIMENTO
dia = int(input(f"Oi {nome} que dia vc nasceu? "))
while dia < 0 or dia > 31:
    print("Ei " + nome + " um mês tem mais de 1 dia e menos de 31, digite o dia correto por favor")
    dia = int(input())

#ESCOLHA DO MÊS
mes = int(input("Em que mês? "))
while mes < 0 or mes > 12:
    print("Ei " + nome + " Um ano tem 12 meses, digite um mês legivel por favor")
    mes = int(input())

#ESCOLHA DO ANO
ano = int(input("Ano? "))


print("Desculpa a pergunta, mas que dia é hj?")

diahj = int(input())

while diahj < 0 or diahj > 31:

    print("Um mês tem mais de 1 dia e menos de 31, digite o dia correto por favor")

    diahj = int(input())

print("E o més?")

meshj = int(input())

while meshj < 0 or meshj > 12:

    print("Ei " + nome + " Um ano tem 12 meses, digite um mês legivel por favor")

    meshj = int(input())

print("E por gentileza o ano? :)")

anoagr = int(input())

while ano > anoagr:

    print("Vc nasceu em " + str(ano) + " ta de brincadeira, digite de novo por favor")
    ano = int(input())


idade = anoagr - ano

if meshj < mes:

    idadeco = idade - 1

    print("Vc tem =" + str(idadeco))

    idadeco1 = idade + 0

    print("Vai fazer= " + str(idadeco1))

if meshj > mes:

    idadeco = idade - 0

    print("Vc tem=" + str(idadeco))

if ano == anoagr:

    idadeco = idade - 0

    print("ignora a idade de cima ;)")

    print("Vc tem=" + str(idadeco))

if meshj == mes:

    if diahj > dia:

        idadeco = idade - 0

        print("Voçe tem: " + str(idadeco))

    if diahj < dia:

        idadeco = idade - 1

        print("Voçe tem: " + str(idadeco))

    if dia == diahj:

        idadeco = idade - 0
        
        print("Voçe tem ou vai fazer: " + str(idadeco))
