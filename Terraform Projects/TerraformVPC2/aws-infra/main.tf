# PROVIDER
provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region = "us-east-1"
 
}

module "createVpc" {
    source ="./modules/vpc"
}


module "createSG" {
    source ="./modules/sg"


}


module "createInstance" {
    source ="./modules/ec2"
    module.aws_subnet.

}
