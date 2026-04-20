"""Testes de carregamento/validação de configuração.

Substitui o antigo `simple_test.py` por testes pytest adequados.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from uol_login_scraper import load_config


def test_load_config_success(config_file: Path) -> None:
    config = load_config(str(config_file))

    assert config["email"] == "teste@bol.com.br"
    assert config["password"] == "senha_super_secreta"
    assert config["timeout"] == 15
    assert config["max_retries"] == 2
    assert config["debug_mode"] is True


def test_load_config_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "does-not-exist.properties"

    with pytest.raises(FileNotFoundError):
        load_config(str(missing))


def test_load_config_placeholder_password_raises(tmp_path: Path) -> None:
    path = tmp_path / "config.properties"
    path.write_text(
        "[DEFAULT]\nemail=x@y.com\npassword=your_password_here\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_config(str(path))


def test_load_config_missing_email_raises(tmp_path: Path) -> None:
    path = tmp_path / "config.properties"
    path.write_text("[DEFAULT]\npassword=abcdef\n", encoding="utf-8")

    with pytest.raises(ValueError):
        load_config(str(path))


def test_load_config_defaults_applied(tmp_path: Path) -> None:
    path = tmp_path / "config.properties"
    path.write_text(
        "[DEFAULT]\nemail=x@y.com\npassword=realpass\n",
        encoding="utf-8",
    )

    config = load_config(str(path))

    assert config["timeout"] == 30
    assert config["max_retries"] == 3
    assert config["debug_mode"] is False
