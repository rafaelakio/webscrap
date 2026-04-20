"""Fixtures compartilhadas para os testes."""

from __future__ import annotations

from pathlib import Path

import pytest

SAMPLE_CONFIG = """[DEFAULT]
email=teste@bol.com.br
password=senha_super_secreta
timeout=15
max_retries=2
debug_mode=true
"""


LOGIN_PAGE_HTML = """
<html>
  <body>
    <form action="/login-submit" method="post">
      <input type="hidden" name="csrf_token" value="abc123" />
      <input type="email" name="email" />
      <input type="password" name="password" />
      <input type="submit" value="Entrar" />
    </form>
  </body>
</html>
"""


@pytest.fixture
def sample_config_content() -> str:
    """Conteúdo de um config.properties válido para testes."""
    return SAMPLE_CONFIG


@pytest.fixture
def config_file(tmp_path: Path, sample_config_content: str) -> Path:
    """Cria um arquivo config.properties temporário."""
    path = tmp_path / "config.properties"
    path.write_text(sample_config_content, encoding="utf-8")
    return path


@pytest.fixture
def login_page_html() -> str:
    """HTML mínimo com um formulário de login no formato esperado."""
    return LOGIN_PAGE_HTML
