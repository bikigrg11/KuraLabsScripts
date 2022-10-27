# //////////////////////////////
# VARIABLES
# //////////////////////////////
variable "aws_access_key" {}

variable "aws_secret_key" {}

variable "bucket_name" {
  default = "bgurung2022-tfstate"
}

# //////////////////////////////
# PROVIDER
# //////////////////////////////
provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region = "us-east-1"
}

# //////////////////////////////
# TERRAFORM USER
# //////////////////////////////
data "aws_iam_user" "terraform" {
  user_name = "terraform"
}

# //////////////////////////////
# S3 BUCKET
# //////////////////////////////
resource "aws_s3_bucket" "bgurung2022-tfstate" {
  bucket = var.bucket_name
  force_destroy = true
}
  resource "aws_s3_bucket_policy" "allow_access_from_another_account" {
  bucket = aws_s3_bucket.bgurung2022-tfstate.id
  policy = data.aws_iam_policy_document.allow_access_tf.json
}

data "aws_iam_policy_document" "allow_access_tf" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::009931682463:user/terraform"]
    }

    actions = [
      "s3:*",
      
    ]

    resources = [
      aws_s3_bucket.bgurung2022-tfstate.arn,
      "${aws_s3_bucket.bgurung2022-tfstate.arn}/*",
    ]
  }
}

# //////////////////////////////
# DYNAMODB TABLE
# //////////////////////////////
resource "aws_dynamodb_table" "tf_db_statelock" {
  name           = "bgurung2022-tfstatelock"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}