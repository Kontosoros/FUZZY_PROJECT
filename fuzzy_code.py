# https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html
# STO PARAKATW LINK EINAI TO IDIO PROVLIMA APLA PIO ANALITIKO ME KODIKO.
# STO PIO PANO LINK EINAI ME LIBRARIES PIO SIMPIKNOMENW
# https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html
# EPISIS STIN TELEFTEA GRAMI EVALA TO plt.show() ALLIOS DEN EMFANIZEI TIS GRAFIKES
import numpy as np

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# New Antecedent/Consequent objects hold universe variables and membership
# functions
age = ctrl.Antecedent(np.arange(0, 101, 1), "AGE")
cigarettes = ctrl.Antecedent(np.arange(0, 51, 1), "Cigarettes")
exercise = ctrl.Antecedent(np.arange(0, 8, 1), "Exercise")
anxiety = ctrl.Antecedent(np.arange(0, 11, 1), "Anxiety")
eating_unhealthy = ctrl.Antecedent(np.arange(0, 11, 1), "Eating unhealthy")
danger_status = ctrl.Consequent(np.arange(0, 101, 5), "Danger_status")

# Auto-membership function population is possible with .automf(3, 5, or 7)


age["Young"] = fuzz.trimf(age.universe, [0, 25, 45])
age["Middle_Aged"] = fuzz.trimf(age.universe, [30, 50, 70])
age["Old"] = fuzz.trimf(age.universe, [55, 80, 100])
# ----------------------------------------------------------
cigarettes["few_cigarettes"] = fuzz.trimf(cigarettes.universe, [0, 10, 20])
cigarettes["normal_cigarettes"] = fuzz.trimf(cigarettes.universe, [10, 25, 40])
cigarettes["high_cigarettes"] = fuzz.trapmf(cigarettes.universe, [25, 40, 50, 50])
# ---------------------------------------------------------
exercise["exercise_low"] = fuzz.trimf(exercise.universe, [0, 1, 3])
exercise["exercise_md"] = fuzz.trimf(exercise.universe, [2, 3, 4])
exercise["exercise_high"] = fuzz.trimf(exercise.universe, [3, 5, 7])
# ---------------------------------------------------------
anxiety["anxiety_low"] = fuzz.trimf(anxiety.universe, [0, 2, 4])
anxiety["anxiety_md"] = fuzz.trimf(anxiety.universe, [2, 5, 8])
anxiety["anxiety_high"] = fuzz.trimf(anxiety.universe, [6, 8, 10])
# ---------------------------------------------------------
eating_unhealthy["rarely"] = fuzz.trimf(eating_unhealthy.universe, [0, 2, 4])
eating_unhealthy["often"] = fuzz.trimf(eating_unhealthy.universe, [3, 5, 7])
eating_unhealthy["very_often"] = fuzz.trimf(eating_unhealthy.universe, [6, 8, 10])
# ----------------------------------------------------------
danger_status["no_danger"] = fuzz.trimf(danger_status.universe, [0, 20, 40])
danger_status["yellow_denger"] = fuzz.trimf(danger_status.universe, [40, 60, 80])
danger_status["red_danger"] = fuzz.trimf(danger_status.universe, [60, 80, 100])


# ------------------------------ VIEWS ------------------------------------------
# age.view()
# cigarettes.view()
# exercise.view()
# anxiety.view()
# eating_unhealthy.view()
# danger_status.view()
# plt.show()

rule1 = ctrl.Rule(age["Young"] & cigarettes["few_cigarettes"] & exercise["exercise_high"] & anxiety["anxiety_low"] & eating_unhealthy["rarely"], danger_status["no_danger"])
rule2 = ctrl.Rule(age["Middle_Aged"] & cigarettes["normal_cigarettes"] & exercise["exercise_md"] & anxiety["anxiety_md"] & eating_unhealthy["often"], danger_status["yellow_denger"])
rule3 = ctrl.Rule(age["Old"] & cigarettes["high_cigarettes"] & exercise["exercise_low"] & anxiety["anxiety_high"] & eating_unhealthy["very_often"], danger_status["red_danger"])

# rule1.view()
danger_ctrl = ctrl.ControlSystem([rule1,rule2,rule3])
danger = ctrl.ControlSystemSimulation(danger_ctrl)

# # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
danger.input["AGE"] = 80
danger.input["Cigarettes"] = 49
danger.input["Exercise"] = 1
danger.input["Anxiety"] = 8
danger.input["Eating unhealthy"] = 7
# # Crunch the numbers
danger.compute()
print("STATUS :", danger.output["Danger_status"])
danger_status.view(sim=danger)
plt.show()
