import random
from Cromossomo import Cromossomo

class Crossover:
    @staticmethod
    def cruzar(pai1, pai2):
        """
        Realiza crossover entre dois cromossomos binários,
        garantindo que cada coluna (atributo) do filho tenha valores únicos (0–4).
        Corrige duplicatas de forma inteligente, substituindo apenas onde necessário.
        Retorna um novo Cromossomo.
        """
        m1 = pai1.get_matriz()
        m2 = pai2.get_matriz()

        nova_matriz = [[-1 for _ in range(5)] for _ in range(5)]  # 5 casas × 5 atributos

        # Recombinação aleatória entre os pais
        for linha in range(5):
            for col in range(5):
                nova_matriz[linha][col] = m1[linha][col] if random.random() < 0.5 else m2[linha][col]

        # Reparo inteligente por coluna
        for col in range(5):
            valores = [nova_matriz[linha][col] for linha in range(5)]
            contagem = {v: valores.count(v) for v in valores}
            duplicados = [v for v, c in contagem.items() if c > 1]
            faltando = [v for v in range(5) if v not in valores]

            if duplicados:
                idx_corrigir = []
                seen = set()
                for i in range(5):
                    val = nova_matriz[i][col]
                    if val in seen:
                        idx_corrigir.append(i)
                    else:
                        seen.add(val)

                random.shuffle(faltando)
                for i, novo_valor in zip(idx_corrigir, faltando):
                    nova_matriz[i][col] = novo_valor

        # Codificação final para vetor binário
        novo_genes = []
        for casa in nova_matriz:
            for valor in casa:
                bin_str = f"{valor:03b}"
                novo_genes.extend([int(b) for b in bin_str])

        return Cromossomo(novo_genes)
