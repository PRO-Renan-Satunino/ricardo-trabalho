import tkinter as tk
from tkinter import messagebox, scrolledtext
from controllers.seguranca_controller import SegurancaController

class SegurancaView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Segurança e Monitoramento")
        self.geometry("600x500")
        self.master = master

        tk.Label(self, text="Registrar Evento de Segurança", font=("Arial", 14)).pack(pady=10)

        self.entry_evento = tk.Entry(self, width=50)
        self.entry_evento.pack(pady=5)

        tk.Button(self, text="Registrar", command=self.registrar_evento).pack(pady=5)

        tk.Label(self, text="Eventos Registrados:", font=("Arial", 12)).pack(pady=10)

        self.text_log = scrolledtext.ScrolledText(self, width=70, height=15)
        self.text_log.pack()

        tk.Button(self, text="Atualizar Lista", command=self.carregar_eventos).pack(pady=5)
        tk.Button(self, text="Voltar", command=self.voltar).pack(pady=10)

        self.carregar_eventos()

    def registrar_evento(self):
        descricao = self.entry_evento.get().strip()
        if not descricao:
            messagebox.showwarning("Atenção", "Digite uma descrição do evento.")
            return
        SegurancaController.salvar_evento(descricao)
        messagebox.showinfo("Sucesso", "Evento registrado com sucesso!")
        self.entry_evento.delete(0, tk.END)
        self.carregar_eventos()

    def carregar_eventos(self):
        self.text_log.delete("1.0", tk.END)
        eventos = SegurancaController.listar_eventos()
        for e in eventos:
            self.text_log.insert(tk.END, f"[{e.data_hora}] {e.descricao}\n")
        self.text_log.see(tk.END)

    def voltar(self):
        self.destroy()
        self.master.deiconify()
