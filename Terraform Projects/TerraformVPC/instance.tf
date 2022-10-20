# VARIABLES
variable "aws_access_key" {}
variable "aws_secret_key" {}

# PROVIDER
provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region = "us-east-1"
 
}

# INSTANCES
resource "aws_instance" "web_server01" {
  ami                    = "ami-08c40ec9ead489470"
  instance_type          = "t2.micro"
  subnet_id              = "${aws_subnet.subnet1.id}"
  vpc_security_group_ids = ["${aws_security_group.web_ssh.id}"]

  key_name = "ubuntu_ec2"

  tags = {
    "Name" : "web_server001"
  }
 
}

resource "aws_instance" "web_server02" {
  ami                    = "ami-08c40ec9ead489470"
  instance_type          = "t2.micro"
  subnet_id              = "${aws_subnet.pri_subnet1.id}"
  vpc_security_group_ids = ["${aws_security_group.web_ssh.id}"]

  key_name = "ubuntu_ec2"

  tags = {
    "Name" : "web_server002"
  }
 
}


output "instance_ip" {
  value = aws_instance.web_server01.public_ip
  
}



