import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "majumonteiro" and senha == "12345":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")
janela.configure(bg="#f0f0f0")

titulo = tk.Label(janela, text="Login", font=("Arial", 16), bg="#f0f0f0")
titulo.pack(pady=10)

label_usuario = tk.Label(janela, text="Usuário:", font=("Arial", 12), bg="#f0f0f0")
label_usuario.pack(pady=5)
entrada_usuario = tk.Entry(janela, font=("Arial", 12))
entrada_usuario.pack(pady=5)

label_senha = tk.Label(janela, text="Senha:", font=("Arial", 12), bg="#f0f0f0")
label_senha.pack(pady=5)
entrada_senha = tk.Entry(janela, font=("Arial", 12), show="*")
entrada_senha.pack(pady=5)

botao_login = tk.Button(janela, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white", command=verificar_login)
botao_login.pack(pady=20)

janela.mainloop()
