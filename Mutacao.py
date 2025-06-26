import random
from Cromossomo import Cromossomo

class Mutacao:
    @staticmethod
    def aplicar(cromossomo):
        """
        Aplica uma mutação leve ao cromossomo: troca dois valores em uma mesma coluna aleatória.
        Preserva a restrição de unicidade por coluna.
        """
        matriz = cromossomo.get_matriz()

        # Escolhe uma coluna aleatória (atributo) para mutar
        col = random.randint(0, 4)

        # Escolhe duas linhas aleatórias para trocar os valores nessa coluna
        i, j = random.sample(range(5), 2)
        matriz[i][col], matriz[j][col] = matriz[j][col], matriz[i][col]

        # Reconstrói os genes binários a partir da matriz mutada
        novo_genes = []
        for casa in matriz:
            for valor in casa:
                bin_str = f"{valor:03b}"
                novo_genes.extend([int(b) for b in bin_str])

        return Cromossomo(novo_genes)
