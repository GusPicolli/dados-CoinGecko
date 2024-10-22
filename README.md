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

- **Versão do Python:** 3.11.1

## Instalação de Dependências

Para instalar as bibliotecas necessárias, utilize o seguinte comando:

```bash
pip install -r requirements.txt

## Bibliotecas Utilizadas

As seguintes bibliotecas são necessárias para o funcionamento do projeto:

- `certifi==2024.7.4`
- `charset-normalizer==3.3.2`
- `colorama==0.4.6`
- `idna==3.7`
- `iniconfig==2.0.0`
- `numpy==2.0.1`
- `packaging==24.1`
- `pandas==2.2.2`
- `pluggy==1.5.0`
- `pyarrow==17.0.0`
- `pytest==8.3.3`
- `python-dateutil==2.9.0.post0`
- `pytz==2024.1`
- `requests==2.32.3`
- `six==1.16.0`
- `tzdata==2024.1`
- `urllib3==2.2.2`
