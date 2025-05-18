from enum import Enum

class TipoOcorrencia(Enum):
    TAREFA = "Tarefa"
    BUG = "Bug"
    MELHORIA = "Melhoria"

class EstadoOcorrencia(Enum):
    ABERTO = "Aberto"
    FECHADO = "Fechado"


class Ocorrencia:
    def __init__(self, id, funcionario, descricao, tipo, projeto):
        if descricao is None or descricao == "":
            raise ValueError("Descrição não pode ser vazia")
        self.id = id
        self.descricao = descricao
        self.estado = EstadoOcorrencia.ABERTO
        self.tipo = tipo
        self.funcionario = funcionario
        self.projeto = projeto