# Projeto de ETL: Monitoramento de Criptomoedas com a API da CoinGecko

**Objetivo:**  
Desenvolver um processo ETL para extrair, transformar e carregar informações sobre as variações de preço das principais criptomoedas.

## Detalhes do Projeto

- **Frequência de Extração:** 3 vezes ao dia.
- **Dados Extraídos:** Preços de abertura e fechamento, horários correspondentes, entre outros.

## Infraestrutura

Utilização de ferramentas da AWS com foco em Terraform, Airflow e Docker.

## Processo ETL

1. **Camada RAW:**
   - Os dados extraídos são armazenados como arquivos `.parquet` em um bucket S3 denominado `RAW`.

2. **Camada WORK:**
   - As colunas dos arquivos RAW são transformadas conforme especificações em `assets/config.preparation.json` e armazenadas em um bucket S3 denominado `WORK`.

## Tecnologia

- **Versão do Python:** 3.9.20

## Instalação de Dependências

Para instalar as bibliotecas necessárias, utilize o seguinte comando:

```bash
pip install -r requirements.txt

## Bibliotecas Utilizadas

As seguintes bibliotecas são necessárias para o funcionamento do projeto:

certifi==2022.12.7
charset-normalizer==2.0.12 
idna==3.3
numpy==1.21.6
pandas==1.3.5
pyarrow==8.0.0
python-dateutil==2.8.2
pytz==2021.3
requests==2.27.1
six==1.16.0
tzdata==2021.5
urllib3==1.26.12
mysql-connector-python==8.0.28
SQLAlchemy==1.3.24
