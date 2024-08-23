# Criar um programa de um sistema que meça a distância do nível d'água em cm. Quando a distância for menor que 150cm irá
# acionar a bomba que vai aumentar essa distância (bombeando a água para fora) até 190cm, que será o gatilho para
# parar a bomba. Se essa distância chegar a menos de 120cm um alerta será acionado até que o nível volte para uma
# distância maior que 150cm.
from time import sleep  # Para colocar pausas entre as medições.

# Calibragem dos limites de distâncias entre o sensor e o nível d'água
ACIONA_BOMBA_ULTRA = 150
ACIONA_ALERTA_ULTRA = 120
PARA_BOMBA_ULTRA = 190
PARA_ALERTA_ULTRA = 150

# Calibragem para o sensor flex
ACIONA_BOMBA_FLEX = 880
ACIONA_ALERTA_FLEX = 930
PARA_BOMBA_FLEX = 770
PARA_ALERTA_FLEX = 880


# Variáveis para indicadores de funcionamento
arduino = bool()
bomba = bool()
alerta = bool()

# Programa em loop enquanto o arduino ficar ligado
while True:
    arduino = bool(True)
    print('Sistema ON')
    sleep(2)  # Pausa
    distancia = int(input("Distância do nível d'água: "))  # Lê o sinal
# Abaixo seguem as condicionais de avaliação
    if distancia > ACIONA_ALERTA_ULTRA:
        print('alerta OFF')
        alerta = bool(False)
    else:
        print('alerta ON')
        alerta = bool(True)
    if distancia > ACIONA_BOMBA_ULTRA:
        print('Bomba OFF')
        bomba = bool(False)
    else:
        print('Bomba ON')
        bomba = bool(True)
# Abaixo o loop que mantém alerta e/ou bomba ligados enquanto o nível não baixar para o limite de parar
    while alerta or bomba:
        arduino = bool(True)
        print('Sistema ON')
        sleep(2)
        distancia = int(input("Distância do nível d'água: "))
        if distancia <= ACIONA_ALERTA_ULTRA:
            alerta = bool(True)
        if distancia <= ACIONA_BOMBA_ULTRA:
            bomba = bool(True)
        if alerta:
            if distancia < PARA_ALERTA_ULTRA:
                print('alerta ON')
            if distancia >= PARA_ALERTA_ULTRA:
                print('alerta OFF')
                alerta = bool(False)
        else:
            print('alerta OFF')
        if bomba:
            if distancia < PARA_BOMBA_ULTRA:
                print('Bomba ON')
            if distancia >= PARA_BOMBA_ULTRA:
                print('Bomba OFF')
                bomba = bool(False)
        else:
            print('Bomba OFF')
