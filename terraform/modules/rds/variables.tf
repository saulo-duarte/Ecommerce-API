variable "subnet_ids" {
  description = "List of subnet IDs"
  type        = list(string)
}

variable "db_username" {
  description = "The database username"
  type        = string
}

variable "db_password" {
  description = "The database password"
  type        = string
}

variable "sg_id" {
  description = "Security Group ID"
  type        = string
}