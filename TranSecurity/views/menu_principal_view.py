import tkinter as tk
from tkinter import messagebox

class MenuPrincipalView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SGTST - Menu Principal")
        self.geometry("600x400")

        tk.Label(self, text="Sistema de Gestão de Transporte e Segurança", font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Cadastro de Usuário", width=25, command=self.abrir_cadastro_usuario).pack(pady=5)
        tk.Button(self, text="Cadastro de Produto", width=25, command=self.abrir_cadastro_produto).pack(pady=5)
        tk.Button(self, text="Cadastro de Transporte", width=25, command=self.abrir_cadastro_transporte).pack(pady=5)
        tk.Button(self, text="Segurança e Monitoramento", width=25, command=self.abrir_seguranca).pack(pady=5)
        tk.Button(self, text="Sair", width=25, command=self.sair).pack(pady=20)

    def abrir_cadastro_usuario(self):
        self.withdraw()
        from views.cadastro_usuario import CadastroUsuarioView
        CadastroUsuarioView(self)

    def abrir_cadastro_produto(self):
        self.withdraw()
        from views.cadastro_produto import CadastroProdutoView
        CadastroProdutoView(self)

    def abrir_cadastro_transporte(self):
        self.withdraw()
        from views.cadastro_transporte import CadastroTransporteView
        CadastroTransporteView(self)

    def abrir_seguranca(self):
        self.withdraw()
        from views.seguranca import SegurancaView
        SegurancaView(self)

    def sair(self):
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
            self.destroy()
