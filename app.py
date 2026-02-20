import streamlit as st

st.set_page_config(page_title="Cent48", page_icon="🪙")

st.title("🪙 Cent48")
st.subheader("Win geld met je skills!")

# Gebruiker inloggen
naam = st.text_input("Wat is je naam?")
if naam:
    st.write(f"Welkom bij Cent48, {naam}!")
    st.info("Jouw huidige saldo: 0 credits (Stort 48 cent bij Levko!)")

# De games
st.write("### Kies je game:")
col1, col2 = st.columns(2)

with col1:
    if st.button("⚡ Reactie Duel (Fee: €0,10)"):
        st.warning("Wacht op een tegenstander...")

with col2:
    if st.button("🔴 Vier op een rij (Fee: €0,25)"):
        st.warning("Bord wordt klaargezet...")

st.sidebar.write("### Beheer")
st.sidebar.button("Stort geld via Rabo Tikkie")
