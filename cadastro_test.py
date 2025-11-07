import pytest
from customtkinter import CTk
from unittest.mock import Mock, patch
from testepp import Cadastro  

@pytest.fixture
def mock_controller():
    controller = Mock()
    controller.banco = Mock()
    controller.show_frame = Mock()
    return controller

@pytest.fixture
def app():
    root = CTk()
    root.withdraw()  
    yield root
    root.destroy()

def test_flag_professor(mock_controller, app):
    cadastro = Cadastro(app, mock_controller)
    cadastro.flag_professor("Sim")
    assert cadastro.professor == "S"
    cadastro.flag_professor("Não")
    assert cadastro.professor == "N"

def test_toggle_senha(mock_controller, app):
    cadastro = Cadastro(app, mock_controller)
    cadastro.senha_cadastro.configure(show="")
    cadastro.toggle_senha()
    assert cadastro.senha_cadastro.cget("show") == "*"
    cadastro.toggle_senha()
    assert cadastro.senha_cadastro.cget("show") == ""

@patch("cadastro.msgbox")
def test_cadastrar_usuario_com_campos_vazios(mock_msgbox, mock_controller, app):
    cadastro = Cadastro(app, mock_controller)
    cadastro.nome_completo.insert(0, "")
    cadastro.email_cadastro.insert(0, "")
    cadastro.senha_cadastro.insert(0, "")
    cadastro.professor = ""
    cadastro.turma.insert(0, "")

    cadastro.cadastrar_usuario()

    mock_msgbox.showerror.assert_called_once_with("Erro", "Todos os campos devem ser preenchidos!")

@patch("cadastro.msgbox")
def test_cadastrar_usuario_sucesso(mock_msgbox, mock_controller, app):
    cadastro = Cadastro(app, mock_controller)
    cadastro.nome_completo.insert(0, "João Silva")
    cadastro.email_cadastro.insert(0, "joao@email.com")
    cadastro.senha_cadastro.insert(0, "senha123")
    cadastro.turma.insert(0, "3A")
    cadastro.professor = "N"

    cadastro.cadastrar_usuario()

    mock_controller.banco.cadastrar_usuario.assert_called_once_with(
        "João Silva", "joao@email.com", "senha123", "3A", "N"
    )
    mock_msgbox.showinfo.assert_called_once()
    mock_controller.show_frame.assert_called_once()
