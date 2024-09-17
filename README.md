# Sistema automático para bomba de porão e alerta de problemas em embarcações - com Arduino 

### Funciona no simulador, porém há que estudar melhor os pinos e suas funções. Rever para aplicar em um projeto real.

## Resumo / Abstract

Abstract: This document is a report, a requirement of the Hands-on Work III course. In it, the author describes how they developed a project for a prototype of an automatic bilge pump system and problem alert. The objective proposed by Professor Rodrigo Ramos Martins is for students to develop an automation project that includes at least 2 sensors and 2 actuators using Arduino in the TinkerCAD simulator. 

Resumo: Este documento é um relatório, requisito da disciplina Hands on Work III. Neste o autor descreve como fez um projeto para um protótipo de um sistema automático para bomba de porão e alerta de problemas. O objetivo proposto pelo professor Rodrigo Ramos Martins é de que os alunos desenvolvam um projeto de automação que inclua ao menos 2 sensores e 2 atuadores utilizando o Arduino no simulador TinkerCAD.

## Problema
A entrada de água nos porões de uma embarcação pode ter consequências graves, como instabilidade, perda de flutuabilidade, curto-circuitos elétricos e, em casos extremos, o naufrágio. Para evitar tais acidentes, é essencial contar com sistemas de detecção e alarme confiáveis, bem como com medidas preventivas adequadas. A automação, nesse contexto, representa uma ferramenta poderosa para garantir a segurança e a integridade das embarcações, além de otimizar as operações a bordo.

## Solução
Para solucionar o problema da entrada de água em porões de embarcações, foi projetado um sistema automático de bombeamento prático e eficiente. A utilização de dois tipos de sensores, digital e analógico, em conjunto com um algoritmo robusto, garante a detecção precisa do nível da água e o acionamento rápido da bomba, minimizando os riscos de danos à embarcação. A solução proposta utiliza uma estratégia de redundância de sensores, para detectar com precisão o nível da água e garantir o funcionamento contínuo da bomba e do sistema de alerta de problemas, mesmo em situações críticas.

O coração desse sistema é o microcontrolador Arduino, que garante a confiabilidade e a robustez da operação. Ele processa os dados dos sensores em tempo real, tomando decisões rápidas e precisas para acionar a bomba quando necessário. Além disso, o Arduino é conhecido por sua resistência a ambientes hostis, o que o torna ideal para aplicações marítimas.

## Projeto
Para criar o protótipo do projeto foi utilizado o simulador TinkerCad (www.tinkercad.com), lá estão presentes diversos componentes eletrônicos para construir os circuitos incluindo o microcontrolador Arduino Uno R3, sensor ultrassônico de distância tipo PING (3 pinos), sensor Flex, motor elétrico, LEDs, buzzer (piezo) entre outros. Os sensores deste projeto são o ultrassônico e o flex (simulando o sensor de boia), os atuadores são o motor elétrico (simulando a bomba de porão), luzes LED e Piezo buzzer para o subsistema de alerta. O sensor de boia, aqui simulado pelo sensor flex, na realidade funciona como um potenciômetro. Uma boia, acoplada a uma haste, move um contato deslizante ao longo de uma trilha resistiva. Conforme o nível da água sobe, a posição do contato varia, alterando a resistência elétrica e gerando um sinal proporcional ao nível.

![Protótipo](https://github.com/Betoxvt/how_3/blob/main/prototitpo.png)

1. Circuitos:
Para montar os circuitos foi utilizada uma placa de ensaio assim as conexões dos pinos, cabos e componentes ficou mais organizada. Algumas adaptações foram feitas no simulador por causa do limite de componentes disponíveis, para a bateria 12v uma fonte ajustada para 12v e 5a e para o sensor de boia o sensor flex foi utilizado.

A alimentação da bomba de porão, para ser eficaz, é feita por um relé ligado à bateria que passa a energia para a bomba quando acionado pelo sinal do Arduino.

3. Lógica e código do programa:
Após a visualização de como seria o desenho do sistema, seus componentes, disposição e conexões o protótipo ficou mais tangível e o próximo passo foi de escrever a lógica para o controlador. O código foi desenvolvido em linguagem Python e testado, até chegar ao refinamento necessário para que os sistemas fossem acionados e parados conforme a ideia inicial, também priorizando acionar e manter os subsistemas funcionando mesmo se apenas um dos sinais dos sensores estiver marcando o limite definido.

Este código foi transcrito manualmente para o simulador que usa linguagem C++, através da ferramenta de código em blocos do TinkerCad. Realmente uma ferramenta muito prática que permite os usuários escreverem o código sem saber C++.
Com o código já inserido no simulador, alguns testes e ajustes foram realizados para conseguir o sinal intermitente do alerta, adicionando pausas com o bloco WAIT 1 sec.

4. Calibração:
Com a estrutura lógica e os componentes em ordem, foram executados vários testes, observando as impressões do monitor serial para chegar ao resultado satisfatório para este primeiro protótipo. Os limites definidos para cada sensor foram armazenados em constantes no código do arduino. Para o sensor ultrassônico de distância, estabelecendo acionar o alerta em 120cm, parar o alerta em 150cm, acionar a bomba em 150cm e parar a bomba em 190cm. Para o sensor flex ficaram definidas acionar o alerta em 930, parar o alerta em 880, acionar a bomba em 880 e parar a bomba em 770. No código estes valores podem ser alterados conforme a embarcação.

5. Simulador 

[Link para acessar o protótipo no simulador](https://www.tinkercad.com/things/4ZVEsjVhmGu-sistema-automatico-com-alerta )

## Considerações Finais 

Durante o desenvolvimento deste projeto pude aprender, de maneira introdutória, sobre a automação utilizando o Arduino. Apesar de usar apenas uma simulação no TinkerCAD pude entender mais sobre a programação e circuitos para um sistema automático com sensores e atuadores.

Apesar de basicamente o projeto funcionar, acredito que seria necessário algum sistema de amortecimento para as medições, pois com o balançar do barco o nível da água no porão certamente sofrerá oscilações e, portanto, afetará o funcionamento do sistema.

E finalmente, dependendo das luzes e dos autofalantes utilizados no sistema de alerta, uma alimentação ligada a bateria do barco e acionada por relé pode ser necessária. Usaria o mesmo método que foi apresentado para a bomba de porão.
No futuro pode-se estudar outras funções para o sistema, como envio de sinal de S.O.S automático ou de monitoramento via internet por satélite, podendo ter a localização GPS integrada. 
