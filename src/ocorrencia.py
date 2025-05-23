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
        if not isinstance(tipo, TipoOcorrencia):
            raise ValueError("Tipo deve ser do tipo TipoOcorrencia")
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

    def fechar_ocorrencia(self):
        self.estado = EstadoOcorrencia.FECHADO
    
    def alterar_funcionario(self, funcionario):
        if self.estado == EstadoOcorrencia.FECHADO:
            raise ValueError("Não é possível alterar o funcionário de uma ocorrência fechada.")
        self.funcionario.remover_ocorrencia(self.id)
        self.funcionario = funcionario
        funcionario.adicionar_ocorrencia(self)