from unittest.mock import patch
import unittest
from unittest.case import TestCase

from os import path
import sys

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)

from cursoaulahu.tambola import Tambola


def shuffle_mock(lista):
    lista.reverse()


class TambolaTestes(TestCase):
    def test_carregar(self):
        tambola = Tambola()
        tambola.carregar([1, 2])
        self.assertListEqual([1, 2], tambola._elementos)
        tambola.carregar([3, 4])
        self.assertListEqual([1, 2, 3, 4], tambola._elementos)

    @patch('cursoaulahu.tambola.random')
    def test_misturar(self, ramdon_mock):
        ramdon_mock.shuffle = shuffle_mock
        tambola = Tambola()
        items = [1, 2]
        tambola.carregar(items)
        tambola.misturar()
        self.assertEqual([2, 1], tambola._elementos)

    @patch('cursoaulahu.tambola.random')
    def test_sortear(self, ramdon_mock):
        ramdon_mock.shuffle = shuffle_mock
        tambola = Tambola()
        items = [1, 2]
        tambola.carregar(items)
        tambola.misturar()
        valor_sorteado = tambola.sortear()
        self.assertEqual(1, valor_sorteado)
        valor_sorteado = tambola()
        self.assertEqual(2, valor_sorteado)

if __name__ == '__main__':
    unittest.main()
