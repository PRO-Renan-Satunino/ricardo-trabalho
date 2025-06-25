import tkinter as tk
from tkinter import messagebox
from controllers.transporte_controller import TransporteController
from models.transporte import Transporte

class CadastroTransporteView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Transporte")
        self.geometry("400x300")
        self.master = master

        tk.Label(self, text="Placa:").pack(pady=5)
        self.entry_placa = tk.Entry(self)
        self.entry_placa.pack()

        tk.Label(self, text="Motorista:").pack(pady=5)
        self.entry_motorista = tk.Entry(self)
        self.entry_motorista.pack()

        tk.Label(self, text="Tipo do Veículo:").pack(pady=5)
        self.entry_tipo = tk.Entry(self)
        self.entry_tipo.pack()

        tk.Button(self, text="Salvar", command=self.salvar_transporte).pack(pady=10)
        tk.Button(self, text="Voltar", command=self.voltar).pack()

    def salvar_transporte(self):
        placa = self.entry_placa.get().strip()
        motorista = self.entry_motorista.get().strip()
        tipo_veiculo = self.entry_tipo.get().strip()

        if not placa or not motorista or not tipo_veiculo:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        transporte = Transporte(placa, motorista, tipo_veiculo)
        TransporteController.salvar_transporte(transporte)
        messagebox.showinfo("Sucesso", "Transporte salvo com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_placa.delete(0, tk.END)
        self.entry_motorista.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)

    def voltar(self):
        self.destroy()
        self.master.deiconify()
