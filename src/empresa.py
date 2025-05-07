from src.funcionario import Funcionario

class Empresa():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if (funcionario in self.funcionarios):
            raise ValueError("Funcionário já cadastrado.")
        self.funcionarios.append(funcionario)