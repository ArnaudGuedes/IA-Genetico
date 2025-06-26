import numpy as np

class Roleta:
    def __init__(self, taxa_sobrevivencia=0.75):
        self.taxa_sobrevivencia = taxa_sobrevivencia

    def girar(self, populacao, fitnesses):
        total = len(populacao)
        n_selecionados = int(total * self.taxa_sobrevivencia)

        # Proteção para fitness total 0
        total_fitness = sum(fitnesses)
        if total_fitness == 0:
            return np.random.choice(populacao, size=n_selecionados, replace=False).tolist()


        probabilidades = [f / total_fitness for f in fitnesses]


        selecionados_idx = np.random.choice(
            range(total),
            size=n_selecionados,
            replace=False,
            p=probabilidades
        )

        sobreviventes = [populacao[i] for i in selecionados_idx]
        return sobreviventes

    def selecionar_elites(individuos, qtd):

        return sorted(individuos, key=lambda ind: ind.get_fitness(), reverse=True)[:qtd]