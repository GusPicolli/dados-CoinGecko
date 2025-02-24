variable "aws_region" {
  description = "The AWS region to create resources in."
  type        = string
  default     = "us-east-1"
}

variable "repository_name" {
  description = "The name of the ECR repository."
  type        = string
  default     = "coingecko-etl"
}

variable "function_name" {
  description = "The name of the Lambda function."
  type        = string
}

variable "repository_url" {
  description = "The URL of the ECR repository."
  type        = string
}

variable "variables" {
  description = "Environment variables for the Lambda function."
  type        = map(string)
}