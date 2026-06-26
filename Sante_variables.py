# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# ============================================================ 
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS 
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
DEPARTEMENTS_CONGO = [              # 12 departements officiels 
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha' 
]     
 
#=== SECTION B : VARIABLES DES 5 HOPITAUX =================== 
# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 284 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1800000 
h1_nb_ruptures = 2
h1_nb_alertes = 2
# ... (completer pour les 4 autres hopitaux) 
 # Hôpital 2 — Hôpital Général de Pointe-Noire
h2_nom = "Hôpital Général de Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "kouilou"
h2_type = "Hôpital Général"
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 128_000
h2_nb_ruptures = 0
h2_nb_alertes = 1

# Hôpital 3 — Hôpital de Dolisie
h3_nom = "Hôpital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hôpital Général"
h3_nb_lits = 95
h3_nb_lits_occupes = 91
h3_nb_medecins = 8
h3_nb_infirmiers = int(input('h3_nb_infirmiers : '))
h3_population_zone = int(input('h3_nb_infirmiers : '))
h3_nb_ruptures = 1
h3_nb_alertes = 2

# Hôpital 4 — Hôpital de district Owando
h4_nom = "Hôpital de district Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "Hôpital de district"
h4_nb_lits = 45
h4_nb_lits_occupes = 32
h4_nb_medecins = 3
h4_nb_infirmiers = int(input('h4_nb_infirmiers : '))
h4_population_zone = int(input('h4_population_zone: '))
h4_nb_ruptures = 3
h4_nb_alertes = 0

# Hôpital 5 — Centre de santé de Impfondo
h5_nom = "Centre de santé de Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de santé"
h5_nb_alertes = 1

# === SECTION C : VARIABLES DES 5 MEDICAMENTS =========
h5_nb_lits = 20
h5_nb_lits_occupes = 19
h5_nb_medecins = 1
h5_nb_infirmiers = int(input('h5_nb_infirmiers: '))
h5_population_zone = int(input('h5_population_zone : '))
h5_nb_ruptures = 2
# TODO : Declarer les 5 medicaments essentiels 
#Médicament 1 
m1_nom = "Artéméther_Luméfantrine"
m1_stock = 3200
m1_seuil_rupture = 2000
m1_cout_unitaire = 3500.0

# Médicament 2 
m2_nom = "Amoxicilline"  
m2_stock = 950
m2_seuil_rupture = 800
m2_cout_unitaire = 850.0

# Médicament 3 
m3_nom = "Paracétamol"
m3_stock = 12400
m3_seuil_rupture = 3000
m3_cout_unitaire = 120.0

# Médicament 4 
m4_nom = "SRO"
m4_stock = 4200
m4_seuil_rupture = 5000
m4_cout_unitaire = 125.0

# Médicament 5 
m5_nom = "Vaccin antipaludéen"
m5_stock = 820
m5_seuil_rupture = 1000
m5_cout_unitaire = 8500.0
 
# === SECTION D : CALCULS D'INITIALISATION =================== 
# TODO : Calculer les KPIs globaux initiaux 

# Total des médecins
total_medecins = (
    h1_nb_medecins +
    h2_nb_medecins +
    h3_nb_medecins +
    h4_nb_medecins +
    h5_nb_medecins
)

# Population totale couverte
POPULATION_TOTALE = (
    h1_population_zone +
    h2_population_zone +
    h3_population_zone +
    h4_population_zone +
    h5_population_zone
)

## Densité médicale nationale (pour 1000 habitants)
DENSITE_MEDICALE_NATIONALE = (total_medecins / POPULATION_TOTALE) * 1000

# Total des lits
total_lits = (
    h1_nb_lits +
    h2_nb_lits +
    h3_nb_lits +
    h4_nb_lits +
    h5_nb_lits
)

# Total des lits occupés
total_lits_occupes = (
    h1_nb_lits_occupes +
    h2_nb_lits_occupes +
    h3_nb_lits_occupes +
    h4_nb_lits_occupes +
    h5_nb_lits_occupes
)

