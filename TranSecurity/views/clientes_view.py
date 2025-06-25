"""
Nome do arquivo: clientes_view.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

import tkinter as tk
from controllers.clientes_controller import salvar_cliente, listar_clientes

def abrir_tela_clientes():
    janela = tk.Toplevel()
    janela.title("Cadastro de Clientes")
    janela.geometry("500x400")

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="CPF:").pack()
    entry_cpf = tk.Entry(janela)
    entry_cpf.pack()

    tk.Label(janela, text="Endereço:").pack()
    entry_endereco = tk.Entry(janela)
    entry_endereco.pack()

    def cadastrar():
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        endereco = entry_endereco.get()
        salvar_cliente(nome, cpf, endereco)
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)

    def exibir_clientes():
        resultado = listar_clientes()
        output.delete(1.0, tk.END)
        output.insert(tk.END, resultado)

    tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)
    tk.Button(janela, text="Listar Clientes", command=exibir_clientes).pack(pady=5)

    output = tk.Text(janela, height=10, width=50)
    output.pack()
