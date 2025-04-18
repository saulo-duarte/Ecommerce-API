# E-commerce Data Generator API

Projeto educacional focado em aprender sobre APIs RESTful, integração com AWS e engenharia de dados.

## 🔧 Tecnologias

- **FastAPI**: API REST com documentação automática.
- **PostgreSQL (AWS RDS)**: Banco relacional gerenciado.
- **SQLAlchemy**: ORM para abstração do banco.
- **Pydantic**: Validação de dados.
- **Docker**: Ambiente de desenvolvimento padronizado.
- **Terraform**: Infraestrutura como código.
- **AWS SDK (boto3)**: Integração com serviços AWS.

## ☁️ AWS Services Utilizados

- **RDS**: Armazenamento dos dados.
- **Secrets Manager**: Gerenciamento seguro de credenciais.
- **CloudWatch**: Logs e monitoramento.
- **EC2**: Hospedagem da API.

## 📌 Objetivos

- Criar API RESTful com FastAPI para gerar dados fictícios de e-commerce.
- Armazenar dados no PostgreSQL (RDS).
- Utilizar padrões de projeto (Repository e Service).
- Implementar CI/CD com GitHub Actions.
- Automatizar infraestrutura com Terraform.

## 🧱 Arquitetura do Projeto

**Camadas:**

- **Routes**: Endpoints HTTP com validação via Pydantic.
- **Services**: Lógica de negócio e orquestração.
- **Repositories**: Acesso a dados (CRUD) via SQLAlchemy.
- **Models**: Tabelas do banco com SQLAlchemy.
- **Schemas**: Entrada/saída dos dados com Pydantic.

---

> Projeto para fins educacionais, sem propósito comercial ou de produção.
