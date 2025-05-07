class Funcionario():
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []
        self.salario = None

    def adicionar_projeto(self, projeto):
        if projeto in self.projetos:
            raise ValueError("Projeto já adicionado.")
        self.projetos.append(projeto)

    def adicionar_salario(self, salario):
        self.salario = salario