variable "bucket_name" {
  description = "Name of the bucket"
}

variable "ip_stream_name" {
  description = ""
}

variable "op_stream_name" {
  description = ""
}

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
