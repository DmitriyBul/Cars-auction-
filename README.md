# Cars Auction
Visualization data for USA auction of automobiles

Обзор и подготовка датасета
=====================
Для начала проанализируем датасет
![Head](https://github.com/DmitriyBul/Cars-auction-/blob/master/head.PNG)

Проверим датасет на наличие отсутствующих значений

![Head](https://github.com/DmitriyBul/Cars-auction-/blob/master/isnull.PNG)

Поиск зависимостей между параметрами
-----------------------------------
Отсутствующих значений нет, что очень хорошо.
***
Построем корреляционную матрицу для оценки зависимостей между численными параметрами.
![Head](https://github.com/DmitriyBul/Cars-auction-/blob/master/Correlation_Matrix.PNG)

Исходя из корреляционной матрицы можно увидеть отрицательную корреляцию между пробегом автомобиля и годом его выпуска. Также схожую зависимость видно у пробега и ценой авто.
***
Цена автомобиля и его год выпуска имеют положительную корреляцию, что вполне логично =)
***
Теперь построим heatmap для более детального рассмотрения зависимости цены от пробега.
![Head](https://github.com/DmitriyBul/Cars-auction-/blob/master/Heatmap.PNG)
