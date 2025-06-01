<img src="https://www.freeiconspng.com/uploads/bike-png-hd-picture-3.png" />

# **Análise de Dados Exploratória**
#### **Contexto**
Uma empresa de aluguel de bicicletas da Coréia do Sul tem o interesse de prever a quantidade de alugueis de bicicletas por hora na capital do país, Seul. Com esse objetivo, esta empresa entrou em contato com a nossa empresa, de consultoria em ciência de dados, para a elaboração deste projeto.

Inicialmente, a empresa nos disponibilizou um arquivo **.csv** contendo a quantidade total de alugueis de bicicletas por hora, mas futuramente ela nos disponibilizará uma API, que será atualizada de hora em hora, com esses dados.

Um grupo de analistas de dados da nossa consultoria realizou uma pesquisa inicial de potenciais variáveis que possam ter correlação com a quantidade total de algueis por hora na cidade. Com base nisso, temos à disposição as seguintes variáveis:

|Variável|Descrição da Variável|Tipo da Variável|
|:-|:-|:-|
|Data|Data do aluguel|Data|
|Quantidade de Bicicletas Alugadas|Representa a quantidade total de bicicletas alugadas na hora de referência|Inteiro|
|Hora|Hora do aluguel|Inteiro|
|Temperatura|Temperatura, em $\small °C$|Contínuo|
|Umidade|Umidade relativa do ar, em $\small \%$|Inteiro|
|Velocidade do Vento|Velocidade do vento, em $\small m/s$|Contínuo|
|Visibilidade|Distância na qual seja capaz de discernir um objeto, em $\small 10\space m$|Inteiro|
|Temperatura de Ponto de Orvalho|Temperatura a que o ar deve ser resfriado para atingir 100% de umidade relativa|Contínuo|
|Radiação Solar|Índice de radiação solar, em $\small MJ/m^2$|Contínuo|
|Volume de Chuva|Volume de chuva, em $mm$|Inteiro|
|Volume de Neve|Volume de neve, em $cm$|Inteiro|
|Estação do Ano|Estação do ano na data do aluguel|Categórica|
|Feriado|Indica se é feriado ou não na data do aluguel|Binária|
|Dia Útil|Indica se é dia útil ou não na data do aluguel|Binária|

#### **Objetivo**

O objetivo desta análise de dados exploratória é o de identificar, por meio de diversos métodos, correlações entre as variáveis *feature* com a variável *target*.

#### **Análise**

##### **PLOT 1: QUANTIDADE ALUGADA DE BICICLETAS POR HORA E POR DIA NO MÊS**

![alt text](src/images/plot1.png)

Analisando a quantidade de bicicletas alugadas por hora ao longo do mês, vemos que a série possui uma sazonalidade, mas que ainda não é possível identificar com clareza a sua periodicidade.

Utilizando o meu conhecimento prévio sobre a utilização de bicicletas alugadas no dia-a-dia, acredito que o dia da semana possa influenciar neste número. Logo, por conta disso, seria interessante fazermos uma análise no período de uma semana.

##### **PLOT 2: QUANTIDADE ALUGADA DE BICICLETAS POR HORA E POR DIA NA SEMANA**

![alt text](src/images/plot2.png)

Sabendo que o dia 04/12/2017 foi uma segunda-feira e o dia 10/12/2017 foi um domingo, é possível observar que os dias de semana (segunda a sexta) são os dias com maiores quantidades de bicicletas alugadas, sendo os finais de semana (sábado e domingo) os dias com menor quantidade de bicicletas alugadas.

Podemos ver também que nos dias de semana acontecem dois picos por dia. Esses picos muito provavelmente são um horário de manhã, quando pessoas utilizam bicicletas alugadas para ir ao trabalho (pode ser faculdade ou escola também), e um à tarde ou à noite (quando voltam para casa). Em uma análise rápida, constatei que esses horários de pico são 09h e 19h.

Em relação à periodicidade da sazonalidade constatada, pode-se observar que ela é de 24 horas (1 dia) nesta série temporal. É possível que esta série temporal também possua uma sazonalidade de 7 dias, por conta da redução da quantidade de bicicletas alugadas aos finais de semana. Para verificar esta hipótese, faremos um gráfico agrupando todas as quantidades de bicicletas alugadas em um dia.

##### **PLOT 3: QUANTIDADE ALUGADA DE BICICLETAS POR DIA NA SEMANA**

![alt text](src/images/plot3.png)

Analisando a série temporal por dia em um período de 4 meses, não parece que ela tenha uma sazonalidade semanal. Podemos concluir nesta análise inicial da série temporal que ela possui sazonalidade de 1 dia.

##### **PLOT 4: TEMPERATURA x QUANTIDADE DE BICICLETAS ALUGADAS**

![alt text](src/images/plot4.png)