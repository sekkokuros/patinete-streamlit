
import streamlit as st
from patinete import PatineteEletrico

st.title("🚲 Painel do Patinete Elétrico")

modelo = st.text_input("Modelo do patinete:")
autonomia = st.number_input("Autonomia (km):", min_value=0)
velocidade = st.number_input("Velocidade Máxima (km/h):", min_value=0)

if st.button("Criar Patinete"):
    patinete = PatineteEletrico(modelo, autonomia, velocidade)
    st.session_state.patinete = patinete
    st.success("Patinete criado com sucesso!")

if "patinete" in st.session_state:
    patinete = st.session_state.patinete

    st.subheader("📋 Informações do Patinete:")
    st.write(f"**Modelo:** {patinete.get_modelo()}")
    st.write(f"**Autonomia:** {patinete.get_autonomia_km()} km")
    st.write(f"**Velocidade Máxima:** {patinete.get_velocidade_max()} km/h")
    st.write(f"**Está Ligado?** {'Sim' if patinete.esta_ligado() else 'Não'}")

    if st.button("Ligar Patinete"):
        msg = patinete.ligar_patinete()
        st.info(msg)
