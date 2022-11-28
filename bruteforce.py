"""Algorithme de force brute:

- Obtenir l'ensemble des combinaisons d'actions parmi une liste d'actions
- Suggérer la liste d'actions la plus rentable

"""

from time import time


actions_cout = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
actions_benefit = {"20": 0.05,
                "30": 0.10,
                "50": 0.15,
                "70": 0.20,
                "60": 0.17,
                "80": 0.25,
                "22": 0.07,
                "26": 0.11,
                "48": 0.13,
                "34": 0.27,
                "42": 0.17,
                "110": 0.09,
                "38": 0.23,
                "14": 0.01,
                "18": 0.03,
                "8": 0.08,
                "4": 0.12,
                "10": 0.14,
                "24": 0.21,
                "114": 0.18}


def get_all_combinations(list_actions):
    combinations = [[]]
    for action in list_actions:
        for combination in combinations.copy():
            new_combination = combination.copy()
            new_combination.append(action)
            if sum(new_combination) <= 500:
                combinations.append(new_combination)
    combinations.remove([])
    return combinations


def find_best_combination(combinations):
    best_combination = None
    best_benefit = 0
    for combination in combinations:
        benefit = 0
        for action in combination:
            benefit += action*actions_benefit[str(action)]
        if benefit > best_benefit:
            best_benefit = benefit
            best_combination = combination
    return best_combination, best_benefit


start_time = time()
combinations = get_all_combinations(actions_cout)
best_combination, best_benefit = find_best_combination(combinations)
end_time = time()
total_time = end_time - start_time
print(f"La combinaison d'actions la plus rentable est: {best_combination}\n" +
f"Le bénéfice est de {best_benefit} euros\n")
print(f"Temps d'exécution: {total_time}s")
