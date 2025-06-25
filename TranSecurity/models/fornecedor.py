class Fornecedor:
    def __init__(self, cnpj, nome, contato):
        self.cnpj = cnpj
        self.nome = nome
        self.contato = contato

    def to_line(self):
        return f"{self.cnpj};{self.nome};{self.contato}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 3:
            return Fornecedor(parts[0], parts[1], parts[2])
        return None
