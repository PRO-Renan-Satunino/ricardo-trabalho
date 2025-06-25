from models.seguranca import EventoSeguranca
import datetime

class SegurancaController:
    arquivo = "data/seguranca.txt"

    @classmethod
    def salvar_evento(cls, descricao):
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        evento = EventoSeguranca(data_hora, descricao)
        with open(cls.arquivo, "a") as f:
            f.write(evento.to_line())

    @classmethod
    def listar_eventos(cls):
        eventos = []
        try:
            with open(cls.arquivo, "r") as f:
                for line in f:
                    evento = EventoSeguranca.from_line(line)
                    if evento:
                        eventos.append(evento)
        except FileNotFoundError:
            pass
        return eventos
