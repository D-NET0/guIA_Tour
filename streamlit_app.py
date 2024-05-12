import streamlit as st
import guia_tour  # Importe o módulo do seu projeto guIAtour

# Configurar a página
st.set_page_config(page_title="guIAtour", page_icon="✈️")

# Coletar informações do usuário
st.title("guIAtour: Planeje sua Viagem dos Sonhos! 🗺️")

destino = st.text_input("Para onde você quer viajar?")
duracao = st.number_input("Quantos dias de viagem?", min_value=1, step=1)
companhia = st.text_input("Quem vai viajar com você?")
hospedagem = st.selectbox("Tipo de Hospedagem", ["Hotel", "Hostel", "Airbnb", "Pousada"])
orcamento = st.slider("Orçamento (em R$)", min_value=500, max_value=10000, step=500)
atividades = st.multiselect("Atividades Desejadas", ["Museus", "Parques", "Gastronomia", "Compras", "Vida Noturna"])
essenciais = st.text_area("O que não pode faltar na sua viagem?")

# Gerar roteiro ao clicar no botão
if st.button("Criar Roteiro"):
  roteiro = guia_tour.gerar_roteiro(
      destino, duracao, companhia, hospedagem, orcamento, atividades, essenciais
  )  # Chame a função do guIAtour
  st.write(roteiro)
