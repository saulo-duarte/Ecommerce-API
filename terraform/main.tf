provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

module "vpc" {
  source = "./modules/vpc"
}

module "ec2" {
  source     = "./modules/ec2"
  vpc_id     = module.vpc.vpc_id
  subnet_id  = module.vpc.public_subnet_id
  sg_id      = module.vpc.security_group_id
  key_name   = var.key_name
}

module "rds" {
  source         = "./modules/rds"
  subnet_ids     = module.vpc.subnet_ids
  sg_id          = module.vpc.security_group_id
  db_username    = var.db_username
  db_password    = var.db_password
}