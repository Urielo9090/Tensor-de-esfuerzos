import numpy as np
import matplotlib.pyplot as plt

# 🔹 1. Ingresar tensor de esfuerzos
print("Introduce el tensor de esfuerzos 3x3 fila por fila:")

sigma = []
for i in range(3):
    fila = list(map(float, input(f"Fila {i+1}: ").split()))
    sigma.append(fila)

sigma = np.array(sigma)

# Validación
if sigma.shape != (3,3):
    raise ValueError("El tensor debe ser 3x3")

# 🔹 2. Número de direcciones
N = int(input("¿Cuántas direcciones deseas evaluar? "))

sigma_n_vals = []
tau_vals = []

# 🔹 3. Cálculo
for i in range(N):
    print(f"\nDirección {i+1}")
    n = np.array(list(map(float, input("Vector [nx ny nz]: ").split())))
    
    # Validación básica
    if np.linalg.norm(n) == 0:
        raise ValueError("El vector no puede ser cero")
    
    # Normalizar
    n = n / np.linalg.norm(n)
    
    # Vector de tracción
    t = sigma @ n
    
    # Esfuerzo normal
    sigma_n = np.dot(t, n)
    
    # Esfuerzo cortante
    tau_vec = t - sigma_n * n
    tau = np.linalg.norm(tau_vec)
    
    sigma_n_vals.append(sigma_n)
    tau_vals.append(tau)

# 🔹 4. Gráfica
plt.figure()
plt.scatter(sigma_n_vals, tau_vals)
plt.xlabel("σ_n (Esfuerzo normal)")
plt.ylabel("τ (Esfuerzo cortante)")
plt.title("Nube de puntos del tensor de esfuerzos")
plt.grid()
plt.show()
