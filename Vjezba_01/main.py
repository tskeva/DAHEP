from ClassDef import Boson, Higgs


# Stvaranje objekata
bozon = Boson("Z bozon", 1, 50)
higgs = Higgs("Higgsov bozon", 0, 30, 125)

# Ispis podataka o bozonu
print("Podaci o bozonu:")
bozon.PrintInfo()

print()

# Ispis podataka o Higgsovom bozonu
print("Podaci o Higgsovom bozonu:")
higgs.PrintInfo()

print("Srednja masa:", higgs.MassMean)
print("Standardna devijacija mase:", higgs.MassSigma)
print("Energija:", higgs.Energy(), "GeV")