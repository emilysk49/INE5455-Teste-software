from datetime import date

class Projeto():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.funcionarios = []
        self.data_inicio = None
        self.data_fim = None

    def adicionar_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            raise ValueError("Funcionário já adicionado ao projeto.")
        self.funcionarios.append(funcionario)

    def adicionar_data_inicio(self, data_inicio):
        ano, mes, dia = data_inicio.split('-')
        self.data_inicio = date(int(ano), int(mes),int(dia))

    def adicionar_data_fim(self, data_fim):
        ano, mes, dia = data_fim.split('-')
        data = date(int(ano), int(mes),int(dia))
        if self.data_inicio and self.data_inicio > data:
            raise ValueError("Data de fim não pode ser anterior à data de início.")
        self.data_fim = data
