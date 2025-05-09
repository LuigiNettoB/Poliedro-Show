from customtkinter import *
from PIL import Image
import sqlite3
import tkinter as tk
import random
import tkinter.messagebox as msgbox
import threading
import tkinter.ttk as ttk

class BancoDeDados:
    def __init__(self, db_file):
        self.dados_conexao = "PI.db"
        self.conexao = sqlite3.connect(self.dados_conexao)
        self.cursor = self.conexao.cursor()
        print('Conectado com sucesso')

    def login_usuario(self, email, senha):
        self.cursor.execute('SELECT * FROM Usuario WHERE email = ? AND senha = ?', (email, senha))
        return self.cursor.fetchall()

    def cadastrar_usuario(self, nome, email, senha):
        self.cursor.execute('INSERT INTO Usuario (nome,email,senha) VALUES (?,?,?)', (nome, email, senha))
        self.conexao.commit()
        print("Cadastro Realizado com sucesso!")
    
    def carregar_dados(self):
        self.cursor.execute("SELECT id, pergunta, altA, altB, altC, altD, dificuldade, correta, dica, materia FROM Pergunta")
        return self.cursor.fetchall()
    
    def carregar_jogadores(self):
        self.cursor.execute("SELECT id, nome, email, turma, professor FROM Usuario")
        return self.cursor.fetchall()

    def carregar_materias(self):
        self.cursor.execute("SELECT sigla FROM Materia")
        return self.cursor.fetchall()

    def cadastrar_pergunta(self, pergunta, alt_a, alt_b, alt_c, alt_d, dica, dificuldade, correta,materia):
        def inserir_no_banco():
            try:
                self.cursor.execute('''
                    INSERT INTO Pergunta (dificuldade, pergunta, altA, altB, altC, altD, correta, dica, materia) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (dificuldade, pergunta, alt_a, alt_b, alt_c, alt_d, correta, dica, materia))
                self.conexao.commit()
                print("Cadastro realizado com sucesso!")
            except Exception as e:
                print(f"Erro: {e}")

        threading.Thread(target=inserir_no_banco, daemon=True).start()

    def deletar_pergunta(self, id):
        def deletar_no_banco():
            try:
                self.cursor.execute('DELETE FROM Pergunta WHERE id = ?', (id,))
                self.conexao.commit()
                print("Deletado com sucesso")
            except Exception as e:
                print(f"Erro: {e}")

        threading.Thread(target=deletar_no_banco, daemon=True).start()

class App(CTk):
    def __init__(self):
        super().__init__()
        self.banco = BancoDeDados("PI.db")
        self.title("Show Do Milhão")
        self.geometry("1200x780")
        self.center_window(1200, 780)
        
        # Container principal para os frames
        self.container = CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Criar todos os frames
        for F in (Login, Materias, Menu, MenuProfessor, Perguntas, PerguntasProfessor, Cadastro, CentralProfessor, Jogadores):
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
                                   width=35, text="", fg_color="#3B5055", hover_color="#2F3E43", corner_radius=8, command=self.toggle_senha)
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
            self.controller.show_frame(MenuProfessor)
        else:
            msgbox.showerror("Erro", "Email ou senha incorretos.")



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

        self.criar_tela()

    def criar_tela(self):
        name_icon = CTkImage(dark_image=Image.open("imagens/user.png"),
                             light_image=Image.open("imagens/user.png"), size=(17, 17))
        email_icon = CTkImage(dark_image=Image.open("imagens/email-icon.png"),
                              light_image=Image.open("imagens/email-icon.png"), size=(20, 20))
        password_icon = CTkImage(dark_image=Image.open("imagens/password-icon.png"),
                                 light_image=Image.open("imagens/password-icon.png"), size=(17, 17))
        signin_icon = CTkImage(dark_image=Image.open("imagens/signin.png"),
                               light_image=Image.open("imagens/signin.png"), size=(17, 17))

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
                 font=("fixedsys", 28, "bold")).grid(row=0, column=0, sticky="w", pady=(50, 5))
        CTkLabel(self.right_frame, text="Crie sua conta", text_color="#ffffff",
                 font=("fixedsys", 16,"bold")).grid(row=1, column=0, sticky="w", pady=(0, 20))

        # Nome
        CTkLabel(self.right_frame, text="  Nome Completo:", text_color="#ffffff", image=name_icon,
                 compound="left", font=("fixedsys", 14, "bold")).grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.nome_completo = CTkEntry(self.right_frame, fg_color="#3B5055", border_color="#B5C6D0",
                                      border_width=2, text_color="#ffffff", height=35,font=("fixedsys",14))
        self.nome_completo.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        # Turma
        CTkLabel(self.right_frame, text="  Turma:", text_color="#ffffff", image=name_icon,
                 compound="left", font=("fixedsys", 14, "bold")).grid(row=4, column=0, sticky="w", pady=(0, 5))
        self.turma = CTkEntry(self.right_frame, fg_color="#3B5055", border_color="#B5C6D0",
                                      border_width=2, text_color="#ffffff", height=35,font=("fixedsys",14))
        self.turma.grid(row=5, column=0, sticky="ew", pady=(0, 20))

        # Email
        CTkLabel(self.right_frame, text="  Email:", text_color="#ffffff", image=email_icon,
                 compound="left", font=("fixedsys", 14, "bold")).grid(row=6, column=0, sticky="w", pady=(0, 5))
        self.email_cadastro = CTkEntry(self.right_frame, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff", height=35,font=("fixedsys",14))
        self.email_cadastro.grid(row=7, column=0, sticky="ew", pady=(0, 20))

        # Senha
        CTkLabel(self.right_frame, text="  Senha:", text_color="#ffffff", image=password_icon,
                 compound="left", font=("fixedsys", 14, "bold")).grid(row=8, column=0, sticky="w", pady=(0, 5))
        self.senha_cadastro = CTkEntry(self.right_frame, fg_color="#3B5055", border_color="#B5C6D0",
                                       border_width=2, text_color="#ffffff", show="*", height=35, font=("fixedsys",14))
        self.senha_cadastro.grid(row=9, column=0, sticky="ew", pady=(0, 30))

        # Botão cadastrar
        CTkButton(self.right_frame, text="CADASTRAR", fg_color="#FF9700", hover_color="#c27402",
                  font=("fixedsys", 22, "bold"), text_color="#ffffff", command=self.cadastrar_usuario, height=45, corner_radius=10).grid(
            row=10, column=0, sticky="ew", pady=(0, 15))

        # Botão login
        CTkButton(self.right_frame, text="Já tem conta? Faça login", fg_color="#D22D23", hover_color="#942019",
                  font=("fixedsys", 14, "bold"), text_color="#ffffff", image=signin_icon,
                  command=lambda: self.controller.show_frame(Login), height=45, corner_radius=10).grid(row=11, column=0, sticky="ew")

    def redimensionar_imagem_lateral(self, event=None):
        new_width = self.left_frame.winfo_width()
        new_height = self.left_frame.winfo_height()

        if new_width > 0 and new_height > 0:
            resized_pil = self.original_img.resize((new_width, new_height), Image.LANCZOS)
            self.current_img = CTkImage(dark_image=resized_pil, light_image=resized_pil, size=(new_width, new_height))
            self.side_label.configure(image=self.current_img)

    def cadastrar_usuario(self):
        nome = self.nome_completo.get()
        email = self.email_cadastro.get()
        senha = self.senha_cadastro.get()

        if not nome or not email or not senha:
            msgbox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            self.controller.banco.cadastrar_usuario(nome, email, senha)
            msgbox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.controller.show_frame(Login)
        except Exception as e:
            msgbox.showerror("Erro", f"Falha ao cadastrar: {str(e)}")


class CentralProfessor(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.criar_tela()
        

    def criar_tela(self):

        CTkButton(self, height=35, width=70, text="Voltar", fg_color="#E44982", text_color="#ffffff", command=lambda: self.controller.show_frame(MenuProfessor)).grid(row = 0, column = 0, padx = (10,0), pady = 10)

        CTkButton(self, width=200, height=300, text="Perguntas", fg_color="#999999", text_color="#ffffff",font=("fixedsys",22,"bold"), command=lambda: self.controller.show_frame(PerguntasProfessor)).grid(row = 1, column = 0, padx = (120,25), pady = 200)
        CTkButton(self, width=200, height=300, text="Jogadores", fg_color="#999999", text_color="#ffffff",font=("fixedsys",22,"bold"), command=lambda: self.controller.show_frame(Jogadores)).grid(row = 1, column =1, padx = 25, pady=200 )
        CTkButton(self, width=200, height=300, text="Matérias", fg_color="#999999", text_color="#ffffff",font=("fixedsys",22,"bold")).grid(row = 1, column = 2, padx=25,pady=200)
        CTkButton(self, width=200, height=300, text="Instruções", fg_color="#999999", text_color="#ffffff", font=("fixedsys",22,"bold")).grid(row=1,column=3,padx=25,pady=200)

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
        

class Materias(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.banco = controller.banco
        self.materias = []
        self.mostrar_materias()
        self.fonte = ("fixedsys",22,"bold")
        self.criar_tela()
    
    def criar_tela(self):

        self.btn_voltar = CTkButton(master=self,text="Voltar",width=100,height=50, font=self.fonte, command=lambda: self.controller.show_frame(MenuProfessor))
        self.btn_voltar.grid(column=0,row=0,padx=(15,0),pady=(10,0))

        CTkLabel(master=self, text="Escolha a matéria para o seu jogo: ", font=("fixedsys",22,"bold")).grid(column=0,row=1,padx=400,pady=(300,30))

        self.input_materia_jogo = CTkOptionMenu(self, values=self.materias, font=("fixedsys",22,"bold"))
        self.input_materia_jogo.grid(column=0,row=2,padx=400,pady=10)

        self.btn_iniciar_jogo = CTkButton(master=self, text="Iniciar", font=("fixedsys",22,"bold"),width=300,height=100,command=lambda: self.controller.show_frame(Perguntas))
        self.btn_iniciar_jogo.grid(column=0,row=3,padx=400,pady=10)

    
    def mostrar_materias(self):
        try:
            self.materias_tuple = self.banco.carregar_materias() 
            for materia in self.materias_tuple:
                self.materias.append(materia[0])
            print(self.materias)
        except Exception as e:
            print("Erro ao carregar materias")

    def mostrar_materia(self,materia):
        print(f"Matéria escolhida: {materia}")
        return materia
    
    


class MenuProfessor(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.criar_tela()

    def criar_tela(self):
        side_img = CTkImage(dark_image=Image.open("imagens/side-img.png"), light_image=Image.open("imagens/side-img.png"), size=(800, 780))

        self.right_frame = CTkFrame(self, width=800, height=780, fg_color="#ffffff")
        self.right_frame.pack_propagate(0)
        self.right_frame.pack(side="right", fill="both")
        CTkLabel(self.right_frame, text="", image=side_img).pack(fill="both", expand=True)

        self.left_frame = CTkFrame(self, width=400, height=780, fg_color="#ffffff")
        self.left_frame.pack_propagate(0)
        self.left_frame.pack(side="left", fill="both")

        CTkButton(self.left_frame, text="Jogar", fg_color="#601E88", hover_color="#E44982", 
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=60, 
                  command=lambda: self.controller.show_frame(Materias)).pack(anchor="w", pady=(400, 0), padx=(25, 0)) 
        CTkButton(self.left_frame, text="Perguntas", fg_color="#601E88", hover_color="#E44982", 
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=60, 
                  command=lambda: self.controller.show_frame(PerguntasProfessor)).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        CTkButton(self.left_frame, text="Opções", fg_color="#601E88", hover_color="#E44982", 
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=60, command=lambda: self.controller.show_frame(CentralProfessor)).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        CTkButton(self.left_frame, text="Sair", fg_color="#601E88", hover_color="#E44982",
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=60, 
                  command=self.controller.destroy).pack(anchor="w", pady=(20, 0), padx=(25, 0))

class Menu(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.criar_tela()

    def criar_tela(self):
        side_img = CTkImage(dark_image=Image.open("imagens/side-img.png"), light_image=Image.open("imagens/side-img.png"), size=(800, 780))
        

        self.right_frame = CTkFrame(self, width=800, height=780, fg_color="#ffffff")
        self.right_frame.pack_propagate(0)
        self.right_frame.pack(side="right", fill="both")
        CTkLabel(self.right_frame, text="", image=side_img).pack(fill="both", expand=True)

        self.left_frame = CTkFrame(self, width=400, height=780, fg_color="#ffffff")
        self.left_frame.pack_propagate(0)
        self.left_frame.pack(side="left", fill="both")

        CTkButton(self.left_frame, text="Jogar", fg_color="#601E88", hover_color="#E44982", 
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=48, 
                  command=lambda: self.controller.show_frame(Perguntas)).pack(anchor="w", pady=(400, 0), padx=(25, 0))
        CTkButton(self.left_frame, text="Estatísticas", fg_color="#601E88", hover_color="#E44982", 
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=48).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        CTkButton(self.left_frame, text="Opções", fg_color="#601E88", hover_color="#E44982", 
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=48).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        CTkButton(self.left_frame, text="Sair", fg_color="#601E88", hover_color="#E44982",
                  font=("Arial Bold", 14), text_color="#ffffff", width=348, height=48, 
                  command=self.controller.destroy).pack(anchor="w", pady=(20, 0), padx=(25, 0))

class Perguntas(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
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
        self.criar_tela()

    def obter_perguntas(self):
        conexao = sqlite3.connect("PI.db")
        cursor = conexao.cursor()
        
        cursor.execute("SELECT dificuldade, pergunta, altA, altB, altC, altD, correta, dica FROM Pergunta")

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

        self.perguntas = self.perguntas_faceis + self.perguntas_medias + self.perguntas_dificeis
        
        cursor.close()
        conexao.close()

        return self.perguntas

    def criar_tela(self):
        self.left_frame = CTkFrame(self, width=850, height=780, fg_color="#ffffff")
        self.left_frame.pack_propagate(0)
        self.left_frame.pack(side="left", fill="both")

        self.right_frame = CTkFrame(self, width=350, height=780, fg_color="#707070", corner_radius=0)
        self.right_frame.pack_propagate(0)
        self.right_frame.pack(side="right", fill="both")
        
        self.frame_pergunta = CTkFrame(self.left_frame, width=800, height=200, fg_color="#999999", corner_radius=10)
        self.frame_pergunta.pack(anchor="w", padx=(25), pady=(50))
        self.frame_pergunta.pack_propagate(False)
        
        self.texto_pergunta = CTkLabel(self.frame_pergunta, text="", font=("Arial Bold", 25), text_color="#ffffff")
        self.texto_pergunta.pack(padx=(25,0), pady=(30,0))

        self.texto_dica = CTkLabel(self.frame_pergunta, text="", font=("Arial Bold", 18), text_color="#ffffff")
        self.texto_dica.pack(padx=(25,0), pady=(35,0))

        self.label_pontuacao = CTkLabel(self.right_frame, text="Pontuação: 0", font=("Arial Bold", 18), text_color="#ffffff")
        self.label_pontuacao.pack(pady=(20, 0)) 

        self.botao_ajuda_dica = CTkButton(self.right_frame, text="Dica", font=("Arial Bold", 18), fg_color="#601E88", 
                                         text_color="#ffffff", width=250, height=100, command=self.mostrar_dica)
        self.botao_ajuda_dica.pack(padx=(25,0), pady=(30,0))

        self.botao_ajuda_50 = CTkButton(self.right_frame, text="50% / 50%", font=("Arial Bold", 18), fg_color="#601E88", 
                                       text_color="#ffffff", width=250, height=100, command=self.eliminar_alternativas)
        self.botao_ajuda_50.pack(padx=(25,0), pady=(30,0))
        
        self.botao_ajuda_pular = CTkButton(self.right_frame, text="Pular", font=("Arial Bold", 18), fg_color="#601E88", 
                                          text_color="#ffffff", width=250, height=100, command=self.pular_pergunta)
        self.botao_ajuda_pular.pack(padx=(25,0), pady=(30,0))
        
        self.botoes_alternativas = []

        self.botao_encerrar = CTkButton(self.right_frame, text="Encerrar Jogo", 
                                      font=("Arial Bold", 18), fg_color="#E44982", 
                                      text_color="#ffffff", width=250, height=100, 
                                      command=lambda: self.controller.show_frame(MenuProfessor))
        self.botao_encerrar.pack(padx=(25,0), pady=(30,0))

        
        for i in range(4):
            botao = CTkButton(self.left_frame, text="", fg_color="#601E88", font=("Arial Bold", 14), 
                             text_color="#ffffff", width=800, height=80, corner_radius=10,
                             command=lambda i=i: self.verificar_resposta(i))
            botao.pack(anchor="w", pady=(20, 0), padx=(25, 0))
            self.botoes_alternativas.append(botao)
        
        self.label_feedback = CTkLabel(self.left_frame, text="", font=("Arial Bold", 18), text_color="#E44982")
        self.label_feedback.pack(pady=(20, 0))
        
        # Frame para tela de jogo encerrado (inicialmente oculto)
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
                self.botoes_alternativas[i].configure(text=alternativas[i], fg_color="#601E88", state="normal")
            
            self.botao_ajuda_dica.configure(state="normal", fg_color="#601E88")
            self.botao_ajuda_50.configure(state="normal", fg_color="#601E88")
            self.botao_ajuda_pular.configure(state="normal", fg_color="#601E88")
            self.label_feedback.configure(text="")
        else:
            self.texto_pergunta.configure(text=f"Quiz concluído! Pontuação final: {self.pontuacao}")
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
                botao.configure(state="disabled")
    
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
            self.label_feedback.configure(text="Correto!", text_color="#2ECC71")
            self.botoes_alternativas[indice].configure(fg_color="#2ECC71")
            self.pontuacao = self.pontos[self.i_pontos]
            self.i_pontos += 1
            self.label_pontuacao.configure(text=f"Pontuação: {self.pontuacao}")
            
            # Desabilitar todos os botões após resposta correta
            for botao in self.botoes_alternativas:
                botao.configure(state="disabled")
            
            # Verificar se atingiu checkpoint (10000 ou 150000 pontos)
            if self.pontuacao in [10000, 150000]:
                self.checkpoint_atingido = True
            
            self.indice_pergunta += 1
            self.after(1000, self.carregar_pergunta)
        else:
            self.label_feedback.configure(text="Não foi dessa vez!", text_color="#E44982")
            self.botoes_alternativas[indice].configure(fg_color="#FF0000")
            
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
                
                self.game_over_points.configure(text=f"Pontuação final: {self.pontuacao}")
                self.game_over_frame.pack(anchor="w", padx=(25), pady=(50))

class PerguntasProfessor(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(width=1200, height=780, fg_color="#ffffff")
        self.pack_propagate(0)
        self.banco = controller.banco
        self.correta = " "
        self.dificuldade = " "
        self.materias=[]
        self.mostrar_materias()
        self.criar_tela()
        self.materia_escolhida = " "
        self.mostrar_dados()
        

    def criar_tela(self):

        self.top_frame = CTkFrame(self, width=1200, height=30, fg_color="#ffffff")
        self.top_frame.pack_propagate(0)
        self.top_frame.pack(side="top", fill="x", padx=10, pady=5)
        
        # Botão Voltar
        CTkButton(self.top_frame, text="Voltar", fg_color="#601E88", hover_color="#E44982",
                 font=("Arial Bold", 12), width=100, height=30,
                 command=lambda: self.controller.show_frame(MenuProfessor)).pack(side="left", padx=10)
        
        self.texto_materia = CTkLabel(self.top_frame, text="Insira a nova matéria: ", text_color="#000")
        self.texto_materia.pack(side="right",fill="both",padx=50,pady=2)

        self.materia = CTkEntry(self.top_frame, width=150, height= 25, fg_color="#ffffff")
        self.materia.pack(side="right", fill="both", padx=10,pady=2)
        
        self.btn_cadastrar_materia = CTkButton(self.top_frame, text="Cadastrar matéria", fg_color="#E44982")
        self.btn_cadastrar_materia.pack(side="right",fill="both",padx=10, pady=2)
        
        self.left_frame = CTkFrame(self, width=550, height=780, fg_color="#707070", corner_radius=0)
        self.left_frame.pack_propagate(0)
        self.left_frame.pack(side="left", fill="both")

        self.right_frame = CTkFrame(self, width=650, height=780, fg_color="#505050", corner_radius=0)
        self.right_frame.pack_propagate(0)
        self.right_frame.pack(side="right", fill="both")

        CTkLabel(self.left_frame, text="Insira a pergunta:", font=("Arial Bold", 18)).pack(anchor="w", padx=(45,0), pady=(40,0))
        self.input_pergunta = CTkEntry(self.left_frame, font=("Arial Bold", 14), width=470, height=33)
        self.input_pergunta.pack(padx=(20,20), pady=(10,0))

        CTkLabel(self.left_frame, text="Insira a alternativa A: ", font=("Arial Bold", 18)).pack(anchor="w", padx=(45,0), pady=(20,0))
        self.input_alt_a = CTkEntry(self.left_frame, font=("Arial Bold", 14), width=470, height=33)
        self.input_alt_a.pack(padx=(20,20), pady=(10,0))

        CTkLabel(self.left_frame, text="Insira a alternativa B: ", font=("Arial Bold", 18)).pack(anchor="w", padx=(45,0), pady=(20,0))
        self.input_alt_b = CTkEntry(self.left_frame, font=("Arial Bold", 14), width=470, height=33)
        self.input_alt_b.pack(padx=(20,20), pady=(10,0))

        CTkLabel(self.left_frame, text="Insira a alternativa C: ", font=("Arial Bold", 18)).pack(anchor="w", padx=(45,0), pady=(20,0))
        self.input_alt_c = CTkEntry(self.left_frame, font=("Arial Bold", 14), width=470, height=33)
        self.input_alt_c.pack(padx=(20,20), pady=(10,0))

        CTkLabel(self.left_frame, text="Insira a alternativa D: ", font=("Arial Bold", 18)).pack(anchor="w", padx=(45,0), pady=(20,0))
        self.input_alt_d = CTkEntry(self.left_frame, font=("Arial Bold", 14), width=470, height=33)
        self.input_alt_d.pack(padx=(20,20), pady=(10,0))

        CTkLabel(self.left_frame, text="Insira a Dica: ", font=("Arial Bold", 18)).pack(anchor="w", padx=(45,0), pady=(20,0))
        self.input_dica = CTkEntry(self.left_frame, font=("Arial Bold", 14), width=470, height=33)
        self.input_dica.pack(padx=(20,20), pady=(10,0))

        self.input_dificuldade = CTkOptionMenu(self.left_frame, values=["---","Fácil", "Médio", "Difícil"], command=self.mostrar_dificuldade)
        self.input_dificuldade.pack(anchor="w", padx=(45,0), pady=(20,0))

        self.input_correta = CTkOptionMenu(self.left_frame, values=["---","A", "B", "C", "D"], command=self.mostrar_correta)
        self.input_correta.pack(anchor="w", padx=(45,0), pady=(10,0))

        self.input_materia = CTkOptionMenu(self.left_frame, values=self.materias, command=self.mostrar_materia)
        self.input_materia.pack(anchor="w", padx=(45,0), pady=(10,0))

        CTkButton(self.left_frame, text="Adicionar Pergunta", width=470, height=40, command=self.cadastrar_pergunta).pack(padx=(20,20), pady=(10,0))

        # Configuração do Treeview com scrollbars
        scrollbar_y = ttk.Scrollbar(self.right_frame, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = ttk.Scrollbar(self.right_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        colunas = ("ID","Pergunta","A", "B", "C", "D", "Dificuldade", "Correta", "Dica", "Materia")

        self.tree = ttk.Treeview(
            self.right_frame,
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

        CTkButton(self.right_frame, text="Deletar", command=self.deletar_dados, width=570, height=55).pack(padx=(40,40), pady=(10,30))
        
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