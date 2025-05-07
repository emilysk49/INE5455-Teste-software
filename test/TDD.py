import unittest
from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto
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

if __name__ == '__main__':
    unittest.main()
