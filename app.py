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
        print('Conectado com sucesso')

    def inserir_perguntas_geog(self):
        try:
            comandos = [
                # FÁCEIS (F)
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é o maior oceano do mundo?', 'Atlântico', 'Índico', 'Ártico', 'Pacífico', 'Pacífico', 'É o maior e mais profundo oceano.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é o rio mais extenso do mundo?', 'Nilo', 'Amazonas', 'Yangtzé', 'Mississippi', 'Amazonas', 'Está na América do Sul.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é o continente com mais países?', 'Ásia', 'África', 'Europa', 'América', 'África', 'Tem mais de 50 países.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é a capital do Brasil?', 'São Paulo', 'Brasília', 'Rio de Janeiro', 'Salvador', 'Brasília', 'Foi inaugurada em 1960.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é o país com maior população?', 'Índia', 'Estados Unidos', 'China', 'Indonésia', 'China', 'Está na Ásia.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é o menor continente do mundo?', 'Europa', 'Austrália', 'Antártida', 'América do Sul', 'Austrália', 'É também um país.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é o deserto mais seco do mundo?', 'Saara', 'Atacama', 'Kalahari', 'Gobi', 'Atacama', 'Fica na América do Sul.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é a capital da França?', 'Paris', 'Londres', 'Berlim', 'Roma', 'Paris', 'É conhecida como cidade luz.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é o maior país do mundo em área territorial?', 'Canadá', 'Estados Unidos', 'China', 'Rússia', 'Rússia', 'Está na Europa e Ásia.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é a montanha mais alta do mundo?', 'Everest', 'K2', 'Makalu', 'Annapurna', 'Everest', 'Fica no Himalaia.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual oceano banha o litoral leste do Brasil?', 'Atlântico', 'Índico', 'Pacífico', 'Ártico', 'Atlântico', 'É o segundo maior oceano.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual país tem o formato de uma bota?', 'França', 'Itália', 'Grécia', 'Alemanha', 'Itália', 'Fica no sul da Europa.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'O que é uma ilha?', 'Montanha', 'Área deserta', 'Área cercada por água', 'Floresta', 'Área cercada por água', 'É cercada por água por todos os lados.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual é a capital da Argentina?', 'Lima', 'Santiago', 'Buenos Aires', 'Montevidéu', 'Buenos Aires', 'Fica às margens do Rio da Prata.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('F', 'Qual país é conhecido por suas pirâmides?', 'Grécia', 'Índia', 'Egito', 'México', 'Egito', 'Fica no nordeste da África.', 'GEOG')''',

                # MÉDIAS (M)
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual é o maior arquipélago do mundo?', 'Filipinas', 'Indonésia', 'Maldivas', 'Japão', 'Indonésia', 'É um país asiático com milhares de ilhas.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Onde fica a nascente do Rio Amazonas?', 'Brasil', 'Colômbia', 'Peru', 'Venezuela', 'Peru', 'Está nos Andes peruanos.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual é o ponto mais alto do Brasil?', 'Pico da Neblina', 'Pico das Agulhas Negras', 'Pico Paraná', 'Monte Roraima', 'Pico da Neblina', 'Está no estado do Amazonas.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual é o maior deserto do mundo em extensão?', 'Saara', 'Atacama', 'Gobi', 'Antártida', 'Antártida', 'É gelado e não arenoso.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual bioma domina o centro-oeste do Brasil?', 'Mata Atlântica', 'Pantanal', 'Cerrado', 'Caatinga', 'Cerrado', 'É típico de clima tropical sazonal.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Quantos fusos horários existem no Brasil atualmente?', '3', '4', '5', '2', '4', 'Houve uma mudança recente por decreto.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual é a capital mais ao sul do Brasil?', 'Curitiba', 'Florianópolis', 'Porto Alegre', 'Campo Grande', 'Porto Alegre', 'Fica no Rio Grande do Sul.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'O que é uma foz deltaica?', 'Saída subterrânea do rio', 'Ramificação de canais na foz', 'Encontro de dois rios', 'Foz em desnível', 'Ramificação de canais na foz', 'Forma um leque na foz do rio.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual é o principal rio da região Sudeste do Brasil?', 'Rio São Francisco', 'Rio Doce', 'Rio Paraná', 'Rio Tietê', 'Rio Paraná', 'Passa por São Paulo e deságua no Prata.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual país tem fronteira com todos os outros da América do Sul, exceto Chile e Equador?', 'Peru', 'Brasil', 'Colômbia', 'Argentina', 'Brasil', 'É o maior da América do Sul.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'O que é uma cordilheira?', 'Lago extenso', 'Planície', 'Conjunto de montanhas', 'Deserto', 'Conjunto de montanhas', 'Forma grandes cadeias montanhosas.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual é a principal corrente marítima fria que afeta o clima do Chile?', 'El Niño', 'Corrente de Humboldt', 'Golfo do México', 'Corrente de Benguela', 'Corrente de Humboldt', 'Vem do Pacífico Sul.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'O que significa latitude?', 'Distância em metros', 'Altura da montanha', 'Distância ao norte ou sul do Equador', 'Distância ao leste', 'Distância ao norte ou sul do Equador', 'Usada para localizar pontos na Terra.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Qual o nome da linha imaginária que divide a Terra ao meio?', 'Trópico de Câncer', 'Meridiano de Greenwich', 'Equador', 'Trópico de Capricórnio', 'Equador', 'Divide hemisfério norte e sul.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('M', 'Quais países fazem parte do Magreb?', 'Egito, Etiópia, Sudão', 'Marrocos, Argélia, Tunísia', 'África do Sul, Namíbia, Angola', 'Níger, Chade, Mali', 'Marrocos, Argélia, Tunísia', 'Estão no norte da África.', 'GEOG')''',

                # DIFÍCEIS (D)
                    # DIFÍCEIS (D)
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'O que é um estuário?', 'Área montanhosa', 'Deserto costeiro', 'Foz em forma de funil de rio', 'Planície tropical', 'Foz em forma de funil de rio', 'Forma-se onde há marés fortes.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual cidade é atravessada pela linha do Equador no Brasil?', 'Belém', 'Boa Vista', 'Macapá', 'Palmas', 'Macapá', 'Está no estado do Amapá.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'O que é a tectônica de placas?', 'Teoria sobre a origem do universo', 'Movimento dos ventos', 'Movimento das placas litosféricas', 'Ciclo da água', 'Movimento das placas litosféricas', 'Explica terremotos e vulcões.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual país possui mais vulcões ativos no mundo?', 'Indonésia', 'Japão', 'Itália', 'Chile', 'Indonésia', 'É um arquipélago no Pacífico.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual cidade está localizada em dois continentes?', 'Moscou', 'Istambul', 'Tóquio', 'Cairo', 'Istambul', 'Fica entre Europa e Ásia.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'O que são dorsais oceânicas?', 'Cordilheiras submarinas', 'Rios profundos', 'Fendas tectônicas', 'Corais gigantes', 'Cordilheiras submarinas', 'Formadas por placas divergentes.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual é o maior aquífero do mundo em volume de água?', 'Guarani', 'Alter do Chão', 'Ogallala', 'Sáhara', 'Alter do Chão', 'Está localizado na região amazônica.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual é a capital mais alta do mundo?', 'Quito', 'La Paz', 'Bogotá', 'Kathmandu', 'La Paz', 'Fica na Bolívia, nos Andes.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual país tem o maior número de fronteiras com outros países?', 'Rússia', 'Brasil', 'Alemanha', 'China', 'China', 'Tem fronteira com 14 países.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'O que é o Anel de Fogo do Pacífico?', 'Corrente oceânica', 'Região de ciclones', 'Área de intensa atividade vulcânica e sísmica', 'Zona de clima árido', 'Área de intensa atividade vulcânica e sísmica', 'Cerca todo o oceano Pacífico.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual fenômeno natural causa tsunamis?', 'Ciclones', 'Erupções vulcânicas', 'Terremotos submarinos', 'Erosão costeira', 'Terremotos submarinos', 'Acontece sob o oceano.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual é o maior delta fluvial do mundo?', 'Delta do Mekong', 'Delta do Nilo', 'Delta do Amazonas', 'Delta do Ganges', 'Delta do Ganges', 'Fica na Índia e Bangladesh.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'O que é um talude continental?', 'Montanha oceânica', 'Zona de transição entre plataforma e fundo oceânico', 'Depressão tectônica', 'Plataforma de coral', 'Zona de transição entre plataforma e fundo oceânico', 'Faz parte da margem continental.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'O que caracteriza o clima mediterrâneo?', 'Chuvas o ano todo', 'Verões secos e invernos chuvosos', 'Invernos rigorosos', 'Alta umidade', 'Verões secos e invernos chuvosos', 'Típico do sul da Europa.', 'GEOG')''',
                '''INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia)
                VALUES ('D', 'Qual o nome da região do Sahel?', 'Floresta equatorial', 'Zona de transição entre deserto e savana', 'Área de monções', 'Pântano africano', 'Zona de transição entre deserto e savana', 'Fica ao sul do Saara.', 'GEOG')'''

            ]
            for sql in comandos:
                self.cursor.execute(sql)

            self.conexao.commit()
            print("Todas as perguntas foram inseridas com sucesso!")

        except Exception as e:
            print(f"Erro ao inserir perguntas: {e}")
   

    def login_usuario(self, email, senha):
        self.cursor.execute('SELECT * FROM Usuario WHERE email = ? AND senha = ?', (email, senha))
        return self.cursor.fetchall()

    def cadastrar_usuario(self, nome, email, senha, turma, professor):
        self.cursor.execute('INSERT INTO Usuario (nome,email,senha,turma,professor) VALUES (?,?,?,?,?)', (nome, email, senha,turma,professor))
        self.conexao.commit()
        print("Cadastro Realizado com sucesso!")
    
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

    def deletar_pergunta(self, id):
        try:
            self.cursor.execute('DELETE FROM Pergunta WHERE id = ?', (id,))
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
        for F in (Login, MateriasJogo,MateriasProfessor, Menu, MenuProfessor, Perguntas, PerguntasProfessor, Cadastro, CentralProfessor, Jogadores):
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
            else:
                self.controller.show_frame(Menu)
        else:
            msgbox.showerror("Erro", "Email ou senha incorretos.")
    
    
    #def cadastrar_geog(self):
        #self.controller.banco.inserir_perguntas_geog()


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
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)  # 4 colunas para os botões

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

        CTkButton(self, height=300, width=200, text="DISCIPLINAS", fg_color="#FF9700",
                  text_color="#ffffff", font=("courier new",22,"bold"),
                  command=lambda: self.controller.show_frame(MateriasProfessor), bg_color="#245d4a", corner_radius=11, hover_color="#c27402", border_color="#FFBB00", border_width=3,  image=img_disciplinas, compound="top").grid(row=1, column=2, padx=15, pady=10)

        CTkButton(self, height=300, width=200, text="INSTRUÇÕES", fg_color="#FF9700",
                  text_color="#ffffff", font=("courier new",22,"bold"), bg_color="#245d4a", corner_radius=11, hover_color="#c27402", border_color="#FFBB00", border_width=3,  image=img_instrucoes, compound="top").grid(row=1, column=3, padx=15, pady=10)

    def redimensionar_imagem(self, event):
        nova_img = self.original_image.resize((event.width, event.height), Resampling.LANCZOS)
        self.background_image = CTkImage(light_image=nova_img, size=(event.width, event.height))
        self.bg_label.configure(image=self.background_image)





