from src.ocorrencia import *

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
    
    def criar_ocorrencia(self, id, descricao, tipo, projeto, prioridade=PrioridadeOcorrencia.MEDIA):
        from src.projeto import Projeto
        if not isinstance(projeto, Projeto):
            raise TypeError("Projeto deve ser do tipo Projeto.")
        if len(self.ocorrencias) >= 10:
            raise ValueError("Número máximo de ocorrências atingido.")
        if projeto.empresa != self.empresa:
            raise ValueError("Projeto não pertence à empresa do funcionário.")
        if projeto not in self.projetos:
            raise ValueError("Projeto não está associado ao funcionário.")
        ocorrencia = Ocorrencia(id, self, descricao, tipo, projeto, prioridade)
        projeto.adicionar_ocorrencia(ocorrencia)
        self.ocorrencias.append(ocorrencia)

        return ocorrencia
    
    def fechar_ocorrencia(self, id):
        for i in range(0, len(self.ocorrencias)+1):
            if i == len(self.ocorrencias):
                raise ValueError("Ocorrência não ligada ao funcionário.")
            if self.ocorrencias[i].id == id:
                ocorrencia = self.ocorrencias[i]
                ocorrencia.fechar_ocorrencia()
                self.ocorrencias.pop(i)
                break
    
    def remover_ocorrencia(self, id):
        for i in range(0, len(self.ocorrencias)+1):
            if i == len(self.ocorrencias):
                raise ValueError("Ocorrência não ligada ao funcionário.")
            if self.ocorrencias[i].id == id:
                self.ocorrencias[i]
                self.ocorrencias.pop(i)
                break
    
    def adicionar_ocorrencia(self, ocorrencia):
        if len(self.ocorrencias) >= 10:
            raise ValueError("Número máximo de ocorrências atingido.")
        self.ocorrencias.append(ocorrencia)