# SEC GROUP
resource "aws_security_group" "web_ssh" {
  name        = "ssh-access"
  description = "open ssh traffic"
  vpc_id      = "${aws_vpc.test-vpc.id}"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = [format("%s/%s",data.external.whatismyip.result["internet_ip"],32)]
    #security_group_id = "sg-123456"


  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    "Name" : "aws-testvpc-sg"
    "Terraform" : "true"
  }

}


