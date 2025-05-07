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
        if (projeto in self.projetos):
            raise ValueError("Projeto já cadastrado.")
        self.projetos.append(projeto)


    def adicionar_funcionario_em_projeto(self, funcionario, projeto):
        projeto.adicionar_funcionario(funcionario)
        funcionario.adicionar_projeto(projeto)