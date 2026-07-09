# ==========================================
# CALCULATRICE - STREAMLIT
# Auteur : Surya Theresia
# ==========================================

import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;
    }

    h1 {
        color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Définition des fonctions
# ==========================================

def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    # Instruction pour éviter la division par zéro
    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro.")
    return a / b


# Ma calculatrice Streamlit
# ==========================================

st.title("🧮 CALCULATRICE - Surya")


# Nombres entrés par l'utilisateur
# ==========================================

nombre1 = st.number_input("Entrez le premier nombre : ")

nombre2 = st.number_input("Entrez le deuxième nombre : ")


# Menu des opérations
# ==========================================

operation = st.selectbox(
    "Choisissez une opération :",
    [
        "1. Addition",
        "2. Soustraction",
        "3. Multiplication",
        "4. Division",
        "5. Quitter"
    ]
)


# Bouton calcul
# ==========================================

if st.button("Calculer"):

    try:

        if operation == "1. Addition":
            resultat = addition(nombre1, nombre2)

        elif operation == "2. Soustraction":
            resultat = soustraction(nombre1, nombre2)

        elif operation == "3. Multiplication":
            resultat = multiplication(nombre1, nombre2)

        elif operation == "4. Division":
            resultat = division(nombre1, nombre2)

        elif operation == "5. Quitter":
            st.write("Merci d'avoir utilisé la calculatrice.")

        else:
            st.write("l'Opération est invalide. Choisissez entre 1 et 5 je vous prie.")


        if operation != "5. Quitter":
            st.success(f"Résultat : {resultat}")


    # Gestion des erreurs
    # ==========================================

    except ValueError:
        st.error("Vous devez entrer un nombre. Les lettres et les caractères (#,*,@) ne sont pas autorisés.")


    except ZeroDivisionError as erreur:
        st.error(f"Erreur : {erreur}")