import matplotlib.pyplot as plt

# Укажите имя вашего файла
filename = 'P3.9I18.72D0.121875.txt'  # замените на имя вашего файла
# Чтение данных из файла
times = []
angles = []
with open(filename, 'r') as file:
    for line in file:
        if line.strip():  # Пропускаем пустые строки
            parts = line.split()
            times.append(float(parts[0]))  # Время (первое значение)
            angles.append(float(parts[1]))  # Угол (второе значение)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(times, angles, 'b-', linewidth=1, label='Угол')
plt.axhline(y=180, color='r', linestyle='--', linewidth=1, label='180°')  # Горизонтальная линия
plt.title('Зависимость угла от времени')
plt.xlabel('Время (секунды)')
plt.ylabel('Угол (градусы)')
plt.legend()  # Показываем легенду
plt.grid(True)
plt.show()