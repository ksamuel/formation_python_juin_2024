import argparse
import secrets
import string


def generer_mot_de_passe(taille, nombre, inclure_caractere_speciaux, prefix):
    caracteres_possibles = string.ascii_lowercase + string.ascii_uppercase
    caracteres_possibles += string.digits

    if inclure_caractere_speciaux:
        caracteres_possibles += string.punctuation

    for _ in range(nombre):
        mot_de_passe = prefix
        for _ in range(taille):
            mot_de_passe += secrets.choice(caracteres_possibles)

        print(mot_de_passe)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Un générateur de mot passe")

    # Paramètres positionnels
    # obligatoire
    parser.add_argument(
        "taille", type=int, help="Le nombre de caractères du mot de passe"
    )

    # optionnel
    parser.add_argument(
        "nombre",
        nargs="?",
        default=1,
        type=int,
        help="Le nombre de mots de passe à générer",
    )

    # Flag
    parser.add_argument(
        "-s",
        "--inclure-caracteres-speciaux",
        action="store_true",
        help="Activer ou pas l'inclusion des caractères speciaux dans le mot de passe",
    )

    # Option (with a default value)
    parser.add_argument(
        "-p",
        "--prefix",
        type=str,
        default="",
        help="Prefixer les mots de passe avec...",
    )

    args = parser.parse_args()

    generer_mot_de_passe(
        nombre=args.nombre,
        taille=args.taille,
        inclure_caractere_speciaux=args.inclure_caracteres_speciaux,
        prefix=args.prefix,
    )
