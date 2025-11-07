import pytest
from unittest.mock import MagicMock, patch
from testepp import Login, App  
import tkinter.messagebox as msgbox

@pytest.fixture
def mock_app():
    app = MagicMock()
    app.banco.login_usuario.return_value = [(1, "João", "joao@email.com", "3A", "N", 10, 1.5, 3, 1)]
    app.banco.carregar_dados_jogador.return_value = [("João", "joao@email.com", "senha123", "3A", "N")]
    app.usuario_logado = {}
    return app


def test_login_sucesso(monkeypatch, mock_app):
    login = Login(None, mock_app)

    login.email_login = MagicMock()
    login.senha_login = MagicMock()
    login.email_login.get.return_value = "joao@email.com"
    login.senha_login.get.return_value = "senha123"

    with patch("tkinter.messagebox.showinfo") as mock_info:
        login.login_usuario()

    mock_app.banco.login_usuario.assert_called_with("joao@email.com", "senha123")
    mock_info.assert_called_once_with("Sucesso", "Login bem-sucedido!")
    assert mock_app.usuario_logado["nome"] == "João"
    mock_app.show_frame.assert_called()


def test_login_falha(monkeypatch, mock_app):
    login = Login(None, mock_app)

    login.email_login = MagicMock()
    login.senha_login = MagicMock()
    login.email_login.get.return_value = "email@errado.com"
    login.senha_login.get.return_value = "senhaErrada"

    mock_app.banco.login_usuario.return_value = []

    with patch("tkinter.messagebox.showerror") as mock_error:
        login.login_usuario()

    mock_app.banco.login_usuario.assert_called_with("email@errado.com", "senhaErrada")
    mock_error.assert_called_once_with("Erro", "Email ou senha incorretos.")
