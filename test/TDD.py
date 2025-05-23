import unittest
from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto
from test.testHelper import *
from src.ocorrencia import *

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
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        self.assertEqual(f1.ocorrencias[0], p1.ocorrencias[0])

    def test_28_inserir_ocorrencia_projeto_outra_empresa(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        empresa_Y, funcionarios2, projetos2 = testHelper.empresa_com_funcionarios_e_projetos(1,1)
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

    def test_30_inserir_ocorrencia_projeto_nao_pertence(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(2,2)
        f1 = funcionarios[0]
        p1 = projetos[0]
        f2 = funcionarios[1]
        p2 = projetos[1]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p2)
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p2)

    def test_31_inserir_mais_de_uma_ocorrencia(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(3,1)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        f3 = funcionarios[2]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p1)
        empresa_W.adicionar_funcionario_em_projeto(f3, p1)
        f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        f2.criar_ocorrencia(457, "Descrição da ocorrência 2", TipoOcorrencia.TAREFA, p1)
        f3.criar_ocorrencia(890, "Descrição da ocorrência 3", TipoOcorrencia.BUG, p1)
        self.assertEqual(len(p1.ocorrencias), 3)
        self.assertEqual(f1.ocorrencias[0], p1.ocorrencias[0])
        self.assertEqual(f2.ocorrencias[0], p1.ocorrencias[1])
        self.assertEqual(f3.ocorrencias[0], p1.ocorrencias[2])

    def test_32_funcionario_responsavel_mais_de_uma_ocorrencia(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        testHelper.criar_ocorrencias(f1, [TipoOcorrencia.MELHORIA, TipoOcorrencia.TAREFA, TipoOcorrencia.BUG], p1)
        self.assertEqual(len(p1.ocorrencias), 3)
        self.assertEqual(len(f1.ocorrencias), 3)
        self.assertEqual(f1.ocorrencias[0], p1.ocorrencias[0])
        self.assertEqual(f1.ocorrencias[1], p1.ocorrencias[1])
        self.assertEqual(f1.ocorrencias[2], p1.ocorrencias[2])

    def test_33_bloqueio_ao_tentar_inserir_11_ocorrencias(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        testHelper.criar_ocorrencias(f1, [TipoOcorrencia.MELHORIA, TipoOcorrencia.BUG]*5, p1) # Criando 10 ocorrencias
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(11, "Descrição da ocorrência 11", TipoOcorrencia.TAREFA, p1)

    def test_34_instanciar_ocorrencia_sem_resumo(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(1, "", TipoOcorrencia.MELHORIA, p1)

    def test_35_instanciar_ocorrencia_com_prioridade_alta(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1, PrioridadeOcorrencia.ALTA)
        self.assertEqual(ocorrencia1.prioridade, PrioridadeOcorrencia.ALTA)
    
    def test_36_instanciar_ocorrencia_com_prioridade_media(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1, PrioridadeOcorrencia.MEDIA)
        self.assertEqual(ocorrencia1.prioridade, PrioridadeOcorrencia.MEDIA)
    
    def test_37_instanciar_ocorrencia_com_prioridade_baixa(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1, PrioridadeOcorrencia.BAIXA)
        self.assertEqual(ocorrencia1.prioridade, PrioridadeOcorrencia.BAIXA)
    
    def test_38_instanciar_ocorrencia_com_prioridade_inexistente(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1, "inexistente")
        
    def test_39_modificar_prioridade_ocorrencia_para_alta(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        ocorrencia1.modificar_prioridade(PrioridadeOcorrencia.ALTA)
        self.assertEqual(ocorrencia1.prioridade, PrioridadeOcorrencia.ALTA)
    
    def test_40_modificar_prioridade_ocorrencia_para_media(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1, PrioridadeOcorrencia.BAIXA)
        ocorrencia1.modificar_prioridade(PrioridadeOcorrencia.MEDIA)
        self.assertEqual(ocorrencia1.prioridade, PrioridadeOcorrencia.MEDIA)

    def test_41_modificar_prioridade_ocorrencia_para_baixa(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        ocorrencia1.modificar_prioridade(PrioridadeOcorrencia.BAIXA)
        self.assertEqual(ocorrencia1.prioridade, PrioridadeOcorrencia.BAIXA)
    
    def test_42_modificar_prioridade_ocorrencia_para_inexistente(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        with self.assertRaises(ValueError):
            ocorrencia1.modificar_prioridade("inexistente")

    def test_43_fechar_uma_ocorrencia_de_um_funcionario_com_1_ocorrencia(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia = f1.criar_ocorrencia(1, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        f1.fechar_ocorrencia(ocorrencia.id)
        self.assertEqual(len(f1.ocorrencias), 0)
        self.assertEqual(ocorrencia.estado, EstadoOcorrencia.FECHADO)

    def test_44_fechar_uma_ocorrencia_de_um_funcionario_com_5_ocorrencias(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencias = testHelper.criar_ocorrencias(f1, [TipoOcorrencia.MELHORIA]*5, p1)
        f1.fechar_ocorrencia(ocorrencias[0].id)
        self.assertEqual(len(f1.ocorrencias), 4)
        self.assertEqual(ocorrencias[0].estado, EstadoOcorrencia.FECHADO)

    def test_45_fechar_uma_ocorrencia_de_um_funcionario_com_10_ocorrencias_e_adicionar_ocorrencia_depois(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencias = testHelper.criar_ocorrencias(f1, [TipoOcorrencia.MELHORIA]*10, p1)
        f1.fechar_ocorrencia(ocorrencias[0].id)
        f1.criar_ocorrencia(11, "Descrição da ocorrência 11", TipoOcorrencia.MELHORIA, p1)
        self.assertEqual(len(f1.ocorrencias), 10)
        self.assertEqual(ocorrencias[0].estado, EstadoOcorrencia.FECHADO)
        self.assertEqual(len(p1.ocorrencias), 11)

    def test_46_funcionario_tenta_fechar_uma_ocorrencia_ligada_a_outr_ao_funcionario(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(2,1)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p1)
        ocorrencia = f2.criar_ocorrencia(1, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        with self.assertRaises(ValueError):
            f1.fechar_ocorrencia(ocorrencia.id)

    def test_47_fechar_ocorrencia_ja_fechado(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia = f1.criar_ocorrencia(1, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        f1.fechar_ocorrencia(ocorrencia.id)
        with self.assertRaises(ValueError):
            f1.fechar_ocorrencia(ocorrencia.id)

    def test_48_modificar_responsavel_por_funcionario_do_mesmo_projeto(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(2,1)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p1)
        ocorrencia = f1.criar_ocorrencia(1, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        p1.modificar_responsavel(f2, ocorrencia)
        self.assertEqual(ocorrencia.funcionario, f2)
        self.assertEqual(len(f1.ocorrencias), 0)
        self.assertEqual(len(f2.ocorrencias), 1)

    def test_49_modificar_responsavel_por_funcionario_do_projeto_diferente(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(2,2)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        p1 = projetos[0]
        p2 = projetos[1]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p2)
        ocorrencia = f1.criar_ocorrencia(1, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        with self.assertRaises(ValueError):
            p1.modificar_responsavel(f2, ocorrencia)

    def test_50_modificar_responsavel_por_funcionario_do_mesmo_projeto_mas_ocorrencia_nao_pertence(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(2,2)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        p1 = projetos[0]
        p2 = projetos[1]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p1)
        ocorrencia = Ocorrencia(5616, f1, "Descrição 1", TipoOcorrencia.TAREFA, p2)
        with self.assertRaises(ValueError):
            p1.modificar_responsavel(f2, ocorrencia)

    def test_51_modificar_responsavel_por_funcionario_do_mesmo_projeto_mas_possui_10_ocorrencias(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(2,1)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p1)
        testHelper.criar_ocorrencias(f1, [TipoOcorrencia.MELHORIA]*10, p1)
        ocorrencia = f2.criar_ocorrencia(222, "Descrição da ocorrência 222", TipoOcorrencia.MELHORIA, p1)
        with self.assertRaises(ValueError):
            p1.modificar_responsavel(f1, ocorrencia)

    def test_52_modificar_responsavel_onde_nao_era_responsavel_da_ocorrencia(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(3,1)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        f3 = funcionarios[2]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p1)
        empresa_W.adicionar_funcionario_em_projeto(f3, p1)
        ocorrencia = f3.criar_ocorrencia(1, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        ocorrencia.funcionario = f1 # Apenas para teste
        with self.assertRaises(ValueError):
            p1.modificar_responsavel(f2, ocorrencia)

    def test_53_modificar_resposavel_ocorrencia_ja_fechada(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(2,1)
        f1 = funcionarios[0]
        f2 = funcionarios[1]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        empresa_W.adicionar_funcionario_em_projeto(f2, p1)
        ocorrencia = f1.criar_ocorrencia(1, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        ocorrencia.fechar_ocorrencia() # Apenas para teste
        with self.assertRaises(ValueError):
            p1.modificar_responsavel(f2, ocorrencia)

    def test_54_instanciar_ocorrencia_com_tipo_tarefa(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.TAREFA, p1)
        self.assertEqual(ocorrencia1.tipo, TipoOcorrencia.TAREFA)
    
    def test_55_instanciar_ocorrencia_com_tipo_bug(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.BUG, p1)
        self.assertEqual(ocorrencia1.tipo, TipoOcorrencia.BUG)
    
    def test_56_instanciar_ocorrencia_com_tipo_melhoria(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        ocorrencia1 = f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        self.assertEqual(ocorrencia1.tipo, TipoOcorrencia.MELHORIA)
    
    def test_57_instanciar_ocorrencia_com_tipo_inexistente(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(123, "Descrição da ocorrência 1", "inexistente", p1)

    def test_58_criar_ocorrencia_com_id_existente(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, p1)
        with self.assertRaises(ValueError):
            f1.criar_ocorrencia(123, "Descrição da ocorrência 2", TipoOcorrencia.MELHORIA, p1)

    def test_59_criar_ocorrencia_com_tipo_errado(self):
        empresa_W, funcionarios, projetos = testHelper.empresa_com_funcionarios_e_projetos(1,1)
        f1 = funcionarios[0]
        p1 = projetos[0]
        empresa_W.adicionar_funcionario_em_projeto(f1, p1)
        with self.assertRaises(TypeError):
            f1.criar_ocorrencia(123, "Descrição da ocorrência 1", TipoOcorrencia.MELHORIA, "inexistente")
if __name__ == '__main__':
    unittest.main()
