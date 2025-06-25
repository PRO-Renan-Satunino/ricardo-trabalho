class GenericoController:
    def __init__(self, arquivo, modelo):
        self.arquivo = arquivo
        self.modelo = modelo

    def salvar(self, obj):
        with open(self.arquivo, 'a') as f:
            f.write(obj.to_line())

    def listar(self):
        lista = []
        try:
            with open(self.arquivo, 'r') as f:
                for line in f:
                    obj = self.modelo.from_line(line)
                    if obj:
                        lista.append(obj)
        except FileNotFoundError:
            pass
        return lista
