# Criar um programa de um sistema que meça a distância do nível d'água em cm. Quando a distância for menor que 150cm irá
# acionar a bomba que vai aumentar essa distância (bombeando a água para fora) até 190cm, que será o gatilho para
# parar a bomba. Se essa distância chegar a menos de 120cm um alarme será acionado até que o nível volte para uma
# distância maior que 150cm.
from time import sleep  # Para colocar pausas entre as medições, evitar sobrecarregar o sistema.

# Calibragem dos limites de distâncias entre o sensor e o nível d'água
aciona_bomba = 150
aciona_alarme = 120
para_bomba = 190
para_alarme = aciona_bomba

# Variáveis que mostram se a bomba ou alarme estão acionados
bomba = bool()
alarme = bool()

# Programa em loop mantido enquanto o arduino ficar ligado
while True:
    sleep(2)  # Pausa
    distancia = int(input("Distância do nível d'água: "))  # Lê o sinal
# Abaixo seguem as condicionais de avaliação
    if distancia > aciona_alarme:
        print('Alarme OFF')
        alarme = bool(False)
    else:
        print('Alarme ON')
        alarme = bool(True)
    if distancia > aciona_bomba:
        print('Bomba OFF')
        bomba = bool(False)
    else:
        print('Bomba ON')
        bomba = bool(True)
# Abaixo o loop que mantém alarme e/ou bomba ligados enquanto o nível não baixar para o limite de parar
    while alarme or bomba:
        sleep(2)
        distancia = int(input("Distância do nível d'água: "))
        if alarme:
            if distancia < para_alarme:
                print('Alarme ON')
            if distancia >= para_alarme:
                print('Alarme OFF')
                alarme = bool(False)
        else:
            print('Alarme OFF')
        if bomba:
            if distancia < para_bomba:
                print('Bomba ON')
            if distancia >= para_bomba:
                print('Bomba OFF')
                bomba = bool(False)
        else:
            print('Bomba OFF')
