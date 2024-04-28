import matplotlib.pyplot as plt

x = list(range(0, 100))
y = x
# créer le plot
plt.plot(x, y)
# changer le style du graphique
plt.style.use("dark_background")
# metter une ligne horizontale rouge
# argument couleur, - pour des lignes, . pour mettre les points 
plt.hlines(60, 0, 50, color="red")
# mettre un titre
plt.title("mon titre")
# label axe x
plt.xlabel("x")
# label axe y
plt.ylabel("y")
# ajouter une légende pour les lignes
plt.legend(["Plot", "seuil du niveau pro"])
# ajouter une grille
plt.grid()
# changer l'organisation des titres etc
plt.tight_layout()
# ajouter une annotation
plt.annotate("mon texte", xy=(50, 60), xytext=(2))
# montrer le graphique
plt.show()
# sauver le graphique
# plt.savefig("plot.png", dpi=600)

#### autre méthode

# créer une grille de 2 lignes et 2 colonnes avec des graphiques
# fig = l'ensemble des graphiques
# axe[0, 0] = le premier graphique
# axe[0, 1] = le deuxième graphique
# etc
fig, ax = plt.subplots(2, 2)
plt.show()

#### autre méthode

plt.scatter(x, y)
plt.bar(x=[...], height=[...])
plt.pie([...], labels=[...])
plt.hist([...], bins=[...])
plt.boxplot([...], labels=[...])
plt.violinplot([...], labels=[...])
plt.errorbar([...], [...], yerr=[...], xerr=[...])
plt.stem([...], [...])
plt.polar([...], [...])
plt.contour([...], [...], [...])
plt.contourf([...], [...], [...])
plt.pcolormesh([...], [...], [...])
plt.matshow([...], [...])
plt.imshow([...], [...])
plt.specgram([...], [...])
