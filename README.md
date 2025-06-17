<img src="https://www.freeiconspng.com/uploads/bike-png-hd-picture-3.png" />

# **Previsão da quantidade de bicicletas alugadas na capital da Coréia do Sul**

#### **Contexto**
Uma empresa de aluguel de bicicletas da Coréia do Sul tem o interesse de prever a quantidade de alugueis de bicicletas por hora na capital do país, Seul. Com esse objetivo, esta empresa entrou em contato com a nossa empresa, de consultoria em ciência de dados, para a elaboração deste projeto.

Inicialmente, a empresa nos disponibilizou um arquivo `.csv`, com 8760 observações, contendo a quantidade total de alugueis de bicicletas por hora, mas futuramente ela nos disponibilizará uma API, que será atualizada de hora em hora, com esses dados.

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
|Volume de Chuva|Volume de chuva, em $mm$|Contínuo|
|Volume de Neve|Volume de neve, em $cm$|Contínuo|
|Estação do Ano|Estação do ano na data do aluguel|Categórica|
|Feriado|Indica se é feriado ou não na data do aluguel|Binária|
|Dia Útil|Indica se é dia útil ou não na data do aluguel|Binária|

#### **Meu papel neste projeto**

O meu papel nestre projeto é o de propor um modelo que consiga prever a quantidade de bicicletas alugadas por hora na capital da Coréia do Sul.

#### **Análise de Dados Exploratória (EDA)**

Foi feita uma análise de dados exploratória, localizada no arquivo `eda.ipynb`, para entender melhor como as variáveis *feature* selecionadas se comportam e como elas influenciam na *target*, além de entender o comportamento da *target* ao longo do tempo, investigando ela como uma componente de uma série temporal.

#### **Modelagem**

Primeiramente, foram testados dois modelos do pacote scikit-learn, *RandomForestRegressor* e *LinearRegression*, com todas as variáveis já pré processadas, o que resultou em um dos modelos (*RandomForestRegressor*) com um $\small R^2$ acima de 0.90 e um erro médio absoluto de aproximadamente 110 bicicletas.

Posteriormente, foi idealizada a criação de uma rede neural artificial do tipo perceptron multicamadas para verificar se um modelo deste tipo conseguiria melhores resultados nas métricas de avaliação do que o de floresta aleatória.

Esta rede neural foi modelada, construída (utilizando o pacote torch) e testada com os dados. Ela apresentou resultados de $\small R^2$ e erro médio absoluto bem parecidos com o de floresta aleatória. Entretanto, o modelo selecionado para o projeto da empresa foi o de floresta aleatória devido à sua simplicidade de treino e resultados bons nas métricas de avaliação, em comparação com o de redes neurais.