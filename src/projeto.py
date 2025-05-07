class Projeto():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
