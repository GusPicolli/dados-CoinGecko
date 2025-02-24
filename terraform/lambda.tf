locals {
  lambda_parameters = {
    ingestao = {
      name              = "coingecko_etl_ingestao"
      variables = {
        RAW_CONFIG = "/opt/airflow/shared/S3/RAW/"   
        RAW_PATH   = "/opt/airflow/shared/S3/WORK/"
      }
      timeout           = "60"
      memory_size       = "512"
      ephemeral_storage = "512"
      command           = "app.to_work"
      vpc_config        = false
    },
    preparacao = {
      name              = "coingecko_etl_preparacao"
      variables = {
        RAW_PATH   = "/opt/airflow/shared/S3/WORK/"
        WORK_CONFIG = "/opt/airflow/dags/assets/config.preparation.json"
        WORK_PATH   = "/opt/airflow/shared/S3/WORK/"
      }
      timeout           = "60"
      memory_size       = "512"
      ephemeral_storage = "512"
      command           = "app.to_work"
      vpc_config        = false
    }
  }
}

resource "aws_lambda_function" "lambda" {
  for_each      = local.lambda_parameters
  function_name = each.value.name

  tags = {
    Name = each.value.name
  }
  role = aws_iam_role.lambda_role.arn

  image_config {
    command = [each.value.command]
  }

  environment {
    variables = each.value.variables
  }

  package_type = "Image"
  image_uri    = "${var.repository_url}:latest"

  timeout = each.value.timeout

  memory_size = each.value.memory_size

  ephemeral_storage {
    size = each.value.ephemeral_storage
  }

  vpc_config {
    subnet_ids         = each.value.vpc_config ? module.network.private_subnets : []
    security_group_ids = each.value.vpc_config ? [aws_security_group.lambda_sg.id] : []
  }

  depends_on = [null_resource.docker_ecr]
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}