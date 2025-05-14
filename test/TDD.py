import unittest
from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto
from test.testHelper import *
from src.ocorrencia import *
from datetime import date

class TDD(unittest.TestCase):
    def test1_criar_empresa_W(self):
        empresa_W = Empresa("W")
        self.assertIsInstance(empresa_W, Empresa)
        self.assertEqual(empresa_W.nome, "W")

    def test2_criar_funcionario(self):
        jose = Funcionario("José")
        self.assertIsInstance(jose, Funcionario)
        self.assertEqual(jose.nome, "José")

    def test3_criar_projeto(self):
        projeto1_X = Projeto("X", 123)
        self.assertIsInstance(projeto1_X, Projeto)
        self.assertEqual(projeto1_X.nome, "X")
        self.assertEqual(projeto1_X.codigo, 123)

    def test4_adicionar_funcionario_empresa(self):
        empresa_W = Empresa("W")
        jose = Funcionario("José")
        empresa_W.adicionar_funcionario(jose)
        self.assertIn(jose, empresa_W.funcionarios)

    def test5_adicionar_funcionario_repetido_empresa(self):
        empresa_W = Empresa("W")
        jose = Funcionario("José")
        empresa_W.adicionar_funcionario(jose)
        with self.assertRaises(ValueError):
            empresa_W.adicionar_funcionario(jose)

    def test6_adicionar_projeto_empresa(self):
        empresa_W = Empresa("W")
        projeto1_X = Projeto("X", 123)
        empresa_W.adicionar_projeto(projeto1_X)
        self.assertIn(projeto1_X, empresa_W.projetos)

    def test7_adicionar_projeto_repetido_empresa(self):
        empresa_W = Empresa("W")
        projeto1_X = Projeto("X", 123)
        empresa_W.adicionar_projeto(projeto1_X)
        with self.assertRaises(ValueError):
            empresa_W.adicionar_projeto(projeto1_X)

    def test8_adicionar_funcionario_da_empresa_em_projeto(self):
        empresa_W = Empresa("W")
        jose = Funcionario("José")
        projeto1_X = Projeto("X", 123)
        empresa_W.adicionar_funcionario(jose)
        empresa_W.adicionar_projeto(projeto1_X)
        empresa_W.adicionar_funcionario_em_projeto(jose, projeto1_X)
        self.assertIn(jose, projeto1_X.funcionarios)
        self.assertIn(projeto1_X, jose.projetos)

    def test9_adicionar_funcionario_que_nao_trabalha_na_empresa_em_projeto(self):
        empresa_W = Empresa("W")
        jose = Funcionario("José")
        projeto1_X = Projeto("X", 123)
        empresa_W.adicionar_projeto(projeto1_X)
        with self.assertRaises(ValueError):
            empresa_W.adicionar_funcionario_em_projeto(jose, projeto1_X)

    def test10_1_adicionar_funcionario_em_um_projeto_repetido(self):
        jose = Funcionario("José")
        projeto1_X = Projeto("X", 123)
        projeto1_X.adicionar_funcionario(jose)
        with self.assertRaises(ValueError):
            projeto1_X.adicionar_funcionario(jose)
    
    def test10_2_adicionar_projeto_em_um_funcionario_repetido(self):
        jose = Funcionario("José")
        projeto1_X = Projeto("X", 123)
        jose.adicionar_projeto(projeto1_X)
        with self.assertRaises(ValueError):
            jose.adicionar_projeto(projeto1_X)

    def test11_adicionar_salario_funcionario(self):
        jose = Funcionario("José")
        jose.adicionar_salario(1000)
        self.assertEqual(jose.salario, 1000)

    def test12_adicionar_salario_funcionario_negativo(self):
        jose = Funcionario("José")
        with self.assertRaises(ValueError):
            jose.adicionar_salario(-1000)

    def test_13_adicionar_data_inicio_projeto(self):
        projeto1_X = Projeto("X", 123)
        data_inicio = "2025-01-31"
        projeto1_X.adicionar_data_inicio(data_inicio)
        self.assertEqual(projeto1_X.data_inicio.isoformat(), data_inicio)
    
    def test_14_adicionar_data_fim_projeto(self):
        projeto1_X = Projeto("X", 123)
        data_fim = "2025-02-28"
        projeto1_X.adicionar_data_fim(data_fim)
        self.assertEqual(projeto1_X.data_fim.isoformat(), data_fim)

    def test_15_adicionar_data_fim_anterior_a_data_inicio_comecando_pela_data_inicial(self):
        projeto1_X = Projeto("X", 123)
        data_inicio = "2025-02-28"
        data_fim = "2025-01-31"
        projeto1_X.adicionar_data_inicio(data_inicio)
        with self.assertRaises(ValueError):
            projeto1_X.adicionar_data_fim(data_fim)
    
    def test_16_adicionar_data_fim_anterior_a_data_inicio_comecando_pela_data_final(self):
        projeto1_X = Projeto("X", 123)
        data_fim = "2025-01-31"
        data_inicio = "2025-02-28"
        projeto1_X.adicionar_data_fim(data_fim)
        with self.assertRaises(ValueError):
            projeto1_X.adicionar_data_inicio(data_inicio)

    def test_17_adicionar_funcionario_com_tipo_diferente(self):
        empresa_W = Empresa("W")
        projeto1_X = Projeto("X", 123)
        with self.assertRaises(TypeError):
            empresa_W.adicionar_funcionario(projeto1_X)
    
    def test_18_adicionar_projeto_com_tipo_diferente(self):
        empresa_W = Empresa("W")
        jose = Funcionario("José")
        with self.assertRaises(TypeError):
            empresa_W.adicionar_projeto(jose)

    def test_19_incluir_funcionario_em_projeto_que_nao_pertence_a_empresa(self):
        empresa_W = Empresa("W")
        empresa_Y = Empresa("Y")
        projeto1_X = Projeto("X", 123)
        jose = Funcionario("José")
        empresa_Y.adicionar_projeto(projeto1_X)
        empresa_W.adicionar_funcionario(jose)
        with self.assertRaises(ValueError):
            empresa_W.adicionar_funcionario_em_projeto(jose, projeto1_X)

    def test_20_adicionar_funcionario_com_tipo_diferente_em_projeto(self):
        projeto1_X = Projeto("X", 123)
        with self.assertRaises(TypeError):
            projeto1_X.adicionar_funcionario(projeto1_X)
    
    def test_21_adicionar_projeto_com_tipo_diferente_em_funcionario(self):
        jose = Funcionario("José")
        with self.assertRaises(TypeError):
            jose.adicionar_projeto(jose)

    def test_22_adicionar_dois_funcionarios_a_um_projeto(self):
        empresa_W = Empresa("W")
        projeto1_X = Projeto("X", 123)
        jose = Funcionario("José")
        maria = Funcionario("Maria")
        empresa_W.adicionar_funcionario(jose)
        empresa_W.adicionar_funcionario(maria)
        empresa_W.adicionar_projeto(projeto1_X)
        empresa_W.adicionar_funcionario_em_projeto(jose, projeto1_X)
        empresa_W.adicionar_funcionario_em_projeto(maria, projeto1_X)
        self.assertIn(jose, projeto1_X.funcionarios)
        self.assertIn(maria, projeto1_X.funcionarios)
        self.assertIn(projeto1_X, jose.projetos)
        self.assertIn(projeto1_X, maria.projetos)
    
    def test_23_adicionar_dois_projetos_a_empresa(self):
        empresa_W = Empresa("W")
        projeto1_X = Projeto("X", 123)
        projeto2_Y = Projeto("Y", 456)
        empresa_W.adicionar_projeto(projeto1_X)
        empresa_W.adicionar_projeto(projeto2_Y)
        self.assertIn(projeto1_X, empresa_W.projetos)
        self.assertIn(projeto2_Y, empresa_W.projetos)

    def test_24_adicionar_dois_funcionarios_a_dois_projetos_diferentes(self):
        empresa_W = Empresa("W")
        projeto1_X = Projeto("X", 123)
        projeto2_Y = Projeto("Y", 456)
        jose = Funcionario("José")
        maria = Funcionario("Maria")
        empresa_W.adicionar_funcionario(jose)
        empresa_W.adicionar_funcionario(maria)
        empresa_W.adicionar_projeto(projeto1_X)
        empresa_W.adicionar_projeto(projeto2_Y)
        empresa_W.adicionar_funcionario_em_projeto(jose, projeto1_X)
        empresa_W.adicionar_funcionario_em_projeto(maria, projeto1_X)
        empresa_W.adicionar_funcionario_em_projeto(maria, projeto2_Y)
        empresa_W.adicionar_funcionario_em_projeto(jose, projeto2_Y)
        self.assertIn(jose, projeto1_X.funcionarios)
        self.assertIn(maria, projeto2_Y.funcionarios)
        self.assertIn(projeto1_X, jose.projetos)
        self.assertIn(projeto2_Y, maria.projetos)
        self.assertIn(projeto2_Y, jose.projetos)
        self.assertIn(projeto1_X, maria.projetos)

    def test_25_adicionar_projeto_a_empresa_diferente(self):
        empresa_W = Empresa("W")
        empresa_Y = Empresa("Y")
        projeto1_X = Projeto("X", 123)
        empresa_W.adicionar_projeto(projeto1_X)
        with self.assertRaises(ValueError):
            empresa_Y.adicionar_projeto(projeto1_X)

