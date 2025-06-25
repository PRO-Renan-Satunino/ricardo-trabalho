"""
Nome do arquivo: funcionarios_controller.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

import os

CAMINHO = "data/funcionarios.txt"

def salvar_funcionario(nome, cpf, cargo):
    with open(CAMINHO, "a", encoding="utf-8") as f:
        f.write(f"{nome};{cpf};{cargo}\n")

def listar_funcionarios():
    if not os.path.exists(CAMINHO):
        return "Nenhum funcionário cadastrado."
    with open(CAMINHO, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        if not linhas:
            return "Nenhum funcionário cadastrado."
        return "".join(linhas)
