# INSTANCES
resource "aws_instance" "web_server01" {
  ami                    = "ami-08c40ec9ead489470"
  instance_type          = "t2.micro"
  subnet_id              = data.vpc.aws_subnet1_id
  vpc_security_group_ids = module.vpc.vpc_security_group_ids

  key_name = "ubuntu_ec2"

  tags = {
    "Name" : "web_server001"
  }

  
 
}

resource "aws_instance" "web_server02" {
  ami                    = "ami-08c40ec9ead489470"
  instance_type          = "t2.micro"
  subnet_id              = "${module.vpc.aws_subnet2_id}"
  vpc_security_group_ids = module.vpc.vpc_security_group_ids

  key_name = "ubuntu_ec2"

  tags = {
    "Name" : "web_server002"
  }
 
}


output "instance_ip" {
  value = aws_instance.web_server01.public_ip
  
}



