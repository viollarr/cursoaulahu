import unittest
from os import path
import sys

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)

from cursoaulahu.telefonista import Telefonista, Telefone


class TelefoneMoc(Telefone):
    def telefonar(self, numero):
        return 'Tel fake para {}'.format(numero)


class TelefonistaTeste(unittest.TestCase):
    def test_adicionar_um_contato(self):
        telefonista = Telefonista()
        contato = ('Victor', '2345678')
        telefonista.adicionar_contato(*contato)
        self.assertEqual([contato], telefonista._contatos)

    def test_adicionar_dois_contatos(self):
        victor = ('Victor', '2345678')
        renzo = ('Renzo', '8765432')
        telefonista = Telefonista()
        telefonista.adicionar_contato(*victor)
        telefonista.adicionar_contato(*renzo)
        self.assertEqual([victor, renzo], telefonista._contatos)

    def test_telefonar_um_contato(self):
        telefonista = Telefonista()
        telefonista._telefone = TelefoneMoc()
        contato = ('Victor', '2345678')
        telefonista.adicionar_contato(*contato)
        resultado_da_ligacao = telefonista.ligar()
        self.assertEqual('Contato Victor, Tel fake para 2345678', resultado_da_ligacao)

    def test_telefonar_dois_contatos(self):
        telefonista = Telefonista()
        telefonista._telefone = TelefoneMoc()
        victor = ('Victor', '2345678')
        renzo = ('Renzo', '8765432')
        telefonista.adicionar_contato(*victor)
        telefonista.adicionar_contato(*renzo)
        resultado_da_ligacao = telefonista.ligar()
        self.assertEqual('Contato Victor, Tel fake para 2345678\nContato Renzo, Tel fake para 8765432',
                         resultado_da_ligacao)


if __name__ == '__main__':
    unittest.main()
