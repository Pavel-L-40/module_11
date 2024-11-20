import pandas as pd
import numpy as np

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"]) # Series фактически является аналогом словаря
print(s)
print()
s = pd.Series(np.linspace(0, 1, 5))
print(s)

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("Выбор одного элемента")
print(s["a"])
print("Выбор нескольких элементов")
print(s[["a", "d"]])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)
print("Фильтрация")
print(s[s > 2])
print('='*10, 'индекс, данные')
s.name = "Данные"
s.index.name = "Индекс"
print(s)

# ===========
# создать многомерный масссив проще всего из словаря

students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}
students = pd.DataFrame(students_marks_dict)
students.index.name = 'id студента'
print(students)
# У объекта класса DataFrame есть индексы по строкам (index) и столбцам (columns):
print(students.index)
print(students.columns)
# Для индекса по строке по умолчанию задаётся числовое значение. Значения индекса можно заменить путём записи списка в атрибут index:
students.index = ["A", "B", "C"]
print(students)
# Для доступа к записям таблицы по строковой метке используется атрибут loc. При использовании строковой метки доступна операция среза:
print(students.loc['B':])

print(type(students["student"]))

