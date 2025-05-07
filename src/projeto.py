from datetime import date

class Projeto():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            raise ValueError("Funcionário já adicionado ao projeto.")
        self.funcionarios.append(funcionario)

    def adicionar_data_inicio(self, data_inicio):
        ano, mes, dia = data_inicio.split('-')
        self.data_inicio = date(int(ano), int(mes),int(dia))
