# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 1 : Classification Stocks Medicaments
# Utilise les notions de S2 (variables, types, operateurs, f-strings)
# + S3 (if/elif/else, conditions composees)
# ============================================================
# --- DONNEES S2 : Variables medicaments --
# (Reimporter depuis sante_variables.py ou redeclarer ici)
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   # FCFA
m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0
m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0
m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0
m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0
# --- CLASSIFICATION MEDICAMENT 1 : Artemether-Lumefantrine --
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
# (Ne pas copier-coller sans adapter les variables !)
# --- COMPTAGE DES ALERTES ---
# S2 (reutilise) : variables numeriques
# S3 (nouveau) : conditions pour compter
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

# =========================
# EDGE CASES (DOCUMENTATION)
# =========================
 #m1_stock= m1_seuil_rupture        # test rupture exacte
 #m2_stock= m2_seuil_rupture + 100  # test passage alerte