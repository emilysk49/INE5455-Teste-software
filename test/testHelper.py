from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto

class testHelper():
    @staticmethod
    def empresa_com_funcionarios_e_projetos(qtd_funcionarios, qtd_projetos):
        empresa_W = Empresa("W")
        funcionarios = []
        projetos = []
        for f in range(qtd_funcionarios):
            funcionario = Funcionario("f"+str((f+1)))
            funcionarios.append(funcionario)
            empresa_W.adicionar_funcionario(funcionario)
        for p in range(qtd_projetos):
            projeto = Projeto("p"+str((p+1)), p+1)
            projetos.append(projeto)
            empresa_W.adicionar_projeto(projeto)

        return empresa_W, funcionarios, projetos

    @staticmethod
    def criar_ocorrencias(funcionario, tiposOcorrencias, projeto):
        ocorrencias = []
        for i in range(len(tiposOcorrencias)):
            ocorrencia = funcionario.criar_ocorrencia(i, f"Descrição da ocorrência {i}", tiposOcorrencias[i], projeto)
            ocorrencias.append(ocorrencia)
        return ocorrencias