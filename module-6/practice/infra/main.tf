terraform {
  backend "s3" {
    bucket = "module-6-backend"
    key    = "stage-terraform.tfstate"
    region = "us-east-1"
  }

}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

data "aws_caller_identity" "current" {}


locals {
  account_id=data.aws_caller_identity.current.account_id
}

output "model_bucket" {
  value = module.s3.name
}

output "ip_stream_arn" {
  value = module.input_stream.stream_arn
}


output "op_stream_arn" {
  value = module.op_stream.stream_arn
}



module "s3"{
    source = "./modules/s3"
    bucket_name = var.bucket_name
}

module "input_stream"{
    source = "./modules/kinesis"
    stream_name             = var.ip_stream_name
    shard_count      = 1
    retention_period = 48
}

module "op_stream"{
    source = "./modules/kinesis"
    stream_name             = var.op_stream_name
    shard_count      = 1
    retention_period = 48
}


module "ecr"{
    source = "./modules/ecr"
    ecr_repo_name=var.ecr_repo_name 
    account_id = local.account_id
    lambda_function_local_path = var.lambda_function_local_path
    docker_image_local_path = var.docker_image_local_path
}