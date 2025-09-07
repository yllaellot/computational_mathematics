import math
import matplotlib.pyplot as plt
import numpy as np

# Настройка стиля графиков
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12

def calculate_forward_difference(func, x_value, step_size):
    """Вычисляет производную методом прямой разности"""
    return (func(x_value + step_size) - func(x_value)) / step_size

def calculate_central_difference(func, x_value, step_size):
    """Вычисляет производную методом центральной разности"""
    return (func(x_value + step_size) - func(x_value - step_size)) / (2 * step_size)

def calculate_backward_difference(func, x_value, step_size):
    """Вычисляет производную методом обратной разности второго порядка"""
    return (3 * func(x_value) - 4 * func(x_value - step_size) + func(x_value - 2 * step_size)) / (2 * step_size)

# Основная функция и её точная производная
function = math.sin
exact_derivative = math.cos
approximate_derivative = lambda x_val, h_val: calculate_backward_difference(function, x_val, h_val)

# Подготовка данных для анализа
step_sizes = []
approximation_errors = []

current_step = 1e-10
point_x = 0.5

while current_step < 0.01:
    step_sizes.append(current_step)
    error = exact_derivative(point_x) - approximate_derivative(point_x, current_step)
    approximation_errors.append(error)
    current_step *= 1.2

# Создание графика
figure, axes = plt.subplots(figsize=(10, 6))

# Использование цветовой палитры
color_palette = plt.cm.viridis(np.linspace(0, 1, 1))

# Построение графика с улучшенным стилем
axes.plot([math.log10(step) for step in step_sizes], 
          [math.log10(abs(error)) for error in approximation_errors], 
          color=color_palette[0], 
          marker='o', 
          linestyle='-', 
          linewidth=2, 
          markersize=5,
          markerfacecolor='white',
          markeredgecolor=color_palette[0],
          markeredgewidth=1.5,
          label='Погрешность вычисления')

# Настройка осей и заголовка
axes.set_xlabel('Логарифм шага (log h)', fontsize=14, fontweight='bold')
axes.set_ylabel('Логарифм погрешности (log error)', fontsize=14, fontweight='bold')
axes.set_title('Зависимость погрешности численного дифференцирования от величины шага', 
               fontsize=14, fontweight='bold', pad=20)

# Настройка сетки
axes.grid(True, linestyle='--', alpha=0.7)

# Добавление легенды
axes.legend(loc='best', frameon=True, fancybox=True, shadow=True)

# Улучшение компоновки
plt.tight_layout()

# Показать график
plt.show()