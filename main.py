from Populacao import Populacao
from Fitness import Fitness
from Roleta import Roleta

# Mapas para transformar genótipos em fenótipos legíveis
mapas = {
    "cor": ["Amarela", "Azul", "Branca", "Verde", "Vermelha"],
    "nacionalidade": ["Norueguês", "Dinamarquês", "Inglês", "Alemão", "Sueco"],
    "bebida": ["Água", "Chá", "Leite", "Café", "Cerveja"],
    "cigarro": ["Dunhill", "Blends", "Pall Mall", "Prince", "BlueMaster"],
    "animal": ["Cachorros", "Cavalos", "Gatos", "Pássaros", "Peixes"]
}

# Parâmetros
TAMANHO_POPULACAO = 10
TAXA_SOBREVIVENCIA = 0.6

# Inicialização
populacao = Populacao(TAMANHO_POPULACAO)
fitness_calc = Fitness()
roleta = Roleta(taxa_sobrevivencia=TAXA_SOBREVIVENCIA)

individuos = populacao.get_individuos()

# Cálculo do fitness para cada indivíduo
fitnesses = []
avaliados = []  # tuplas (cromossomo, fitness, regras)
for cromo in individuos:
    fit, regras = fitness_calc.calcular(cromo)
    fitnesses.append(fit)
    avaliados.append((cromo, fit, regras))

# === Antes da roleta ===
print("=== População Inicial ===\n")
for idx, (cromo, score, regras) in enumerate(avaliados, 1):
    print(f"Indivíduo {idx}:")
    for i, casa in enumerate(cromo.get_matriz()):
        casa_legivel = {
            "cor": mapas["cor"][casa[0]],
            "nacionalidade": mapas["nacionalidade"][casa[1]],
            "bebida": mapas["bebida"][casa[2]],
            "cigarro": mapas["cigarro"][casa[3]],
            "animal": mapas["animal"][casa[4]]
        }
        print(f"  Casa {i+1}: {casa_legivel}")
    print(f"Fitness: {score} | Regras atendidas: {regras}\n")

# Seleção por roleta
sobreviventes = roleta.girar(individuos, fitnesses)

# === Depois da roleta ===
print("=== Sobreviventes ===\n")
for idx, cromo in enumerate(sobreviventes, 1):
    score, regras = fitness_calc.calcular(cromo)
    print(f"Sobrevivente {idx}:")
    for i, casa in enumerate(cromo.get_matriz()):
        casa_legivel = {
            "cor": mapas["cor"][casa[0]],
            "nacionalidade": mapas["nacionalidade"][casa[1]],
            "bebida": mapas["bebida"][casa[2]],
            "cigarro": mapas["cigarro"][casa[3]],
            "animal": mapas["animal"][casa[4]]
        }
        print(f"  Casa {i+1}: {casa_legivel}")
    print(f"Fitness: {score} | Regras atendidas: {regras}\n")
