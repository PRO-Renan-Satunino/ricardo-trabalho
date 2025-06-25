class Cliente:
    def __init__(self, cnpj, nome, endereco):
        self.cnpj = cnpj
        self.nome = nome
        self.endereco = endereco

    def to_line(self):
        return f"{self.cnpj};{self.nome};{self.endereco}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 3:
            return Cliente(parts[0], parts[1], parts[2])
        return None
