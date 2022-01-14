Учебный проект магистратуры Наука о Данных, МИСиС Университет Науки и Технологи, Москва, Россия, январь 2022

Moscow University of Science and Technology, Data Science Master Study Project

# Построение рекомендательной системы для любителей вин.

![alt text](./media/wine_recommener.jpeg "Title")

# Результаты

## Ноутбуки
1. Подготовка данных и основные методы [здесь](./notebooks/rec_sys_notebook_1_of_2.ipynb)
2. DeepFM модель [здесь](./notebooks/rec_sys_notebook_2_of_2.ipynb)

## Приложение
Для предоставления доступа к результатам, разработано [веб-приложение](https://misis-rec-sys.herokuapp.com). Можно [прочитать инструкцию](./frontend.md) по сборке и развёртыванию.

# Описание
Рекомендательная система - комплекс алгоритмов, программ и сервисов, задача которых предсказать, что может заинтересовать того или иного пользователя. В работе использован датасет - набор данных с Kaggle (собран с сайта WineEnthusiast). Набор данных включает в себя ~130 000 экспертных обзоров вин с такими фичами, как страна производства вина, описание обозревателя, рейтинг баллов, цена, регион, сорт и винодельня.

## Задача
Составить рекомендателную систему вин для пользователя.

## Список разработанных моделей
- Popularity-based (подход, основанный на IMDB weighted average)
-  Popularity-based (price/quality)
-  Popularity-based (лучшая оценка от каждого эксперта)
-  Content-based (correliation matrix)
-  Collaborative based Generalized Matrix Factorization (GMF)
-  DeepFM подход (Factorization-Machine based neural network)

## Наблюдения
Сравнение popularity-based и content-based подхода с использованием метрикСделана попытка показать на конкретном примере разницу эффективностей работы popularity-based и content-based подходов с использованием метрики precision@k - доли релевантных предсказаний среди первых k ответов, где k = 10 в нашем случае.Сложность объективной/метрической оценки состоит в том, что характер имеющегося датасета не дает возможности получить некий эталонный ожидаемый ответ для модели, относительно которого можно сверять результаты работы разных моделей. По этой причине пришлось принять некоторые допущения и уточнить/доработать классическую формулу выбранной метрики.

Будем считать результат релевантным, если рекомендуемое системой вино:
1. Имеет ту же страну производства что и вино, для которого делается рекомендация (географический фактор - зачастую осноопределяющий при выборе вина)
2. Имеет рейтинг не меньше чем на 3 пункта ниже относительно рейтинга вина, для которого делается рекомендация (вкусовой фактор - оценка дегустатора, которая агрегирует внутри себя все особенности вина)
3. Имеет цену не выше 20% относительно цены вина, для которого делается рекомендация (ценовой фактор - можно порекомендовать хорошее вино, но если оно будет сильно отличаться по цене относительно вина, для которого делается рекомендация, то вряд ли рекомендуемое вино будет приобретено и попробовано (исходим из теории рационального выбора), и, следовательно, такая рекомендация нерелевантна). Для тех вин, где цена не указана, данная проверка не выполняется.

DeepFM подход (Factorization-Machine based neural network)

Модель предсказывает вероятность того, что user поставит оценку например 80 данному вину, т.е мы получаем массив с оценками и вероятностями, и берем 10 самых больших вероятностей.

## Заключение

Для дальнейшей работы рекомендуется сделать попытку расширить датасет путем генерации недостающих данных, а так же использовать другие датасеты с большим количеством данных, чтобы улучшить качество предсказаний.


