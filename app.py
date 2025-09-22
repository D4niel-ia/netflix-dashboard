import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# -----------------------
# Carregar dados
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
    return df

df = load_data()

# -----------------------
# Título
# -----------------------
st.title("🎬 Netflix Dashboard")
st.markdown("Análise interativa do catálogo da Netflix")

# -----------------------
# KPIs
# -----------------------
col1, col2 = st.columns(2)
with col1:
    st.metric("Total de Títulos", df.shape[0])
with col2:
    st.metric("Total de Países", df["country"].nunique())

# -----------------------
# Filtros
# -----------------------
st.sidebar.header("Filtros")
tipo = st.sidebar.multiselect("Tipo", df["type"].unique(), default=df["type"].unique())
ano = st.sidebar.slider("Ano de lançamento", int(df["release_year"].min()), int(df["release_year"].max()), (2000, 2020))

df_filtered = df[(df["type"].isin(tipo)) & (df["release_year"].between(ano[0], ano[1]))]

st.write(f"Mostrando {df_filtered.shape[0]} títulos filtrados")

# -----------------------
# Gráfico 1 - Filmes por Ano
# -----------------------
st.subheader("📅 Quantidade de títulos por ano de lançamento")
fig1 = px.histogram(df_filtered, x="release_year", color="type", nbins=30)
st.plotly_chart(fig1, use_container_width=True)

# -----------------------
# Gráfico 2 - Conteúdo por Gênero
# -----------------------
st.subheader("🎭 Distribuição por Gênero")
df_genres = df_filtered.assign(genre=df_filtered["listed_in"].str.split(",")).explode("genre")
df_genres["genre"] = df_genres["genre"].str.strip()
genre_counts = df_genres["genre"].value_counts().head(10)

fig2 = px.pie(values=genre_counts.values, names=genre_counts.index)
st.plotly_chart(fig2, use_container_width=True)

# -----------------------
# Gráfico 3 - Top Países
# -----------------------
st.subheader("🌍 Top 10 Países com mais títulos")
country_counts = df_filtered["country"].value_counts().head(10)
fig3 = px.bar(x=country_counts.index, y=country_counts.values, labels={"x":"País","y":"Quantidade"})
st.plotly_chart(fig3, use_container_width=True)