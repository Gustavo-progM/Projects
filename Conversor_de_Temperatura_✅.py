print("---------------------------->Conversor de Temperatura<---------------------------------")

# ESCOLHA DO VALOR Á SER CONVERTIDO
temperatura = float(input("Qual valor você quer converter? "))

# ESCOLHA DAS UNIDADES DE TEMPERATURA PARA CONVERSÃO
escolha = str(input("Você gostaria de converter Celsius para Fahrenheint digite CF ou de Fahrenheint para Celsius escreva FC: ")).upper()
while escolha != "CF" and escolha != "FC":
    print("Resposta inválida, escreva CF ou FC")
    escolha = input().upper()

# SISTEMAS DE SOMA DAS TEMPERATURAS - Celsius para Fahrenheit: F = (C * 9/5) + 32
if escolha == "CF":
    escolha = "celsius para fahrenheint"
    tempc = temperatura * 9 / 5 + 32
    print("Sua temperatura é =" + str(tempc) + "°F")

# SISTEMAS DE SOMA DAS TEMPERATURAS - Fahrenheit para Celsius: C = (F - 32) * 5/9
if escolha == "FC":
    escolha = "farehneint pra celsius"
    tempf = temperatura - 32 * 5 / 9
    print("Sua temperatura é =" + str(tempf) + "°C")

# LOOPING DE REPETIÇÃO   
quero = str(input("Gostaria de fazer um novo cálculo?(s/n): ")).lower()
while quero != "s" and quero != "n":
    print("resposta inválida, digite S(sim) ou N(não)")
    quero = input().lower()
if quero == "s":
    while quero == "s":
        temperatura = float(input("Quanto?"))
        escolha = str(input("Você gostaria de converter Celsius para Fahrenheint digite CF ou de Fahrenheint para Celsius digite FC: ")).upper()
        while escolha != "CF" and escolha != "FC":
            print("Resposta inválida, digite CF ou FC")
            escolha = input().upper()
        if escolha == "CF":
            escolha = "celsius para fahrenheint"
            tempc = temperatura * 9 / 5 + 32
            print("Sua temperatura é =" + str(tempc) + "°F")
        if escolha == "FC":
            escolha = "farehneint pra celsius"
            tempf = temperatura - 32 * 5 / 9
            print("Sua temperatura é =" + str(tempf) + "°C")
        quero = str(input("Gostaria de fazer um novo cálculo? ")).lower()
if quero == "n":
    print("Ok")