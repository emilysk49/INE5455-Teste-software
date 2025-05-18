from src.ocorrencia import Ocorrencia

class Funcionario():
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []
        self.salario = None
        self.empresa = None
        self.ocorrencias = []

    def adicionar_projeto(self, projeto):
        from src.projeto import Projeto
        if not isinstance(projeto, Projeto):
            raise TypeError("Projeto deve ser do tipo Projeto.")
        if projeto in self.projetos:
            raise ValueError("Projeto já adicionado.")
        self.projetos.append(projeto)

    def adicionar_salario(self, salario):
        if salario < 0:
            raise ValueError("Salário não pode ser negativo.")
        self.salario = salario

    def adicionar_a_empresa(self, empresa):
        self.empresa = empresa
    
    def criar_ocorrencia(self, id, descricao, tipo, projeto):
        # from src.projeto import Projeto
        # if not isinstance(projeto, Projeto):
        #     raise TypeError("Projeto deve ser do tipo Projeto.")
        # if projeto not in self.projetos:
        #     raise ValueError("Projeto não está associado ao funcionário.")
        if projeto.empresa != self.empresa:
            raise ValueError("Projeto não pertence à empresa do funcionário.")
        ocorrencia = Ocorrencia(id, self, descricao, tipo, projeto)
        self.ocorrencias.append(ocorrencia)
        projeto.adicionar_ocorrencia(ocorrencia)