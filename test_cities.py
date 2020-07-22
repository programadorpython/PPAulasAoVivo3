import unittest
from city_functions import cidade_pais
from Carros.carros import Carro

class CidadesTestCase(unittest.TestCase):
    """
    Testes para as funções em 'city_functions.py'
    """

    def test_cidade_pais(self):
        """
        Faz um simlpes teste as strings cidade e pais.
        :return:
        """
        carro = Carro('Fiesta', 'Ford')
        # var_cidade_pais = cidade_pais('santiago', 'chile')
        var_carro_concluido = carro.carro_concluido()
        self.assertEqual(var_carro_concluido, 'Fiesta está pronto para ser vendido!')
        # self.assertEqual(var_cidade_pais, 'Santiago, Chile')

if __name__ == 'main':
    unittest.main()