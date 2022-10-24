# VPC
resource "aws_vpc" "test-vpc" {
  cidr_block           = "172.26.0.0/16"
  enable_dns_hostnames = "true"

  tags = {
    "Name" : "test-vpc"
  }
}

# INTERNET GATEWAY
resource "aws_internet_gateway" "gw_1" {
  vpc_id = "${aws_vpc.test-vpc.id}"
}

# SUBNET 1
resource "aws_subnet" "subnet1" {
  cidr_block              = "172.26.0.0/18"
  vpc_id                  = "${aws_vpc.test-vpc.id}"
  map_public_ip_on_launch = "true"
  availability_zone       = data.aws_availability_zones.available.names[0]
}

resource "aws_route_table_association" "route-subnet1" {
  subnet_id      = aws_subnet.subnet1.id
  route_table_id = aws_route_table.route_table1.id
}


# SUBNET 2
resource "aws_subnet" "subnet2" {
  cidr_block              = "172.26.64.0/18"
  vpc_id                  = "${aws_vpc.test-vpc.id}"
  map_public_ip_on_launch = "true"
  availability_zone       = data.aws_availability_zones.available.names[0]
}


resource "aws_route_table_association" "route-subnet2" {
  subnet_id      = aws_subnet.subnet2.id
  route_table_id = aws_route_table.route_table1.id
}


# ROUTE TABLE
resource "aws_route_table" "route_table1" {
  vpc_id = "${aws_vpc.test-vpc.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.gw_1.id}"
  }
}

# DATA
data "aws_availability_zones" "available" {
  state = "available"
}

