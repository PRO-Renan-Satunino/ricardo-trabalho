import tkinter as tk
from tkinter import messagebox
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController

class CadastroUsuarioView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Usuário")
        self.geometry("400x300")
        self.master = master

        tk.Label(self, text="CPF:").pack(pady=5)
        self.entry_cpf = tk.Entry(self)
        self.entry_cpf.pack()

        tk.Label(self, text="Nome:").pack(pady=5)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()

        tk.Label(self, text="Função:").pack(pady=5)
        self.entry_funcao = tk.Entry(self)
        self.entry_funcao.pack()

        tk.Button(self, text="Salvar", command=self.salvar_usuario).pack(pady=10)
        tk.Button(self, text="Voltar", command=self.voltar).pack()

    def salvar_usuario(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        funcao = self.entry_funcao.get()

        if not cpf or not nome or not funcao:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        usuario = Usuario(cpf, nome, funcao)
        UsuarioController.salvar_usuario(usuario)
        messagebox.showinfo("Sucesso", "Usuário salvo com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_cpf.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_funcao.delete(0, tk.END)

    def voltar(self):
        self.destroy()
        self.master.deiconify()
