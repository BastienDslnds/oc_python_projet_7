"""Algorithme optimisé"""

import csv
from time import time


MAX_COST = 500
INPUT_FILE = csv.DictReader(open("datas/dataset1_Python+P7.csv"))


def get_actions(input_file):
    """Obtenir les données sur les actions.

    Args:
        input_file (DictReader): fichier avec les actions

    Returns:
        actions(list): liste d'actions
    """
    actions = []
    for row in input_file:
        price = float(row['price'])
        profit = float(row['profit'])
        if price > 0 and profit > 0:
            actions.append(row)
    return actions


def sort_actions_by_benefit(actions):
    """
    Tri la liste de dictionnaires selon le profit.
    """

    def get_benefit(action):
        profit = float(action['profit'])

        return profit

    actions_sorted = sorted(actions, key=get_benefit)

    return actions_sorted


def get_optimized_combination(sorted_actions, max_cost):
    """
    HYPOTHÈSE : la liste de dictionnaires est triée par ordre croissant des profits.

    Retourne un tuple constitué d'une liste optimisée contenant les noms des actions sélectionnées,
    la valeur du bénéfice et le coût total.
    """
    result = []
    cost = 0
    benefit = 0
    i = len(sorted_actions) - 1
    while i >= 0:
        action = sorted_actions[i]
        if (cost + float(action['price'])) < max_cost:
            result.append(action['name'])
            cost += float(action['price'])
            benefit += float(action['profit']) / 100 * float(action['price'])
        i -= 1

    return (result, benefit, cost)


start_time = time()
actions = get_actions(INPUT_FILE)
sorted_actions = sort_actions_by_benefit(actions)
combination, benefit, cost = get_optimized_combination(
    sorted_actions, MAX_COST
)
end_time = time()
total_time = end_time - start_time

print("\nStratégie gloutonne")
print("-------------------")
print("Meilleure stratégie d'investissement : {}".format(combination))
print("Bénéfice de la combinaison : {}".format(benefit))
print("Coût de la combinaison : {}".format(cost))
print(f"Temps d'exécution: {total_time}s")
print()
