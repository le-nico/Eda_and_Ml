import pandas as pd
import seaborn as sns
import streamlit as st
import io  # <- Import necessario per catturare l’output

# streamlit run app.py

# PER VEDERE LA APP IN RETE
# streamlit run app.py --server.address=0.0.0.0
# http://<TUO-IP-LOCALE>:8501

# 👤 Lista di utenti e password (in chiaro)
# USER_CREDENTIALS = {
#     "alice": "1234",
#     "bob": "abcd"
# }

# Sidebar login
# st.sidebar.title("🔐 Login")
# username = st.sidebar.text_input("Username")
# password = st.sidebar.text_input("Password", type="password")

# if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
#     st.success(f"Benvenuto, {username}!")
#     # Metti qui la tua app
#     st.set_page_config(page_title="Titanic", layout="wide")
#     st.title("💳 EDA TITANIC")
# else:
#     st.warning("Inserisci credenziali valide per continuare")
#     st.stop()  # Blocca l'esecuzione dell'app finché non si fa login

# SE NON SI USA IL LOG IN
st.set_page_config(page_title="Titanic", layout="wide")
st.title("💳 EDA TITANIC")

titanic = sns.load_dataset("titanic")
# La funzione sns.load_dataset() restituisce direttamente un pandas.DataFrame.

# Cattura output di .info()
buffer = io.StringIO()
titanic.info(buf=buffer)
info_str = buffer.getvalue()

# Visualizza in Streamlit
st.subheader("📋 Info")
# st.text(info_str)
st.code(info_str, language="text") 

st.subheader("📋 Head")
st.dataframe(titanic.head())