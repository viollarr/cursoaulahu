import unittest
from unittest import TestCase
# from unittest.mock import Mock
from os import path
import sys

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)

from cao import cachorro


class CaoTeste(TestCase):

    def test_nomear_cao_rex_true(self):
        result = cachorro.Cao('Rex')
        self.assertEqual('Rex', result.nome)

    def test_get_patas_mamiferos_deficiente(self):
        result = cachorro.Cao('Rex')
        result.patas = 3
        self.assertEqual(3, result.patas)

if __name__ == '__main__':
    unittest.main()
