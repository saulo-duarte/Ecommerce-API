resource "aws_instance" "app" {
    ami                         = "ami-0c67065b5ac5afe3a"
    instance_type               = "t2.micro"
    subnet_id                   = var.subnet_id
    vpc_security_group_ids      = [var.sg_id]
    key_name                    = var.key_name
    associate_public_ip_address = true

    user_data = <<-EOF
               #!/bin/bash
              yum update -y

              yum install git -y

              amazon-linux-extras install docker -y
              service docker start
              usermod -a -G docker ec2-user

              curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose

              amazon-linux-extras enable postgresql17.2
              yum install postgresql -y
              EOF

    tags = {
        Name = "AppServer"
    }
}