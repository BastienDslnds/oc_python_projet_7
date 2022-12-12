"""Algorithme de force brute = algorithme de résolution exacte.
- Obtenir l'ensemble des combinaisons d'actions parmi une liste d'actions
- Suggérer la liste d'actions la plus rentable
"""

from time import time


actions = [
    {'nom': "Action-1", 'cout': 20, 'profit': 0.05},
    {'nom': "Action-2", 'cout': 30, 'profit': 0.10},
    {'nom': "Action-3", 'cout': 50, 'profit': 0.15},
    {'nom': "Action-4", 'cout': 70, 'profit': 0.20},
    {'nom': "Action-5", 'cout': 60, 'profit': 0.17},
    {'nom': "Action-6", 'cout': 80, 'profit': 0.25},
    {'nom': "Action-7", 'cout': 22, 'profit': 0.07},
    {'nom': "Action-8", 'cout': 26, 'profit': 0.11},
    {'nom': "Action-9", 'cout': 48, 'profit': 0.13},
    {'nom': "Action-10", 'cout': 34, 'profit': 0.27},
    {'nom': "Action-11", 'cout': 42, 'profit': 0.17},
    {'nom': "Action-12", 'cout': 110, 'profit': 0.09},
    {'nom': "Action-13", 'cout': 38, 'profit': 0.23},
    {'nom': "Action-14", 'cout': 14, 'profit': 0.01},
    {'nom': "Action-15", 'cout': 18, 'profit': 0.03},
    {'nom': "Action-16", 'cout': 8, 'profit': 0.08},
    {'nom': "Action-17", 'cout': 4, 'profit': 0.12},
    {'nom': "Action-18", 'cout': 10, 'profit': 0.14},
    {'nom': "Action-19", 'cout': 24, 'profit': 0.21},
    {'nom': "Action-20", 'cout': 114, 'profit': 0.18},
]


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
            combination_benefit += action['profit'] * action['cout']
            combination_depense += action['cout']
        if (
            best_depense <= combination_depense <= max_expense
            and combination_benefit >= best_benefit
        ):
            best_benefit = combination_benefit
            best_combination = combination
            best_depense = combination_depense
    return best_combination, best_benefit, best_depense


start_time = time()
combinations = get_all_combinations(actions)
best_combination, best_benefit, best_depense = find_best_combination(
    combinations, 500.0
)
end_time = time()
total_time = end_time - start_time

print("\nRésolution exacte:\n")
print(
    f"La combinaison d'actions la plus rentable est: {[action['nom'] for action in best_combination]}\n"
    + f"Le bénéfice est de {best_benefit} euros\n"
    + f"La dépense est de {best_depense}\n"
)
print(f"Temps d'exécution: {total_time}s")
print(f"Nombre de combinaisons: {len(combinations)}")
