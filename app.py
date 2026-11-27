import pandas as pd          # Manipula tabelas. O apelido pd encurta os comandos.
import plotly.express as px  # Desenha os gráficos pedidos no simulado.
import streamlit as st 

df = pd.read_csv("dados_transporte_bh.csv", sep = ";")

st.set_page_config(page_title="Transporte BH", layout="wide")

st.title("Dados Transportes")

st.header("Graficos / Tabelas:")


df[" TOTAL USUARIOS"] = df[" TOTAL USUARIOS"].astype(int)




opcao = st.sidebar.radio("Escolha o que ver", ["Tabela", "Gráficos"])
# A opção selecionada fica em opcao. Os espaços no começo das linhas indicam
# quais comandos pertencem a cada escolha. Toda vez que a escolha muda, o app roda de novo.
if opcao == "Tabela":
    st.dataframe(df, hide_index=True)
else:
    st.write("foi mal fessoara eu n estudei dessa vez kkkk")