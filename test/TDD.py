import unittest
from src.empresa import Empresa

class TDD(unittest.TestCase):
    def test1_criar_empresa_W(self):
        empresa_W = Empresa("W")
        self.assertIsInstance(empresa_W, Empresa)
        self.assertEqual(empresa_W.nome, "W")

    def test2_criar_funcionario(self):
        jose = Funcionario("José")
        self.assertIsInstance(jose, Funcionario)
        self.assertEqual(jose.nome, "Jose")

if __name__ == '__main__':
    unittest.main()
