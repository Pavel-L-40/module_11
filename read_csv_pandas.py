import numpy as np
import pandas as pd

students = pd.read_csv('Students_Performance.csv')
print(students.head()) # возвращается пять первых строк

print(students.tail(3)) # для получения последних n строк используется метод tail(n)
print(students[10:13])

print(students[students["test preparation course"] == "completed"]["math score"].head())

# Для выполнения операции группировки в pandas используется метод groupby() воспользуемся методом count(), чтобы определить количество сгруппированных записей.
print(students.groupby(["gender", "test preparation course"])["writing score"].count())
