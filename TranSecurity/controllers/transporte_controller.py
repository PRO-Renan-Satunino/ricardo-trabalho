from models.transporte import Transporte

class TransporteController:
    arquivo = "data/transportes.txt"

    @classmethod
    def salvar_transporte(cls, transporte):
        with open(cls.arquivo, "a") as f:
            f.write(transporte.to_line())

    @classmethod
    def listar_transportes(cls):
        transportes = []
        try:
            with open(cls.arquivo, "r") as f:
                for line in f:
                    transporte = Transporte.from_line(line)
                    if transporte:
                        transportes.append(transporte)
        except FileNotFoundError:
            pass
        return transportes
