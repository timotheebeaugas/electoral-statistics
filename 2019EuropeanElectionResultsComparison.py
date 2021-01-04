import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data import
data = pd.read_csv("resultats-definitifs-par-departement.csv")

# Department selection
departement = "75"

# Data preparation
departementName = str(data[data['Code du département']==departement]['Libellé du département'].values.ravel()).replace("[","").replace("]","").replace("'","")
formattedData = data[data['Code du département']==departement][['% Abs/Ins','Unnamed: 176','Unnamed: 50','Unnamed: 225','Unnamed: 218','% Voix/Exp','Unnamed: 99']].values.ravel().tolist()
nationalAverage = ['49,88', '23,34', '22,42', '13,48', '8,48', '6,31', '6,19']
y2 = []
y1 = []
x = ["Abstentions", "RN", "LREM", "EELV", "LR", "LFI", "PS"]

# Number typing and deleting commas
for sa,ss in zip(formattedData,nationalAverage):
    y2.append(float(sa.replace(",",".")))
    y1.append(float(ss.replace(",",".")))

# Formatting chart bars
w = 0.25
bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]

# Graphic creation
plt.bar(bar1, y1, 0.25, color=["lightgrey","mediumslateblue","moccasin","mediumspringgreen","cornflowerblue","salmon","pink"], label="Résultat national")
plt.bar(bar2, y2, 0.25, color=["grey","darkblue","orange","limegreen","royalblue","red","deeppink"], label="Résultat départemental")
plt.xlabel("Abstentions et partis politiques")
plt.ylabel("Résultats (%)")
plt.xticks(bar1+w/2,x)
plt.title("Elections européennes 2019 : Résultats nationaux et départementaux ("+departementName+")")
plt.legend()
plt.grid(False)
plt.show()
