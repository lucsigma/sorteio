
import streamlit as st
import random
import time

# Configuração inicial da página
st.set_page_config(page_title="Sorteio de Nomes", layout="centered")

# Título do app
st.title("🎉 Sorteio ")

# Entrada de nomes
st.subheader("cadstre os Nomes")
nomes_input = st.text_area("Digite os nomes separados por vírgula:", placeholder="Exemplo: Ana, João, Pedro, Maria")

# Botão para iniciar o sorteio
if st.button("Sortear"):
    if nomes_input.strip():
        nomes = [nome.strip() for nome in nomes_input.split(",")]

        # Temporizador visual
        st.subheader(" sorteio iniciado...")
        countdown_placeholder = st.empty()  # Placeholder para o temporizador
        for i in range(10, 0, -1):  # Contagem regressiva de 3 a 1
            countdown_placeholder.write(f"⏳ Sorteando em {i} segundos...")
            time.sleep(1)

        # Limpa o temporizador
        countdown_placeholder.empty()

        # Sorteio
        nome_sorteado = random.choice(nomes)
        st.success(f"O ganhador(a) é: *{nome_sorteado}* 🎉")
        st.balloons()
    else:
        st.error("Por favor, insira pelo menos um nome para realizar o sorteio.")

# Rodapé
st.markdown("---")
st.caption("participe ❤ e ganhe você tambem!")