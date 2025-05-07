class Funcionario():
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)