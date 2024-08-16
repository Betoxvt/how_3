# Criar um programa de um sistema que meça a distância do nível d'água em cm. Quando a distância for menor que 150cm irá
# acionar a bomba que vai aumentar essa distância (bombeando a água para fora) até 190cm, que será o gatilho para
# parar a bomba. Se essa distância chegar a menos de 120cm um alarme será acionado até que o nível volte para uma
# distância maior que 150cm.
from time import sleep

aciona_bomba = 150
aciona_alarme = 120
para_bomba = 190
para_alarme = aciona_bomba
bomba = bool()
alarme = bool()


while True:
    distancia = int(input("Distância do nível d'água: "))
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
    while alarme or bomba:
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
