terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

variable "access_key" {
    type        = string
}

variable "secret_key" {
    type        = string
}

variable "keypair_name" {
    type        = string
}

variable "security_group" {
    type        = string
}

provider "aws" {
  access_key = var.access
  secret_key = var.secret
  region     = "us-east-2"
}

resource "aws_instance" "instance" {
  ami             = "ami-00399ec92321828f5"
  instance_type   = "t2.micro"
  security_groups = [var.security_group]
  key_name        = var.keypair_name
  tags = {
    Name = "ubuntu-20.04"
  }
}
