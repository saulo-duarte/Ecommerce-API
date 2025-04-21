variable "aws_region" {
  default = "sa-east-1"
}

variable "aws_profile" {
  default = "terraform"
}

variable "key_name" {
  description = "Chave SSH criada na AWS"
}

variable "db_username" {
  description = "Usuário do banco PostgreSQL"
}

variable "db_password" {
  description = "Senha do banco"
  sensitive   = true
}
