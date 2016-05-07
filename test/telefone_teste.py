from os import path
import sys
import unittest

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)

from cursoaulahu.telefonista import Telefone


class TelefoneTestes(unittest.TestCase):
    def test_telefonar(self):
        telefone = Telefone()
        self.assertEqual('Telefonando para 2345678', telefone.telefonar('2345678'))
        self.assertEqual('Telefonando para 8765432', telefone.telefonar('8765432'))


if __name__ == '__main__':
    unittest.main()
