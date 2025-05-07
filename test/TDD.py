import unittest
from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto

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

if __name__ == '__main__':
    unittest.main()
