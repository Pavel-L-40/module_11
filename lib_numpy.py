import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(f"a[0] = {a[0]}")
print(f"b[0] = {b[0]}")

print(a.ndim)
print(b.ndim)
print(a.shape)
print(b.shape)
print(a.size)
print(b.dtype)
print(a.itemsize)
print(b.itemsize)

a = np.eye(5,5,0, 'int') #создаёт массив с единицами на главной диагонали и нулевыми остальными элементами:
print(a)
a = np.arange(1, 5, 0.4) # Эта функция похожа на стандартную функцию range(), но возвращает массив и может создавать диапазон значений из вещественных чисел.
print(a)

a = np.linspace(1, 5, 10)  # задаётся начало, конец диапазона и количество значений
print(a)
# ========================================================= reshape ====================================================
print('\n', '*' * 10, 'reshape: ','*'* 10 ,'\n')


a = np.zeros((4, 3), dtype="uint8")
print(a)
print()
a = a.reshape((2, 6))  #  изменения размерности массива
print(a)

# ========================================================== resize ====================================================
print('='*10, 'resize', '='*10)
a = np.zeros((4, 3), dtype="uint8")
print(a)
print()
a.resize((2, 2, 3))
print(a)
# ===========================

a = np.array([9, 8, 7])
b = np.array([1, 2, 3])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# умножение матриц dot
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]])
print(a @ b)

# транспонирование и поворот

a = np.arange(1, 13).reshape(4, 3)
print(a)
print("Транспонирование")
print(a.transpose())
print("Поворот влево")
print(np.rot90(a))
print("Поворот вправо")
print(np.rot90(a, -1))


a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a.sum(axis=0))  # сумма чисел в каждом столбце
print(a.sum(axis=1))  # сумма чисел в каждой строке
print(a.min(axis=0))  # минимум по столбцам
print(a.max(axis=1))  # максимум по строкам
# ========================================= срезы массивов =========================
a = np.arange(1, 13).reshape(3, 4)
print(a)
print()
print(a[:2, 2:])
print()
print(a[:, ::2])
# ============================================= элементы первой оси массивов ===============
a = np.arange(1, 13).reshape(3, 4)
print(a)
for row in a:
    print(row)
