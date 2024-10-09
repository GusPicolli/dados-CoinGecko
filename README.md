Projeto de ETL para a API da CoinGecko com informações do mercado de criptomoedas.
Extração das informações relacionadas as variações de preço das principais moedas na CoinGecko com uma recorrência de 3 vezes ao dia. Informações como preço de abertura e fechamento, horário de abertura e fechamento, etc. 

A ideia do projeto é monitorar os ativos e suas variações, com uma infraestrutura que explore o uso de várias ferramentas dentro do ambiente da AWS, aprofundando a aplicação do Terraform, Airflow e Docker nesse desenvolvimento.

Processo de ETL definido com 2 camadas de armazenamento e tratamento do dado com origem via API:
    Camadas RAW - WORK

Na primeira etapa, a informação extraida na origem é armazenada como um arquivo ".parquet" em um bucket s3 "RAW".

Na segunda etapa, as colunas do arquivos da RAW são convertidas de acordo com a especificação no arquivo de metadado em assets/config.preparation.json e armazenados em um bucket s3 WORK.

Versão Python utilizada: 3.11.1

Para instalar as bibliotecas necessárias do processo, usar o comando abaixo:

pip install -r requirements

Biblioteca utilizadas:

certifi==2024.7.4
charset-normalizer==3.3.2
colorama==0.4.6
idna==3.7
iniconfig==2.0.0
numpy==2.0.1
packaging==24.1
pandas==2.2.2
pluggy==1.5.0
pyarrow==17.0.0
pytest==8.3.3
python-dateutil==2.9.0.post0
pytz==2024.1
requests==2.32.3
six==1.16.0
tzdata==2024.1
urllib3==2.2.2