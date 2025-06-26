from Populacao import Populacao
from EvolucaoGenetica import EvolucaoGenetica

# === Mapas para fenotipagem ===
mapas = {
    "cor": ["Amarela", "Azul", "Branca", "Verde", "Vermelha"],
    "nacionalidade": ["Norueguês", "Dinamarquês", "Inglês", "Alemão", "Sueco"],
    "bebida": ["Água", "Chá", "Leite", "Café", "Cerveja"],
    "cigarro": ["Dunhill", "Blends", "Pall Mall", "Prince", "BlueMaster"],
    "animal": ["Cachorros", "Cavalos", "Gatos", "Pássaros", "Peixes"]
}

# === Parâmetros do Algoritmo ===
TAMANHO_POPULACAO = 10
TAXA_ELITES = 0.2          # 20%
TAXA_CROSSOVER = 0.7      # 60%
TAXA_MUTACAO = 0.3       # 70%
NUM_GERACOES = 400         # 0 para ilimitado
FITNESS_OBJETIVO = 99      # 0 para ignorar

# === Verificação das taxas ===
if TAXA_ELITES + TAXA_CROSSOVER > 1.0:
    print("Erro: A soma da taxa de elites e da taxa de crossover excede 100%.")
    print(f"Taxa de elites: {TAXA_ELITES * 100:.0f}%")
    print(f"Taxa de crossover: {TAXA_CROSSOVER * 100:.0f}%")
    print(f"Soma total: {(TAXA_ELITES + TAXA_CROSSOVER) * 100:.0f}%")
    exit(1)

# === Inicialização ===
populacao = Populacao(TAMANHO_POPULACAO).get_individuos()
evolucao = EvolucaoGenetica()
avaliados, fitnesses = evolucao.avaliar_populacao(populacao)
melhor_fitness_geral = max(fitnesses)
geracao = 0

# === Loop Evolutivo ===
while True:
    print(f"\n=== Geração {geracao} ===")
    for idx, (cromo, fit, regras) in enumerate(avaliados, 1):
        print(f"Indivíduo {idx} - Fitness: {fit} | Regras atendidas: {regras}")
        casas = cromo.to_fenotipo(mapas)
        for i, casa in enumerate(casas):
            print(f"  Casa {i+1}: {casa}")
        print()

    # Critério de parada por fitness
    if FITNESS_OBJETIVO > 0 and melhor_fitness_geral >= FITNESS_OBJETIVO:
        print(f"\n✅ Solução ótima encontrada na geração {geracao} com fitness {melhor_fitness_geral}!")
        break

    # Critério de parada por número de gerações
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

# === Exibe Melhor Solução Final ===
melhor_indice = fitnesses.index(max(fitnesses))
melhor_cromossomo, melhor_fitness, regras_atendidas = avaliados[melhor_indice]

print("\n=== Melhor Solução Final ===")
print(f"Fitness: {melhor_fitness}")
print(f"Regras atendidas: {regras_atendidas}")
casas = melhor_cromossomo.to_fenotipo(mapas)
for i, casa in enumerate(casas):
    print(f"  Casa {i+1}: {casa}")