class Jogadores(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.criar_tela()
        self.banco = controller.banco
        self.mostrar_dados()

    def criar_tela(self):
        self.left_frame = CTkFrame(self, width=800, height=750, fg_color="#333", corner_radius=0)
        self.left_frame.pack_propagate(0)
        self.left_frame.pack(side="left", fill="both")

        self.right_frame = CTkFrame(self,width=400, height=750, fg_color="#555", corner_radius=0)
        self.right_frame.pack_propagate(0)
        self.right_frame.pack(side="right", fill="both")

        scrollbar_y = ttk.Scrollbar(self.left_frame, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = ttk.Scrollbar(self.left_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        colunas = ("ID","Nome","Email", "Turma", "Professor")

        self.tree = ttk.Treeview(
            self.left_frame,
            columns=colunas,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )
        self.tree.pack(fill="both", expand=True, padx=(40,40), pady=(40,10))

        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")


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
        

class MateriasJogo(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.banco = controller.banco
        self.materias = []
        self.mostrar_materias()
        self.materia = " "
        self.fonte = ("fixedsys",22,"bold")
        self.criar_tela()
    
    def criar_tela(self):

        self.btn_voltar = CTkButton(master=self,text="Voltar",width=100,height=50, font=self.fonte, command=lambda: self.controller.show_frame(MenuProfessor))
        self.btn_voltar.grid(column=0,row=0,padx=(15,0),pady=(10,0))

        CTkLabel(master=self, text="Escolha a matéria para o seu jogo: ", font=("fixedsys",22,"bold")).grid(column=0,row=1,padx=400,pady=(300,30))

        self.input_materia_jogo = CTkOptionMenu(self, values=self.materias, font=("fixedsys",22,"bold"),command=self.mostrar_materia)
        self.input_materia_jogo.grid(column=0,row=2,padx=(400,10),pady=10)

        self.confirmar_materia = CTkButton(self,text="Confirmar Matéria", font=("courier new",14,"bold"), command=self.atualizar_materia_atual)
        self.confirmar_materia.grid(column = 0, row = 3, padx=100, pady=10)

        self.btn_iniciar_jogo = CTkButton(master=self, text="Iniciar", font=("fixedsys",22,"bold"),width=300,height=100,command=lambda: self.controller.show_frame(Perguntas))
        self.btn_iniciar_jogo.grid(column=0,row=4,padx=10,pady=10)

    
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
        
        

class MateriasProfessor(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.criar_tela()
        self.mostrar_materias_perguntas()
    
    def criar_tela(self):
        
        

        self.left_frame = CTkFrame(self, width=800, height=750, fg_color="#333", corner_radius=0)
        self.left_frame.pack_propagate(0)
        self.left_frame.pack(side="left", fill="both")

        self.right_frame = CTkFrame(self,width=400, height=750, fg_color="#555", corner_radius=0)
        self.right_frame.pack_propagate(0)
        self.right_frame.pack(side="right", fill="both")

        self.btn_cadastrar_materia = CTkButton(self.right_frame, text="Cadastrar matéria",width=200, fg_color="#E44982", command=self.adicionar_matéria)
        self.btn_cadastrar_materia.pack()

        self.texto_materia = CTkLabel(self.right_frame, text="Insira a nova matéria: ", text_color="#000")
        self.texto_materia.pack(side="right",fill="both",padx=50,pady=2)

        self.materia = CTkEntry(self.right_frame, width=150, height= 25, fg_color="#ffffff")
        self.materia.pack(side="right", padx=10,pady=2)
        
        

        scrollbar_y = ttk.Scrollbar(self.left_frame, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = ttk.Scrollbar(self.left_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        colunas = ("ID","Materia(s)", "Número de Perguntas")

        self.tree = ttk.Treeview(
            self.left_frame,
            columns=colunas,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )
        self.tree.pack(fill="both", expand=True, padx=(40,40), pady=(40,10))

        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

    def mostrar_materias_perguntas(self):
        for sigla, qtd in self.controller.banco.carregar_materias_perguntas():
            self.tree.insert("", "end", values=(sigla, qtd))

    def adicionar_matéria(self):
        if self.materia.get() == "":
            msgbox.showerror("Erro", "Digite alguma matéria para cadastro!")
        else:
            self.controller.banco.cadastrar_materia(self.materia.get())


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
        self.pontuacao = 0  # Inicia com 0 pontos
        self.checkpoint_atingido = False  # Flag para verificar se atingiu checkpoint
        self.materia_selecionada = None
        self.tempo_inicio = time.time()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

        self.criar_tela()

        print(self.materia_atual)

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

        self.perguntas = self.perguntas_faceis[0:1] + self.perguntas_medias[0:1] + self.perguntas_dificeis[0:1]
        
        cursor.close()
        conexao.close()

        return self.perguntas

    def criar_tela(self):
        self.left_frame = CTkFrame(self, fg_color="#3B3B3B", corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_propagate(False)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=4)  # dá mais espaço para os botões
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

        # Novo frame apenas para os botões
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

    
    def carregar_pergunta(self):
        # Esconde a tela de game over se estiver visível
        self.game_over_frame.pack_forget()
        
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
        pergunta_atual = self.perguntas[self.indice_pergunta]
        alternativa_selecionada = self.botoes_alternativas[indice].cget("text")
        
        if alternativa_selecionada == pergunta_atual["correta"]:
            self.botoes_alternativas[indice].configure(fg_color="#25734D", border_color="#34A16D")
            self.pontuacao = self.pontos[self.i_pontos]
            self.i_pontos += 1
            self.botão_pontuação.configure(text=f"Prêmio: R$ {self.pontuacao}")
            
            # Desabilitar todos os botões após resposta correta
            for botao in self.botoes_alternativas:
                botao.configure(state="disabled")
            
            # Verificar se atingiu checkpoint (10000 ou 150000 pontos)
            if self.pontuacao in [10000, 150000]:
                self.checkpoint_atingido = True
            
            self.indice_pergunta += 1
            self.after(1000, self.carregar_pergunta)
        else:
            self.botoes_alternativas[indice].configure(fg_color="#D22D23",border_color="#DB453D" )
            
            # Verificar se tem checkpoint para usar
            if self.checkpoint_atingido:
                self.checkpoint_atingido = False
                self.label_feedback.configure(text="Você errou, mas usou seu checkpoint! Continue jogando.", text_color="#F39C12")
                self.after(1000, self.carregar_pergunta)
            else:
                # Mostrar tela de jogo encerrado
                for botao in self.botoes_alternativas:
                    botao.configure(state="disabled")
                
                self.botao_ajuda_dica.configure(state="disabled")
                self.botao_ajuda_50.configure(state="disabled")
                self.botao_ajuda_pular.configure(state="disabled")
                
                self.mostrar_janela_fim_jogo()

    
    def mostrar_janela_fim_jogo(self):
        janela = CTkToplevel(self)
        janela.title("Fim de Jogo")
        janela.geometry("400x250")
        janela.grab_set()
        
        # Centraliza a janela imediatamente após criação
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
        self.botao_ajuda_dica.configure(state="able", fg_color="#25734D")
        self.botao_ajuda_50.configure(state="able", fg_color="#25734D")
        self.botao_ajuda_pular.configure(state="able", fg_color="#25734D")
        self.i_pontos = 0
        self.pontuacao = 0
        self.checkpoint_atingido = False

        for i, botao in enumerate(self.botoes_alternativas):
            botao.grid(row=i, column=0, sticky="nsew", pady=(10 if i > 0 else 0, 0))  


        self.botão_pontuação.configure(text="Prêmio: R$ 0")
        self.carregar_pergunta()

    def mostrar_janela_jogo_concluido(self):
        janela = CTkToplevel(self)
        janela.title("Fim de Jogo")
        janela.geometry("400x250")
        janela.grab_set()
        
        # Centraliza a janela imediatamente após criação
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
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        CTkButton(self.left_frame, text="<<<<", height=35, width=70, fg_color="#D22D23", hover_color="#942019", border_width=3, border_color= "#DB453D", font=("courier new", 18, "bold"), command= lambda: self.controller.show_frame(CentralProfessor)).place(x=20, y=20)

        CTkLabel(self.left_frame, text="Pergunta:", font=("courier new", 18, "bold")).grid(row=0, column=0, sticky="w", padx=20, pady=(75, 0))
        self.input_pergunta = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_pergunta.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa A:", font=("courier new", 18, "bold")).grid(row=2, column=0, sticky="w", padx=20, pady=(10, 0))
        self.input_alt_a = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_a.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa B:", font=("courier new", 18, "bold")).grid(row=4, column=0, sticky="w", padx=20, pady=(10, 0))
        self.input_alt_b = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_b.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa C:", font=("courier new", 18, "bold")).grid(row=6, column=0, sticky="w", padx=20, pady=(10, 0))
        self.input_alt_c = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_c.grid(row=7, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Alternativa D:", font=("courier new", 18, "bold")).grid(row=8, column=0, sticky="w", padx=20, pady=(10, 0))
        self.input_alt_d = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_alt_d.grid(row=9, column=0, padx=20, pady=5, sticky="ew")

        CTkLabel(self.left_frame, text="Dica:", font=("courier new", 18, "bold")).grid(row=10, column=0, sticky="w", padx=20, pady=(10, 0))
        self.input_dica = CTkEntry(self.left_frame, font=("courier new", 14, "bold"), height=37, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff")
        self.input_dica.grid(row=11, column=0, padx=20, pady=5, sticky="ew")

        self.options_frame = CTkFrame(self.left_frame, fg_color="transparent")
        self.options_frame.grid(row=12, column=0, padx=20, pady=5, sticky="w")

        self.input_dificuldade = CTkOptionMenu(self.options_frame, values=["Fácil", "Médio", "Difícil"], command=self.mostrar_dificuldade, font=("courier new", 16, "bold"), height=32,  text_color="#ffffff", fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700")
        self.input_dificuldade.set("Dificuldade..")
        self.input_dificuldade.grid(row=0, column=0, padx=10, pady=15)

        self.input_correta = CTkOptionMenu(self.options_frame, values=["A", "B", "C", "D"], command=self.mostrar_correta, font= ("courier new", 16, "bold"), height=32,fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700")
        self.input_correta.set("Correta..")
        self.input_correta.grid(row=0, column=1, padx=10, pady=15)

        self.input_materia = CTkOptionMenu(self.options_frame, values=self.materias, command=self.mostrar_materia, font=("courier new", 16, "bold"), height=32, fg_color="#3B5055",button_color="#3B5055",button_hover_color="#FF9700")
        self.input_materia.set("Disciplina..")
        self.input_materia.grid(row=0, column=2, padx=10, pady=15)


        CTkButton(self.left_frame, text="ADICIONAR", command=self.cadastrar_pergunta, font=("courier new", 18, "bold"), height=65, fg_color="#25734D", hover_color="#14402b",corner_radius=11, border_color="#34A16D", border_width=3 ).grid(row=13, column=0, padx=20, pady=10, sticky="ew"); 


        colunas = ("ID", "Pergunta", "A", "B", "C", "D", "Dificuldade", "Correta", "Dica", "Disciplina")

        self.tree = ttk.Treeview(self.right_frame, columns=colunas, show="headings")
        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar_y = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        scrollbar_x = ttk.Scrollbar(self.right_frame, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=1, column=0, sticky="ew")

        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        CTkButton(self.right_frame, text="DELETAR", command=self.deletar_dados, fg_color="#D22D23",hover_color="#942019", corner_radius=11, border_color="#DB453D", border_width=3 , height=65, font=("courier new", 18, "bold")).grid(row=2, column=0, columnspan=2, pady=15, sticky="ew")
  
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

    


if __name__ == "__main__":
    app = App()
    app.mainloop()