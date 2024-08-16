# Sistema automático de bomba de porão e alerta de falha

## Protótipo ainda em desenvolvimento.
* Falta implementar o sistema com  a boia mecânica.
* Falta calibrar as medições, os números funcionam... mas creio que precisa de algo mais realista, claro que a calibragem depende da embarcação.
* Quando estiver tudo planejado vou criar o protótipo no Tinkercad.

Para solucionar o problema da entrada de água em porões de embarcações, foi projetado um sistema automático de bombeamento prático e eficiente. A utilização de dois tipos de sensores, digital e analógico, em conjunto com um algoritmo robusto, garante a detecção precisa do nível da água e o acionamento rápido da bomba, minimizando os riscos de danos à embarcação. A solução proposta utiliza uma estratégia de redundância de sensores, para detectar com precisão o nível da água e garantir o funcionamento contínuo da bomba e do sistema de alerta de falha, mesmo em situações críticas.

O coração desse sistema é o microcontrolador Arduino, que garante a confiabilidade e a robustez da operação. Ele processa os dados dos sensores em tempo real, tomando decisões rápidas e precisas para acionar a bomba quando necessário. Além disso, o Arduino é conhecido por sua resistência a ambientes hostis, o que o torna ideal para aplicações marítimas.

1. Bomba automática
* Sensores: Nível de água. Sensor Ultrassônico e Boia mecânica (Potenciômetro)
* Atuador: Eletro bomba (Motor elétrico)

O sistema de bombeamento será ativado quando o sinal proveniente do sensor de nível, filtrado por um filtro passa-baixa para eliminar ruídos de alta frequência, ultrapassar o limiar estabelecido. O sinal será lido pelo arduino, quando atingir a distância de 150cm em relação ao nível d'água ele vai ativar o sistema da bomba que permanecerá ativo até que essa distância aumente para 190cm.
O sistema da bomba contém um relay que é ativado pelo sinal do arduino. este reLê é alimentado pela bateria da embarcação, que quando fecha passa a alimentar a bomba.

2. Alerta de falha
* Sensor: Nível de água. Sensor Ultrassônico e Boia mecânica (Potenciômetro)
* Atuadores: Luz (led) e Som (piezo)

O sistema de alerta opera de forma similar ao sistema de bombeamento, porém, é acionado quando a distância entre o sensor e o nível d'água chega em 120cm e cessando quando essa distância chegar a 150cm. Quando o sistema de alerta está ativo, o microcontrolador Arduino controla a intermitência dos LEDs e piezoelétricos, proporcionando uma sinalização visual e sonora clara e eficiente.
