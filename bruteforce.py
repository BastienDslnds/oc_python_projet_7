"""Algorithme de force brute = algorithme de résolution exacte.
- Obtenir l'ensemble des combinaisons d'actions parmi une liste d'actions
- Suggérer la liste d'actions la plus rentable
"""

import csv
from time import time


MAX_EXPENSE = 500
INPUT_FILE = csv.DictReader(open("datas/dataset_partie1.csv"))


def get_actions(input_file):
    """Obtenir les données sur les actions à partir d'un fichier.

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


def get_all_combinations(datas):
    """Obtenir toutes les combinaisons possibles d'actions.

    Args:
        datas (list): liste d'actions sous forme de dictionnaire

    Returns:
        combinations (list): liste de combinaisons d'action(s)
    """
    combinations = [[]]
    for data in datas:
        for combination in combinations.copy():
            new_combination = combination.copy()
            new_combination.append(data)
            combinations.append(new_combination)
    return combinations


def find_best_combination(combinations, max_expense):
    """Obtenir la meilleure combinaison.

    Args:
        combinations (list): liste de combinaisons d'action(s)
        max_expense (int): dépense maximale autorisée

    Returns:
        tuple:(meilleure combinaison, bénéfice associé, dépense associée)
    """
    best_combination = None
    best_benefit = 0
    best_depense = 0
    for combination in combinations:
        combination_benefit = 0
        combination_depense = 0
        for action in combination:
            combination_benefit += (
                float(action['profit']) / 100 * float(action['price'])
            )
            combination_depense += float(action['price'])
        if (
            best_depense <= combination_depense <= max_expense
            and combination_benefit >= best_benefit
        ):
            best_benefit = combination_benefit
            best_combination = combination
            best_depense = combination_depense
    return best_combination, best_benefit, best_depense


actions = get_actions(INPUT_FILE)
start_time = time()
combinations = get_all_combinations(actions)
best_combination, best_benefit, best_depense = find_best_combination(
    combinations, MAX_EXPENSE
)
end_time = time()
total_time = end_time - start_time

print("\nRésolution exacte")
print("-------------------")
print(
    f"La meilleure stratégie d'investissement est: {[action['name'] for action in best_combination]}\n"
    + f"Le bénéfice est de {best_benefit} euros\n"
    + f"La dépense est de {best_depense}\n"
)
print(f"Temps d'exécution: {total_time}s")
print(f"Nombre de combinaisons: {len(combinations)}")
