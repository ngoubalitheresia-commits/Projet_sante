# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 2 — Challenge Entreprise
# Rapport comparatif des 3 hôpitaux du département du Pool
# ============================================================

# ============================================================
# HÔPITAL DISTRICT DE KINKALA
# ============================================================

budget_trim_kinkala = 12500000
consultations_ext_kinkala = 1847
hospitalisations_kinkala = 312
deces_hodpitaliers_kinkala= 8
lits_totaux_kinkala= 45
lits_occupes_kinkala = 41
medecins_permanants_kinkala= 3
population_desservie_kinkala= 85000

# ============================================================
# CMS DE VINDZA
# ============================================================

budget_trim_vindza = 6800000
consultations_ext_vindza = 923
hospitalisations_vindza = 87
deces_hospitaliers_vindza= 2
lits_totaux_vindza= 20
lits_occupes_vindza= 14
medecins_permanents_vindza= 1
population_desservie_vindza = 42000

# ============================================================
# HÔPITAL DE KINDAMBA
# ============================================================

budget_trim_kindamba = 9200000
consultations_ext_kindamba = 1234
hospitalisations_kindamba = 201
deces_hospitaliers_kindamba = 11
lits_totaux_kindamba= 35
lits_occupes_kindamba = 33
medecins_permanants_kindamba = 2
population_desservie_kindamba= 67000

# ============================================================
# CALCUL DES KPIs
# ============================================================

# ---------- KINKALA ----------
patients_kinkala = consultations_ext_kinkala + hospitalisations_kinkala

cout_patient_kinkala = round(
    budget_trim_kinkala / patients_kinkala, 2
)

taux_occupation_kinkala = round(
    (lits_occupes_kinkala/ lits_totaux_kinkala) * 100,
    2
)

densite_kinkala = round(
    (medecins_permanants_kinkala / population_desservie_kinkala) * 1000,
    2
)

taux_mortalite_kinkala = round(
    (deces_hodpitaliers_kinkala / hospitalisations_kinkala) * 100,
    2)

# ---------- VINDZA ----------
patients_vindza = consultations_ext_vindza + hospitalisations_vindza

cout_patient_vindza = round(
    budget_trim_vindza / patients_vindza,
    2
)

taux_occupation_vindza = round(
    (lits_occupes_vindza / lits_totaux_vindza) * 100,
    2
)

densite_vindza = round(
    (medecins_permanents_vindza / population_desservie_vindza) * 1000,
    2
)

taux_mortalite_vindza = round(
    (deces_hospitaliers_vindza / hospitalisations_vindza) * 100,
    2
)

# ---------- KINDAMBA ----------
patients_kindamba = consultations_ext_kindamba + hospitalisations_kindamba

cout_patient_kindamba = round(
    budget_trim_kindamba / patients_kindamba,
    2
)

taux_occupation_kindamba = round(
    (lits_occupes_kindamba / lits_totaux_kindamba) * 100,
    2
)

densite_kindamba = round(
    (medecins_permanants_kindamba / population_desservie_kindamba) * 1000,
    2
)

taux_mortalite_kindamba = round(
    (deces_hospitaliers_kindamba / hospitalisations_kindamba) * 100,
    2
)

# ============================================================
# IDENTIFICATION DES HÔPITAUX CRITIQUES
# ============================================================
#Situation critique (taux de mortalité >2% ou densité<0,05)

critique_kinkala = (
    taux_mortalite_kinkala > 2
    or densite_kinkala < 0.05
)

critique_vindza = (
    taux_mortalite_vindza > 2
    or densite_vindza < 0.05
)

critique_kindamba = (
    taux_mortalite_kindamba > 2
    or densite_kindamba < 0.05
)

statut_kinkala = "SITUATION CRITIQUE" if critique_kinkala else " STABLE"
statut_vindza = " SITUATION CRITIQUE" if critique_vindza else "STABLE"
statut_kindamba = "SITUATION CRITIQUE" if critique_kindamba else " STABLE"

# ============================================================
# BONUS
# Budget nécessaire pour avoir 5 médecins par hôpital
# ============================================================

cout_medecin = 1_200_000

medecins_a_recruter = (
    max(0, 5 - medecins_permanants_kinkala)
    + max(0, 5 - medecins_permanents_vindza)
    + max(0, 5 - medecins_permanants_kindamba)
)

cout_total_recrutement = (
    medecins_a_recruter * cout_medecin
)

budget_total = (
    budget_trim_kinkala
    + budget_trim_vindza
    + budget_trim_kindamba
)

budget_suffisant = (
    budget_total >= cout_total_recrutement
)

# ============================================================
# RAPPORT CONSOLIDÉ
# ============================================================

print("=" * 70)
print("RAPPORT COMPARATIF DES HÔPITAUX DU DÉPARTEMENT DU POOL")
print("=" * 70)

print(f"""
Hôpital District de Kinkala
------------------------------------------------------------
Coût moyen par patient : {cout_patient_kinkala} FCFA
Taux d'occupation      : {taux_occupation_kinkala} %
Densité médicale       : {densite_kinkala} médecins / 1000 hab.
Taux de mortalité      : {taux_mortalite_kinkala} %
Statut                 : {statut_kinkala}
""")

print(f"""
CMS de Vindza
------------------------------------------------------------
Coût moyen par patient : {cout_patient_vindza} FCFA
Taux d'occupation      : {taux_occupation_vindza} %
Densité médicale       : {densite_vindza} médecins / 1000 hab.
Taux de mortalité      : {taux_mortalite_vindza} %
Statut                 : {statut_vindza}
""")

print(f"""
Hôpital de Kindamba
------------------------------------------------------------
Coût moyen par patient : {cout_patient_kindamba} FCFA
Taux d'occupation      : {taux_occupation_kindamba} %
Densité médicale       : {densite_kindamba} médecins / 1000 hab.
Taux de mortalité      : {taux_mortalite_kindamba} %
Statut                 : {statut_kindamba}
""")

print("=" * 70)
print("BONUS : RECRUTEMENT DE MÉDECINS")
print("=" * 70)

print(f"Budget total disponible : {budget_total:,} FCFA")
print(f"Médecins à recruter : {medecins_a_recruter}")
print(f"Coût du recrutement : {cout_total_recrutement:,} FCFA")

if budget_suffisant:
    print(" Le budget est suffisant pour disposer de 5 médecins dans chaque hôpital.")
else:
    manque = cout_total_recrutement - budget_total
    print(f" Budget insuffisant. Il manque {manque:,} FCFA.")

print("=" * 70)
print("FIN DU RAPPORT")
print("=" * 70)



#Densite < 0.05 et taux_mortalite > 2%
#le fait est que tous les  hôpitaux sont critiques à cause de la densité, car :
#Kinkala = 0.04 → critique par densité. 
#Vindza = 0.02 → critique par densité. 
#Kindamba = 0.03 → critique par densité. 
#En plus, les trois ont aussi un taux de mortalité supérieur à 2 % :
#Kinkala ≈ 2.56 % 
#Vindza ≈ 2.30 % 
#Kindamba ≈ 5.47 % 
#Avec les données , les trois hôpitaux seront donc signalés "CRITIQUE", ce qui est cohérent avec les critères donnés dans l'énoncé. 
