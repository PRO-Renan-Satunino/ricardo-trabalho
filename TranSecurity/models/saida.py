class Saida:
    def __init__(self, cliente, carga, destino, hora_saida, hora_retorno, km_ini, km_fim):
        self.cliente = cliente
        self.carga = carga
        self.destino = destino
        self.hora_saida = hora_saida
        self.hora_retorno = hora_retorno
        self.km_ini = km_ini
        self.km_fim = km_fim

    def to_line(self):
        return f"{self.cliente};{self.carga};{self.destino};{self.hora_saida};{self.hora_retorno};{self.km_ini};{self.km_fim}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 7:
            return Saida(*parts)
        return None
