# Guia de Início Rápido - UOL Login Scraper

## 3 Passos para Começar

### 1. Instale as Dependências (1 minuto)

```bash
cd webscrap

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt
```

### 2. Configure as Credenciais (30 segundos)

```bash
# Copie o arquivo de exemplo
copy config.properties.example config.properties

# Edite config.properties com suas credenciais
notepad config.properties
```

**config.properties:**
```properties
# Login credentials
email=seu_email@bol.com.br
password=sua_senha

# Optional settings
timeout=30
max_retries=3
debug_mode=false
```

### 3. Execute o Scraper (30 segundos)

```bash
python uol_login_scraper.py
```

**Saída esperada:**
```
Fetching login page...
Form action URL: https://conta.uol.com.br/some-action
Form fields found: ['email', 'password', 'csrf_token']
Submitting login form...
Login appears successful!
Login result: True
```

## Teste Rápido

Para testar sem configurar arquivo:

```bash
python simple_test.py
```

## Próximos Passos

- Leia o [README.md](README.md) completo
- Explore o código em `uol_login_scraper.py`
- Consulte a documentação de [deployment AWS Lambda](README.md#aws-lambda-deployment)

## Comandos Úteis

```bash
# Ver logs detalhados
python uol_login_scraper.py --debug

# Testar conexão
python -c "import requests; print(requests.get('https://www.uol.com.br').status_code)"

# Verificar dependências
pip list
```

## Troubleshooting Rápido

### Erro de módulo não encontrado
```bash
pip install -r requirements.txt
```

### Erro de credenciais
Verifique se o arquivo `config.properties` existe e está preenchido corretamente.

### Erro de rede
Verifique sua conexão com a internet e tente novamente.
