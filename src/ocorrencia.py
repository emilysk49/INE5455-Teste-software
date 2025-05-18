from enum import Enum

class TipoOcorrencia(Enum):
    TAREFA = "Tarefa"
    BUG = "Bug"
    MELHORIA = "Melhoria"

class EstadoOcorrencia(Enum):
    ABERTO = "Aberto"
    FECHADO = "Fechado"

class PrioridadeOcorrencia(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

class Ocorrencia:
    def __init__(self, id, funcionario, descricao, tipo, projeto, prioridade=PrioridadeOcorrencia.MEDIA):
        if descricao is None or descricao == "":
            raise ValueError("Descrição não pode ser vazia")
        if not isinstance(prioridade, PrioridadeOcorrencia):
            raise ValueError("Prioridade deve ser do tipo PrioridadeOcorrencia")
        self.id = id
        self.descricao = descricao
        self.estado = EstadoOcorrencia.ABERTO
        self.tipo = tipo
        self.funcionario = funcionario
        self.projeto = projeto
        self.prioridade = prioridade
    
    def modificar_prioridade(self, prioridade):
        if not isinstance(prioridade, PrioridadeOcorrencia):
            raise ValueError("Prioridade deve ser do tipo PrioridadeOcorrencia")
        self.prioridade = prioridade