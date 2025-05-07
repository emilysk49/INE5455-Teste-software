class Projeto():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            raise ValueError("Funcionário já adicionado ao projeto.")
        self.funcionarios.append(funcionario)
