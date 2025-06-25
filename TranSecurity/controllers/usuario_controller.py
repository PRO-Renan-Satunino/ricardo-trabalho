from models.usuario import Usuario

class UsuarioController:
    arquivo = "data/usuarios.txt"

    @classmethod
    def salvar_usuario(cls, usuario):
        with open(cls.arquivo, "a") as f:
            f.write(usuario.to_line())

    @classmethod
    def listar_usuarios(cls):
        usuarios = []
        try:
            with open(cls.arquivo, "r") as f:
                for line in f:
                    usuario = Usuario.from_line(line)
                    if usuario:
                        usuarios.append(usuario)
        except FileNotFoundError:
            pass
        return usuarios
