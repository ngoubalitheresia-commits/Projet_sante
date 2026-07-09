# ==========================================
# CALCULATRICE - 
# Auteur : Surya Theresia
# ==========================================


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


# # Ma calculatrice
# ==========================================

while True:

    try:

        # Nombres entrés par l'utilisateur
        # ==========================================

        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))


        # Menu des opérations
        # ==========================================

        print("\nChoisissez une opération :")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")


        # L'utilisateur choisit une opération

        operation = input("Votre choix : ")


        # Les calculs
        # ==========================================

        if operation == "1":
            resultat = addition(nombre1, nombre2)

        elif operation == "2":
            resultat = soustraction(nombre1, nombre2)

        elif operation == "3":
            resultat = multiplication(nombre1, nombre2)

        elif operation == "4":
            resultat = division(nombre1, nombre2)

        elif operation == "5":
            print("Merci d'avoir utilisé la calculatrice.")
            break

        else:
            print("l'Opération est invalide. Choisissez entre 1 et 5 je vous prie.")
            continue


        # Afficher le résultat
        # ==========================================

        print("Résultat :", resultat)


    # Gestion des erreurs
    # ==========================================

    except ValueError:
        print("Vous devez entrer un nombre. Les lettres et les caractères (#,*,@) ne sont pas autorisés.")


    except ZeroDivisionError as erreur:
        print("Erreur :", erreur)