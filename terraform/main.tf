provider "aws" {
  region = var.aws_region
}

## Inclui o repositório ECR
#module "ecr" {
#  source = "./"
#  repository_name = "repositorio-coingecko"
#}

# Inclui as funções Lambda de ingestão
module "lambda_ingestao" {
  source = "./"
  repository_url = module.ecr.repository_url
  function_name = "coingecko_etl_ingestao"
  variables = {
    RAW_CONFIG = "/opt/airflow/shared/S3/RAW/"
    RAW_PATH = "/opt/airflow/shared/S3/WORK/"
  }
}

# Inclui as funções Lambda de preparação
module "lambda_preparacao" {
  source = "./"
  repository_url = module.ecr.repository_url
  function_name = "coingecko_etl_preparacao"
  variables = {
    RAW_PATH = "/opt/airflow/shared/S3/WORK/"
    WORK_CONFIG = "/opt/airflow/dags/assets/config.preparation.json"
    WORK_PATH = "/opt/airflow/shared/S3/WORK/"
  }
}