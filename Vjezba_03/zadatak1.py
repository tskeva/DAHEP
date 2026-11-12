
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mase = np.linspace(185, 215, 1000)

plt.plot(mase, norm.pdf(mase, 200, 2), label="μ = 200, σ = 2")
plt.plot(mase, norm.pdf(mase, 200, 4), label="μ = 200, σ = 4")
plt.plot(mase, norm.pdf(mase, 205, 2), label="μ = 205, σ = 2")

plt.xlabel("Masa (GeV)")
plt.ylabel("Gustoca vjerojatnosti (1/GeV)")
plt.title("Gaussove raspodjele")
plt.legend()
plt.grid()
plt.show()

vjerojatnost1 = norm.sf(205, 200, 2)

vjerojatnost2 = norm.cdf(201, 200, 2) - norm.cdf(199, 200, 2)

vjerojatnost3 = norm.sf(203, 200, 2)**2

print("Vjerojatnost za masu >= 205 GeV:", vjerojatnost1)
print("Vjerojatnost za masu od 199 do 201 GeV:", vjerojatnost2)
print("Vjerojatnost za dvije neovisne cestice mase > 203 GeV:", vjerojatnost3)