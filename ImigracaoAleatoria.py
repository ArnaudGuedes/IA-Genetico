import random
from Cromossomo import Cromossomo

class ImigracaoAleatoria:
    @staticmethod
    def gerar(qtd):

        imigrantes = []

        for _ in range(qtd):
            matriz = []


            colunas = [random.sample(range(5), 5) for _ in range(5)]


            for i in range(5):
                casa = [colunas[j][i] for j in range(5)]
                matriz.append(casa)

            # Codifica em genes binários
            genes = []
            for casa in matriz:
                for valor in casa:
                    bin_str = f"{valor:03b}"
                    genes.extend([int(b) for b in bin_str])

            imigrantes.append(Cromossomo(genes))

        return imigrantes
