import numpy as np
import matplotlib.pyplot as plt

# Tensor de ejemplo (puedes cambiarlo)
sigma = np.array([
    [8, 5, 4],
    [3, 7, 1],
    [-9, 1, 6]
])

N = 500

sigma_n_vals = []
tau_vals = []

for _ in range(N):
    # Dirección aleatoria en esfera
    n = np.random.randn(3)
    n = n / np.linalg.norm(n)
    
    t = sigma @ n
    sigma_n = np.dot(t, n)
    tau_vec = t - sigma_n * n
    tau = np.linalg.norm(tau_vec)
    
    sigma_n_vals.append(sigma_n)
    tau_vals.append(tau)

# Gráfica
plt.figure()
plt.scatter(sigma_n_vals, tau_vals, s=10)
plt.xlabel("σ_n")
plt.ylabel("τ")
plt.title("Nube de puntos (tensor de esfuerzos)")
plt.grid()
plt.show()
