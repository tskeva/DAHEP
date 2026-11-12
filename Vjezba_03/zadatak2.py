
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

vrijednosti = np.linspace(-5, 5, 1000)

kumulativna = norm.cdf(vrijednosti, 0, 1)

plt.plot(vrijednosti, kumulativna, color="blue")

plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Kumulativna funkcija standardne normalne raspodjele")
plt.grid()
plt.show()