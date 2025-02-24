resource "aws_ecr_repository" "repository_pipeline" {
  name = var.repository_name

  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}

resource "null_resource" "docker_ecr" {
  triggers = {
    ecr_repository_name = var.repository_name
  }

  provisioner "local-exec" {
    command = <<EOF
      docker build -t ${var.repository_name}:latest -f ../docker/Dockerfile ../
    EOF
  }

  provisioner "local-exec" {
    command = <<EOF
      docker tag ${var.repository_name}:latest ${aws_ecr_repository.repository_pipeline.repository_url}:latest
    EOF
  }

  provisioner "local-exec" {
    command = <<EOF
      docker push ${aws_ecr_repository.repository_pipeline.repository_url}:latest
    EOF
  }

  depends_on = [aws_ecr_repository.repository_pipeline]
}
output "repository_url" {
  description = "The URL of the ECR repository."
  value       = aws_ecr_repository.repository_pipeline.repository_url
}