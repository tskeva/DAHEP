import uproot
import numpy as np
import awkward as ak
import matplotlib.pyplot as plt

# Otvaranje ROOT datoteke
datoteka = uproot.open("Vjezba_02/podaci/ggH125_ZZ4lAnalysis.root")

# Otvaranje stabla candTree
stablo = datoteka["ZZTree/candTree"]

# Ucitavanje podataka o leptonima
podaci = stablo.arrays(["LepPt", "LepEta", "LepPhi"])

print("Podaci su uspjesno ucitani!")
print("Broj dogadaja:", len(podaci))

print("Podaci o leptonima prvog dogadaja:")
print("Pt:", podaci["LepPt"][0])
print("Eta:", podaci["LepEta"][0])
print("Phi:", podaci["LepPhi"][0])

# Izracun komponenti impulsa svih leptona
px = podaci["LepPt"] * np.cos(podaci["LepPhi"])
py = podaci["LepPt"] * np.sin(podaci["LepPhi"])
pz = podaci["LepPt"] * np.sinh(podaci["LepEta"])

# Ispis komponenti impulsa za prvi dogadaj
print("Komponente impulsa prvog dogadaja:")
print("px:", px[0])
print("py:", py[0])
print("pz:", pz[0])

# Izracun energije svih leptona (masa leptona je 0)
energija = np.sqrt(px**2 + py**2 + pz**2)

# Ispis energija cetiri leptona prvog dogadaja
print("Energije leptona prvog dogadaja:")
print(energija[0])

# Izracun invariantne mase prvog Z bozona
energija_z = energija[:, 0] + energija[:, 1]

px_z = px[:, 0] + px[:, 1]
py_z = py[:, 0] + py[:, 1]
pz_z = pz[:, 0] + pz[:, 1]

masa_z = np.sqrt(np.maximum(
    energija_z**2 - px_z**2 - py_z**2 - pz_z**2, 0
))

print("Invariantna masa prvog Z bozona:")
print(masa_z[0])

# Izracun invariantne mase Higgsova bozona
energija_h = ak.sum(energija, axis=1)

px_h = ak.sum(px, axis=1)
py_h = ak.sum(py, axis=1)
pz_h = ak.sum(pz, axis=1)

masa_h = np.sqrt(np.maximum(
    energija_h**2 - px_h**2 - py_h**2 - pz_h**2, 0
))

print("Invariantna masa Higgsova bozona:")
print(masa_h[0])

# Crtanje histograma invariantnih masa
plt.figure(figsize=(10, 6))

# Histogram Higgsova bozona - crvena boja
plt.hist(masa_h, bins=100, range=(0, 200),
         color="red", alpha=0.6, label="Higgsov bozon")

# Histogram prvog Z bozona - plava boja
plt.hist(masa_z, bins=100, range=(0, 200),
         color="blue", alpha=0.6, label="Z bozon")

# Naslov i oznake osi
plt.xlabel("Invariantna masa (GeV/c²)")
plt.ylabel("Broj dogadaja")
plt.title("Invariantne mase Higgsova i Z bozona")

# Legenda
plt.legend()
plt.savefig("Vjezba_02/histogram_masa.png", dpi=300, bbox_inches="tight")
# Prikaz grafa
plt.show()