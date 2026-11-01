# seoul_bike_data.xlsx

Aluguel de Bicicletas em Seul

### Contexto

O uso de sistemas de compartilhamento de bicicletas públicas explodiu em todo o mundo, tornando-se uma peça chave da mobilidade urbana sustentável. A cidade de Seul, na Coreia do Sul, implementou um desses sistemas, e entender os padrões de uso é crucial para otimizar sua operação, garantir a disponibilidade de bicicletas e melhorar a experiência do usuário.

Este conjunto de dados oferece a oportunidade de investigar uma questão central: **O que influencia a decisão de uma pessoa em alugar uma bicicleta em uma metrópole movimentada?** Fatores como a hora do dia, o clima, a estação do ano e feriados desempenham um papel significativo. Este dataset permite explorar essas relações e construir modelos preditivos para antecipar a demanda.

---

### Conteúdo

Este conjunto de dados contém **8.760 registros horários** sobre o aluguel de bicicletas no sistema público de Seul, abrangendo um período completo de um ano. Cada registro corresponde a uma hora e contém as seguintes informações:

* **`Date`**: A data da observação (no formato DD/MM/AAAA).
* **`Rented Bike Count`**: A variável alvo. É a contagem total de bicicletas alugadas naquela hora.
* **`Hour`**: A hora do dia (0-23).
* **`Temperature(°C)`**: A temperatura em graus Celsius.
* **`Humidity(%)`**: A umidade relativa do ar em porcentagem.
* **`Wind speed (m/s)`**: A velocidade do vento em metros por segundo.
* **`Visibility (10m)`**: A visibilidade em uma escala de 10 metros (valor máximo de 2000).
* **`Dew point temperature(°C)`**: A temperatura do ponto de orvalho em graus Celsius.
* **`Solar Radiation (MJ/m2)`**: A radiação solar.
* **`Rainfall(mm)`**: A quantidade de chuva em milímetros.
* **`Snowfall (cm)`**: A quantidade de neve em centímetros.
* **`Seasons`**: A estação do ano (Inverno, Primavera, Verão, Outono).
* **`Holiday`**: Indica se o dia é feriado ('Holiday') ou não ('No Holiday').
* **`Functioning Day`**: Indica se o serviço de aluguel estava operacional ('Yes') ou não ('No').

O dataset está limpo, sem valores ausentes, tornando-o ideal para iniciar projetos de análise e modelagem rapidamente.

출처: Kaggle (igorfiori/seoul-bike-data-xlsx)
태그: 
라이선스: CC BY-SA 4.0
수정일: 2025-06-11T21:43:23.610Z
