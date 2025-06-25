class Produto:
    def __init__(self, codigo, descricao, peso):
        self.codigo = codigo
        self.descricao = descricao
        self.peso = peso

    def to_line(self):
        return f"{self.codigo};{self.descricao};{self.peso}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 3:
            return Produto(parts[0], parts[1], parts[2])
        return None
