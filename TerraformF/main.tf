
# Naming TF File - Component-environemtn-region-anything_else.tf 
# Example: networking-dev-usa.tf

# Variables at the top and then the providers block


# variable "instance_type" {
#     type =  string
#     default = ""
# }

# resource "aws_instance" "webserver" {
#     ami = "ami-abc123"
#     type = "instance_type"
# }

variable "aws_access_key" {

}

variable "aws_secret_key" {
  
}

provider "aws" {
    access_key = var.aws_access_key
    secret_key = var.aws_secret_key   
    region = "us-east-1"
}

resource "aws_s3_bucket" "first_bucket" {
  bucket = "mykurabucket2022"

}

resource "aws_s3_bucket_acl" "bucket_acl01" {
  bucket = aws_s3_bucket.first_bucket.id
  acl    = "private"

}