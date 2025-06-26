from Cromossomo import Cromossomo
import random

class Populacao:
    def __init__(self, tamanho):
        self.individuos = [self._gerar_cromossomo() for _ in range(tamanho)]

    def _gerar_cromossomo(self):
        # Cria 75 bits aleatórios (0 ou 1)
        genes = [random.randint(0, 1) for _ in range(75)]
        return Cromossomo(genes)

    def get_individuos(self):
        return self.individuos
