from datetime import date
from src.funcionario import Funcionario

class Projeto():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.funcionarios = []
        self.data_inicio = None
        self.data_fim = None
        self.empresa = None
        self.ocorrencias = []

    def adicionar_a_empresa(self, empresa):
        if self.empresa is not None:
            raise ValueError("Projeto já associado a uma empresa.")
        self.empresa = empresa

    def adicionar_funcionario(self, funcionario):
        if not isinstance(funcionario, Funcionario):
            raise TypeError("Funcionário deve ser do tipo Funcionario.")
        if funcionario in self.funcionarios:
            raise ValueError("Funcionário já adicionado ao projeto.")
        self.funcionarios.append(funcionario)

    def adicionar_ocorrencia(self, ocorrencia):
        if (ocorrencia.id in [o.id for o in self.ocorrencias]):
            raise ValueError("Ocorrência com esse ID já adicionada ao projeto.")
        self.ocorrencias.append(ocorrencia)

    def adicionar_data_inicio(self, data_inicio):
        ano, mes, dia = data_inicio.split('-')
        data = date(int(ano), int(mes),int(dia))
        if self.data_fim and data > self.data_fim:
            raise ValueError("Data de início não pode ser posterior à data de fim.")
        self.data_inicio = data

    def adicionar_data_fim(self, data_fim):
        ano, mes, dia = data_fim.split('-')
        data = date(int(ano), int(mes),int(dia))
        if self.data_inicio and self.data_inicio > data:
            raise ValueError("Data de fim não pode ser anterior à data de início.")
        self.data_fim = data

    def modificar_responsavel(self, funcionario, ocorrencia):
        if funcionario not in self.funcionarios:
            raise ValueError("Funcionário não está associado a este projeto.")
        if ocorrencia not in self.ocorrencias:
            raise ValueError("Ocorrência não está associada a este projeto.")
        ocorrencia.alterar_funcionario(funcionario)