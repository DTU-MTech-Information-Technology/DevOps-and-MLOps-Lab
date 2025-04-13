variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  default = "t2.micro"
  type    = string
}

variable "key_name" {
  description = "SSH key name in AWS"
  type        = string
}
