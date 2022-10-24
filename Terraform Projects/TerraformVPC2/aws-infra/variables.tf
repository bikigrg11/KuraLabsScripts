variable "aws_access_key" {}

variable "aws_secret_key" {}

variable "availability_zone_names" {
  type    = list(string)
  default = ["us-west-1a"]
}

output "aws_subnet1_id" {
  value = "${aws_subnet.subnet1.id}"
}

output "aws_subnet2_id" {
  value = "${aws_subnet.subnet2.id}"
}