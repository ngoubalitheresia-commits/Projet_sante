# ============================================================
# CHALLENGE ENTREPRISE — TABLEAU DE BORD SANITAIRE
# ============================================================

print("=" * 64)
print("  TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE")
print("  Date : 16 janvier 2026  |  Pour le Conseil des Ministres")
print("=" * 64)
print("  HOPITAL                    OCCUPATION   ALERTES    NIVEAU GLOBAL")

#=== SECTION B : VARIABLES DES 5 HOPITAUX =================== 
# =========================
# COMPTEURS NATIONAUX
# =========================
total_ruptures = 0
nb_hopitaux_critiques = 0

# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 298
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1800000 
h1_nb_ruptures = 2
h1_nb_alertes = 2

taux_occupation = (h1_nb_lits_occupes / h1_nb_lits) * 100
#NIVEAU D'OCCUPATION
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"
#NIVEAU D'ALERTE
if h1_nb_ruptures >= 2 or taux_occupation > 95:
    niveau_global = "[CRITIQUE]"
elif h1_nb_ruptures>= 1 or taux_occupation > 85 or (h1_nb_alertes >= 2 and h1_nb_medecins < 5):
    niveau_global = "[PREOCCUPANT]"
else:
    niveau_global = "[SATISFAISANT]"

if niveau_global == "[CRITIQUE]":
    nb_hopitaux_critiques += 1

total_ruptures += h1_nb_ruptures

print(f"{h1_nom:25} {taux_occupation:6.1f}% {niveau_occ}   {h1_nb_ruptures}R + {h1_nb_alertes}A   {niveau_global}")

 # Hôpital 2 — Hôpital Général de Pointe-Noire
h2_nom = "Hôpital Général de Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Pointe-Noire"
h2_type = "Hôpital Général"
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_ruptures = 0
h2_nb_alertes = 1

taux_occupation =(h2_nb_lits_occupes / h2_nb_lits) * 100
#NIVEAU D'OCCUPATION
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"
#NIVEAU D'ALERTE
if h2_nb_ruptures >= 2 or taux_occupation > 95:
    niveau_global = "[CRITIQUE]"
elif h2_nb_ruptures >= 1 or taux_occupation > 85 or (h2_nb_alertes >= 2 and h2_nb_medecins < 5):
    niveau_global = "[PREOCCUPANT]"
else:
    niveau_global = "[SATISFAISANT]"

if niveau_global == "[CRITIQUE]":
    nb_hopitaux_critiques += 1

total_ruptures += h2_nb_ruptures

print(f"{h2_nom:25} {taux_occupation:6.1f}% {niveau_occ}   {h2_nb_ruptures}R + {h2_nb_alertes}A   {niveau_global}")

# Hôpital 3 — Hôpital de Dolisie
h3_nom = "Hôpital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hôpital Général"
h3_nb_lits = 95
h3_nb_lits_occupes = 91
h3_nb_medecins = 8
h3_nb_ruptures = 1
h3_nb_alertes = 2

taux_occupation = (h3_nb_lits_occupes / h3_nb_lits) * 100
#NIVEAU D'OCCUPATION
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"
#NIVEAU D'ALERTE
if h3_nb_ruptures >= 2 or taux_occupation > 95:
    niveau_global = "[CRITIQUE]"
elif h3_nb_ruptures >= 1 or taux_occupation > 85 or (h3_nb_alertes >= 2 and h3_nb_medecins < 5):
    niveau_global = "[PREOCCUPANT]"
else:
    niveau_global = "[SATISFAISANT]"

if niveau_global == "[CRITIQUE]":
    nb_hopitaux_critiques += 1

total_ruptures += h3_nb_ruptures

print(f"{h3_nom:25} {taux_occupation:6.1f}% {niveau_occ}   {h3_nb_ruptures}R + {h3_nb_alertes}A   {niveau_global}")

# Hôpital 4 — Hôpital de district Owando
h4_nom = "Hôpital de district Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "Hôpital de district"
h4_nb_lits = 45
h4_nb_lits_occupes = 32
h4_nb_medecins = 3
h4_nb_ruptures = 3
h4_nb_alertes = 0

taux_occupation = (h4_nb_lits_occupes / h4_nb_lits) * 100
#NIVEAU D'OCCUPATION
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"
#NIVEAU D'ALERTE
if h4_nb_ruptures >= 2 or taux_occupation > 95:
    niveau_global = "[CRITIQUE]"
elif h4_nb_ruptures >= 1 or taux_occupation > 85 or (h4_nb_alertes >= 2 and h4_nb_medecins < 5):
    niveau_global = "[PREOCCUPANT]"
else:
    niveau_global = "[SATISFAISANT]"

if niveau_global == "[CRITIQUE]":
    nb_hopitaux_critiques += 1

total_ruptures += h4_nb_ruptures

print(f"{h4_nom:25} {taux_occupation:6.1f}% {niveau_occ}   {h4_nb_ruptures}R + {h4_nb_alertes}A   {niveau_global}")


# Hôpital 5 — Centre de santé de Impfondo
h5_nom = "Centre de santé de Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de santé"
h5_nb_lits = 20
h5_nb_lits_occupes = 19
h5_nb_medecins = 1
h5_nb_ruptures = 2
h5_nb_alertes = 1
#NIVEAU D'OCCUPATION
taux_occupation = (h5_nb_lits_occupes / h5_nb_lits) * 100

if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"
#NIVEAU D'ALERTE
if h5_nb_ruptures >= 2 or taux_occupation > 95:
    niveau_global = "[CRITIQUE]"
elif h5_nb_ruptures >= 1 or taux_occupation > 85 or (h5_nb_alertes >= 2 and h5_nb_medecins < 5):
    niveau_global = "[PREOCCUPANT]"
else:
    niveau_global = "[SATISFAISANT]"

if niveau_global == "[CRITIQUE]":
    nb_hopitaux_critiques += 1

total_ruptures += h5_nb_ruptures
# AFFICHAGE D'UNE LIGNE DU TABLEAU
print(f"{h5_nom:25} {taux_occupation:6.1f}% {niveau_occ}   {h5_nb_ruptures}R + {h5_nb_alertes}A   {niveau_global}")

# =========================
# BILAN FINAL
# =========================
#Calculer le coût des commandes urgentes (BONUS)
#cout_unitaire = 450000
#cout_total = total_ruptures * cout_unitaire


print("-" * 63)
print(f"{nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
#Compter les ruptures nationales
print(f"{total_ruptures} ruptures de stock identifiees a l'echelle nationale")
print("RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA")
print("=" * 64)