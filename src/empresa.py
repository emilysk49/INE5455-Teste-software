from src.funcionario import Funcionario
from src.projeto import Projeto

class Empresa():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionar_funcionario(self, funcionario):
        if (not isinstance(funcionario, Funcionario)):
            raise TypeError("O objeto não é um funcionário.")
        if (funcionario in self.funcionarios):
            raise ValueError("Funcionário já cadastrado.")
        self.funcionarios.append(funcionario)

    def adicionar_projeto(self, projeto):
        if (not isinstance(projeto, Projeto)):
            raise TypeError("O objeto não é um projeto.")
        if (projeto in self.projetos):
            raise ValueError("Projeto já cadastrado.")
        self.projetos.append(projeto)

    def adicionar_funcionario_em_projeto(self, funcionario, projeto):
        if projeto not in self.projetos:
            raise ValueError("Projeto não cadastrado na empresa.")
        if (funcionario not in self.funcionarios):
            raise ValueError("Funcionário não cadastrado.")
        projeto.adicionar_funcionario(funcionario)
        funcionario.adicionar_projeto(projeto)