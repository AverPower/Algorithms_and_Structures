Задача A.Очень простой поток
ограничение по времени на тест
5 секунд
ограничение по памяти на тест
1024 мегабайта
ввод
стандартный ввод
вывод
стандартный вывод

Дан неориентированный граф, состоящий из N вершин и M ребер.

У каждого ребра которого есть маленькая пропускная способность. Между любой парой вершин может быть больше одного ребра.

Исток находится в вершине 1, а сток в вершине N. Требуется найти максимальный поток между истоком и стоком.
Входные данные

В первой строке записано натуральное число N — число вершин (2 ≤ N ≤ 100).

Во второй строке записано натуральное число M — число ребер (1 ≤ M ≤ 5000).

Далее в M строках идет описание ребер. Каждое ребро задается тройкой целых чисел Ai, Bi, Ci, где Ai, Bi — номера вершин, которые соединяет ребро (), а Ci (0 ≤ Ci ≤ 20) — пропускная способность этого ребра.
Выходные данные

Выведите максимальный поток между вершинами с номерами 1 и N.



Задача B. Просто поток
ограничение по времени на тест
5 секунд
ограничение по памяти на тест
1024 мегабайта
ввод
стандартный ввод
вывод
стандартный вывод

Дана система из узлов и труб, по которым может течь вода. Для каждой трубы известна наибольшая скорость, с которой вода может протекать через нее. Известно, что вода течет по трубам таким образом, что за единицу времени в каждый узел (за исключением двух — источника и стока) втекает ровно столько воды, сколько из него вытекает.

Ваша задача — найти наибольшее количество воды, которое за единицу времени может протекать между источником и стоком, а также скорость течения воды по каждой из труб.

Трубы являются двусторонними, то есть вода в них может течь в любом направлении. Между любой парой узлов может быть более одной трубы.
Входные данные

В первой строке записано натуральное число 𝑁
— количество узлов в системе (2≤𝑁≤100). Известно, что источник имеет номер 1, а сток номер 𝑁. Во второй строке записано натуральное 𝑀 (1≤𝑀≤5000) — количество труб в системе. Далее в 𝑀 строках идет описание труб. Каждая труба задается тройкой целых чисел 𝐴𝑖, 𝐵𝑖, 𝐶𝑖, где 𝐴𝑖, 𝐵𝑖 — номера узлов, которые соединяет данная труба (𝐴𝑖≠𝐵𝑖), а 𝐶𝑖 (0≤𝐶𝑖≤104

) — наибольшая допустимая скорость течения воды через данную трубу.
Выходные данные

В первой строке выведите наибольшее количество воды, которое протекает между источником и стоком за единицу времени. Далее выведите 𝑀
строк, в каждой из которых выведите скорость течения воды по соответствующей трубе. Если направление не совпадает с порядком узлов, заданным во входных данных, то выводите скорость со знаком минус. Числа выводите с точностью 10−3.



Задача C. Разрез
ограничение по времени на тест
2 секунды
ограничение по памяти на тест
1024 мегабайта
ввод
стандартный ввод
вывод
стандартный вывод

Найдите минимальный разрез между вершинами 1 и 𝑛

в заданном неориентированном графе.
Входные данные

На первой строке входного файла содержится 𝑛
(2≤𝑛≤100) — число вершин в графе и 𝑚 (0≤𝑚≤400) — количество ребер. На следующих 𝑚 строках входного файла содержится описание ребер. Ребро описывается номерами вершин, которые оно соединяет, и его пропускной способностью (положительное целое число, не превосходящее 10000000

), при этом никакие две вершины не соединяются более чем одним ребром.
Выходные данные

На первой строке выходного файла должны содержаться количество ребер в минимальном разрезе и их суммарная пропускная способность. На следующей строке выведите возрастающую последовательность номеров ребер (ребра нумеруются в том порядке, в каком они были заданы во входном файле).
