class Fitness:
    def __init__(self):
        pass

    def calcular(self, cromossomo):
        matriz = cromossomo.get_matriz()  # Agora retorna a matriz decodificada a partir dos genes
        score = 0
        regras_atendidas = []

        # Regra 1: O Norueguês vive na primeira casa.
        if matriz[0][1] == 0:
            score += 1
            regras_atendidas.append(1)

        # Regra 2: O Inglês vive na casa Vermelha.
        if any(casa[1] == 2 and casa[0] == 4 for casa in matriz):
            score += 1
            regras_atendidas.append(2)

        # Regra 3: O Sueco tem Cachorros.
        if any(casa[1] == 4 and casa[4] == 0 for casa in matriz):
            score += 1
            regras_atendidas.append(3)

        # Regra 4: O Dinamarquês bebe Chá.
        if any(casa[1] == 1 and casa[2] == 1 for casa in matriz):
            score += 1
            regras_atendidas.append(4)

        # Regra 5: A casa Verde fica à esquerda da casa Branca.
        for i in range(4):
            if matriz[i][0] == 3 and matriz[i+1][0] == 2:
                score += 1
                regras_atendidas.append(5)
                break

        # Regra 6: O homem na casa Verde bebe Café.
        if any(casa[0] == 3 and casa[2] == 3 for casa in matriz):
            score += 1
            regras_atendidas.append(6)

        # Regra 7: O homem que fuma Pall Mall cria Pássaros.
        if any(casa[3] == 2 and casa[4] == 3 for casa in matriz):
            score += 1
            regras_atendidas.append(7)

        # Regra 8: O homem na casa Amarela fuma Dunhill.
        if any(casa[0] == 0 and casa[3] == 0 for casa in matriz):
            score += 1
            regras_atendidas.append(8)

        # Regra 9: O homem na casa do meio bebe Leite.
        if matriz[2][2] == 2:
            score += 1
            regras_atendidas.append(9)

        # Regra 10: O homem que fuma Blends vive ao lado do que tem Gatos.
        for i in range(5):
            if matriz[i][3] == 1:
                if (i > 0 and matriz[i-1][4] == 2) or (i < 4 and matriz[i+1][4] == 2):
                    score += 1
                    regras_atendidas.append(10)
                    break

        # Regra 11: O homem que cria Cavalos vive ao lado do que fuma Dunhill.
        for i in range(5):
            if matriz[i][4] == 1:
                if (i > 0 and matriz[i-1][3] == 0) or (i < 4 and matriz[i+1][3] == 0):
                    score += 1
                    regras_atendidas.append(11)
                    break

        # Regra 12: O homem que fuma BlueMaster bebe Cerveja.
        if any(casa[3] == 4 and casa[2] == 4 for casa in matriz):
            score += 1
            regras_atendidas.append(12)

        # Regra 13: O Alemão fuma Prince.
        if any(casa[1] == 3 and casa[3] == 3 for casa in matriz):
            score += 1
            regras_atendidas.append(13)

        # Regra 14: O Norueguês vive ao lado da casa Azul.
        for i in range(5):
            if matriz[i][1] == 0:
                if (i > 0 and matriz[i-1][0] == 1) or (i < 4 and matriz[i+1][0] == 1):
                    score += 1
                    regras_atendidas.append(14)
                    break

        # Regra 15: O homem que fuma Blends é vizinho do que bebe Água.
        for i in range(5):
            if matriz[i][3] == 1:
                if (i > 0 and matriz[i-1][2] == 0) or (i < 4 and matriz[i+1][2] == 0):
                    score += 1
                    regras_atendidas.append(15)
                    break


        fitness = int((score / 15) * 99 + 1)
        return fitness, regras_atendidas
