```python id="pna2026"
# ==============================
# RAPPORT STOCK PNA CONGO
# ==============================

# ===== DONNEES =====
# Artemether-Lumefantrine
m1_stock = 8450
m1_seuil = 2000
m1_prix = 3500
m1_consommation = 1200

# Amoxicilline 500mg
m2_stock = 3200
m2_seuil = 800
m2_prix = 850
m2_consommation = 650

# Serum de rehydratation
m3_stock = 15600
m3_seuil = 5000
m3_prix = 125
m3_consommation = 3800


# ===== CALCULS =====

# Valeur stock
valeur_m1 = m1_stock * m1_prix
valeur_m2 = m2_stock * m2_prix
valeur_m3 = m3_stock * m3_prix

# Mois de stock restants
mois_m1 = m1_stock / m1_consommation
mois_m2 = m2_stock / m2_consommation
mois_m3 = m3_stock / m3_consommation

# Statuts
statut_m1 = "OK" if mois_m1 > 2 else "ALERTE" if mois_m1 >= 1 else "RUPTURE"
statut_m2 = "OK" if mois_m2 > 2 else "ALERTE" if mois_m2 >= 1 else "RUPTURE"
statut_m3 = "OK" if mois_m3 > 2 else "ALERTE" if mois_m3 >= 1 else "RUPTURE"

# Valeur totale stock
valeur_totale = valeur_m1 + valeur_m2 + valeur_m3

# Medicament le plus critique (plus petit mois restant)
mois_min = min(mois_m1, mois_m2, mois_m3)
jours_avant_rupture = int(mois_min * 30)


# ===== AFFICHAGE =====

print("=" * 50)
print(" RAPPORT STOCK PHARMACIE CENTRALE DU CONGO")
print("=" * 50)

print("\nArtemether-Lumefantrine")
print("Valeur stock :", valeur_m1, "FCFA")
print("Mois restants :", round(mois_m1, 1))
print("Statut :", statut_m1)

print("\nAmoxicilline 500mg")
print("Valeur stock :", valeur_m2, "FCFA")
print("Mois restants :", round(mois_m2, 1))
print("Statut :", statut_m2)

print("\nSerum de rehydratation")
print("Valeur stock :", valeur_m3, "FCFA")
print("Mois restants :", round(mois_m3, 1))
print("Statut :", statut_m3)

print("\n==============================")
print("VALEUR TOTALE STOCK :", valeur_totale, "FCFA")
print("Jours avant rupture critique :", jours_avant_rupture)
print("=" * 50)
```
