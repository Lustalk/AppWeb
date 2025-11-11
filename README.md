# 🚗 Vehicle Ads Dashboard

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

*A beautiful and interactive dashboard for analyzing used vehicle advertisements*

[English](#english) | [Português](#português)

LIVE PROJECT : https://appweb-2y4x.onrender.com
</div>

---

## English

### 📋 Overview

An interactive Streamlit dashboard designed to explore and analyze used vehicle advertisements from the `vehicles.csv` dataset. This tool provides comprehensive visualizations and insights into vehicle pricing, conditions, manufacturers, and market trends.

### ✨ Features

#### 📊 Interactive Data Viewer
- Explore the complete dataset with a dynamic, searchable table
- Filter option to include/exclude manufacturers with less than 1000 ads
- Real-time data updates and sorting capabilities

#### 📈 Visualizations

1. **Vehicle Types by Manufacturer**
   - Stacked bar chart displaying distribution of vehicle types (SUV, sedan, pickup, etc.)
   - Compare offerings across different manufacturers

2. **Condition vs Model Year Analysis**
   - Grouped bar chart showing vehicle conditions (excellent, good, fair, etc.)
   - Track condition trends across model years

3. **Price Distribution Comparison**
   - Side-by-side histogram and box plot comparison
   - Select and compare two manufacturers simultaneously
   - Identify pricing patterns and outliers

4. **Additional Insights**
   - Odometer reading distribution histogram
   - Price vs Odometer scatter plot analysis
   - Correlation between mileage and pricing

### 📦 Dataset Structure

The dashboard analyzes the `vehicles.csv` file containing the following fields:

| Column | Description |
|--------|-------------|
| `price` | Vehicle listing price |
| `model_year` | Year of manufacture |
| `model` | Vehicle model name |
| `condition` | Vehicle condition rating |
| `cylinders` | Engine cylinder count |
| `fuel` | Fuel type |
| `odometer` | Mileage reading |
| `transmission` | Transmission type |
| `type` | Vehicle type (SUV, sedan, etc.) |
| `paint_color` | Exterior color |
| `is_4wd` | Four-wheel drive indicator |
| `date_posted` | Advertisement posting date |
| `days_listed` | Duration of listing |

> **Note**: Manufacturer information is extracted from the first word of the `model` column.

### 🚀 Installation

#### Prerequisites
- Python 3.1 or higher
- pip package manager

#### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd vehicle-ads-dashboard
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install pandas plotly streamlit
```

3. Ensure `vehicles.csv` is in the project directory

### 💻 Usage

Run the dashboard:
```bash
streamlit run app.py
```

The application will open automatically in your default web browser at `http://localhost:8501`

### 📁 Project Structure

```
vehicle-ads-dashboard/
│
├── app.py                 # Main Streamlit application
├── vehicles.csv           # Dataset file
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── LEIAME.md             # Portuguese documentation

---

## Português

### 📋 Visão Geral

Um dashboard interativo desenvolvido em Streamlit para explorar e analisar anúncios de veículos usados a partir do conjunto de dados `vehicles.csv`. Esta ferramenta oferece visualizações abrangentes e insights sobre preços, condições, fabricantes e tendências de mercado.

### ✨ Funcionalidades

#### 📊 Visualizador de Dados Interativo
- Explore o conjunto completo de dados com tabela dinâmica e pesquisável
- Opção de filtro para incluir/excluir fabricantes com menos de 1000 anúncios
- Atualizações de dados em tempo real e recursos de ordenação

#### 📈 Visualizações

1. **Tipos de Veículos por Fabricante**
   - Gráfico de barras empilhadas exibindo distribuição de tipos de veículos (SUV, sedã, picape, etc.)
   - Compare ofertas entre diferentes fabricantes

2. **Análise Condição vs Ano do Modelo**
   - Gráfico de barras agrupadas mostrando condições dos veículos (excelente, bom, razoável, etc.)
   - Acompanhe tendências de condição ao longo dos anos

3. **Comparação de Distribuição de Preços**
   - Histograma e box plot lado a lado
   - Selecione e compare dois fabricantes simultaneamente
   - Identifique padrões de preços e valores atípicos

4. **Insights Adicionais**
   - Histograma de distribuição do hodômetro
   - Gráfico de dispersão Preço vs Hodômetro
   - Correlação entre quilometragem e preços

### 📦 Estrutura do Conjunto de Dados

O dashboard analisa o arquivo `vehicles.csv` contendo os seguintes campos:

| Coluna | Descrição |
|--------|-----------|
| `price` | Preço do anúncio do veículo |
| `model_year` | Ano de fabricação |
| `model` | Nome do modelo do veículo |
| `condition` | Classificação da condição do veículo |
| `cylinders` | Número de cilindros do motor |
| `fuel` | Tipo de combustível |
| `odometer` | Leitura da quilometragem |
| `transmission` | Tipo de transmissão |
| `type` | Tipo de veículo (SUV, sedã, etc.) |
| `paint_color` | Cor exterior |
| `is_4wd` | Indicador de tração nas quatro rodas |
| `date_posted` | Data de publicação do anúncio |
| `days_listed` | Duração do anúncio |

> **Observação**: A informação do fabricante é extraída da primeira palavra da coluna `model`.

### 🚀 Instalação

#### Pré-requisitos
- Python 3.1 ou superior
- Gerenciador de pacotes pip

#### Configuração

1. Clone o repositório:
```bash
git clone <url-do-repositório>
cd vehicle-ads-dashboard
```

2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

Ou instale os pacotes individualmente:
```bash
pip install pandas plotly streamlit
```

3. Certifique-se de que `vehicles.csv` está no diretório do projeto

### 💻 Uso

Execute o dashboard:
```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no seu navegador padrão em `http://localhost:8501`

### 📁 Estrutura do Projeto

```
vehicle-ads-dashboard/
│
├── app.py                 # Aplicação principal Streamlit
├── vehicles.csv           # Arquivo do conjunto de dados
├── requirements.txt       # Dependências Python
├── README.md             # Documentação em inglês
└── LEIAME.md             # Este arquivo