#################### AULA 2 TDD DAQUI PARA BAIXO ####################

    def test_26_instanciar_ocorrencia(self):
        projeto1_X = Projeto("X", 123)
        jose = Funcionario("José")
        ocorrencia1 = Ocorrencia(123, jose, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, projeto1_X)
        self.assertIsInstance(ocorrencia1, Ocorrencia)
        self.assertEqual(ocorrencia1.id, 123)
        self.assertEqual(ocorrencia1.descricao, "Descrição da ocorrência 1")
        self.assertEqual(ocorrencia1.tipo, TipoOcorrencia.MELHORIA)
        self.assertEqual(ocorrencia1.funcionario, jose)
        self.assertEqual(ocorrencia1.projeto, projeto1_X)
    
    def test_27_inserir_uma_ocorrencia_em_um_projeto(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_adicionar_funcionarios_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)

    def test_28_inserir_ocorrencia_projeto_outra_empresa(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_adicionar_funcionarios_projetos(1,1)
        empresa_Y, funcionarios2, projetos2 = testHelper.empresa_adicionar_funcionarios_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        f2 = funcionarios2[0]
        p2 = projetos2[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_Y.adicionar_funcionario_em_projeto(f2, p2)
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p2)
    
    def test_29_inserir_ocorrencia_funcionario_sem_empresa(self):
        empresa_W = Empresa("W")
        f1 = Funcionario("José")
        p1 = Projeto("X", 123)
        empresa_W.adicionar_projeto(p1)
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)

if __name__ == '__main__':
    unittest.main()
