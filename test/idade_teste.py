import unittest
from datetime import datetime
from unittest.case import TestCase
from os import path
import sys

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)

from cursoaulahu import idade
from cursoaulahu.idade import minutos_desde_nascimento


class IdadeTests(TestCase):
    def test_minutos_desde_nascimento(self):
        idade.get_agora = lambda: datetime(1985, 5, 3, 0, 0, 2)
        self.assertEqual(1, minutos_desde_nascimento(1985, 5, 3))


if __name__ == '__main__':
    unittest.main()
