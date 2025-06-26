# cromossomo.py

import copy

class Cromossomo:
    def __init__(self, matriz):
        self.matriz = matriz

    def get_matriz(self):
        return self.matriz

    def to_fenotipo(self, mapas):
        casas = []
        for casa in self.matriz:
            casa_legivel = {
                "cor": mapas["cor"][casa[0]],
                "nacionalidade": mapas["nacionalidade"][casa[1]],
                "bebida": mapas["bebida"][casa[2]],
                "cigarro": mapas["cigarro"][casa[3]],
                "animal": mapas["animal"][casa[4]]
            }
            casas.append(casa_legivel)
        return casas

    def mostrar(self, mapas):
        casas = self.to_fenotipo(mapas)
        for i, casa in enumerate(casas):
            print(f"Casa {i+1}: {casa}")

    def clone(self):
        return Cromossomo(copy.deepcopy(self.matriz))
