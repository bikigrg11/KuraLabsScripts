output "aws_subnet1_id" {
  value = "${aws_subnet.subnet1.id}"
}

output "aws_subnet2_id" {
  value = "${aws_subnet.subnet2.id}"
}

output "vpc_security_group_ids" {
  value = ["${aws_security_group.web_ssh.id}"]
}

