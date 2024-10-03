import matplotlib.pyplot as plt  # Importa la biblioteca para crear gráficos

# Datos del MRU
velocidad = 30  # km/h  # Define la velocidad constante de la moto en kilómetros por hora
tiempo = [0, 1, 2, 3, 4, 5]  # horas  # Crea una lista de tiempos en horas
distancia = [velocidad * t for t in tiempo]  # Calcula la distancia recorrida para cada tiempo

# Crear la figura del gráfico
plt.figure(figsize=(10, 5))  # Crea una nueva figura para el gráfico con un tamaño de 10x5 pulgadas

# Graficar los datos
plt.plot(tiempo, distancia, marker='o')  # Dibuja un gráfico de la distancia recorrida en función del tiempo, con puntos marcados con círculos

# Marcar un punto específico
plt.plot(3, distancia[3], 'ro')  # Marca un punto rojo en la posición correspondiente a la tercera hora

# Añadir título y etiquetas
plt.title('MRU: Posición vs. Tiempo')  # Añade un título al gráfico
plt.xlabel('Tiempo (horas)')  # Etiqueta el eje x como "Tiempo (horas)"
plt.ylabel('Distancia (km)')  # Etiqueta el eje y como "Distancia (km)"

# Mostrar la cuadrícula y el gráfico
plt.grid(True)  # Muestra una cuadrícula en el gráfico para facilitar la lectura
plt.show()  # Muestra el gráfico en la pantalla
