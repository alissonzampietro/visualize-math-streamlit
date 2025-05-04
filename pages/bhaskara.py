import numpy as np
import matplotlib.pyplot as plt
import cmath
import streamlit as st

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue', zorder=1)
    plt.axhline(0, color='gray', linestyle='--')

    if delta >= 0:
        plt.plot([x1.real, x2.real], [0, 0], 'ro', label='Roots')
    else:
        plt.text(-9, max(y)*0.8, 'No real roots', color='red')

    plt.title(f'Bhaskara (Quadratic) Formula: {a}x² + {b}x + {c}')
    plt.legend()
    plt.grid(True)
    return plt

st.write('Bhaskara (Quadratic) Formula')
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("A", value=1)
with col2:
    b = st.number_input("B", value=4)
with col3:
    c = st.number_input("C", value=1)
st.pyplot(bhaskara(a, b, c))
