# Definir o provedor AWS
provider "aws" {
  region = "us-east-1" # Escolha sua região
}

# Criar um bucket S3 para armazenar os dados do ETL
resource "aws_s3_bucket" "dados_coingecko" {
  bucket = "coingecko-bucket"

  tags = {
    Name        = "ETL CoinGecko"
    Environment = "dev"
  }
}

resource "aws_instance" "etl_server" {
  ami           = "ami"  # Ubuntu 22.04 LTS
  instance_type = "t2.nano"  # Instância gratuita para testes
  #key_name      = "minha-chave-aws"  # Nome da sua chave SSH
  #security_groups = ["meu-grupo-seguranca"]

  tags = {
    Name = "ETL-Airflow-Test"
  }
}
