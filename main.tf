terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

# Define the providers for diffrent zones
provider "aws" {
  alias = "west-2"
  profile = "default"
  region  = "us-west-2"
  
}

provider "aws" {
  alias = "west-1"
  profile = "default"
  region  = "us-west-1"
  
}

provider "aws" {
  alias = "east-1"
  profile = "default"
  region  = "us-east-1"
  
}

# Define the resources
resource "aws_instance" "master1" {
  ami           = "ami-a0b89fc0"
  instance_type = "t2.micro"
  provider = "aws.west-1"
}

resource "aws_instance" "master2" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"
  provider = "aws.west-2"
}


resource "aws_instance" "master3" {
  ami           = "ami-2f442839"
  instance_type = "t2.micro"
  provider = "aws.east-1"
}





