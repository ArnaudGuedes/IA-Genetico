import copy
import random

class Cromossomo:
    def __init__(self, genes=None):
        # 75 bits se não forem fornecidos
        self.genes = genes if genes is not None else [random.randint(0, 1) for _ in range(75)]

    def clone(self):
        return Cromossomo(copy.deepcopy(self.genes))

    def get_genes(self):
        return self.genes

    def get_matriz(self):
        """
        Converte os 75 bits para uma matriz 5x5 com valores inteiros de 0 a 4
        Cada atributo (cor, nacionalidade, ...) é representado por 3 bits → total 5 casas × 5 atributos = 75 bits
        """
        matriz = []
        for i in range(0, 75, 15):  # Cada casa tem 15 bits = 5 atributos × 3 bits
            casa = []
            for j in range(0, 15, 3):  # Cada atributo = 3 bits
                bits = self.genes[i + j: i + j + 3]
                valor = int("".join(str(b) for b in bits), 2)
                # Valor máximo permitido: 0–4. Se maior, reduz (ajuste opcional)
                valor = valor % 5
                casa.append(valor)
            matriz.append(casa)
        return matriz

    def to_fenotipo(self, mapas):
        """
        Traduz a matriz decodificada para uma versão legível (usando os mapas)
        """
        matriz = self.get_matriz()
        casas = []
        for casa in matriz:
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
        """
        Exibe o fenótipo do cromossomo de forma formatada
        """
        casas = self.to_fenotipo(mapas)
        for i, casa in enumerate(casas):
            print(f"Casa {i+1}: {casa}")
