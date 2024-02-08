import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Función para calcular la proyección de inversión con interés compuesto
def calcular_proyeccion(aporte_mensual, tasa_anual, años):
    meses = int(años * 12)  # Convertir años a meses
    tasa_mensual = tasa_anual / 12 / 100
    capital = [0]  # Lista para almacenar el capital acumulado en cada mes
    for mes in range(1, meses + 1):
        capital.append(capital[-1] * (1 + tasa_mensual) + aporte_mensual)
    return capital

# Configurar la página de Streamlit
st.title('Proyección de inversión con interés compuesto')

# Obtener los valores de inversión del usuario
aporte_mensual = st.number_input('Aporte mensual:', min_value=0.0, step=100.0)
tasa_anual = st.number_input('Tasa de interés anual (%):', min_value=0.0, step=0.5)
años = st.number_input('Años:', min_value=1.0, step=1.0)

# Verificar si se han ingresado datos
if aporte_mensual == 0 or tasa_anual == 0 or años == 0:
    st.image('logo.png', width=200)
else:
    # Calcular la proyección de inversión
    capital = calcular_proyeccion(aporte_mensual, tasa_anual, años)

    # Graficar la proyección de inversión
    st.write('### Gráfica de proyección de inversión')
    meses = np.arange(len(capital))
    fig, ax = plt.subplots()  # Crear una figura y ejes
    ax.plot(meses, capital, marker='o', linestyle='-', color='gold', markersize=5)
    ax.set_xlabel('Mes')
    ax.set_ylabel('Capital acumulado')
    ax.set_title('rendimientos')

    # Mostrar solo números enteros en el eje Y
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    # Configurar la grilla
    ax.grid(True)

    st.pyplot(fig)  # Mostrar la figura en Streamlit

