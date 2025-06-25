class EventoSeguranca:
    def __init__(self, data_hora, descricao):
        self.data_hora = data_hora
        self.descricao = descricao

    def to_line(self):
        return f"{self.data_hora};{self.descricao}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 2:
            return EventoSeguranca(parts[0], parts[1])
        return None
