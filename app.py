from customtkinter import *
from customtkinter import CTkImage
from PIL import Image, ImageTk
from PIL.Image import Resampling
import sqlite3
import tkinter as tk
import random
import time
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk


class BancoDeDados:
    def __init__(self, db_file):
        self.dados_conexao = "PI.db"
        self.conexao = sqlite3.connect(self.dados_conexao)
        self.cursor = self.conexao.cursor()
        self.usuario_atual = ""
        self.dados_usuario = ()
        self.dados_jogo = []
        print('Conectado com sucesso')

    def get_usuario_atual(self):
        return self.usuario_atual

    def get_dados_jogo(self):
        return self.dados_jogo

    def atualizar_estatisticas_usuario(self, email, pontuacao_max, tempo_medio, num_acertos, qntd_jogos):
        """Atualiza as estatísticas do usuário no banco de dados"""
        try:
            self.cursor.execute('''
                UPDATE Usuario 
                SET pontuacao_max = ?, 
                    tempo_medio = ?, 
                    num_acertos = ?, 
                    qntd_jogos = ?
                WHERE email = ?
            ''', (pontuacao_max, tempo_medio, num_acertos, qntd_jogos, email))
            self.conexao.commit()
            print("Estatísticas do usuário atualizadas com sucesso!")
            
            # Atualiza os dados locais também
            if self.usuario_atual:
                self.usuario_atual = (
                    self.usuario_atual[0],  # id
                    self.usuario_atual[1],  # nome
                    self.usuario_atual[2],  # email
                    self.usuario_atual[3],  # turma
                    self.usuario_atual[4],  # senha
                    pontuacao_max,
                    tempo_medio,
                    num_acertos,
                    qntd_jogos
                )
                self.dados_jogo = self.usuario_atual[5:]
        except Exception as e:
            print(f"Erro ao atualizar estatísticas do usuário: {e}")

    def inserir_perguntas_mat(self):
        try:
            comandos = [
                # Fácil (F) - 15 perguntas
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual é a função das raízes nas plantas?', 'Absorver água e nutrientes', 'Produzir sementes', 'Realizar fotossíntese', 'Atrair polinizadores', 'Absorver água e nutrientes', 'As raízes absorvem água e sais minerais.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual órgão bombeia o sangue no corpo humano?', 'Coração', 'Pulmão', 'Fígado', 'Rim', 'Coração', 'O coração é responsável pela circulação sanguínea.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'O que é fotossíntese?', 'Processo das plantas para produzir energia', 'Respiração celular', 'Digestão', 'Reprodução', 'Processo das plantas para produzir energia', 'A fotossíntese usa luz solar para produzir energia.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual componente do sangue transporta oxigênio?', 'Hemoglobina', 'Plaquetas', 'Plasma', 'Glóbulos brancos', 'Hemoglobina', 'Hemoglobina transporta oxigênio no sangue.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual animal é um mamífero?', 'Cachorro', 'Cobra', 'Tubarão', 'Pombo', 'Cachorro', 'Mamíferos possuem pelos e amamentam filhotes.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual o órgão responsável pela respiração nos humanos?', 'Pulmão', 'Fígado', 'Coração', 'Estômago', 'Pulmão', 'Os pulmões realizam as trocas gasosas.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual o principal nutriente absorvido pelas plantas?', 'Água', 'Proteína', 'Gordura', 'Carboidrato', 'Água', 'A água é essencial para as plantas.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual é o sentido do paladar?', 'Língua', 'Nariz', 'Olhos', 'Ouvidos', 'Língua', 'A língua detecta sabores.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual destes animais é um réptil?', 'Cobra', 'Gato', 'Elefante', 'Golfinho', 'Cobra', 'Cobras são répteis.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'O que as plantas precisam para crescer?', 'Luz solar, água e nutrientes', 'Oxigênio e calor', 'Gás carbônico e fogo', 'Solo e vento', 'Luz solar, água e nutrientes', 'Esses são os principais fatores para o crescimento.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual é o sistema do corpo responsável pela digestão?', 'Sistema digestório', 'Sistema nervoso', 'Sistema respiratório', 'Sistema circulatório', 'Sistema digestório', 'O sistema digestório processa os alimentos.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual célula é a unidade básica dos seres vivos?', 'Célula', 'Átomo', 'Molécula', 'Tecido', 'Célula', 'Todos os seres vivos são formados por células.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual é a cor das plantas?', 'Verde', 'Azul', 'Vermelho', 'Amarelo', 'Verde', 'Devido à clorofila.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual é o maior órgão do corpo humano?', 'Pele', 'Fígado', 'Cérebro', 'Pulmão', 'Pele', 'A pele é o maior órgão do corpo.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('F', 'Qual destes é um animal invertebrado?', 'Inseto', 'Cachorro', 'Águia', 'Elefante', 'Inseto', 'Insetos não possuem coluna vertebral.', 'BIO')",

                # Médio (M) - 15 perguntas
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual organela celular produz energia?', 'Mitocôndria', 'Ribossomo', 'Cloroplasto', 'Lisossomo', 'Mitocôndria', 'Mitocôndria é a “usina de energia” da célula.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual é a função dos ribossomos?', 'Síntese de proteínas', 'Produção de lipídios', 'Digestão celular', 'Armazenamento de água', 'Síntese de proteínas', 'Ribossomos produzem proteínas.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual tipo de reprodução ocorre por bipartição?', 'Assexuada', 'Sexuada', 'Bipartição', 'Fragmentação', 'Bipartição', 'Bactérias se reproduzem por bipartição.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual sistema humano combate infecções?', 'Sistema imunológico', 'Sistema digestório', 'Sistema nervoso', 'Sistema circulatório', 'Sistema imunológico', 'Sistema imunológico defende o corpo.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual é a função dos glóbulos brancos?', 'Defender o organismo', 'Transportar oxigênio', 'Coagular sangue', 'Produzir hormônios', 'Defender o organismo', 'Glóbulos brancos combatem infecções.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'O que é DNA?', 'Material genético', 'Proteína', 'Hormônio', 'Enzima', 'Material genético', 'DNA contém informação genética.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual processo celular replica o DNA?', 'Fase S', 'Mitose', 'Meiose', 'Fase G1', 'Fase S', 'Na fase S ocorre a replicação do DNA.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'O que fazem os cloroplastos?', 'Fotossíntese', 'Respiração', 'Digestão', 'Excreção', 'Fotossíntese', 'Cloroplastos captam luz para energia.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual é o tecido responsável pelo transporte de água nas plantas?', 'Xilema', 'Floema', 'Parênquima', 'Colênquima', 'Xilema', 'Xilema transporta água.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual a função do sistema nervoso?', 'Controlar as funções do corpo', 'Transportar oxigênio', 'Digestionar alimentos', 'Produzir hormônios', 'Controlar as funções do corpo', 'O sistema nervoso controla o corpo.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'O que é a respiração celular?', 'Produção de energia em células', 'Fotossíntese', 'Transporte de nutrientes', 'Divisão celular', 'Produção de energia em células', 'Respiração celular libera energia.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual é a principal molécula energética das células?', 'ATP', 'ADN', 'ARN', 'Glicose', 'ATP', 'ATP é a “moeda energética”.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual é a função do floema nas plantas?', 'Transportar seiva elaborada', 'Transportar seiva bruta', 'Suportar a planta', 'Armazenar nutrientes', 'Transportar seiva elaborada', 'Floema leva nutrientes para as células.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual tipo de tecido forma os músculos?', 'Tecido muscular', 'Tecido epitelial', 'Tecido conjuntivo', 'Tecido nervoso', 'Tecido muscular', 'Músculos são formados por tecido muscular.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('M', 'Qual a principal função dos glóbulos vermelhos?', 'Transportar oxigênio', 'Defender o corpo', 'Coagular sangue', 'Produzir anticorpos', 'Transportar oxigênio', 'Glóbulos vermelhos levam oxigênio.', 'BIO')",

                # Difícil (D) - 15 perguntas
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual a função dos lisossomos?', 'Degradação de substâncias', 'Produção de energia', 'Síntese de proteínas', 'Transporte celular', 'Degradação de substâncias', 'Lisossomos digerem resíduos.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual é o papel do DNA?', 'Armazenar informação genética', 'Produzir proteínas', 'Regular metabolismo', 'Gerar energia', 'Armazenar informação genética', 'DNA contém o código genético.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'O que ocorre na fase S do ciclo celular?', 'Duplicação do DNA', 'Divisão celular', 'Crescimento celular', 'Morte celular', 'Duplicação do DNA', 'DNA é replicado na fase S.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual hormônio é produzido pela tireoide?', 'Tiroxina', 'Insulina', 'Adrenalina', 'Cortisol', 'Tiroxina', 'Tiroxina regula o metabolismo.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual processo produz gametas?', 'Meiose', 'Mitose', 'Fissão binária', 'Fragmentação', 'Meiose', 'Meiose reduz cromossomos pela metade.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual é a função das enzimas?', 'Catalisar reações químicas', 'Produzir energia', 'Armazenar nutrientes', 'Defender células', 'Catalisar reações químicas', 'Enzimas aceleram reações.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'O que são nucleotídeos?', 'Unidades do DNA e RNA', 'Tipos de proteínas', 'Moléculas de gordura', 'Partes da célula', 'Unidades do DNA e RNA', 'Nucleotídeos formam ácidos nucleicos.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual o processo da respiração celular?', 'Glicose + oxigênio → energia + CO2 + água', 'Fotossíntese', 'Fermentação', 'Digestão', 'Glicose + oxigênio → energia + CO2 + água', 'Respiração celular libera energia.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'O que ocorre na mitose?', 'Divisão celular para crescimento', 'Produção de gametas', 'Replicação do DNA', 'Morte celular', 'Divisão celular para crescimento', 'Mitose divide células para crescimento.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual a função dos plasmídeos nas bactérias?', 'Transferir genes', 'Produzir energia', 'Formar parede celular', 'Armazenar nutrientes', 'Transferir genes', 'Plasmídeos carregam genes extras.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'O que é apoptose?', 'Morte celular programada', 'Crescimento celular', 'Divisão celular', 'Metabolismo', 'Morte celular programada', 'Apoptose é morte celular controlada.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual a estrutura que controla a entrada e saída na célula?', 'Membrana plasmática', 'Núcleo', 'Citoplasma', 'Mitocôndria', 'Membrana plasmática', 'Membrana controla o que entra e sai.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'O que são anticorpos?', 'Proteínas que combatem antígenos', 'Vitaminas', 'Hormônios', 'Enzimas', 'Proteínas que combatem antígenos', 'Anticorpos protegem contra invasores.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual é o papel do RNA mensageiro?', 'Transcrever informação do DNA para proteína', 'Transportar oxigênio', 'Produzir energia', 'Degradar nutrientes', 'Transcrever informação do DNA para proteína', 'RNA mensageiro leva código para ribossomos.', 'BIO')",
                "INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) VALUES ('D', 'Qual o papel do sistema endócrino?', 'Produzir hormônios', 'Defender o corpo', 'Realizar respiração', 'Controlar movimentos', 'Produzir hormônios', 'Sistema endócrino regula funções pelo sangue.', 'BIO')",
            ]
            for sql in comandos:
                self.cursor.execute(sql)
            self.conexao.commit()
            print("Todas as perguntas foram inseridas com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir perguntas: {e}")


    def carregar_estatisticas(self,id_jogador):
        self.cursor.execute("SELECT pontuacao_max, tempo_medio, num_acertos, qntd_jogos FROM Usuario WHERE id = ?", (id_jogador,))
        return self.cursor.fetchall()[0]
    
    def login_usuario(self, email, senha):
        self.cursor.execute('SELECT * FROM Usuario WHERE email = ? AND senha = ?', (email, senha))
        self.dados_usuario = self.cursor.fetchall()
        if self.dados_usuario:
            self.usuario_atual = self.dados_usuario[0]
            self.dados_jogo = self.dados_usuario[0][5:] if len(self.dados_usuario[0]) > 5 else []
        return self.dados_usuario

    def cadastrar_usuario(self, nome, email, senha, turma, professor):
        try:
            self.cursor.execute('''
                INSERT INTO Usuario (nome, email, senha, turma, professor, pontuacao_max, tempo_medio, num_acertos, qntd_jogos) 
                VALUES (?, ?, ?, ?, ?, 0, 0, 0, 0)
            ''', (nome, email, senha, turma, professor))
            self.conexao.commit()
            print("Cadastro Realizado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
            return False
    
    def carregar_dados(self):
        self.cursor.execute("SELECT id, pergunta, altA, altB, altC, altD, dificuldade, correta, dica, materia FROM Pergunta")
        return self.cursor.fetchall()
    
    def carregar_jogadores(self):
        self.cursor.execute("SELECT id, nome, email, turma, professor FROM Usuario")
        return self.cursor.fetchall()
    
    def carregar_dados_jogador(self,email):
        self.cursor.execute("SELECT nome,email,senha,turma,professor FROM Usuario WHERE email = ?", (email,))
        return self.cursor.fetchall()

    def carregar_materias(self):
        self.cursor.execute("SELECT sigla FROM Materia")
        return self.cursor.fetchall()[1::]
    
    def carregar_materias_perguntas(self):
        self.cursor.execute('''SELECT m.sigla, COUNT(p.pergunta) as quantidade_perguntas
                            FROM Materia m
                            LEFT JOIN Pergunta p ON m.sigla = p.materia
                            GROUP BY m.sigla
                            ORDER BY m.sigla;
                            ''')
        return self.cursor.fetchall()
    
    def filtrar_perguntas(self, disciplina, dificuldade):
        if (disciplina == "" or disciplina == "Todas") and dificuldade != "":
            self.cursor.execute("SELECT id, pergunta, altA, altB, altC, altD, dificuldade, correta, dica, materia FROM Pergunta WHERE dificuldade = ?",(dificuldade,))
            return self.cursor.fetchall()
        elif (dificuldade == "" or dificuldade== "Todas") and disciplina != "":
            self.cursor.execute("SELECT id, pergunta, altA, altB, altC, altD, dificuldade, correta, dica, materia FROM Pergunta WHERE materia = ?", (disciplina,))
            return self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT id, pergunta, altA, altB, altC, altD, dificuldade, correta, dica, materia FROM Pergunta WHERE materia = ? AND dificuldade = ? ", (disciplina,dificuldade))
            return self.cursor.fetchall()

    def cadastrar_materia(self,sigla):
        self.cursor.execute("INSERT INTO Materia (sigla) VALUES (?)",(sigla,))
        self.conexao.commit()

    def cadastrar_pergunta(self, pergunta, alt_a, alt_b, alt_c, alt_d, dica, dificuldade, correta,materia):
            try:
                self.cursor.execute('''
                    INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (dificuldade, pergunta, alt_a, alt_b, alt_c, alt_d, correta, dica, materia))
                self.conexao.commit()
                print("Cadastro realizado com sucesso!")
            except Exception as e:
                print(f"Erro: {e}")

    def deletar_pergunta(self, id_jogador):
        try:
            self.cursor.execute('DELETE FROM Pergunta WHERE id = ?', (id_jogador,))
            self.conexao.commit()
            print("Deletado com sucesso")
        except Exception as e:
            print(f"Erro: {e}")

    def materia_atual(self,materia):
        self.cursor.execute("UPDATE MateriaAtual SET materia = ? WHERE id = 1", (materia,))
        self.conexao.commit()

    def mostrar_materia_atual(self):
        self.cursor.execute("SELECT materia FROM MateriaAtual")
        return self.cursor.fetchall()

class App(CTk):
    def __init__(self):
        super().__init__()
        self.banco = BancoDeDados("PI.db")
        self.title("Show Do Milhão")
        self.geometry("1200x780")
        self.center_window(1200, 780)

        self.usuario_logado = {
            'nome': '',
            'email': '',
            'senha': '',
            'turma': '',
            'professor': 'N'  # Valor padrão
        }
        
        # Container principal para os frames
        self.container = CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Criar todos os frames
        for F in (Login, MateriasJogo, Menu, MenuProfessor, Perguntas, PerguntasProfessor, Cadastro, CentralProfessor, Jogadores):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Login)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        # Ajustar tamanho da janela conforme necessário
        if cont == Login or cont == Cadastro:
            self.geometry("1200x780")
            self.center_window(1200, 780)
        else:
            self.geometry("1200x780")
            self.center_window(1200, 780)
    
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        self.geometry(f'{width}x{height}+{position_left}+{position_top}')

class BaseFrame(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        

class Login(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.configure(fg_color="#1E1E1E")
        self.dados_jogador = []


        # Tornar layout base responsivo
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Carregar imagem original
        self.original_img = Image.open("imagens/fundo-verde-balatro-vertical.png")
        self.side_label = None
        self.current_img = None

        

        self.criar_tela()

    def criar_tela(self):
        email_icon = CTkImage(dark_image=Image.open("imagens/email.png"),
                              light_image=Image.open("imagens/email.png"), size=(20, 20))
        password_icon = CTkImage(dark_image=Image.open("imagens/cadeado.png"),
                                 light_image=Image.open("imagens/cadeado.png"), size=(17, 17))
        signup_icon = CTkImage(dark_image=Image.open("imagens/useradd.png"),
                               light_image=Image.open("imagens/useradd.png"), size=(17, 17))
        self.eye_icon = CTkImage(dark_image=Image.open("imagens/olho-senha.png"),
                               light_image=Image.open("imagens/olho-senha.png"), size=(17, 17))
        self.closed_eye = CTkImage(dark_image=Image.open("imagens/ocultar-senha.png"),
                               light_image=Image.open("imagens/ocultar-senha.png"), size=(17, 17))


        # Frame lateral com imagem
        self.left_frame = CTkFrame(self, fg_color="#ffffff")
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_propagate(False)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        resized_img = CTkImage(dark_image=self.original_img, light_image=self.original_img, size=(400, 580))
        self.current_img = resized_img
        self.side_label = CTkLabel(self.left_frame, text="", image=self.current_img)
        self.side_label.grid(row=0, column=0, sticky="nsew")

        self.left_frame.bind("<Configure>", self.redimensionar_imagem_lateral)

        # Frame de login
        self.frame_login = CTkFrame(self, fg_color="#1E1E1E",corner_radius=0)
        self.frame_login.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)
        self.frame_login.grid_columnconfigure(0, weight=1)

        # Título e subtítulo
        CTkLabel(self.frame_login, text="Faça seu Login", text_color="#ffffff",
                 font=("courier new", 28, "bold")).grid(row=0, column=0, sticky="w", pady=(50, 5))
        CTkLabel(self.frame_login, text="Entre na sua conta", text_color="#ffffff",
                 font=("courier new", 16, "bold")).grid(row=1, column=0, sticky="w", pady=(0, 20))

        # Campo de email
        CTkLabel(self.frame_login, text=" Email:", text_color="#ffffff", image=email_icon,
                 compound="left", font=("courier new", 16, "bold")).grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.email_login = CTkEntry(self.frame_login, fg_color="#3B5055", border_color="#B5C6D0",
                                    border_width=2, text_color="#ffffff", height=35,corner_radius=8, font=("courier new",14, "bold"))
        self.email_login.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        # Campo de senha
        CTkLabel(self.frame_login, text=" Senha:", text_color="#ffffff", image=password_icon,
                 compound="left", font=("courier new", 16, "bold")).grid(row=4, column=0, sticky="w", pady=(0, 5))
        

        senha_frame = CTkFrame(self.frame_login, fg_color="transparent")
        senha_frame.grid(row=5, column=0, sticky="ew", pady=(0, 30))
        senha_frame.grid_columnconfigure(0, weight=1)

        # Campo de senha 
        self.senha_login = CTkEntry(senha_frame, fg_color="#3B5055", border_color="#B5C6D0",
                             border_width=2, text_color="#ffffff", show="*", height=35,
                            corner_radius=8, font=("courier new", 14, "bold"))
        self.senha_login.grid(row=0, column=0, sticky="ew")

        # Botão de mostrar/ocultar senha 
        self.btn_ocultar_senha = CTkButton(senha_frame, image=self.closed_eye, height=35,
                                   width=35, text="", fg_color="#3B5055", hover_color="#2F3E43", corner_radius=8, command=self.toggle_senha,border_color="#B5C6D0", border_width=2)
        self.btn_ocultar_senha.grid(row=0, column=1, padx=(5, 0))

        # Botão login
        CTkButton(self.frame_login, text="LOGIN", fg_color="#FF9700", hover_color="#c27402",
                  font=("courier new", 22, "bold"), text_color="#ffffff", command=self.login_usuario, height=45, corner_radius=10).grid(row=6, column=0, sticky="ew", pady=(10, 15))

        # Botão cadastro
        CTkButton(self.frame_login, text="Ainda não tem conta? Cadastre-se", fg_color="#D22D23", hover_color="#942019",
                  font=("courier new", 14,"bold"), text_color="#ffffff", image=signup_icon,
                  command=lambda: self.controller.show_frame(Cadastro), height=45).grid(row=7, column=0, sticky="ew", pady=(10,0))
        
        imagem = CTkImage(dark_image=Image.open("imagens/logo-poliedro-1.png"),
                      light_image=Image.open("imagens/logo-poliedro-1.png"),
                      size=(80, 80))
        
        imagem_label = CTkLabel(self, image=imagem, text="")
        imagem_label.place(relx=1.0, rely=1.0, x=-100, y=-100)


    def toggle_senha(self):
        if self.senha_login.cget("show") == "":
            self.senha_login.configure(show="*")
            self.btn_ocultar_senha.configure(image=self.closed_eye)
        else:
            self.senha_login.configure(show="")
            self.btn_ocultar_senha.configure(image=self.eye_icon)



    def redimensionar_imagem_lateral(self, event=None):
        new_width = self.left_frame.winfo_width()
        new_height = self.left_frame.winfo_height()

        if new_width > 0 and new_height > 0:
            resized_pil = self.original_img.resize((new_width, new_height), Image.LANCZOS)
            self.current_img = CTkImage(dark_image=resized_pil, light_image=resized_pil, size=(new_width, new_height))
            self.side_label.configure(image=self.current_img)

    def login_usuario(self):
        email = self.email_login.get()
        senha = self.senha_login.get()
        valores = self.controller.banco.login_usuario(email, senha)

        if valores:
            msgbox.showinfo("Sucesso", "Login bem-sucedido!")
            dados = self.controller.banco.carregar_dados_jogador(email)[0]
            self.controller.frames[Perguntas].estatisticas_banco = self.controller.frames[Perguntas].carregar_dados_usuario()
            
            # Preenche os dados do usuário de forma estruturada
            self.controller.usuario_logado = {
                'nome': dados[0],
                'email': dados[1],
                'senha': dados[2],
                'turma': dados[3],
                'professor': dados[4]
            }
            
            if self.controller.usuario_logado['professor'] == "S":
                self.controller.show_frame(MenuProfessor)
                print(self.controller.banco.get_usuario_atual()[0])
            else:
                self.controller.show_frame(Menu)
        else:
            msgbox.showerror("Erro", "Email ou senha incorretos.")
    
    
    #def cadastrar_geog(self):
        #self.controller.banco.inserir_perguntas_mat()


class Cadastro(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.configure(fg_color="#1E1E1E")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.original_img = Image.open("imagens/fundo-verde-balatro-vertical.png")
        self.side_label = None
        self.current_img = None
        self.professor = "N"

        self.criar_tela()

    def criar_tela(self):
        name_icon = CTkImage(dark_image=Image.open("imagens/usuario.png"),
                             light_image=Image.open("imagens/usuario.png"), size=(17, 17))
        email_icon = CTkImage(dark_image=Image.open("imagens/email.png"),
                              light_image=Image.open("imagens/email.png"), size=(20, 20))
        password_icon = CTkImage(dark_image=Image.open("imagens/cadeado.png"),
                                 light_image=Image.open("imagens/cadeado.png"), size=(17, 17))
        signin_icon = CTkImage(dark_image=Image.open("imagens/login.png"),
                               light_image=Image.open("imagens/login.png"), size=(17, 17))
        self.eye_icon = CTkImage(dark_image=Image.open("imagens/olho-senha.png"),
                               light_image=Image.open("imagens/olho-senha.png"), size=(17, 17))
        self.closed_eye = CTkImage(dark_image=Image.open("imagens/ocultar-senha.png"),
                               light_image=Image.open("imagens/ocultar-senha.png"), size=(17, 17))

        # Frame da imagem à esquerda
        self.left_frame = CTkFrame(self, fg_color="#1E1E1E")
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_propagate(False)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        resized_img = CTkImage(dark_image=self.original_img, light_image=self.original_img, size=(400, 580))
        self.current_img = resized_img
        self.side_label = CTkLabel(self.left_frame, text="", image=self.current_img)
        self.side_label.grid(row=0, column=0, sticky="nsew")

        self.left_frame.bind("<Configure>", self.redimensionar_imagem_lateral)

        # Frame direito com campos de cadastro
        self.right_frame = CTkFrame(self, fg_color="#1E1E1E")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Título
        CTkLabel(self.right_frame, text="Faça seu Cadastro", text_color="#ffffff",
                 font=("courier new", 28, "bold")).grid(row=0, column=0, sticky="w", pady=(40, 5))
        CTkLabel(self.right_frame, text="Crie sua conta", text_color="#ffffff",
                 font=("courier new", 16,"bold")).grid(row=1, column=0, sticky="w", pady=(0, 20))

        # Nome
        CTkLabel(self.right_frame, text="  Nome Completo:", text_color="#ffffff", image=name_icon,
                 compound="left", font=("courier new", 14, "bold")).grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.nome_completo = CTkEntry(self.right_frame, fg_color="#3B5055", border_color="#B5C6D0",
                                      border_width=2, text_color="#ffffff", height=35,font=("courier new",14))
        self.nome_completo.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        # Turma
        CTkLabel(self.right_frame, text="  Turma:", text_color="#ffffff", image=name_icon,
                 compound="left", font=("courier new", 14, "bold")).grid(row=4, column=0, sticky="w", pady=(0, 5))
        self.turma = CTkEntry(self.right_frame, fg_color="#3B5055", border_color="#B5C6D0",
                                      border_width=2, text_color="#ffffff", height=35,font=("courier new",14))
        self.turma.grid(row=5, column=0, sticky="ew", pady=(0, 20))

        # Email
        CTkLabel(self.right_frame, text="  Email:", text_color="#ffffff", image=email_icon,
                 compound="left", font=("courier new", 14, "bold")).grid(row=6, column=0, sticky="w", pady=(0, 5))
        self.email_cadastro = CTkEntry(self.right_frame, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff", height=35,font=("courier new",14))
        self.email_cadastro.grid(row=7, column=0, sticky="ew", pady=(0, 20))

        #Professor?
        CTkLabel(self.right_frame, text="Professor?", text_color="#ffffff", font= ("courier new",14,"bold")).grid(row=8, column =0, sticky="w", pady=(0,5))

        self.professor = CTkOptionMenu(self.right_frame, values=["Não","Sim"], text_color="#ffffff", fg_color="#3B5055", height=35,button_color="#3B5055",button_hover_color="#3B5055", font=("courier new",14,"bold"), command=self.flag_professor, dropdown_fg_color="#3B5055", dropdown_font=("courier new",14,"bold"), dropdown_text_color="#ffffff")
        self.professor.set("Selecione uma opção...")
        self.professor.grid(row = 9, column = 0, sticky = "ew", pady=(0,20))
        
        # Senha
        CTkLabel(self.right_frame, text="  Senha:", text_color="#ffffff", image=password_icon,
                 compound="left", font=("courier new", 14, "bold")).grid(row=10, column=0, sticky="w", pady=(0, 5))
        senha_frame = CTkFrame(self.right_frame, fg_color="transparent")
        senha_frame.grid(row=11, column=0, sticky="ew", pady=(0, 30))
        senha_frame.grid_columnconfigure(0, weight=1)

        # Campo de senha 
        self.senha_cadastro = CTkEntry(senha_frame, fg_color="#3B5055", border_color="#B5C6D0",
                             border_width=2, text_color="#ffffff", show="*", height=35,
                            corner_radius=8, font=("courier new", 14, "bold"))
        self.senha_cadastro.grid(row=0, column=0, sticky="ew")

        # Botão de mostrar/ocultar senha 
        self.btn_ocultar_senha = CTkButton(senha_frame, image=self.closed_eye, height=35,
                                   width=35, text="", fg_color="#3B5055", hover_color="#2F3E43", corner_radius=8, command=self.toggle_senha, border_color="#B5C6D0", border_width=2)
        self.btn_ocultar_senha.grid(row=0, column=1, padx=(5, 0))

        

        # Botão cadastrar
        CTkButton(self.right_frame, text="CADASTRAR", fg_color="#FF9700", hover_color="#c27402",
                  font=("courier new", 22, "bold"), text_color="#ffffff", command=self.cadastrar_usuario, height=45, corner_radius=10).grid(
            row=12, column=0, sticky="ew", pady=(0, 15))

        # Botão login
        CTkButton(self.right_frame, text="Já tem conta? Faça login", fg_color="#D22D23", hover_color="#942019",
                  font=("courier new", 14, "bold"), text_color="#ffffff", image=signin_icon,
                  command=lambda: self.controller.show_frame(Login), height=45, corner_radius=10).grid(row=13, column=0, sticky="ew")

    def redimensionar_imagem_lateral(self, event=None):
        new_width = self.left_frame.winfo_width()
        new_height = self.left_frame.winfo_height()

        if new_width > 0 and new_height > 0:
            resized_pil = self.original_img.resize((new_width, new_height), Image.LANCZOS)
            self.current_img = CTkImage(dark_image=resized_pil, light_image=resized_pil, size=(new_width, new_height))
            self.side_label.configure(image=self.current_img)

    def toggle_senha(self):
        if self.senha_cadastro.cget("show") == "":
            self.senha_cadastro.configure(show="*")
            self.btn_ocultar_senha.configure(image=self.closed_eye)
        else:
            self.senha_cadastro.configure(show="")
            self.btn_ocultar_senha.configure(image=self.eye_icon)

    def cadastrar_usuario(self):
        nome = self.nome_completo.get()
        email = self.email_cadastro.get()
        senha = self.senha_cadastro.get()
        turma = self.turma.get()
        professor = self.professor

        if not nome or not email or not senha or not professor:
            msgbox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            self.controller.banco.cadastrar_usuario(nome, email, senha,turma, professor)
            msgbox.showinfo("Sucesso", f"{nome}, {email}, {turma},{professor},{senha}")
            self.controller.show_frame(Login)
        except Exception as e:
            msgbox.showerror("Erro", f"Falha ao cadastrar: {str(e)}")

    def flag_professor(self,professor):
        if professor == "Sim":
            self.professor = "S"
        else:
            self.professor = "N"
            



class CentralProfessor(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.configure(width=1200, height=780)

        # Configura o grid principal da tela
        self.grid_rowconfigure((0, 2), weight=1)  # Espaço acima e abaixo dos botões
        self.grid_rowconfigure(1, weight=3)       # Linha dos botões
        self.grid_columnconfigure((0, 1, 2), weight=1)  # 3 colunas para os botões

        # Carrega e exibe a imagem de fundo
        self.original_image = Image.open("imagens/fundo-verde-balatro-horizontal.png")
        self.background_image = None
        self.bg_label = CTkLabel(self, text="")
        self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.redimensionar_imagem)

        # Carregamento das imagens dos botões
        img_perguntas = CTkImage(light_image=Image.open("imagens/perguntas.png"),size=(60, 60))
        img_jogadores = CTkImage(light_image=Image.open("imagens/jogadores.png"),size=(60, 60))
        img_disciplinas = CTkImage(light_image=Image.open("imagens/disciplinas.png"),size=(60, 60))
        img_instrucoes = CTkImage(light_image=Image.open("imagens/instrucoes.png"),size=(60, 60))


        # Botão Voltar no canto superior
        CTkButton(self, height=35, width=70, text="<<<<", fg_color="#D22D23",hover_color="#942019",bg_color="#245d4a", text_color="#ffffff",border_color="#DB453D", border_width=3,
                  command=lambda: self.controller.show_frame(MenuProfessor), font=("courier new",18,"bold")).place(x=30, y=30)

        # Botões principais diretamente na grid do BaseFrame
        CTkButton(self, height=300, width=200, text="PERGUNTAS", fg_color="#FF9700",
                  text_color="#ffffff", font=("courier new",22,"bold"),
                  command=lambda: self.controller.show_frame(PerguntasProfessor), bg_color="#245d4a", corner_radius=11, hover_color="#c27402", border_color="#FFBB00", border_width=3, image=img_perguntas, compound="top").grid(row=1, column=0, padx=15, pady=10)

        CTkButton(self, height=300, width=200, text="JOGADORES", fg_color="#FF9700",
                  text_color="#ffffff", font=("courier new",22,"bold"),
                  command=lambda: self.controller.show_frame(Jogadores), bg_color="#245d4a", corner_radius=11, hover_color="#c27402", border_color="#FFBB00", border_width=3,  image=img_jogadores, compound="top").grid(row=1, column=1, padx=15, pady=10)

        CTkButton(self, height=300, width=200, text="INSTRUÇÕES", fg_color="#FF9700",
                  text_color="#ffffff", font=("courier new",22,"bold"), bg_color="#245d4a", corner_radius=11, hover_color="#c27402", border_color="#FFBB00", border_width=3,  image=img_instrucoes, compound="top").grid(row=1, column=2, padx=15, pady=10)

    def redimensionar_imagem(self, event):
        nova_img = self.original_image.resize((event.width, event.height), Resampling.LANCZOS)
        self.background_image = CTkImage(light_image=nova_img, size=(event.width, event.height))
        self.bg_label.configure(image=self.background_image)





class Jogadores(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#1E1E1E")
        self.pack_propagate(0)
        self.criar_tela()
        self.banco = controller.banco
        self.estatisticas = []
        self.pontuacao_max=""
        self.tempo_medio = ""
        self.num_acertos = ""
        self.qntd_jogos = ""
        self.mostrar_dados()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, uniform="grupo")
        self.grid_columnconfigure(1, weight=1, uniform="grupo")

    def criar_tela(self):
        
        self.left_frame = CTkFrame(self, fg_color="#1E1E1E")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.left_frame.grid_columnconfigure(0, weight=1)

        self.right_frame = CTkFrame(self, fg_color="#1E1E1E", corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        CTkButton(self.left_frame, height=35, width=70, text="<<<<", fg_color="#D22D23",hover_color="#942019", text_color="#ffffff",border_color="#DB453D", border_width=3,
                  command=lambda: self.controller.show_frame(CentralProfessor), font=("courier new",18,"bold")).place(x=15, y=15)

        CTkLabel(self.left_frame, text="Maior Pontuação: ", text_color="#ffffff", font=("courier new",18,"bold")).grid(row=0, column=0, padx=30, pady=(100,0))
        self.frame_pontuacao = CTkButton(self.left_frame, text=" ", font=("courier new",18,"bold"), text_color="#ffffff", height=55, fg_color="#25734D", hover_color="#25734D",corner_radius=11, border_color="#34A16D", border_width=3)
        self.frame_pontuacao.grid(row=1, column=0, padx=80, pady=10, sticky="ew")

        CTkLabel(self.left_frame, text="Tempo médio por pergunta: ", text_color="#ffffff", font=("courier new",18,"bold")).grid(row=2, column=0, padx=30, pady=8)
        self.frame_tempo_medio = CTkButton(self.left_frame, text=" ", font=("courier new",18,"bold"), text_color="#ffffff", height=55, fg_color="#25734D", hover_color="#25734D",corner_radius=11, border_color="#34A16D", border_width=3)
        self.frame_tempo_medio.grid(row=3, column=0, padx=80, pady=10, sticky="ew")

        CTkLabel(self.left_frame, text="Número máximo de acertos consecutivos: ", text_color="#ffffff", font=("courier new",18,"bold")).grid(row=4, column=0, padx=30, pady=8)
        self.frame_num_acertos = CTkButton(self.left_frame, text=" ", font=("courier new",18,"bold"), text_color="#ffffff", height=55, fg_color="#25734D", hover_color="#25734D",corner_radius=11, border_color="#34A16D", border_width=3)
        self.frame_num_acertos.grid(row=5, column=0, padx=80, pady=10, sticky="ew")

        CTkLabel(self.left_frame, text="Quantidade de jogos: ", text_color="#ffffff", font=("courier new",18,"bold")).grid(row=6, column=0, padx=30, pady=8)
        self.frame_qntd_jogos = CTkButton(self.left_frame, text=" ", font=("courier new",18,"bold"), text_color="#ffffff", height=55, fg_color="#25734D", hover_color="#25734D",corner_radius=11, border_color="#34A16D", border_width=3 )
        self.frame_qntd_jogos.grid(row=7, column=0, padx=80, pady=10, sticky="ew")



        colunas = ("ID","Nome","Email", "Turma")

        self.tree = ttk.Treeview(self.right_frame, columns=colunas, show="headings")
        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.grid(row=1, column=0, sticky="nsew", pady=10)

        scrollbar_y = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=1, column=1, sticky="ns")

        scrollbar_x = ttk.Scrollbar(self.right_frame, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=2, column=0, sticky="ew")

        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        self.btn_mostrar_estatisticas = CTkButton(self.right_frame, text="CARREGAR ESTATÍSTICAS", text_color="#ffffff", height=60, command=self.mostrar_estatisticas, fg_color="#FF9700", hover_color="#c27402",corner_radius=11, border_color="#FFBB00", border_width=3, font=("courier new",18,"bold") )
        self.btn_mostrar_estatisticas.grid(row=3, column=0, sticky="ew", pady=15)

        

    def mostrar_dados(self):
        try:
            # Limpar a treeview antes de adicionar novos dados
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            self.registros = self.banco.carregar_jogadores()

            for linha in self.registros:
                linha_limpa = tuple(str(item).strip("(),'\"") for item in linha)
                self.tree.insert("", "end", values=linha_limpa)
        except Exception as e:
            print("Erro ao carregar dados:", e)

    def mostrar_estatisticas(self):
        jogador_selecionado = self.tree.selection()
        
        if not jogador_selecionado:
            msgbox.showwarning("Aviso", "Por favor, selecione um jogador da lista.")
            return

        item_id = jogador_selecionado[0]
        valores_selecionados = self.tree.item(item_id)['values']

        if not valores_selecionados:
            msgbox.showerror("Erro", "Erro ao obter os dados do jogador selecionado.")
            return

        id_jogador = valores_selecionados[0]
        self.estatisticas = self.controller.banco.carregar_estatisticas(id_jogador)
        self.pontuacao_max = self.estatisticas[0]
        self.tempo_medio = f"{self.estatisticas[1]:.2f}"
        self.num_acertos = self.estatisticas[2]
        self.qntd_jogos = self.estatisticas[3]

        self.frame_pontuacao.configure(text=self.pontuacao_max)
        self.frame_tempo_medio.configure(text=self.tempo_medio)
        self.frame_num_acertos.configure(text=self.num_acertos)
        self.frame_qntd_jogos.configure(text=self.qntd_jogos)

        

class MateriasJogo(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#1E1E1E")
        self.pack_propagate(0)
        self.banco = controller.banco
        self.materias = []
        self.mostrar_materias()
        self.materia = " "
        self.criar_tela()
    
    def criar_tela(self):
        # Configura a grade principal para centralizar elementos
        self.grid_columnconfigure(0, weight=1)

        # Botão de voltar no canto superior esquerdo (sem centralizar)
        self.btn_voltar = CTkButton(self, text="<<<<", width=70, height=35,
                                    font=("courier new", 18, "bold"),
                                    command=lambda: self.controller.show_frame(MenuProfessor),
                                    fg_color="#D22D23", hover_color="#942019",
                                    border_width=3, border_color="#DB453D")
        self.btn_voltar.place(x=20, y=20)  # mantém o botão de voltar fixo no canto

        # Título centralizado
        CTkLabel(master=self, text="Escolha a matéria para o seu jogo: ",
                font=("courier new", 22, "bold"),text_color="#ffffff").grid(column=0, row=0, pady=(300, 30), sticky="n")

        # Frame das disciplinas centralizado
        self.frame_disciplinas = CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.frame_disciplinas.grid(row=1, column=0)

        # OptionMenu e botão de confirmar dentro do frame
        self.input_materia_jogo = CTkOptionMenu(self.frame_disciplinas, values=self.materias,
                                                font=("courier new", 18, "bold"),
         
                                               command=self.mostrar_materia, height=45, fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700", dropdown_fg_color="#3B5055", dropdown_font=("courier new",14,"bold"), dropdown_text_color="#ffffff")
        self.input_materia_jogo.set("Selecione a disciplina..")
        self.input_materia_jogo.grid(column=0, row=0, padx=10, pady=10)

        self.confirmar_materia = CTkButton(self.frame_disciplinas, text="CONFIRMAR",
                                        font=("courier new", 18, "bold"),
                                        command=self.atualizar_materia_atual, height=45,fg_color="#FF9700",hover_color="#c27402", corner_radius=8, border_color="#FFBB00", border_width=3 )
        self.confirmar_materia.grid(column=1, row=0, padx=20, pady=10)

        # Botão de iniciar jogo centralizado
        self.btn_iniciar_jogo = CTkButton(master=self, text="JOGAR",
                                        font=("courier new", 22, "bold"),
                                        width=500, height=80,
                                        command=lambda: self.controller.show_frame(Perguntas), fg_color="#25734D", hover_color="#14402b", corner_radius=11, border_color="#34A16D", border_width=3)
        self.btn_iniciar_jogo.grid(column=0, row=2, pady=40)


    
    def mostrar_materias(self):
        try:
            self.materias_tuple = self.banco.carregar_materias() 
            for materia in self.materias_tuple:
                self.materias.append(materia[0])
            print(self.materias)
        except Exception as e:
            print("Erro ao carregar materias")

    def mostrar_materia(self,materia):
        self.materia = materia
        print(self.materia)


    def atualizar_materia_atual(self):
        self.banco.materia_atual(self.materia)
        
        



class MenuProfessor(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(fg_color="#1E1E1E")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=7)

        self.original_img = Image.open("imagens/fundo-verde-balatro-vertical.png")
        self.side_label = None
        self.current_img = None

        self.menu_img_original = Image.open("imagens/logo-topo.png")  # Substitua pelo caminho real
        self.menu_img_label = None
        self.menu_img_atual = None

        self.criar_tela()

    def criar_tela(self):

        # Frame de login
        self.frame_menu = CTkFrame(self, fg_color="#1E1E1E",corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew", padx=20, pady=40)
        self.frame_menu.grid_columnconfigure(0, weight=1)

        self.image_frame = CTkFrame(self, fg_color="#1E1E1E", corner_radius=0)
        self.image_frame.grid(row=0, column=1, sticky="nsew")
        self.image_frame.grid_propagate(False)
        self.image_frame.grid_rowconfigure(0, weight=1)
        self.image_frame.grid_columnconfigure(0, weight=2)

        resized_img = CTkImage(dark_image=self.original_img, light_image=self.original_img, size=(400, 580))
        self.current_img = resized_img
        self.side_label = CTkLabel(self.image_frame, text="", image=self.current_img)
        self.side_label.grid(row=0, column=1, sticky="nsew")

        self.image_frame.bind("<Configure>", self.redimensionar_imagem_lateral)

        resized_menu_img = CTkImage(dark_image=self.menu_img_original, light_image=self.menu_img_original, size=(500, 260))
        self.menu_img_atual = resized_menu_img
        self.menu_img_label = CTkLabel(self.frame_menu, text="", image=self.menu_img_atual)
        self.menu_img_label.grid(row=0, column=0, pady=(50, 10))

        self.frame_menu.bind("<Configure>", self.redimensionar_imagem_menu)

        

        CTkButton(self.frame_menu, text="JOGAR", fg_color="#25734D", hover_color="#14402b", 
                  font=("courier new", 25, "bold"), text_color="#ffffff",  height=70, 
                  command=lambda: self.controller.show_frame(MateriasJogo), corner_radius=11, border_color="#34A16D", border_width=3).grid(column = 0, row = 1, sticky = "ew", pady=(130,20)) 
        CTkButton(self.frame_menu, text="CENTRAL PROFESSOR", fg_color="#FF9700", hover_color="#c27402", 
                  font=("courier new", 25, "bold"), text_color="#ffffff",  height=70, command=lambda: self.controller.show_frame(CentralProfessor), corner_radius=11, border_color="#FFBB00", border_width=3).grid(column = 0, row=2, sticky="ew", pady=(0,20))
        CTkButton(self.frame_menu, text="SAIR", fg_color="#D22D23", hover_color="#942019",
                  font=("courier new", 25, "bold"), text_color="#ffffff", height=70, 
                  command=self.controller.destroy, corner_radius=11, border_color="#DB453D", border_width=3).grid(column = 0, row = 3, sticky="ew", pady=(0,30))


    def redimensionar_imagem_lateral(self, event=None):
        new_width = self.image_frame.winfo_width()
        new_height = self.image_frame.winfo_height()

        if new_width > 0 and new_height > 0:
            resized_pil = self.original_img.resize((new_width, new_height), Image.LANCZOS)
            self.current_img = CTkImage(dark_image=resized_pil, light_image=resized_pil, size=(new_width, new_height))
            self.side_label.configure(image=self.current_img)

    def redimensionar_imagem_menu(self, event=None):
        new_width = self.frame_menu.winfo_width()
        altura_desejada = 180

        if new_width > 0:
            resized_pil = self.menu_img_original.resize((int(new_width * 0.8), altura_desejada), Image.LANCZOS)
            self.menu_img_atual = CTkImage(dark_image=resized_pil, light_image=resized_pil, size=(resized_pil.width, altura_desejada))
            self.menu_img_label.configure(image=self.menu_img_atual)



class Menu(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(fg_color="#1E1E1E")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=7)

        self.original_img = Image.open("imagens/fundo-verde-balatro-vertical.png")
        self.side_label = None
        self.current_img = None

        self.menu_img_original = Image.open("imagens/logo-topo.png")  # Substitua pelo caminho real
        self.menu_img_label = None
        self.menu_img_atual = None

        self.criar_tela()

    def criar_tela(self):

        # Frame de login
        self.frame_menu = CTkFrame(self, fg_color="#1E1E1E",corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew", padx=20, pady=40)
        self.frame_menu.grid_columnconfigure(0, weight=1)

        self.image_frame = CTkFrame(self, fg_color="#1E1E1E", corner_radius=0)
        self.image_frame.grid(row=0, column=1, sticky="nsew")
        self.image_frame.grid_propagate(False)
        self.image_frame.grid_rowconfigure(0, weight=1)
        self.image_frame.grid_columnconfigure(0, weight=2)

        resized_img = CTkImage(dark_image=self.original_img, light_image=self.original_img, size=(400, 580))
        self.current_img = resized_img
        self.side_label = CTkLabel(self.image_frame, text="", image=self.current_img)
        self.side_label.grid(row=0, column=1, sticky="nsew")

        self.image_frame.bind("<Configure>", self.redimensionar_imagem_lateral)

        resized_menu_img = CTkImage(dark_image=self.menu_img_original, light_image=self.menu_img_original, size=(500, 260))
        self.menu_img_atual = resized_menu_img
        self.menu_img_label = CTkLabel(self.frame_menu, text="", image=self.menu_img_atual)
        self.menu_img_label.grid(row=0, column=0, pady=(50, 10))

        self.frame_menu.bind("<Configure>", self.redimensionar_imagem_menu)

        

        CTkButton(self.frame_menu, text="JOGAR", fg_color="#25734D", hover_color="#14402b", 
                  font=("courier new", 25, "bold"), text_color="#ffffff",  height=70, 
                  command=lambda: self.controller.show_frame(MateriasJogo), corner_radius=11,border_color="#34A16D", border_width=3).grid(column = 0, row = 1, sticky = "ew", pady=(170,20)) 
        CTkButton(self.frame_menu, text="SAIR", fg_color="#D22D23", hover_color="#942019",
                  font=("courier new", 25, "bold"), text_color="#ffffff", height=70, 
                  command=self.controller.destroy, corner_radius=11,border_color="#DB453D", border_width=3).grid(column = 0, row = 3, sticky="ew", pady=(0,30))


    def redimensionar_imagem_lateral(self, event=None):
        new_width = self.image_frame.winfo_width()
        new_height = self.image_frame.winfo_height()

        if new_width > 0 and new_height > 0:
            resized_pil = self.original_img.resize((new_width, new_height), Image.LANCZOS)
            self.current_img = CTkImage(dark_image=resized_pil, light_image=resized_pil, size=(new_width, new_height))
            self.side_label.configure(image=self.current_img)

    def redimensionar_imagem_menu(self, event=None):
        new_width = self.frame_menu.winfo_width()
        altura_desejada = 180

        if new_width > 0:
            resized_pil = self.menu_img_original.resize((int(new_width * 0.8), altura_desejada), Image.LANCZOS)
            self.menu_img_atual = CTkImage(dark_image=resized_pil, light_image=resized_pil, size=(resized_pil.width, altura_desejada))
            self.menu_img_label.configure(image=self.menu_img_atual)

class Perguntas(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.materia_atual = self.controller.banco.mostrar_materia_atual()[0][0]
        self.perguntas = self.obter_perguntas()
        self.indice_pergunta = 0
        self.ajuda_dica_usada = False
        self.ajuda_50_usada = False
        self.ajuda_pular_usada = False
        self.pontos = [1000,2000,3000,5000,10000,20000,30000,50000,100000,150000,200000,300000,400000,500000,750000,1000000]
        self.i_pontos = 0
        self.pontuacao = 0
        self.checkpoint_atingido = False
        self.materia_selecionada = None
        self.id_usuario=" "
        self.estatisticas_banco = []
        
        # Variáveis para estatísticas
        self.tempos_respostas = []
        self.acertos_consecutivos = 0
        self.maior_acerto_consecutivo = 0

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

        self.criar_tela()

    def carregar_dados_usuario(self):
        """Carrega os dados do usuário do banco de dados"""
        dados_usuario = self.controller.banco.get_dados_jogo()
        print(dados_usuario)
        if dados_usuario and len(dados_usuario) >= 5:
            self.pontuacao_max = dados_usuario[1] 
            self.tempo_medio = dados_usuario[2] 
            self.num_acertos = dados_usuario[3]
            self.qntd_jogos = dados_usuario[4]
        else:
            self.pontuacao_max = 0
            self.tempo_medio = 0
            self.num_acertos = 0
            self.qntd_jogos = 0
        print(f"Pont: {self.pontuacao_max}")
        print(f"Tempo: {self.tempo_medio}")
        print(f"Num: {self.num_acertos}")
        print(f"Qtd: {self.qntd_jogos}")


    def atualizar_dados_usuario(self):
        """Atualiza os dados do usuário no banco de dados"""
        if hasattr(self.controller.banco, 'usuario_atual') and len(self.controller.banco.usuario_atual) > 2:
            email = self.controller.banco.usuario_atual[2]
            
            # Calcula os novos valores
            nova_pontuacao_max = max(self.pontuacao, self.pontuacao_max)
            novo_tempo_medio = self.calcular_tempo_medio()
            novo_num_acertos = max(self.maior_acerto_consecutivo, self.num_acertos)
            nova_qntd_jogos = self.qntd_jogos + 1
            
            self.controller.banco.atualizar_estatisticas_usuario(
                email, 
                nova_pontuacao_max,
                novo_tempo_medio,
                novo_num_acertos,
                nova_qntd_jogos
            )

    def calcular_tempo_medio(self):
        """Calcula o tempo médio por pergunta"""
        if not self.tempos_respostas:
            return self.tempo_medio
        
        tempo_atual = sum(self.tempos_respostas[1:]) / len(self.tempos_respostas[1:])
        
        if self.tempo_medio == 0:
            return tempo_atual
        
        return (self.tempo_medio + tempo_atual) / 2

    def obter_perguntas(self):
        conexao = sqlite3.connect("PI.db")
        cursor = conexao.cursor()
        
        cursor.execute("SELECT dificuldade, pergunta, altA, altB, altC, altD, correta, dica FROM Pergunta WHERE materia = ?", (self.materia_atual,))

        self.perguntas_faceis = []
        self.perguntas_medias = []
        self.perguntas_dificeis = []

        for row in cursor.fetchall():
            dificuldade, pergunta, alt_a, alt_b, alt_c, alt_d, correta, dica = row
            
            pergunta_dict = {
                "pergunta": pergunta,
                "alternativas": [alt_a, alt_b, alt_c, alt_d],
                "correta": correta,
                "dica": dica
            }
            
            if dificuldade == "F":
                self.perguntas_faceis.append(pergunta_dict)
            elif dificuldade == "M":
                self.perguntas_medias.append(pergunta_dict)
            elif dificuldade == "D":
                self.perguntas_dificeis.append(pergunta_dict)

        random.shuffle(self.perguntas_faceis)
        random.shuffle(self.perguntas_medias)
        random.shuffle(self.perguntas_dificeis)

        self.perguntas = self.perguntas_faceis[0:6] + self.perguntas_medias[0:7] + self.perguntas_dificeis[0:6]
        
        cursor.close()
        conexao.close()

        return self.perguntas

    def criar_tela(self):
        self.left_frame = CTkFrame(self, fg_color="#3B3B3B", corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_propagate(False)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=4)
        self.left_frame.grid_columnconfigure(0, weight=1)

        self.right_frame = CTkFrame(self, fg_color="#1E1E1E", corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_propagate(False)
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_columnconfigure(0, weight=1)
        
        self.frame_pergunta = CTkFrame(self.left_frame, height=200, fg_color="#3B5055", corner_radius=11, border_width=3, border_color="#B5C6D0")
        self.frame_pergunta.grid(column=0, row=0, sticky="nsew", padx=25, pady=(25, 0))
        self.frame_pergunta.grid_propagate(False)

        self.texto_pergunta = CTkLabel(self.frame_pergunta, text="", font=("courier new", 22, "bold"), text_color="#ffffff")
        self.texto_pergunta.grid(column=0, row=0, sticky="ew", pady=25, padx=25)

        self.texto_dica = CTkLabel(self.frame_pergunta, text="", font=("courier new", 18, "bold"), text_color="#ffffff")
        self.texto_dica.grid(column=0, row=1, sticky="ew", pady=15, padx=10)

        self.frame_botoes = CTkFrame(self.left_frame, fg_color="transparent")
        self.frame_botoes.grid(row=1, column=0, sticky="nsew", padx=25, pady=25)
        self.frame_botoes.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_botoes.grid_columnconfigure(0, weight=1)

        self.botoes_alternativas = []
        for i in range(4):
            botao = CTkButton(self.frame_botoes, text="", fg_color="#FF9700", font=("courier new", 25, "bold"),
                            text_color="#FFFFFF", corner_radius=10,
                            command=lambda i=i: self.verificar_resposta(i), hover_color="#c27402", border_color="#FFBB00")
            botao.grid(row=i, column=0, sticky="nsew", pady=(10 if i > 0 else 0, 0))  
            self.botoes_alternativas.append(botao)

        self.botão_pontuação = CTkButton(self.right_frame, text="R$ 0", font=("courier new", 25,"bold"), text_color="#ffffff", fg_color="#0269A0", height=90, corner_radius=10)
        self.botão_pontuação.grid(column=0, row=0, padx=15, pady=(40,60), sticky="ew")

        self.botao_ajuda_dica = CTkButton(self.right_frame, text="DICA", font=("courier new", 20, "bold"), fg_color="#25734D", 
                                        text_color="#ffffff",  height=80, command=self.mostrar_dica, corner_radius=10, hover_color="#14402b", border_color="#34A16D",  border_width=3)
        self.botao_ajuda_dica.grid(row=1, column=0, padx=15, pady=10, sticky="ew")

        self.botao_ajuda_50 = CTkButton(self.right_frame, text="50% / 50%", font=("courier new", 20, "bold"), fg_color="#25734D", 
                                    text_color="#ffffff",  height=80, command=self.eliminar_alternativas, corner_radius=10, hover_color="#14402b", border_color="#34A16D",  border_width=3)
        self.botao_ajuda_50.grid(row=2, column=0, padx=15, pady=10, sticky="ew")
        
        self.botao_ajuda_pular = CTkButton(self.right_frame, text="PULAR", font=("courier new", 20, "bold"), fg_color="#25734D", 
                                        text_color="#ffffff",  height=80, command=self.pular_pergunta, corner_radius=10, hover_color="#14402b", border_color="#34A16D",  border_width=3)
        self.botao_ajuda_pular.grid(row=3, column=0, padx=15, pady=(10,40), sticky="ew")
        
        self.botao_encerrar = CTkButton(self.right_frame, text="ENCERRAR", 
                                    font=("courier new", 20, "bold"), fg_color="#D22D23", 
                                    text_color="#ffffff",  height=150, 
                                    command=self.mostrar_janela_fim_jogo, corner_radius=10, hover_color="#942019",border_color="#DB453D", border_width=3)
        self.botao_encerrar.grid(row=4, column=0, padx=15, pady=(40,25), sticky="ew")

        self.game_over_frame = CTkFrame(self.left_frame, width=800, height=500, fg_color="#ffffff", corner_radius=10)
        self.game_over_label = CTkLabel(self.game_over_frame, text="Jogo Encerrado", font=("Arial Bold", 40), text_color="#FF0000")
        self.game_over_label.pack(pady=(150, 30))
        self.game_over_points = CTkLabel(self.game_over_frame, text="", font=("Arial Bold", 30))
        self.game_over_points.pack(pady=(0, 50))

        self.carregar_pergunta()

    def dados_jogo(self):
        return self.controller.banco.get_dados_jogo()
    
    def carregar_pergunta(self):
        self.game_over_frame.pack_forget()
        self.tempo_pergunta_inicio = time.time()
        
        if self.indice_pergunta < len(self.perguntas):
            pergunta_atual = self.perguntas[self.indice_pergunta]
            self.texto_pergunta.configure(text=pergunta_atual["pergunta"])
            self.texto_dica.configure(text="")
            
            alternativas = pergunta_atual["alternativas"]
            random.shuffle(alternativas)
            
            for i in range(4):
                self.botoes_alternativas[i].configure(text=alternativas[i], fg_color="#FF9700", state="normal", border_color="#FFBB00", border_width=4)
        else:
            self.mostrar_janela_jogo_concluido()
            for botao in self.botoes_alternativas:
                botao.pack_forget()

    def imprimir_estatisticas(self):
        """Imprime as estatísticas do jogo no terminal"""
        estatisticas = {
            "Pontuação atual": self.pontuacao,
            "Pontuação máxima anterior": self.pontuacao_max,
            "Nova pontuação máxima": max(self.pontuacao, self.pontuacao_max),
            "Tempo médio por pergunta (esta sessão)": f"{sum(self.tempos_respostas[1:])/len(self.tempos_respostas[1:]):.2f}s" if self.tempos_respostas else "N/A",
            "Tempo médio histórico": f"{self.tempo_medio:.2f}s",
            "Novo tempo médio": f"{self.calcular_tempo_medio():.2f}s",
            "Maior sequência de acertos (esta sessão)": self.maior_acerto_consecutivo,
            "Maior sequência de acertos (histórico)": self.num_acertos,
            "Nova maior sequência de acertos": max(self.maior_acerto_consecutivo, self.num_acertos),
            "Total de jogos (incluindo este)": self.qntd_jogos + 1
        }
        
        print("\n" + "="*50)
        print("ESTATÍSTICAS DO JOGO".center(50))
        print("="*50)
        for chave, valor in estatisticas.items():
            print(f"{chave}:".ljust(35) + f"{valor}".rjust(15))
        print("="*50 + "\n")
    
    def mostrar_dica(self):
        if not self.ajuda_dica_usada:
            self.ajuda_dica_usada = True
            self.botao_ajuda_dica.configure(state="disabled", fg_color="#888888")
            pergunta_atual = self.perguntas[self.indice_pergunta]
            self.texto_dica.configure(text=pergunta_atual["dica"])
    
    def eliminar_alternativas(self):
        if not self.ajuda_50_usada:
            self.ajuda_50_usada = True
            self.botao_ajuda_50.configure(state="disabled", fg_color="#888888")
            pergunta_atual = self.perguntas[self.indice_pergunta]
            incorretas = [botao for botao in self.botoes_alternativas if botao.cget("text") != pergunta_atual["correta"]]
            random.shuffle(incorretas)
            for botao in incorretas[:2]:
                botao.configure(state="disabled", fg_color="#D22D23", border_color="#DB453D")
    
    def pular_pergunta(self):
        if not self.ajuda_pular_usada:
            self.ajuda_pular_usada = True
            self.botao_ajuda_pular.configure(state="disabled", fg_color="#888888")
            self.indice_pergunta += 1
            self.carregar_pergunta()
    
    def verificar_resposta(self, indice):
        tempo_resposta = time.time() - self.tempo_pergunta_inicio
        print(f"{tempo_resposta:.0f}")
        self.tempos_respostas.append(tempo_resposta)

        pergunta_atual = self.perguntas[self.indice_pergunta]
        alternativa_selecionada = self.botoes_alternativas[indice].cget("text")
        
        if alternativa_selecionada == pergunta_atual["correta"]:
            self.botoes_alternativas[indice].configure(fg_color="#25734D", border_color="#34A16D")
            self.pontuacao = self.pontos[self.i_pontos]
            self.i_pontos += 1
            self.botão_pontuação.configure(text=f"Prêmio: R$ {self.pontuacao}")
            
            for botao in self.botoes_alternativas:
                botao.configure(state="disabled")
            
            if self.pontuacao in [10000, 150000]:
                self.checkpoint_atingido = True

            self.acertos_consecutivos += 1
            if self.acertos_consecutivos > self.maior_acerto_consecutivo:
                self.maior_acerto_consecutivo = self.acertos_consecutivos
            
            self.indice_pergunta += 1
            self.after(1000, self.carregar_pergunta)
        else:
            self.acertos_consecutivos = 0
            self.botoes_alternativas[indice].configure(fg_color="#D22D23",border_color="#DB453D" )
            
            if self.checkpoint_atingido:
                self.checkpoint_atingido = False
                self.label_feedback.configure(text="Você errou, mas usou seu checkpoint! Continue jogando.", text_color="#F39C12")
                self.after(1000, self.carregar_pergunta)
            else:
                for botao in self.botoes_alternativas:
                    botao.configure(state="disabled")
                
                self.botao_ajuda_dica.configure(state="disabled")
                self.botao_ajuda_50.configure(state="disabled")
                self.botao_ajuda_pular.configure(state="disabled")
                
                self.atualizar_dados_usuario()
                self.mostrar_janela_fim_jogo()

    def mostrar_janela_fim_jogo(self):
        self.imprimir_estatisticas()
        janela = CTkToplevel(self)
        janela.title("Fim de Jogo")
        janela.geometry("400x250")
        janela.grab_set()
        
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 250) // 2
        janela.geometry(f"400x250+{x}+{y}")

        CTkLabel(janela, text="Você perdeu!", font=("Arial Bold", 22), text_color="#E44982").pack(pady=20)
        CTkLabel(janela, text=f"Pontuação final: {self.pontuacao}", font=("Arial", 18)).pack(pady=10)

        def voltar_menu():
            janela.destroy()
            self.reiniciar_jogo()
            self.controller.show_frame(MenuProfessor)

        def recomeçar_jogo():
            janela.destroy()
            self.reiniciar_jogo()

        CTkButton(janela, text="Voltar ao Menu", font=("Arial Bold", 16), fg_color="#888888", 
                command=voltar_menu, width=200).pack(pady=10)

        CTkButton(janela, text="Recomeçar Jogo", font=("Arial Bold", 16), fg_color="#601E88", 
                command=recomeçar_jogo, width=200).pack(pady=10)
        
    def reiniciar_jogo(self):
        self.perguntas = self.obter_perguntas()
        self.indice_pergunta = 0
        self.ajuda_dica_usada = False
        self.ajuda_50_usada = False
        self.ajuda_pular_usada = False
        self.botao_ajuda_dica.configure(state="normal", fg_color="#25734D")
        self.botao_ajuda_50.configure(state="normal", fg_color="#25734D")
        self.botao_ajuda_pular.configure(state="normal", fg_color="#25734D")
        self.i_pontos = 0
        self.pontuacao = 0
        self.checkpoint_atingido = False
        self.tempos_respostas = []
        self.acertos_consecutivos = 0

        for i, botao in enumerate(self.botoes_alternativas):
            botao.grid(row=i, column=0, sticky="nsew", pady=(10 if i > 0 else 0, 0))  

        self.botão_pontuação.configure(text="Prêmio: R$ 0")
        self.carregar_pergunta()

    def mostrar_janela_jogo_concluido(self):
        self.atualizar_dados_usuario()
        self.imprimir_estatisticas()
        
        janela = CTkToplevel(self)
        janela.title("Fim de Jogo")
        janela.geometry("400x250")
        janela.grab_set()
        
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 250) // 2
        janela.geometry(f"400x250+{x}+{y}")

        CTkLabel(janela, text="Você Ganhouu!", font=("Arial Bold", 22), text_color="#E44982").pack(pady=20)
        CTkLabel(janela, text=f"Pontuação final: {self.pontuacao}", font=("Arial", 18)).pack(pady=10)

        def voltar_menu():
            janela.destroy()
            self.reiniciar_jogo()
            self.controller.show_frame(MenuProfessor)

        def recomeçar_jogo():
            janela.destroy()
            self.reiniciar_jogo()

        CTkButton(janela, text="Voltar ao Menu", font=("Arial Bold", 16), fg_color="#888888", 
                command=voltar_menu, width=200).pack(pady=10)

        CTkButton(janela, text="Recomeçar Jogo", font=("Arial Bold", 16), fg_color="#601E88", 
                command=recomeçar_jogo, width=200).pack(pady=10)


class PerguntasProfessor(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#1E1E1E")
        self.pack_propagate(0)
        self.banco = controller.banco
        self.correta = " "
        self.dificuldade = " "
        self.materias=[]
        self.mostrar_materias()
        self.criar_tela()
        self.materia_escolhida = " "
        self.disciplina_filtrada = ""
        self.dificuldade_filtrada = ""
        self.mostrar_dados()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, uniform="grupo")
        self.grid_columnconfigure(1, weight=1, uniform="grupo")
        

    def criar_tela(self):
        self.left_frame = CTkFrame(self, fg_color="#1E1E1E")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(2, weight=1)

        self.right_frame = CTkFrame(self, fg_color="#1E1E1E", corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        CTkButton(self.left_frame, text="<<<<", height=35, width=70, fg_color="#D22D23", hover_color="#942019", border_width=3, border_color= "#DB453D", font=("courier new", 18, "bold"), command= lambda: self.controller.show_frame(CentralProfessor)).place(x=10, y=10)

        self.frame_disciplinas = CTkFrame(self.left_frame, fg_color="transparent", corner_radius=11, height=100,  border_width=2, border_color="#B5C6D0")
        self.frame_disciplinas.grid(row = 0, column = 0, padx=20, pady=(60,3), sticky="ew")
        self.frame_disciplinas.grid_columnconfigure(1, weight=1)

        CTkLabel(self.frame_disciplinas, text="Nova disciplina:", font=("courier new",18,"bold"),text_color="#ffffff").grid(row=0, column=0, padx=(10,4),pady=5)

        self.input_nova_disciplina = CTkEntry(self.frame_disciplinas, height=35, fg_color="#3B5055", font=("courier new",14,"bold"), border_width=2, border_color="#B5C6D0",text_color="#ffffff")
        self.input_nova_disciplina.grid(row=0, column = 1, padx=5, pady=5, sticky="ew")

        self.cadastrar_disciplina = CTkButton(self.frame_disciplinas, text="ADD", height=35, width=50, font=("courier new",14,"bold"), fg_color="#25734D", hover_color="#14402b", command=self.adicionar_materia)
        self.cadastrar_disciplina.grid(row = 0, column = 2, pady=5, padx=6)

        CTkLabel(self.left_frame, text="Pergunta:", font=("courier new", 18, "bold"),text_color="#ffffff").grid(row=1, column=0, sticky="w", padx=20, pady=(7, 0))
        self.input_pergunta = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_pergunta.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa A:", font=("courier new", 18, "bold"),text_color="#ffffff").grid(row=3, column=0, sticky="w", padx=20, pady=(7, 0))
        self.input_alt_a = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_a.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa B:", font=("courier new", 18, "bold"),text_color="#ffffff").grid(row=5, column=0, sticky="w", padx=20, pady=(7, 0))
        self.input_alt_b = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_b.grid(row=6, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa C:", font=("courier new", 18, "bold"),text_color="#ffffff").grid(row=7, column=0, sticky="w", padx=20, pady=(7, 0))
        self.input_alt_c = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_c.grid(row=8, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa D:", font=("courier new", 18, "bold"),text_color="#ffffff").grid(row=9, column=0, sticky="w", padx=20, pady=(7, 0))
        self.input_alt_d = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_d.grid(row=10, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Dica:", font=("courier new", 18, "bold"),text_color="#ffffff").grid(row=11, column=0, sticky="w", padx=20, pady=(7, 0))
        self.input_dica = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_dica.grid(row=12, column=0, padx=20, pady=5, sticky="ew")

        self.options_frame = CTkFrame(self.left_frame, fg_color="transparent")
        self.options_frame.grid(row=13, column=0, padx=20, pady=5, sticky="w")

        self.input_dificuldade = CTkOptionMenu(self.options_frame, values=["Fácil", "Médio", "Difícil"], command=self.mostrar_dificuldade, font=("courier new", 16, "bold"), height=32,  text_color="#ffffff", fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700")
        self.input_dificuldade.set("Dificuldade..")
        self.input_dificuldade.grid(row=0, column=0, padx=10, pady=10)

        self.input_correta = CTkOptionMenu(self.options_frame, values=["A", "B", "C", "D"], command=self.mostrar_correta, font= ("courier new", 16, "bold"), height=32,fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700")
        self.input_correta.set("Correta..")
        self.input_correta.grid(row=0, column=1, padx=10, pady=10)

        self.input_materia = CTkOptionMenu(self.options_frame, values=self.materias, command=self.mostrar_materia, font=("courier new", 16, "bold"), height=32, fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700")
        self.input_materia.set("Disciplina..")
        self.input_materia.grid(row=0, column=2, padx=10, pady=10)


        CTkButton(self.left_frame, text="ADICIONAR", command=self.cadastrar_pergunta, font=("courier new", 18, "bold"), height=65, fg_color="#25734D", hover_color="#14402b",corner_radius=11, border_color="#34A16D", border_width=3 ).grid(row=14, column=0, padx=20, pady=10, sticky="ew"); 

        self.frame_filtros = CTkFrame(self.right_frame, fg_color= "transparent", corner_radius=0)
        self.frame_filtros.grid(row=0, column=0,padx=5, pady=25)

        CTkLabel(self.frame_filtros, text="Filtrar: ", font=("courier new", 16,"bold"),text_color="#ffffff").grid(row=0, column=0, padx=6, pady=5)

        self.filtro_disciplina = CTkOptionMenu(self.frame_filtros,values=self.materias+ ["Todas"],font=("courier new",14,"bold"), text_color="#ffffff", fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700", command=self.filtro_disciplina)
        self.filtro_disciplina.set("Disciplina")
        self.filtro_disciplina.grid(row=0, column=1, padx=6, pady=5)

        self.filtro_dificuldade=CTkOptionMenu(self.frame_filtros, values=["Fácil","Média","Difícil","Todas"], font=("courier new", 14,"bold"), text_color="#ffffff", fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700", command=self.filtro_dificuldade)
        self.filtro_dificuldade.set("Dificuldade")
        self.filtro_dificuldade.grid(row=0, column=2, padx=6, pady=5)

        self.btn_filtrar=CTkButton(self.frame_filtros, text="FILTRAR", font=("courier new",14,"bold"), fg_color="#FF9700", hover_color="#c27402", border_color="#FFBB00", border_width=3, command=self.filtrar_pergunta)
        self.btn_filtrar.grid(row=0, column=3, padx=6, pady=5)


        colunas = ("ID", "Pergunta", "A", "B", "C", "D", "Dificuldade", "Correta", "Dica", "Disciplina")

        self.tree = ttk.Treeview(self.right_frame, columns=colunas, show="headings")
        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.grid(row=1, column=0, sticky="nsew")

        scrollbar_y = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=1, column=1, sticky="ns")

        scrollbar_x = ttk.Scrollbar(self.right_frame, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=2, column=0, sticky="ew")

        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        CTkButton(self.right_frame, text="DELETAR", command=self.deletar_dados, fg_color="#D22D23",hover_color="#942019", corner_radius=11, border_color="#DB453D", border_width=3 , height=65, font=("courier new", 18, "bold")).grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")
  
    def mostrar_dados(self):
        try:
            # Limpar a treeview antes de adicionar novos dados
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            self.registros = self.banco.carregar_dados()

            for linha in self.registros:
                linha_limpa = tuple(str(item).strip("(),'\"") for item in linha)
                self.tree.insert("", "end", values=linha_limpa)
        except Exception as e:
            print("Erro ao carregar dados:", e)

    def mostrar_materias(self):
        try:
            self.materias_tuple = self.banco.carregar_materias() 
            for materia in self.materias_tuple:
                self.materias.append(materia[0])
            print(self.materias)
        except Exception as e:
            print("Erro ao carregar materias")

    def deletar_dados(self):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            msgbox.showwarning("Aviso", "Nenhuma pergunta selecionada!")
            return
            
        valores_selecionados = self.tree.item(item_selecionado)['values']
        id_pergunta = valores_selecionados[0]
        
        # Confirmar antes de deletar
        if msgbox.askyesno("Confirmar", "Tem certeza que deseja deletar esta pergunta?"):
            # Remove da interface
            self.tree.delete(item_selecionado)
            
            # Chama a deleção no banco
            self.banco.deletar_pergunta(id_pergunta)
            
            # Atualiza os dados
            self.mostrar_dados()

    def mostrar_dificuldade(self, dificuldade):
        self.dificuldade = {"Fácil": "F", "Médio": "M", "Difícil": "D"}.get(dificuldade, " ")

    def mostrar_materia(self,materia):
        self.materia = materia
        print(self.materia)

    def mostrar_correta(self, alternativa):
        alternativas = {
            "A": self.input_alt_a.get(),
            "B": self.input_alt_b.get(),
            "C": self.input_alt_c.get(),
            "D": self.input_alt_d.get()
        }
        self.correta = alternativas.get(alternativa, " ")

    def filtro_disciplina(self, disciplina_filtrada):
        self.disciplina_filtrada = disciplina_filtrada
        print(self.disciplina_filtrada)

    def filtro_dificuldade(self, dificuldade_filtrada):
        if dificuldade_filtrada == "Fácil":
            self.dificuldade_filtrada = "F"
        elif dificuldade_filtrada == "Média":
            self.dificuldade_filtrada = "M"
        elif dificuldade_filtrada == "Difícil":
            self.dificuldade_filtrada = "D"
        elif dificuldade_filtrada == "Todas":
            self.dificuldade_filtrada= "Todas"
        else:
            self.dificuldade_filtrada = ""
        print(self.dificuldade_filtrada)

    def filtrar_pergunta(self):
        if self.disciplina_filtrada == "" and self.dificuldade_filtrada == "":
            msgbox.showerror("Erro", "Selecione pelo menos um filtro")
        elif self.disciplina_filtrada == "Todas" and self.dificuldade_filtrada == "Todas":
            try:
                # Limpar a treeview antes de adicionar novos dados
                for item in self.tree.get_children():
                    self.tree.delete(item)
                    
                self.registros = self.banco.carregar_dados()

                for linha in self.registros:
                    linha_limpa = tuple(str(item).strip("(),'\"") for item in linha)
                    self.tree.insert("", "end", values=linha_limpa)
            except Exception as e:
                print("Erro ao carregar dados:", e)

        else: 
            try:
                # Limpar a treeview antes de adicionar novos dados
                for item in self.tree.get_children():
                    self.tree.delete(item)
                    
                self.registros = self.banco.filtrar_perguntas(self.disciplina_filtrada,self.dificuldade_filtrada)

                for linha in self.registros:
                    linha_limpa = tuple(str(item).strip("(),'\"") for item in linha)
                    self.tree.insert("", "end", values=linha_limpa)
            except Exception as e:
                print("Erro ao carregar dados:", e)

    def cadastrar_pergunta(self):
        pergunta = self.input_pergunta.get()
        alt_a = self.input_alt_a.get()
        alt_b = self.input_alt_b.get()
        alt_c = self.input_alt_c.get()
        alt_d = self.input_alt_d.get()
        dica = self.input_dica.get()
        
        
        if not all([pergunta, alt_a, alt_b, alt_c, alt_d, dica]) or self.dificuldade == " " or self.correta == " " or self.materia == " ":
            msgbox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
            
        try:
            self.banco.cadastrar_pergunta(pergunta, alt_a, alt_b, alt_c, alt_d, dica, self.dificuldade, self.correta, self.materia)
            msgbox.showinfo("Sucesso", "Pergunta cadastrada com sucesso!")
            
            # Limpar campos após cadastro
            self.input_pergunta.delete(0, 'end')
            self.input_alt_a.delete(0, 'end')
            self.input_alt_b.delete(0, 'end')
            self.input_alt_c.delete(0, 'end')
            self.input_alt_d.delete(0, 'end')
            self.input_dica.delete(0, 'end')
            self.input_dificuldade.set("---")
            self.input_correta.set("---")
            self.input_materia.set("---")
            self.dificuldade = " "
            self.correta = " "
            self.materia = " "
            
            # Atualizar a lista de perguntas
            self.mostrar_dados()

    
        except Exception as e:
            msgbox.showerror("Erro", f"Erro ao cadastrar pergunta:\n{e}")

    def adicionar_materia(self):
        if self.input_nova_disciplina.get() == "":
            msgbox.showerror("Erro", "Digite alguma disciplina para cadastro!")
        else:
            self.controller.banco.cadastrar_materia(self.input_nova_disciplina.get())

    

if __name__ == "__main__":
    app = App()
    app.mainloop()