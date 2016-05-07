import random


class Tambola:
    def __init__(self):
        self._elementos = []

    def carregar(self, elementos):
        self._elementos.extend(elementos)

    def misturar(self):
        random.shuffle(self._elementos)
