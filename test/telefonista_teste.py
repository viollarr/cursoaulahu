import unittest
from unittest.mock import Mock
from os import path
import sys

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)

from cursoaulahu.telefonista import Telefonista, Telefone


class TelefoneMock(Telefone):
    def __init__(self):
        self.numero = None

    def telefonar(self, numero):
        self.numero = numero
        return 'Tel fake para {}'.format(self.numero)


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

    def test_telefonar_um_contato_sem_utilizar_pacote_mock(self):
        telefonista = Telefonista()
        telefone_mock = TelefoneMock()
        telefonista._telefone = telefone_mock
        contato = ('Victor', '2345678')
        telefonista.adicionar_contato(*contato)
        resultado_da_ligacao = telefonista.ligar()
        self.assertEqual('Contato Victor, Tel fake para 2345678', resultado_da_ligacao)
        self.assertEqual('2345678', telefone_mock.numero)

    def test_telefonar_um_contato_utilizando_pacote_mock(self):
        telefonista = Telefonista()
        telefone_mock = Mock()
        telefonista._telefone = telefone_mock
        telefone_mock.telefonar = Mock(return_value='Tel fake para 2345678')
        contato = ('Victor', '2345678')
        telefonista.adicionar_contato(*contato)
        resultado_da_ligacao = telefonista.ligar()
        telefone_mock.telefonar.assert_called_once_with('2345678')
        self.assertEqual('Contato Victor, Tel fake para 2345678', resultado_da_ligacao)

    def test_telefonar_dois_contatos(self):
        telefonista = Telefonista()
        telefone_mock = TelefoneMock()
        telefonista._telefone = telefone_mock
        victor = ('Victor', '2345678')
        renzo = ('Renzo', '8765432')
        telefonista.adicionar_contato(*victor)
        telefonista.adicionar_contato(*renzo)
        resultado_da_ligacao = telefonista.ligar()
        self.assertEqual('Contato Victor, Tel fake para 2345678\nContato Renzo, Tel fake para 8765432',
                         resultado_da_ligacao)


if __name__ == '__main__':
    unittest.main()
