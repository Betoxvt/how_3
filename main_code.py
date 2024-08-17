# Criar um programa de um sistema que meça a distância do nível d'água em cm. Quando a distância for menor que 150cm irá
# acionar a bomba que vai aumentar essa distância (bombeando a água para fora) até 190cm, que será o gatilho para
# parar a bomba. Se essa distância chegar a menos de 120cm um alerta será acionado até que o nível volte para uma
# distância maior que 150cm.
# Agora nesta segunda parte, vamos adicionar o sensor mecânico tipo bóia. Importante saber como calibrar a boia para
# atuar em paralelo com o sensor ultrassônico, de preferência com os mesmos valores numéricos.
# Aqui a lógica busca priorizar acionar a bomba e o alerta se qualquer um dos sensores atingir o limiar de gatilho.
# Apenas desativando os atuadores quando ambos estabilizarem no limite calibrado para parar.

# Valores dos limites de acionamento e parada, calibrar conforme a embarcação.
aciona_bomba = 150
aciona_alerta = 120
para_bomba = 190
para_alerta = 150


# Acende as luzes
arduino = bool(True)
bomba = bool(True)
alerta = bool(True)

# Programa em loop enquanto o arduino ficar ligado
while True:
    arduino = bool(True)
    print('Sistema ON')
# Leituras iniciais
    distancia = int(input("Distância do nível d'água: "))  # Lê o sinal do sensor ultrassônico
    sinal_flex = int(input("Sinal do flex (bóia): "))  # Lê o sinal do sensor flex (bóia)
# Abaixo seguem as condicionais de avaliação
    if distancia > aciona_alerta and sinal_flex > aciona_alerta:
        print('alerta OFF')
        alerta = bool(False)
    else:
        print('alerta ON')
        alerta = bool(True)
    if distancia > aciona_bomba and sinal_flex > aciona_bomba:
        print('Bomba OFF')
        bomba = bool(False)
    else:
        print('Bomba ON')
        bomba = bool(True)
# Abaixo o loop que mantém alerta e/ou bomba ligados enquanto o nível não baixar para o limite de parar
    while alerta or bomba:
        distancia = int(input("Distância do nível d'água: "))
        sinal_flex = int(input("Sinal do flex (bóia): "))
        if distancia <= aciona_alerta or sinal_flex <= aciona_alerta:
            alerta = bool(True)
        if distancia <= aciona_bomba or sinal_flex <= aciona_bomba:
            bomba = bool(True)
        if alerta:
            if distancia < para_alerta or sinal_flex < para_alerta:
                print('alerta ON')
            if distancia >= para_alerta and sinal_flex >= para_alerta:
                print('alerta OFF')
                alerta = bool(False)
        else:
            print('alerta OFF')
        if bomba:
            if distancia < para_bomba or sinal_flex < para_bomba:
                print('Bomba ON')
            if distancia >= para_bomba and sinal_flex >= para_bomba:
                print('Bomba OFF')
                bomba = bool(False)
        else:
            print('Bomba OFF')
