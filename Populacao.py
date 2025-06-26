from Cromossomo import Cromossomo
import random

class Populacao:
    def __init__(self, tamanho):
        self.individuos = [self._gerar_cromossomo() for _ in range(tamanho)]

    def _gerar_cromossomo(self):

        matriz = []

        # Para cada atributo (coluna), gere uma permutação de 0 a 4
        colunas = [random.sample(range(5), 5) for _ in range(5)]  # 5 atributos

        # Transpor colunas para linhas (casas)
        for i in range(5):  # 5 casas
            casa = [colunas[j][i] for j in range(5)]  # pega os 5 atributos da casa i
            matriz.append(casa)

        # Converte a matriz para vetor de bits (75 bits = 5 casas × 5 atributos × 3 bits)
        genes = []
        for casa in matriz:
            for valor in casa:
                bin_str = f"{valor:03b}"  # 3 bits por valor
                genes.extend([int(b) for b in bin_str])

        return Cromossomo(genes)

    def get_individuos(self):
        return self.individuos
