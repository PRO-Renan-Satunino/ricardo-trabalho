"""
Nome do arquivo: clientes_controller.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

import os

CAMINHO = "data/clientes.txt"

def salvar_cliente(nome, cpf, endereco):
    with open(CAMINHO, "a", encoding="utf-8") as f:
        f.write(f"{nome};{cpf};{endereco}\n")

def listar_clientes():
    if not os.path.exists(CAMINHO):
        return "Nenhum cliente cadastrado."
    with open(CAMINHO, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        if not linhas:
            return "Nenhum cliente cadastrado."
        return "".join(linhas)
