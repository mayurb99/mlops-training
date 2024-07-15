resource "aws_ecr_repository" "repo" {
  name                 = var.ecr_repo_name
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }

  force_delete = true
}

#resource "null_resource" "ecr_image" {
#  triggers = {
#    python_file = md5(file(var.lambda_function_local_path))
#    docker_file = md5(file(var.docker_image_local_path))
#  }
#
#  provisioner "local-exec" {
#    command = <<-EOF
#        ls -a
#        cd ../
#      
#    EOF
#  }
#}

// Wait for the image to be uploaded, before lambda config runs
data aws_ecr_image lambda_image {
 depends_on = [
   aws_ecr_repository.repo
 ]
 repository_name = var.ecr_repo_name
 image_tag       = var.ecr_image_tag
}

output "image_uri" {
  value     = "${aws_ecr_repository.repo.repository_url}:${data.aws_ecr_image.lambda_image.image_tag}"
}