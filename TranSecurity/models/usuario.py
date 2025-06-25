class Usuario:
    def __init__(self, cpf, nome, funcao):
        self.cpf = cpf
        self.nome = nome
        self.funcao = funcao

    def to_line(self):
        return f"{self.cpf};{self.nome};{self.funcao}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 3:
            return Usuario(parts[0], parts[1], parts[2])
        return None
