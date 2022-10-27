#terraform version and backend
terraform {
  backend "s3"{}
}

variable "aws_access_key" {}

variable "aws_secret_key" {}

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region = "us-east-1"
  
}

# data "aws_availability_zones" "azs" {}

# module "vpc" {
#   source = "terraform-aws-modules/vpc/aws"

#   name = var.vpc_name
#   cidr = var.vpc_cidr

#   azs             = var.vpc_azs
#   private_subnets = var.vpc_private_subnets
#   public_subnets  = var.vpc_public_subnets

#   enable_nat_gateway = var.vpc_enable_nat_gateway
#   single_nat_gateway  = var.vpc_enable_nat_gateway

#   tags = var.vpc_tags
# }

# module "web_server_sg" {
#   source              = "terraform-aws-modules/security-group/aws"
#   name                = "web-server"
#   description         = "Security group for web-server"
#   vpc_id              = module.vpc.vpc_id
#   ingress_cidr_blocks = ["0.0.0.0/0"]
#   ingress_rules       = ["http-80-tcp"]
# }


resource "aws_instance" "web_server01" {
  ami = "ami-08c40ec9ead489470"
  instance_type = "t2.micro"
  key_name = "ubuntu_ec2"
  vpc_security_group_ids = [aws_security_group.web_ssh.id]

  user_data = "${file("deploy.sh")}"

  tags = {
    "Name" : "Webserver001"
  }
  
}

output "instance_ip" {
#   value = module.ec2_instances
    value = aws_instance.web_server01.public_ip
  
}
