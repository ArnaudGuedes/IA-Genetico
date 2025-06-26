import random
from Cromossomo import Cromossomo

class ImigracaoAleatoria:
    @staticmethod
    def gerar(qtd):
        """
        Gera 'qtd' indivíduos aleatórios válidos (sem repetições por coluna).
        Cada indivíduo terá genes binários consistentes com o modelo original.
        """
        imigrantes = []

        for _ in range(qtd):
            matriz = []

            # Para cada coluna (atributo), sorteia uma permutação de 0 a 4
            colunas = [random.sample(range(5), 5) for _ in range(5)]

            # Transpõe colunas para obter a matriz casa x atributo
            for i in range(5):  # 5 casas
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
