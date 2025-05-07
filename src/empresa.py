from src.funcionario import Funcionario

class Empresa():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionar_funcionario(self, funcionario):
        if (funcionario in self.funcionarios):
            raise ValueError("Funcionário já cadastrado.")
        self.funcionarios.append(funcionario)

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)