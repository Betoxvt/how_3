# Sistema automático de bomba de porão e alerta de falha

Para solucionar o problema da entrada de água em porões de embarcações, foi projetado um sistema automático de bombeamento prático e eficiente. A utilização de dois tipos de sensores, digital e analógico, em conjunto com um algoritmo robusto, garante a detecção precisa do nível da água e o acionamento rápido da bomba, minimizando os riscos de danos à embarcação. A solução proposta utiliza uma estratégia de redundância de sensores, para detectar com precisão o nível da água e garantir o funcionamento contínuo da bomba e do sistema de alerta de falha, mesmo em situações críticas.

O coração desse sistema é o microcontrolador Arduino, que garante a confiabilidade e a robustez da operação. Ele processa os dados dos sensores em tempo real, tomando decisões rápidas e precisas para acionar a bomba quando necessário. Além disso, o Arduino é conhecido por sua resistência a ambientes hostis, o que o torna ideal para aplicações marítimas.

1. Bomba automática
* Sensores: Nível de água. Sensor Ultrassônico e Boia mecânica (Potenciômetro)
* Atuador: Eletro bomba (Motor elétrico)

O sistema de bombeamento será ativado quando o sinal proveniente do sensor de nível, filtrado por um filtro passa-baixa para eliminar ruídos de alta frequência, ultrapassar o limiar estabelecido. O sinal será lido pelo arduino, qundo atingir o nível 4 (escala de 0 a 9) ele vai ativar o sistema da bomba até o nível chegar a 1.
O sistema da bomba contém um relay que é ativado pelo sinal do arduino. este reLê é alimentado pela bateria da embarcação, que quando fecha passa a alimentar a bomba.

2. Alerta de falha
* Sensor: Nível de água. Sensor Ultrassônico e Boia mecânica (Potenciômetro)
* Atuadores: Luz (led) e Som (piezo)

O sistema de alerta de falha funciona similar ao da bomba, porém, ativa no nível 6 e para no 4. Enquanto ativado, o arduino acionara intermitentemente os leds e piezos.
