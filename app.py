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
    # QUESTÃO 1 — Linha de Taquaril
    # Pedido: mostrar como o IQVU de Taquaril mudou de 1994 a 2016, com um
    # marcador em cada ano disponível, linha coral e anos como categorias.
    # O que já temos? df_tabela contém os DOIS bairros. Ler o filtro de dentro
    # para fora ajuda: primeiro perguntamos “esta linha é de Taquaril?”;
    # depois df_tabela[...] seleciona as linhas com resposta verdadeira.
    df_taquaril = df[df["NOMEUP"] == "Taquaril"]
    fig_taquaril = px.line(
        df_taquaril,
        x="ANO",       # A posição horizontal indica quando o índice foi medido.
        y="IQVU",      # A altura do ponto indica quanto o índice valia.
        markers=True,  # Desenha uma bolinha em cada medição.
        title="1. Evolução do IQVU de Taquaril",
    )
    # update_traces altera a linha e seus pontos depois de criar a figura.
    fig_taquaril.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    # category dá uma posição a cada ano presente, sem criar marcas intermediárias.
    fig_taquaril.update_xaxes(type="category")
    st.plotly_chart(fig_taquaril)
    # Confira: 7 pontos; o primeiro vale 0.412 e o último vale 0.568.