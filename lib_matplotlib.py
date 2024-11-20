import pandas as pd
import matplotlib.pyplot as plt
students = pd.read_csv("Students_Performance.csv")

plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()
