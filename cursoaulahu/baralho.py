from random import shuffle


class Carta(object):
    naipes = 'paus ouros copas espadas'.split()
    valores = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return 'Carta({}, {})'.format(self.valor, self.naipe)

    def __str__(self):
        return self.valor + ' de ' + self.naipe

    @classmethod
    def todas(cls):
        return [cls(v, n) for n in cls.naipes for v in cls.valores]


class CartaDeTruco(Carta):
    valores = '2 3 4 5 6 7 J Q K A'.split()


class Baralho(object):
    def __init__(self):
        self.cartas = Carta.todas()

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __setitem__(self, key, value):
        self.cartas[key] = value


print(Carta.todas())
print(CartaDeTruco.todas())
baralho = Baralho()
print(len(baralho))
print(baralho[0])

shuffle(baralho)
for c in baralho:
    print(c)
