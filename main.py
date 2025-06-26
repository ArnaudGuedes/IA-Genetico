from Populacao import Populacao
from EvolucaoGenetica import EvolucaoGenetica
import matplotlib.pyplot as plt

mapas = {
    "cor": ["Amarela", "Azul", "Branca", "Verde", "Vermelha"],
    "nacionalidade": ["Norueguês", "Dinamarquês", "Inglês", "Alemão", "Sueco"],
    "bebida": ["Água", "Chá", "Leite", "Café", "Cerveja"],
    "cigarro": ["Dunhill", "Blends", "Pall Mall", "Prince", "BlueMaster"],
    "animal": ["Cachorros", "Cavalos", "Gatos", "Pássaros", "Peixes"]
}

TAMANHO_POPULACAO = 50
TAXA_ELITES = 0.1
TAXA_CROSSOVER = 0.7
TAXA_MUTACAO = 0.5
NUM_GERACOES = 10
FITNESS_OBJETIVO = 99



if TAXA_ELITES + TAXA_CROSSOVER > 1.0:
    print("Erro: A soma da taxa excede 100%.")

    exit(1)


populacao = Populacao(TAMANHO_POPULACAO).get_individuos()
evolucao = EvolucaoGenetica()
avaliados, fitnesses = evolucao.avaliar_populacao(populacao)
melhor_fitness_geral = max(fitnesses)
geracao = 0


historico_fitness = []
historico_regras = []

while True:
    print(f"\n=== Geração {geracao} ===")
    for idx, (cromo, fit, regras) in enumerate(avaliados, 1):
        print(f"Indivíduo {idx} - Fitness: {fit} | Regras atendidas: {regras}")
        casas = cromo.to_fenotipo(mapas)
        for i, casa in enumerate(casas):
            print(f"  Casa {i+1}: {casa}")
        print()

        historico_fitness.append(max(fitnesses))
        historico_regras.append(len(regras))


    if FITNESS_OBJETIVO > 0 and melhor_fitness_geral >= FITNESS_OBJETIVO:
        print(f"\n✅ Solução ótima encontrada na geração {geracao} com fitness {melhor_fitness_geral}!")
        break


    if NUM_GERACOES > 0 and geracao >= NUM_GERACOES:
        print(f"\n🏁 Limite de gerações atingido ({NUM_GERACOES}). Melhor fitness obtido: {melhor_fitness_geral}")
        break

    # Evolução
    nova_info, nova_populacao, _ = evolucao.evoluir(
        populacao,
        taxa_elites=TAXA_ELITES,
        taxa_crossover=TAXA_CROSSOVER,
        taxa_mutacao=TAXA_MUTACAO
    )

    populacao = nova_populacao
    avaliados, fitnesses = evolucao.avaliar_populacao(populacao)
    melhor_fitness_geral = max(fitnesses)
    geracao += 1

# exibindo resultados
plt.figure(figsize=(12, 5))

# Evolução do Fitness
plt.subplot(1, 2, 1)
plt.plot(historico_fitness, 'b-', linewidth=2)
plt.title('Evolução do Melhor Fitness')
plt.xlabel('Geração')
plt.ylabel('Fitness (0-100)')
plt.grid(True)

# Evolução das Regras Atendidas
plt.subplot(1, 2, 2)
plt.plot(historico_regras, 'r-', linewidth=2)
plt.title('Regras Atendidas pelo Melhor Indivíduo')
plt.xlabel('Geração')
plt.ylabel('Número de Regras (0-15)')
plt.ylim(0, 15)
plt.grid(True)

plt.tight_layout()
plt.savefig('evolucao_fitness.png', dpi=300, bbox_inches='tight')
plt.close()

melhor_indice = fitnesses.index(max(fitnesses))
melhor_cromossomo, melhor_fitness, regras_atendidas = avaliados[melhor_indice]

print("\n=== Melhor Solução Final ===")
print(f"Fitness: {melhor_fitness}")
print(f"Regras atendidas: {regras_atendidas}")
casas = melhor_cromossomo.to_fenotipo(mapas)
for i, casa in enumerate(casas):
    print(f"  Casa {i+1}: {casa}")
