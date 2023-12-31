import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

# Function to generate a random binary string of length n
def generate_random_binary_string(n):
    return ''.join(np.random.choice(['0', '1'], size=n))

# Function to update the plot
def actualizar_grafica(porcentajes_ceros, fig_container):
    nuevo_punto = int(generate_random_binary_string(100), 2)
    porcentaje_ceros = (100 * bin(nuevo_punto).count('0')) / 100
    porcentajes_ceros.append(porcentaje_ceros)

    # Update the plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(1, len(porcentajes_ceros) + 1)),
                             y=porcentajes_ceros,
                             mode='lines+markers',
                             name='Porcentaje de Ceros (%)'))

    fig_container.plotly_chart(fig, use_container_width=True)

# Create a Streamlit app
st.title('Actualización Gráfica')
porcentajes_ceros = [0]
fig_container = st.empty()

# Update the plot in a loop
while True:
    actualizar_grafica(porcentajes_ceros, fig_container)
    time.sleep(1)  # Wait for 1 second before the next update


