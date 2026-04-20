# Guia de Contribuição - UOL Login Scraper

Obrigado por considerar contribuir com este projeto! Este documento fornece diretrizes para colaboração.

## 📋 Índice

- [Código de Conduta](#código-de-conduta)
- [Como Contribuir](#como-contribuir)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Desenvolvimento Local](#desenvolvimento-local)
- [Padrões de Código](#padrões-de-código)
- [Processo de Pull Request](#processo-de-pull-request)
- [Segurança](#segurança)

## 🤝 Código de Conduta

Este projeto adere a um código de conduta. Ao participar, você concorda em manter um ambiente respeitoso e colaborativo.

## 🚀 Como Contribuir

### 1. Fork e Clone

```bash
# Fork o repositório no GitHub
# Clone seu fork
git clone https://github.com/seu-usuario/webscrap.git
cd webscrap
```

### 2. Configure o Ambiente

```bash
# Crie ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt
```

### 3. Crie uma Branch

```bash
git checkout -b feature/minha-contribuicao
```

### 4. Faça suas Alterações

- Modifique código Python
- Adicione testes
- Atualize documentação

### 5. Teste suas Alterações

```bash
# Execute o scraper
python uol_login_scraper.py

# Execute testes simples
python simple_test.py
```

### 6. Commit e Push

```bash
git add .
git commit -m "feat: adiciona nova funcionalidade"
git push origin feature/minha-contribuicao
```

### 7. Abra um Pull Request

- Vá para o repositório original no GitHub
- Clique em "New Pull Request"
- Selecione sua branch
- Descreva suas alterações detalhadamente

## 📁 Estrutura do Projeto

```
webscrap/
├── uol_login_scraper.py          # Script principal
├── simple_test.py                # Script de teste
├── requirements.txt              # Dependências Python
├── config.properties.example     # Template de configuração
├── config.properties             # Configuração (não versionado)
├── .gitignore                    # Arquivos ignorados
├── README.md                     # Documentação principal
├── QUICKSTART.md                 # Guia de início rápido
├── CONTRIBUTING.md               # Este arquivo
└── terraform/                    # Infraestrutura como código
    └── README.md
```

## 💻 Desenvolvimento Local

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Conta UOL/BOL para testes

### Configuração

1. **Crie arquivo de configuração:**
```bash
cp config.properties.example config.properties
```

2. **Edite com suas credenciais de teste:**
```properties
email=teste@bol.com.br
password=senha_teste
timeout=30
max_retries=3
debug_mode=true
```

3. **Execute:**
```bash
python uol_login_scraper.py
```

## 📝 Padrões de Código

### Python

#### Estilo

- Siga PEP 8
- Use 4 espaços para indentação
- Máximo de 100 caracteres por linha
- Use docstrings para funções

#### Nomenclatura

```python
# Funções: snake_case
def fetch_login_page():
    pass

# Classes: PascalCase
class LoginScraper:
    pass

# Constantes: UPPER_SNAKE_CASE
DEFAULT_TIMEOUT = 30

# Variáveis: snake_case
user_email = "test@example.com"
```

#### Docstrings

```python
def uol_login_scraper(email, password):
    """
    Realiza login no UOL/BOL.

    Args:
        email (str): Email do usuário
        password (str): Senha do usuário

    Returns:
        bool: True se login bem-sucedido, False caso contrário

    Raises:
        requests.RequestException: Erro de rede
    """
    pass
```

#### Tratamento de Erros

```python
# ✓ Correto: Trate exceções específicas
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    logger.error("Timeout ao acessar URL")
    return False
except requests.RequestException as e:
    logger.error(f"Erro de rede: {e}")
    return False

# ✗ Evite: Catch genérico
try:
    # código
except Exception:
    pass
```

#### Logging

```python
# ✓ Correto: Use logging module
import logging

logger = logging.getLogger(__name__)
logger.info(f"Acessando URL: {url}")

# ✗ Evite: Print statements
print(f"Acessando URL: {url}")
```

### Web Scraping

#### Boas Práticas

```python
# Use headers realistas
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'pt-BR,pt;q=0.9',
}

# Respeite rate limiting
import time
time.sleep(1)  # Aguarde entre requisições

# Trate erros HTTP
response.raise_for_status()

# Use timeout
response = requests.get(url, timeout=30)
```

## 🔄 Processo de Pull Request

### Workflow de Branches

Use sempre branches com prefixo descritivo, criadas a partir de `main`:

- `feature/<descricao-curta>` — novas funcionalidades
- `fix/<descricao-curta>` — correções de bugs
- `chore/<descricao-curta>` — tarefas de manutenção, tooling, CI
- `docs/<descricao-curta>` — mudanças de documentação
- `refactor/<descricao-curta>` — refatorações sem mudança de comportamento

Fluxo: feature branch → Pull Request → code review → merge em `main` (nunca commite direto em `main`).

### Processo de Code Review

- Todo PR **requer pelo menos 1 approval** antes do merge.
- Reviewers devem verificar: clareza do código, cobertura de testes, impacto em segurança e aderência ao style guide.
- Autor deve responder comentários e aplicar sugestões (ou justificar) antes de solicitar re-review.

### Como Criar PRs

1. Use um título descritivo no formato Conventional Commits (`feat: ...`, `fix: ...`, `chore: ...`).
2. Preencha o template (`.github/pull_request_template.md`) por completo.
3. Vincule a(s) issue(s) relacionadas usando `Closes #<n>` ou `Fixes #<n>`.
4. Marque como Draft enquanto ainda houver trabalho em progresso.
5. Garanta que o CI está verde antes de pedir review.

### Branch Protection (para administradores)

Configure `main` em **GitHub Settings → Branches → Branch protection rules → Add rule**:

- [x] **Require a pull request before merging** — 1 approving review obrigatório.
- [x] **Require status checks to pass before merging** — marque os checks do workflow `CI` (`lint-and-test`, `pre-commit`).
- [x] **Require branches to be up to date before merging**.
- [x] **Include administrators**.
- [x] (Opcional, recomendado) **Require conversation resolution before merging**.

### Checklist

Antes de submeter um PR, verifique:

- [ ] Código funciona corretamente
- [ ] Código segue PEP 8
- [ ] Documentação foi atualizada
- [ ] Não há credenciais no código
- [ ] .gitignore está atualizado
- [ ] Commit messages são descritivas

### Formato de Commit Messages

Use o padrão Conventional Commits:

```
tipo(escopo): descrição curta

Descrição mais detalhada se necessário.

Fixes #123
```

**Tipos:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Alterações na documentação
- `refactor`: Refatoração de código
- `test`: Adição ou correção de testes
- `chore`: Tarefas de manutenção

**Exemplos:**

```bash
feat(scraper): adiciona suporte para captcha

Implementa detecção e tratamento de captcha usando 2captcha API.
Inclui testes e documentação.

Closes #45
```

```bash
fix(login): corrige timeout em páginas lentas

Aumenta timeout de 10s para 30s.
Adiciona retry com backoff exponencial.

Fixes #67
```

## 🔒 Segurança

### Regras Importantes

1. **NUNCA commite credenciais**
   - Use `config.properties` (já no .gitignore)
   - Use variáveis de ambiente em produção
   - Use secrets managers (AWS Secrets Manager, etc)

2. **Proteja dados sensíveis**
   ```python
   # ✓ Correto: Mascare senhas em logs
   logger.info(f"Login com email: {email}")

   # ✗ Evite: Logar senhas
   logger.info(f"Login: {email}:{password}")
   ```

3. **Valide entrada do usuário**
   ```python
   # Valide formato de email
   import re
   if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
       raise ValueError("Email inválido")
   ```

4. **Use HTTPS**
   ```python
   # ✓ Correto
   url = "https://conta.uol.com.br"

   # ✗ Evite
   url = "http://conta.uol.com.br"
   ```

### Reportar Vulnerabilidades

Para reportar vulnerabilidades de segurança:
1. **NÃO** abra uma issue pública
2. Envie email para: security@example.com
3. Inclua detalhes da vulnerabilidade
4. Aguarde resposta antes de divulgar

## 🐛 Reportando Bugs

### Template de Bug Report

```markdown
**Descrição do Bug**
Descrição clara e concisa do problema.

**Como Reproduzir**
1. Execute '...'
2. Configure '...'
3. Observe '...'

**Comportamento Esperado**
O que deveria acontecer.

**Comportamento Atual**
O que está acontecendo.

**Logs**
```
Cole logs relevantes aqui (SEM SENHAS!)
```

**Ambiente:**
- Python version: [3.7, 3.8, 3.9, 3.10]
- OS: [Windows 10, Ubuntu 20.04, etc]
- requests version: [2.28.0]

**Contexto Adicional**
Qualquer outra informação relevante.
```

## 💡 Sugerindo Melhorias

### Áreas para Contribuição

- [ ] Suporte a outros sites (Gmail, Hotmail, etc)
- [ ] Detecção e tratamento de captcha
- [ ] Testes unitários e de integração
- [ ] Interface web (Flask/Django)
- [ ] CLI com argumentos
- [ ] Suporte a proxy
- [ ] Retry automático com backoff
- [ ] Métricas e monitoramento
- [ ] Docker container
- [ ] CI/CD pipeline

## 📚 Recursos Úteis

- [Requests Documentation](https://requests.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)

## ⚖️ Considerações Legais

- Respeite os Termos de Serviço do UOL
- Use apenas para fins educacionais e pessoais
- Não faça scraping agressivo (rate limiting)
- Considere usar APIs oficiais quando disponíveis

## ❓ Dúvidas

Se tiver dúvidas sobre como contribuir:

1. Abra uma issue com a tag `question`
2. Descreva sua dúvida claramente
3. Aguarde resposta da comunidade

## 🙏 Agradecimentos

Obrigado por contribuir! Sua ajuda torna este projeto melhor para todos.

---

**Nota**: Este é um projeto educacional. Use com responsabilidade e ética.