##Taux d'occupation moyen (%)
taux_occupation= (total_lits_occupes / total_lits) * 100

##Valeur totale du stock de médicaments (FCFA)
VALEUR_STOCK_TOTALE = (
    m1_stock* m1_cout_unitaire +
    m2_stock * m2_cout_unitaire +
    m3_stock * m3_cout_unitaire +
    m4_stock* m4_cout_unitaire +
    m5_stock * m5_cout_unitaire
)

# === SECTION E : RAPPORT D'INVENTAIRE ======================= 
# TODO : Afficher le rapport initial du systeme de sante 

print("=" * 60)
print("      RAPPORT INITIAL DU SYSTÈME DE SANTÉ")
print("=" * 60)

print("\nHÔPITAUX ENREGISTRÉS :", 5)
print("MÉDICAMENTS ESSENTIELS :", 5)

print("\n------ INDICATEURS GLOBAUX ------")
print(f"Population totale couverte : {POPULATION_TOTALE:,} habitants")
print(f"Nombre total de médecins : {total_medecins}")
print(f"Densité médicale : {DENSITE_MEDICALE_NATIONALE:.2f} médecins pour 1000 habitants")
print(f"Taux moyen d'occupation des lits : {taux_occupation:.2f} %")
print(f"Valeur totale du stock : {VALEUR_STOCK_TOTALE:,.2f} FCFA")

print("\n------ HÔPITAUX ------")
print(f"1. {h1_nom} ({h1_ville})")
print(f"2. {h2_nom} ({h2_ville})")
print(f"3. {h3_nom} ({h3_ville})")
print(f"4. {h4_nom} ({h4_ville})")
print(f"5. {h5_nom} ({h5_ville})")

print("\n------ MÉDICAMENTS ------")
print(f"- {m1_nom} : {m1_stock} unités")
print(f"- {m2_nom} : {m2_stock} unités")
print(f"- {m3_nom} : {m3_stock} unités")
print(f"- {m4_nom} : {m4_stock} unités")
print(f"- {m5_nom} : {m5_stock} unités")

print("\nSystème initialisé avec succès.")
print("=" * 60)

#SECTION F: CLASSIFICATION STATUT STOCKS 
# S3 (nouveau) : if / elif / else
# S2 (reutilise) : operateurs arithmetiques pour calcul des seuils
#m1
if m1_stock <= m1_seuil_rupture:
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut  = "ALERTE STOCK"
    m1_couleur = " [ORANGE]"
    m1_action  = "Commande urgente a declencher sous 72h"
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut  = "STOCK LIMITE"
    m1_couleur = "[JAUNE] "
    m1_action  = "Surveillance renforcee — planifier commande"
else:
    m1_statut  = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action  = 'Situation normale — suivi standard'
 # TODO : Reproduire la meme logique pour m2, m3, m4, m5
    # m2
if m2_stock <= m2_seuil_rupture:
    m2_statut  = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut  = "ALERTE STOCK"
    m2_couleur = " [ORANGE]"
    m2_action  = "Commande urgente a declencher sous 72h"
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut  = "STOCK LIMITE"
    m2_couleur = "[JAUNE] "
    m2_action  = 'Surveillance renforcee — planifier commande'
else:
    m2_statut  = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action  ='Situation normale — suivi standard'
   #m3
if  m3_stock <= m3_seuil_rupture:
    m3_statut  = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action  = 'Alerte immediate PNA — commande express sous 24h'

elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut  = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action  = 'Commande urgente a declencher sous 72h'

elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut  = 'STOCK LIMITE'
    m3_couleur = '[JAUNE]'
    m3_action  = 'Surveillance renforcee — planifier commande'

else:
    m3_statut  = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action  = 'Situation normale — suivi standard'
    #m4
if  m4_stock <= m4_seuil_rupture:
    m4_statut  = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action  = 'Alerte immediate PNA — commande express sous 24h'

elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut  = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action  = 'Commande urgente a declencher sous 72h'

elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut  = 'STOCK LIMITE'
    m4_couleur = '[JAUNE]'
    m4_action  = 'Surveillance renforcee — planifier commande'

else:
    m4_statut  = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action  = 'Situation normale — suivi standard'

    #m5
if  m5_stock <= m5_seuil_rupture:
    m5_statut  = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action  = 'Alerte immediate PNA — commande express sous 24h'

elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut  = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action  = 'Commande urgente a declencher sous 72h'

elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut  = 'STOCK LIMITE'
    m5_couleur = '[JAUNE]'
    m5_action  = 'Surveillance renforcee — planifier commande'

else:
    m5_statut  = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action  = 'Situation normale — suivi standard'
#SECTION G: CLASSIFICATION OCCUPATION HOPITAUX
#NIVEAU D'OCCUPATION
    taux_occupation = (h1_nb_lits_occupes / h1_nb_lits) * 100
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"

    taux_occupation =(h2_nb_lits_occupes / h2_nb_lits) * 100
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"

    taux_occupation = (h3_nb_lits_occupes / h3_nb_lits) * 100
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"
taux_occupation = (h4_nb_lits_occupes / h4_nb_lits) * 100

if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"

taux_occupation = (h5_nb_lits_occupes / h5_nb_lits) * 100
if taux_occupation > 95:
    niveau_occ = "[CRI]"
elif taux_occupation > 85:
    niveau_occ = "[ALT]"
else:
    niveau_occ = "[OK ]"

#SECTION H : Classification couverture vaccinale 
# ============================================================
# CLASSIFICATION COUVERTURE VACCINALE — DSS SANTE PUBLIQUE
# ============================================================

print("=" * 60)
print("  CLASSIFICATION COUVERTURE VACCINALE PAR DEPARTEMENT")
print("=" * 60)
print("Departement        Population  Vaccines   Taux   Statut OMS")
print("-" * 60)

# =========================
# FONCTION D'AFFICHAGE
# =========================
def afficher_vaccin(dept, pop, vacc):
    taux = (vacc / pop) * 100

    # Classification OMS
    if taux >= 95:
        statut = "ZONE SATISFAISANTE"
    elif taux >= 80:
        statut = "ZONE INSUFFISANTE"
    elif taux >= 50:
        statut = "ZONE A RISQUE"
    else:
        statut = "ZONE CRITIQUE"

    print(f"{dept:18} {pop:10} {vacc:10} {taux:6.1f}%  {statut}")

    return taux

# =========================
# DONNEES
# =========================

t1 = afficher_vaccin("Brazzaville", 450000, 418500)
t2 = afficher_vaccin("Pointe-Noire", 280000, 229600)
t3 = afficher_vaccin("Pool", 120000, 54000)
t4 = afficher_vaccin("Sangha", 85000, 35700)

# =========================
# BILAN GLOBAL
# =========================

print("-" * 60)

taux_moyen = (t1 + t2 + t3 + t4) / 4

print(f"Taux moyen national : {taux_moyen:.1f}%")

if taux_moyen >= 90:
    print("RECOMMANDATION : Situation globale satisfaisante")
elif taux_moyen >= 75:
    print("RECOMMANDATION : Renforcer la couverture vaccinale")
else:
    print("RECOMMANDATION : Situation critique — intervention urgente")

print("=" * 60)

#SECTION I : Rapport d'etat global avec alertes 

# --- COMPTAGE DES ALERTES ---
# S2 (reutilise) : variables numeriques
# S3 (nouveau) : conditions pour compter
# ETAT GLOBAL AVEC ALERTES MEDICAMENTS
nb_ruptures_critiques = 0
nb_alertes_stock      = 0
# TODO : Utiliser des if pour incrementer les compteurs
# Exemple : if m1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = 
nb_ruptures_critiques + 1

# M1
if m1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques+ 1
elif m1_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1

# M2
if m2_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques+1
elif m2_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1

# M3
if m3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques+1
elif m3_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1

