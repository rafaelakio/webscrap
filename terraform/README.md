# Terraform - webscrap

Configuração Terraform para deploy do web scraper como AWS Lambda.

## 📁 Estrutura

```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
└── terraform.tfvars.example
```

## 🚀 Deploy

### Recursos Criados

- Lambda Function
- Lambda Layer (dependências Python)
- Secrets Manager (credenciais UOL)
- CloudWatch Log Group
- EventBridge Rule (agendamento opcional)
- SNS Topic (notificações)
- CloudWatch Alarm (monitoramento de erros)
- IAM Roles e Policies

### Pré-requisitos

Criar os pacotes Lambda:

```bash
# 1. Criar Lambda Layer com dependências
mkdir -p python
pip install requests beautifulsoup4 lxml -t python/
zip -r lambda_layer.zip python/
rm -rf python

# 2. Criar pacote da função
zip lambda_function.zip uol_login_scraper.py
```

### Deploy

```bash
# Copiar e editar variáveis
cp terraform.tfvars.example terraform.tfvars
# IMPORTANTE: Edite uol_email e uol_password

# Inicializar Terraform
terraform init

# Planejar mudanças
terraform plan

# Aplicar configuração
terraform apply
```

## 🎮 Executar Scraper

### Manualmente via AWS CLI

```bash
# Invocar Lambda
aws lambda invoke \
  --function-name webscrap-scraper \
  --payload '{}' \
  response.json

# Ver resultado
cat response.json
```

### Manualmente via Console AWS

1. Acesse Lambda no console AWS
2. Selecione a função `webscrap-scraper`
3. Clique em "Test"
4. Configure um evento de teste vazio: `{}`
5. Execute

### Agendamento Automático

Para executar automaticamente:

1. Edite `terraform.tfvars`:
```hcl
enable_schedule     = true
schedule_expression = "rate(1 hour)"  # ou "cron(0 9 * * ? *)"
```

2. Aplique mudanças:
```bash
terraform apply
```

## 🔒 Gerenciar Credenciais

### Atualizar Credenciais

```bash
# Via AWS CLI
aws secretsmanager update-secret \
  --secret-id webscrap-credentials \
  --secret-string '{"email":"novo@email.com","password":"nova-senha"}'

# Via Console AWS
# 1. Acesse Secrets Manager
# 2. Selecione webscrap-credentials
# 3. Clique em "Retrieve secret value"
# 4. Edite e salve
```

### Ver Credenciais Atuais

```bash
aws secretsmanager get-secret-value \
  --secret-id webscrap-credentials \
  --query SecretString \
  --output text
```

## 📊 Monitoramento

### Ver Logs

```bash
# Logs em tempo real
aws logs tail /aws/lambda/webscrap-scraper --follow

# Últimas 50 linhas
aws logs tail /aws/lambda/webscrap-scraper --since 1h
```

### Métricas

```bash
# Ver invocações
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Invocations \
  --dimensions Name=FunctionName,Value=webscrap-scraper \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Sum
```

## 🔔 Notificações

### Configurar Email para Alertas

```bash
# Obter ARN do tópico SNS
SNS_TOPIC=$(terraform output -raw sns_topic_arn)

# Inscrever email
aws sns subscribe \
  --topic-arn $SNS_TOPIC \
  --protocol email \
  --notification-endpoint seu-email@example.com

# Confirme a inscrição no email recebido
```

## 🔧 Configuração

### Variáveis Importantes

- `uol_email`: Email para login no UOL
- `uol_password`: Senha (armazenada no Secrets Manager)
- `enable_schedule`: Habilitar execução agendada
- `schedule_expression`: Expressão de agendamento

### Expressões de Agendamento

```hcl
# A cada hora
schedule_expression = "rate(1 hour)"

# A cada 30 minutos
schedule_expression = "rate(30 minutes)"

# Diariamente às 9h UTC
schedule_expression = "cron(0 9 * * ? *)"

# Segunda a sexta às 8h UTC
schedule_expression = "cron(0 8 ? * MON-FRI *)"
```

## 🗑️ Destruir Recursos

```bash
terraform destroy
```

## 💰 Custos Estimados

- Lambda: Primeira 1M requests grátis
- Secrets Manager: $0.40/mês por secret
- CloudWatch Logs: ~$0.50/GB
- Total: ~$1-2/mês (uso leve)

## 📝 Notas

- Credenciais são armazenadas com segurança no Secrets Manager
- Lambda tem timeout de 60 segundos
- Logs são retidos por 7 dias
- CloudWatch Alarm dispara após 3 erros em 5 minutos
- Use com responsabilidade e respeite os termos de serviço do UOL
