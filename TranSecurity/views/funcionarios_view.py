"""
Nome do arquivo: funcionarios_view.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

import tkinter as tk
from controllers.funcionarios_controller import salvar_funcionario, listar_funcionarios

def abrir_tela_funcionarios():
    janela = tk.Toplevel()
    janela.title("Cadastro de Funcionários")
    janela.geometry("500x400")

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="CPF:").pack()
    entry_cpf = tk.Entry(janela)
    entry_cpf.pack()

    tk.Label(janela, text="Cargo:").pack()
    entry_cargo = tk.Entry(janela)
    entry_cargo.pack()

    def cadastrar():
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        cargo = entry_cargo.get()
        salvar_funcionario(nome, cpf, cargo)
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)

    def exibir_funcionarios():
        resultado = listar_funcionarios()
        output.delete(1.0, tk.END)
        output.insert(tk.END, resultado)

    tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)
    tk.Button(janela, text="Listar Funcionários", command=exibir_funcionarios).pack(pady=5)

    output = tk.Text(janela, height=10, width=50)
    output.pack()
