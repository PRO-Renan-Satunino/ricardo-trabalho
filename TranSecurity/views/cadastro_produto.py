import tkinter as tk
from tkinter import messagebox
from controllers.produto_controller import ProdutoController
from models.produto import Produto

class CadastroProdutoView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Produto")
        self.geometry("400x300")
        self.master = master

        tk.Label(self, text="Código:").pack(pady=5)
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.pack()

        tk.Label(self, text="Descrição:").pack(pady=5)
        self.entry_descricao = tk.Entry(self)
        self.entry_descricao.pack()

        tk.Label(self, text="Peso (kg):").pack(pady=5)
        self.entry_peso = tk.Entry(self)
        self.entry_peso.pack()

        tk.Button(self, text="Salvar", command=self.salvar_produto).pack(pady=10)
        tk.Button(self, text="Voltar", command=self.voltar).pack()

    def salvar_produto(self):
        codigo = self.entry_codigo.get().strip()
        descricao = self.entry_descricao.get().strip()
        peso = self.entry_peso.get().strip()

        if not codigo or not descricao or not peso:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        # Validar se peso é número
        try:
            peso_valor = float(peso)
        except ValueError:
            messagebox.showerror("Erro", "Peso deve ser um número válido.")
            return

        produto = Produto(codigo, descricao, peso_valor)
        ProdutoController.salvar_produto(produto)
        messagebox.showinfo("Sucesso", "Produto salvo com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_codigo.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_peso.delete(0, tk.END)

    def voltar(self):
        self.destroy()
        self.master.deiconify()