# M4
if m4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques =nb_ruptures_critiques+ 1
elif m4_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1

# M5
if m5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques =nb_ruptures_critiques+ 1
elif m5_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1

# --- AFFICHAGE RAPPORT --
# S2 (reutilise) : f-strings structurees
# S3 (nouveau) : statuts et couleurs determines par les conditions
print('=' * 65)
print('  RAPPORT DE STOCK — PHARMACIE NATIONALE D APPROVISIONNEMENT')
print('  Date : 15 janvier 2026')
print('=' * 65)
# TODO : Afficher les 5 medicaments avec leur statut
print(f'  {m1_couleur} {m1_nom}')
print(f'      Stock : {m1_stock} unites | Seuil : {m1_seuil_rupture}')
print(f'      Statut : {m1_statut}')
print(f'      Action : {m1_action}')
print('-' * 65)

print(f'  {m2_couleur} {m2_nom}')
print(f'      Stock : {m2_stock} unites | Seuil : {m2_seuil_rupture}')
print(f'      Statut : {m2_statut}')
print(f'      Action : {m2_action}')
print('-' * 65)

print(f'  {m3_couleur} {m3_nom}')
print(f'      Stock : {m3_stock} unites | Seuil : {m3_seuil_rupture}')
print(f'      Statut : {m3_statut}')
print(f'      Action : {m3_action}')
print('-' * 65)

print(f'  {m4_couleur} {m4_nom}')
print(f'      Stock : {m4_stock} unites | Seuil : {m4_seuil_rupture}')
print(f'      Statut : {m4_statut}')
print(f'      Action : {m4_action}')
print('-' * 65)

print(f'  {m5_couleur} {m5_nom}')
print(f'      Stock : {m5_stock} unites | Seuil : {m5_seuil_rupture}')
print(f'      Statut : {m5_statut}')
print(f'      Action : {m5_action}')
print('-' * 65)

 # TODO : Afficher le bilan final (compteurs + alerte prioritaire)
 #compteurs 
print('=' * 65)
print('  BILAN STOCK — PNA CONGO')
print(f'  Ruptures critiques : {nb_ruptures_critiques}')
print(f'  Alertes stock      : {nb_alertes_stock}')
print(f'  Stocks normaux     : {5 - nb_ruptures_critiques - nb_alertes_stock}')
print('=' * 65)

# Alerte prioritaire
if nb_ruptures_critiques > 0:
    print(f'  !! ALERTE PRIORITAIRE : {nb_ruptures_critiques} medicaments en RUPTURE CRITIQUE !!')
    print('  Transmettre immediatement au Dr. MOUKALA (PNA)')
print('=' * 65)


# ETAT GLOBAL AVEC ALERTES HOPITAUX
#NIVEAU D'ALERTE H1
# COMPTEURS NATIONAUX
nb_hopitaux_critiques = 0
nb_ruptures_totales = 0
total_ruptures = 0
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

#NIVEAU D'ALERTE H3
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

#NIVEAU D'ALERTE H4
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
#NIVEAU D'ALERTE H5
if h5_nb_ruptures >= 2 or taux_occupation > 95:
    niveau_global = "[CRITIQUE]"
elif h5_nb_ruptures >= 1 or taux_occupation > 85 or (h5_nb_alertes >= 2 and h5_nb_medecins < 5):
    niveau_global = "[PREOCCUPANT]"
else:
    niveau_global = "[SATISFAISANT]"

if niveau_global == "[CRITIQUE]":
    nb_hopitaux_critiques += 1

total_ruptures += h5_nb_ruptures
print(f"{h5_nom:25} {taux_occupation:6.1f}% {niveau_occ}   {h5_nb_ruptures}R + {h5_nb_alertes}A   {niveau_global}")
# RAPPORT
print("-" * 63)
print(f"{nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
#Compter les ruptures nationales
print(f"{total_ruptures} ruptures de stock identifiees a l'echelle nationale")
print("RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA")
print("=" * 64)