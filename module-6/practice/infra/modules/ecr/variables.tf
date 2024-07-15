variable "ecr_repo_name" {
  description = "Name of the repo"
}

variable "lambda_function_local_path" {
    type        = string
    description = "Local path to lambda function / python file"
}

variable "docker_image_local_path" {
    type        = string
    description = "Local path to Dockerfile"
}

variable "region" {
    type        = string
    description = "region"
    default = "us-east-1"
}

variable "account_id" {
}


variable "ecr_image_tag" {
    type        = string
    description = "ECR repo name"
    default = "latest"
}