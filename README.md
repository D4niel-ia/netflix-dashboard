# 📊 Netflix Dashboard com Streamlit

Este projeto é um **Dashboard Interativo** construído com [Streamlit](https://streamlit.io/) para explorar o dataset público **Netflix Movies and TV Shows** (Kaggle).  
Ele permite visualizar estatísticas sobre títulos disponíveis, como **quantidade de filmes e séries, países com mais produções e gêneros mais populares**.

---

## 🚀 Funcionalidades

- Exibição de **KPIs principais** (total de títulos, filmes, séries).  
- **Filtros dinâmicos** por ano, país e tipo de conteúdo.  
- **Gráficos interativos**:
  - Filmes por ano (Bar Chart).
  - Distribuição por gênero (Pie Chart).
  - Top 10 países com mais títulos.

---

## 🛠️ Instalação e Execução

### 1. Clone este repositório
```bash
git clone https://github.com/seu-usuario/netflix-dashboard.git
cd netflix-dashboard
```

### 2. Crie e ative o ambiente virtual (opcional, mas recomendado)
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

### 3. Instale as dependências
pip install -r requirements.txt

** Se não tiver o arquivo requirements.txt, instale manualmente:
pip install pandas matplotlib streamlit

### 4. Execute o dashboard
streamlit run app.py

📂 Estrutura do Projeto
netflix-dashboard/
│── data/
│   └── netflix_titles.csv
│── app.py
│── requirements.txt
│── README.md

🌐 Deploy

O projeto está disponível no Streamlit Cloud:
👉 Acessar Dashboard Online

📸 Prints do Dashboard
    - Tela Inicial
    - Filtro por Ano
    - Top Países

📊 Dataset
O dataset usado está disponível no Kaggle:
👉 Netflix Movies and TV Shows

    👨‍💻 Autor

Projeto desenvolvido para prática de Python, Pandas e Streamlit.
