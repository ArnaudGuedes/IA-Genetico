import random
from Fitness import Fitness
from Roleta import Roleta
from Crossover import Crossover
from Mutacao import Mutacao
from ImigracaoAleatoria import ImigracaoAleatoria

class EvolucaoGenetica:
    def __init__(self):
        self.fitness_calc = Fitness()
        self.roleta = Roleta()

    def avaliar_populacao(self, individuos):
        resultados = []
        fitnesses = []
        for cromo in individuos:
            fit, regras = self.fitness_calc.calcular(cromo)
            resultados.append((cromo, fit, regras))
            fitnesses.append(fit)
        return resultados, fitnesses

    def selecionar_sobreviventes(self, individuos, fitnesses, taxa_sobrevivencia, genes_elites):
        self.roleta.taxa_sobrevivencia = taxa_sobrevivencia
        sobreviventes = self.roleta.girar(individuos, fitnesses)
        return [s for s in sobreviventes if tuple(s.get_genes()) not in genes_elites]

    def selecionar_elites(self, individuos, fitnesses, n):
        populacao_avaliada = [(cromo, fit) for cromo, fit in zip(individuos, fitnesses)]
        ordenados = sorted(populacao_avaliada, key=lambda x: x[1], reverse=True)
        return [cromo for cromo, _ in ordenados[:n]]

    def aplicar_crossover(self, pais, taxa_crossover, filhos_necessarios):
        filhos = []
        tentativas = 0
        while len(filhos) < filhos_necessarios and tentativas < 1000:
            p1, p2 = random.sample(pais, 2)
            if random.random() < taxa_crossover:
                filho = Crossover.cruzar(p1, p2)
            else:
                filho = p1.clone()
            filhos.append((filho, "crossover"))
            tentativas += 1
        return filhos

    def aplicar_mutacao(self, individuos_com_origem, taxa_mutacao):
        mutados = []
        houve_mutacao = False
        for cromo, origem in individuos_com_origem:
            foi_mutado = False
            if random.random() < taxa_mutacao:
                cromo = Mutacao.aplicar(cromo)
                foi_mutado = True
                houve_mutacao = True
            mutados.append((cromo, origem, foi_mutado))

        if not houve_mutacao and mutados:
            idx = random.randint(0, len(mutados) - 1)
            cromo_forcado, origem_forcado, _ = mutados[idx]
            cromo_forcado = Mutacao.aplicar(cromo_forcado)
            mutados[idx] = (cromo_forcado, origem_forcado, True)

        return mutados

    def aplicar_imigracao(self, qtd):
        imigrantes = ImigracaoAleatoria.gerar(qtd)
        return [(ind, "imigrante", False) for ind in imigrantes]

    def evoluir(self, populacao_atual, taxa_elites, taxa_crossover, taxa_mutacao):
        tamanho_original = len(populacao_atual)


        resultados, fitnesses = self.avaliar_populacao(populacao_atual)


        qtd_elites = int(tamanho_original * taxa_elites)
        qtd_crossover = int(tamanho_original * taxa_crossover)
        qtd_imigrantes = tamanho_original - qtd_elites - qtd_crossover


        elites = self.selecionar_elites(populacao_atual, fitnesses, qtd_elites)
        elite_wrappers = [(e, "elite", False) for e in elites]
        genes_elites = [tuple(e.get_genes()) for e in elites]


        pais_disponiveis = self.selecionar_sobreviventes(populacao_atual, fitnesses, 1.0, genes_elites)
        filhos_crossover = self.aplicar_crossover(pais_disponiveis, taxa_crossover=1.0,
                                                  filhos_necessarios=qtd_crossover)


        filhos_mutados = self.aplicar_mutacao(filhos_crossover, taxa_mutacao)


        imigrantes = self.aplicar_imigracao(qtd_imigrantes)


        nova_populacao_info = elite_wrappers + filhos_mutados + imigrantes
        nova_populacao = [ind for ind, _, _ in nova_populacao_info]


        self.estatisticas = {
            "elites": qtd_elites,
            "crossover": qtd_crossover,
            "mutados": sum(1 for _, _, m in filhos_mutados if m),
            "imigrantes": qtd_imigrantes
        }

        return nova_populacao_info, nova_populacao, resultados

