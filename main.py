import doctest
import copy
import functools

def autotest(func):
    globs = copy.copy(globals())
    globs.update({func.__name__: func})
    doctest.run_docstring_examples(
        func, globs, verbose=True, name=func.__name__)
    return func


import json
from ast import literal_eval

nom_fichier = 'information_u.json'

"""methode divise par 16 le nombre de personne#  """


def calcul(nb_part):
    nb_grp = 16 // int(nb_part)

    return nb_grp


"""rajout du JSON pour sauvegarder les compétenses et les niveaux"""
"""methode pour sauvegarder dans un fichier json"""


def sav_com(item, lvl, comp):
    with open(nom_fichier, 'w') as fichier:
        json.dump(str({'nom': item, 'Niveau': lvl, 'compétence': comp}), fichier)


"""methode pour lire le fichier json"""


def read_com():
    with open(nom_fichier, 'r') as fichier:
        information_user = json.load(fichier)
        return information_user


"""rattachement de la méthode lire et sauvegarde dans la prise en compte des compétences"""


def comp(lvl, comp):
    comp = ""
    lvl = ""
    comp = input("\033[32m La compétence :\033[0m").lower()
    for item in participant:
        lvl = input("\033[32m Quel est le niveau de " + item + ":\033[0m").lower()
        sav_com(item, lvl, comp)
        information_utilisateur = literal_eval(read_com())
        for (key, valeur) in information_utilisateur.items():
            print(f"{key} est sur {valeur}")


"""methode qui randomise les participant dans groupe et les supprimes ce participant de la liste"""


def create_grp():
    for i in y:
        groupe = []
        for i in x:
            used = random.choice(participant)
            groupe.append(used)
            participant.remove(used)

        list_grp.append(groupe)

        if len(participant) < int(nb_part):
            groupe = []
            for item in participant:
                groupe = list_grp[-1]
                groupe.append(item)
                participant.remove(item)

            print("\033[31mVoici les groupes {0}\033[0m".format(list_grp))

            """Methode qui permet de tester une partie du code """

            @autotest
            def calcul(nb_part):

                """NB only INT

                >>> calcul(4)
                4
                """
                return 16 // int(nb_part)

            """methode qui vérouille la demande en interger et limite les demandes de groupe de 1 à 8 participants maximum"""

            def check_nb_part():

                nb = "0"
                while int(nb) > 8 or int(nb) == 0:

                    try:
                        nb = int(input(
                            "\033[32mVeuillez entrer le nombre de personne dans un groupe entre 1 et 8 personnes: \033[0m"))

                    except ValueError:
                        print("Vous n'avez pas saisi de nombre entre 1 et 8")

                nb_part = nb

                return nb_part

            import random

            print("\033[32m\n----------------------------------------\n\033[0m")
            print('\033[32mBienvenue dans votre application.\033[0m')
            print("\033[32m\n----------------------------------------\n\033[0m")

            """boucle qui indique à l'utilisateur ce qu'il souhaite faire et lance les méthodes en fonction des réponses"""
            choix = ""
            while choix != "q":
                choix = input("\033[33m\n(s) Pour créer des groupes.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
                if choix == "s":
                    participant = ["Farid", "Marie", "Phichet", "Arthur", "Antoine", "Hatice", "Giovanni", "Mickael",
                                   "Rachid", "Julien", "Vivien", "Kevin", "Josephine", "Valentin", "Camille", "Tanguy"]

                    nb_part = check_nb_part()

                    nb_grp = calcul(nb_part)
                    x = range(int(nb_part))
                    y = range(int(nb_grp))
                    list_grp = []

                    A = ""
                    lvl = ""
                    while A != "o" and A != "n":
                        A = input("\033[32m Souhaitez-vous faire des groupes par compétence. (o/n) : \033[0m").lower()

                        if A == "n":
                            create_grp()

                        if A == "o":
                            comp(lvl, comp)

                if choix == "q":
                    print("A bientôt.")