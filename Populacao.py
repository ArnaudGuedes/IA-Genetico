from Cromossomo import Cromossomo
import random

class Populacao:
    def __init__(self, tamanho):
        self.individuos = [self._gerar_cromossomo() for _ in range(tamanho)]

    def _gerar_cromossomo(self):
        atributos = [random.sample(range(5), 5) for _ in range(5)]
        matriz = [list(casa) for casa in zip(*atributos)]
        return Cromossomo(matriz)

    def get_individuos(self):
        return self.individuos
