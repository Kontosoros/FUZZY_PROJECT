# https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html
# STO PARAKATW LINK EINAI TO IDIO PROVLIMA APLA PIO ANALITIKO ME KODIKO.
# STO PIO PANO LINK EINAI ME LIBRARIES PIO SIMPIKNOMENW
# https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html
# EPISIS STIN TELEFTEA GRAMI EVALA TO plt.show() ALLIOS DEN EMFANIZEI TIS GRAFIKES
import numpy as np

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def test(danger, danger_status):
    for age in range(1,100):
        danger.input["age"] = age
        for cigarettes in range(1, 50):
            danger.input["Cigarettes"] = cigarettes
            for exercise in range (1, 7):
                danger.input["Exercise"] = exercise
                for anxiety in range(1, 10):
                    danger.input["Anxiety"] = anxiety
                    for eating_unhealthy in range(1, 10):
                        danger.input["Eating unhealthy"] = eating_unhealthy
                        print("age", age)
                        print("Cigarettes", cigarettes)
                        print("Exercise", exercise)
                        print("Anxiety", anxiety)
                        print("Eating unhealthy", eating_unhealthy)
                        danger.compute()
                        print("STATUS :", danger.output["Danger_status"])
                        # danger_status.view(sim=danger)
                        print("=====================================")




# New Antecedent/Consequent objects hold universe variables and membership
# functions
age = ctrl.Antecedent(np.arange(0, 101, 1), "age")
cigarettes = ctrl.Antecedent(np.arange(0, 21, 1), "Cigarettes")
exercise = ctrl.Antecedent(np.arange(0, 8, 1), "Exercise")
anxiety = ctrl.Antecedent(np.arange(0, 11, 1), "Anxiety")
eating_unhealthy = ctrl.Antecedent(np.arange(0, 11, 1), "Eating unhealthy")
danger_status = ctrl.Consequent(np.arange(0, 101, 5), "Danger_status")

# Auto-membership function population is possible with .automf(3, 5, or 7)


# Oi ilikiakes omades einai 0-24, 25-65, 65-100
age["Young"] = fuzz.trimf(age.universe, [0, 0, 45])
age["Middle_Aged"] = fuzz.trimf(age.universe, [0, 45, 100])
age["Old"] = fuzz.trimf(age.universe, [45, 100, 100])
# ----------------------------------------------------------
# ligo kapnisma, os 5 tsigara, metrio 0-10, max 5, polu 5-20 max apo 10
cigarettes["few_cigarettes"] = fuzz.trimf(cigarettes.universe, [0, 0, 5])
cigarettes["normal_cigarettes"] = fuzz.trimf(cigarettes.universe, [0, 5, 10])
cigarettes["high_cigarettes"] = fuzz.trapmf(cigarettes.universe, [5, 10, 20, 20])
# ---------------------------------------------------------
# ligi askisi 0-2 fores tin evdomada, metria 3-5, max 5-7
exercise["exercise_low"] = fuzz.trimf(exercise.universe, [0, 0, 2])
exercise["exercise_md"] = fuzz.trimf(exercise.universe, [0, 3, 5])
exercise["exercise_high"] = fuzz.trapmf(exercise.universe, [3, 5, 7, 7])
# ---------------------------------------------------------
anxiety["anxiety_low"] = fuzz.trimf(anxiety.universe, [0, 0, 3])
anxiety["anxiety_md"] = fuzz.trimf(anxiety.universe, [0, 3, 6])
anxiety["anxiety_high"] = fuzz.trapmf(anxiety.universe, [3, 6, 10, 10])
# ---------------------------------------------------------
# troo ygeiina = os 1 fastfood den egine tipota, os 3, metrio 1-5, max 3, an8ygeiina 3-10 fores, max apo 5
eating_unhealthy["rarely"] = fuzz.trapmf(eating_unhealthy.universe, [0, 0, 1, 3])
eating_unhealthy["often"] = fuzz.trimf(eating_unhealthy.universe, [1, 3, 5])
eating_unhealthy["very_often"] = fuzz.trapmf(eating_unhealthy.universe, [3, 5, 10, 10])
# ----------------------------------------------------------
danger_status["no_danger"] = fuzz.trimf(danger_status.universe, [0, 0, 50])
danger_status["yellow_danger"] = fuzz.trimf(danger_status.universe, [00, 50, 100])
danger_status["red_danger"] = fuzz.trimf(danger_status.universe, [50, 100, 100])


# ------------------------------ VIEWS ------------------------------------------
# age.view()
# cigarettes.view()
# exercise.view()
# anxiety.view()
# eating_unhealthy.view()
# danger_status.view()
# plt.show()

rules = []

# for young and middle aged, everything low should have no danger
rules.append(ctrl.Rule((age["Young"] | age["Middle_Aged"]) & (cigarettes["few_cigarettes"] | exercise["exercise_high"] | anxiety["anxiety_low"] | eating_unhealthy["rarely"]), danger_status["no_danger"]))
# for middle danger
#young & mid age, one of each variations
rules.append(ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"] & exercise["exercise_high"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"] & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"] & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"] & exercise["exercise_high"] & anxiety["anxiety_low"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"] & exercise["exercise_high"] & anxiety["anxiety_low"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["few_cigarettes"] & exercise["exercise_high"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["few_cigarettes"] & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["few_cigarettes"] & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))

#young and mid age, two of each variations
#eating_unhealthy["often"] fixed
rules.append(ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["few_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["few_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))

#anxiety["anxiety_md"] fixed
rules.append(ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["few_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))

#exercise["exercise_md"] fixed
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"] & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))

#young and mid age, three of each variations
# eating_unhealthy["often"] and anxiety["anxiety_md"] fixed
rules.append(ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["few_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"]  & exercise["exercise_high"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))

#eating_unhealthy["often"] and exercise["exercise_md"] fixed
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_low"] & eating_unhealthy["often"], danger_status["yellow_danger"]))

#anxiety["anxiety_md"] and exercise["exercise_md"] fixed
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["rarely"], danger_status["yellow_danger"]))

#young and mid age, four of each variations
#eating_unhealthy["often"], anxiety["anxiety_md"], exercise["exercise_md"] fixed
rules.append(ctrl.Rule(age["Young"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))
rules.append(ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"]  & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_danger"]))


# for everything on high should have red danger
rules.append(ctrl.Rule((age["Old"] | age["Middle_Aged"]) & (cigarettes["high_cigarettes"] | exercise["exercise_low"] | anxiety["anxiety_high"] | eating_unhealthy["very_often"]), danger_status["red_danger"]))


# rule1.view()
danger_ctrl = ctrl.ControlSystem(rules)
danger = ctrl.ControlSystemSimulation(danger_ctrl)

# # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
danger.input["age"] = 80
danger.input["Cigarettes"] = 49
danger.input["Exercise"] = 1
danger.input["Anxiety"] = 8
danger.input["Eating unhealthy"] = 7
# # Crunch the numbers
danger.compute()
print("STATUS :", danger.output["Danger_status"])
danger_status.view(sim=danger)
plt.show()
test(danger, danger_status)