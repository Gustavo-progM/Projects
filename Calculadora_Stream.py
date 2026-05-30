import streamlit as st
st.markdown("<h1 style='text-align: center;'>Calculadora</h1>", unsafe_allow_html=True)

def inserir_numero_raiz_quadrada():
    global num1

    num1 = st.number_input("Digite o número:", value=1)

def inserir_numeros_divisao():
    global num1, num2

    num1 = st.number_input("Digite o primeiro número:", value=0)
    num2 = st.number_input("Digite o segundo número:", value=1)
    st.caption("Pressione enter para confirmar")
    while num2 == 0:
        st.warning("Divisão por zero não é permitida.")
        num2 = st.number_input("Digite o segundo número:", value=1)
    return num1, num2

def Inserir_numeros_porcentagem():
    global num1, porcentagem

    num1 = st.number_input("Digite o Número sem desconto:", value=1)
    porcentagem = st.number_input("Digite a porcentagem:", value=1)

    while porcentagem > 100:
        st.warning("A porcentagem não pode ser maior que 100%")
        porcentagem = st.number_input("Digite a porcentagem:", value=1)
    while porcentagem < 0:
        st.warning("A porcentagem não pode ser menor que 0%")
        porcentagem = st.number_input("Digite a porcentagem:", value=1)
    return num1, porcentagem

def inserir_numeros():
    global num1, num2

    num1 = st.number_input("Digite o primeiro número:", value=1)
    num2 = st.number_input("Digite o segundo número:", value=1)
#Escolher Operação
def escolha_da_operacao():

    operacao = st.selectbox("Escolha a operação:", ("Soma", "Subtração", "Multiplicação", "Divisão", "Porcentagem", "Raiz Quadrada"))
    
    match operacao:
        case "Soma":inserir_numeros(),calcular_soma()
        case "Subtração":inserir_numeros(),calcular_subtracao()
        case "Multiplicação":inserir_numeros(),calcular_multiplicacao()
        case "Divisão":inserir_numeros_divisao(),calcular_divisao()
        case "Porcentagem":Inserir_numeros_porcentagem(),calcular_porcentagem()
        case "Raiz Quadrada":inserir_numero_raiz_quadrada(),calcular_raiz_quadrada()
    return operacao

#Funções de Cálculos
def calcular_porcentagem():
    calculo = st.button("Calcular")
    if (calculo == True):
        resultado = (num1 * porcentagem) / 100
        st.write(f"O resultado de {num1} por {porcentagem}% é: {resultado}")

def calcular_subtracao():
    calculo = st.button("Calcular")
    if (calculo == True):
        resultado = num1 - num2
        st.write(f"O resultado de {num1} - {num2} é: {resultado}")

def calcular_multiplicacao():
    calculo = st.button("Calcular")
    if (calculo == True):
        resultado = num1 * num2
        st.write(f"O resultado de {num1} * {num2} é: {resultado}")

def calcular_divisao():
    calculo = st.button("Calcular")
    if (calculo == True):
        resultado = num1 / num2
        st.write(f"O resultado de {num1} / {num2} é: {resultado}")

def calcular_soma():
    calculo = st.button("Calcular")
    if (calculo == True):
        resultado = num1 + num2
        st.write(f"O resultado de {num1} + {num2} é: {resultado}")

def calcular_raiz_quadrada():
    calculo = st.button("Calcular")
    if (calculo == True):
        resultado = num1 ** (1/2)
        st.write(f"A raiz quadrada de {num1} é: {resultado}")

# Chama a função para escolher a operação
escolha_da_operacao()