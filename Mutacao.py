import random
from Cromossomo import Cromossomo

class Mutacao:
    @staticmethod
    def aplicar(cromossomo):

        matriz = cromossomo.get_matriz()


        col = random.randint(0, 4)


        i, j = random.sample(range(5), 2)
        matriz[i][col], matriz[j][col] = matriz[j][col], matriz[i][col]

        # Reconstrói os genes binários a partir da matriz mutada
        novo_genes = []
        for casa in matriz:
            for valor in casa:
                bin_str = f"{valor:03b}"
                novo_genes.extend([int(b) for b in bin_str])

        return Cromossomo(novo_genes)
