import unittest

class TDD(unittest.TestCase):
    def test1_criar_empresa_W(self):
        empresa_W = Empresa("W")
        self.assertIsInstance(empresa_W, Empresa)
        self.assertEqual(empresa_W.nome, "W")


if __name__ == '__main__':
    unittest.main()
