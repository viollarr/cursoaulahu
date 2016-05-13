import sys
from os import path

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)


class Mamifero:
    patas = 2

    def __init__(self, nome):
        self.nome = nome

    def fazer_barulho(self):
        raise NotImplementedError('deveria implementar esse cara')

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Mamifero({!r})'.format(self.nome)


class Cao(Mamifero):
    patas = 4

    def __init__(self, nome, nervoso=False):
        super().__init__(nome)
        self.nervoso = nervoso

    def fazer_barulho(self):
        if self.nervoso:
            return 'Gram Gram'
        return 'Au Au'

    def __repr__(self):
        return 'Cao({!r},{!r})'.format(self.nome, self.nervoso)

# rex = Cao('Rex')
# print(rex)
# print(rex.patas)
# print(id(rex.patas))
#
# toto = Cao('Totó')
# print(toto)
# print(id(toto.patas))
# print(toto.__dict__)
# toto.patas = 3
# print(toto.__dict__)
# print(toto.patas)
# del toto.patas
# print(toto.__dict__)
# print(toto.patas)
# print(rex.patas)
# print(Cao.patas)
