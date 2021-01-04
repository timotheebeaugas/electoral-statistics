import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygal

# data recovery
europeanElectionData = pd.read_csv("resultats-definitifs-par-departement.csv")
PresidentialElectionData = pd.read_csv("Presidentielle_2017_Resultats_Tour_1_c - Départements Tour 1.csv")

i = 1
abstentionDifferential = {}
abstentionDifferentialWithNames = {}

# create a loop to iterate over the array
while i < 97:
    departmentCode = PresidentialElectionData[i-1:i]['Code du département'].values[0]
    departmentName = PresidentialElectionData[i-1:i]['Libellé du département'].values[0]
    abstention2017 = float(PresidentialElectionData[i-1:i]['% Vot/Ins'].values[0].replace(",","."))
    abstention2019 = europeanElectionData[i-1:i]['% Vot/Ins'].values

    abstentionEuropeanElections = 0

    for value in abstention2019:
        abstentionEuropeanElections += float(value.replace(",","."))

    abstentionDifferential[departmentCode] = round(abstention2017 - abstentionEuropeanElections)
    abstentionDifferentialWithNames[departmentName] = round(abstention2017 - abstentionEuropeanElections)
    i += 1

# interactive map creation
fr_chart = pygal.maps.fr.Departments(human_readable=True)
fr_chart.title = 'Ecart entre la participation à l\'élection présidentielle de 2017 et à l\'élection européennes de 2019'
fr_chart.add('Différentiel en points',abstentionDifferential)
fr_chart.render_in_browser()

# ranking of the ten most demobilized departments
count = 0
top10Abstention = {}

# sorting values
for value1, value2 in sorted(abstentionDifferentialWithNames.items(), key=lambda x: x[1], reverse=True):
    top10Abstention[value1] = value2
    count += 1
    if count == 10:
        break

x = list(top10Abstention.keys())
y = list(top10Abstention.values())

# graphic creation
plt.scatter(x, y, c = 'red')
plt.xlabel("Départements")
plt.ylabel("Points d'écart")
plt.title('Classement des dix départements où l\'écart entre la participation à l\'élection présidentielle de 2017 et à l\'élection européennes de 2019 est le plus fort')
plt.show()