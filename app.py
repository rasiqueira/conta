import streamlit as st

def calcular_pagamento(pessoa, valor_da_conta):
    if pessoa.lower() == "marido":
        return f"Ok, você pode pagar. O valor é R${valor_da_conta:.2f}."
    elif pessoa.lower() == "esposa":
        return "Hoje não é o seu dia de pagar! Vamos deixar para o marido."
    else:
        return "Parece que você não é o marido. Só ele pode pagar hoje!"

# Título do aplicativo
st.title('Quem paga a conta?')

# Entradas do usuário
pessoa = st.text_input("Que integrante da família vai pagar a conta?")
valor_da_conta = st.number_input("Qual o valor da conta?", min_value=0.0, format="%.2f")

# Botão para calcular
if st.button('Calcular'):
    resultado = calcular_pagamento(pessoa, valor_da_conta)
    st.write(resultado)
    if pessoa.lower() == "marido":
        st.image("IMG_20231123_221318.jpg")
