class Peca:
    def __init__(self, codigo, nome, fornecedor, preco):
        self.codigo = codigo
        self.nome = nome
        self.fornecedor = fornecedor
        self.preco = preco

    def to_line(self):
        return f"{self.codigo};{self.nome};{self.fornecedor};{self.preco}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 4:
            return Peca(parts[0], parts[1], parts[2], parts[3])
        return None
