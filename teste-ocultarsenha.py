import tkinter as tk
import customtkinter as ctk



# Função para alternar entre mostrar e ocultar a senha
def toggle_password():
    if entry_password.cget("show") == "":
        entry_password.configure(show="*")
        btn_toggle.configure(text="Mostrar")
    else:
        entry_password.configure(show="")
        btn_toggle.configure(text="Ocultar")

# Configurar a janela principal
root = ctk.CTk()

# Criar um campo de entrada para senha
entry_password = ctk.CTkEntry(root, show="*", width=200)
entry_password.pack(padx=20, pady=10)

# Criar um botão para alternar entre mostrar e ocultar a senha
btn_toggle = ctk.CTkButton(root, text="Ocultar", command=toggle_password)
btn_toggle.pack(padx=20, pady=10)

# Iniciar o loop principal
root.mainloop()


