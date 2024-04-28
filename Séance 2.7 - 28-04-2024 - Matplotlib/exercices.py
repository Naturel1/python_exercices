import matplotlib.pyplot as plt


import numpy as np


# ex 1
def equidistant_values(begin: int, end: int, n: int) -> list[int]:
    step = (end - begin) / (n - 1)
    return list(map(lambda x: begin + x * step, range(n)))


# ex 2
def draw_plot(func):
    x = equidistant_values(0, 10, 10000)
    y = list(map(func, x))
    plt.plot(x, y)


# ex 3
def draw_plots(func):
    x = equidistant_values(0, 10, 10000)
    y = list(map(func, x))
    plt.plot(x, y, label="sin(x)")
    y = list(map(lambda i: 2 * func(i), x))
    plt.plot(x, y, label="2 * sin(x)")
    y = list(map(lambda i: func(2 * i), x))
    plt.plot(x, y, label="sin(2x)")
    y = list(map(lambda i: func(i ** 2), x))
    plt.plot(x, y, label="sin(x²)")
    plt.legend()


# ex 4
# ex 5
# ex 6
languages = {"Java": 22.2, "Python": 17.6, "C++": 6.7, "C#": 7.7, "JavaScript": 8, "PHP": 8.8}


def language_plot(data: dict[str, int]) -> None:
    # /i\ pycharm n'affiche pas les valeur en string sur le graphique
    keys = list(data.keys())
    values = list(data.values())
    positions = range(len(keys))
    plt.bar(x=positions, height=values, tick_label=keys)
    plt.xlabel('Langage de programmation')
    plt.ylabel('Popularité')
    plt.title('Popularité des langages de programmation')
    plt.xticks(rotation=45)
    # plt.savefig("plot.png", dpi=600)


# ex 7
def language_pie_chart(data: dict[str, int]) -> None:
    labels = list(data.keys())
    sizes = list(data.values())

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Popularité des langages de programmation')


# ex 8
def scatter_plot_random_data(num_points):
    x = np.random.normal(loc=0, scale=1, size=num_points)
    y = np.random.normal(loc=0, scale=1, size=num_points)

    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Nuage de points aléatoire')


# ex 9
random_data = np.random.normal(loc=0, scale=1, size=1000)


def create_histogram(data, bins=10, density=False, alpha=1.0):
    plt.hist(data, bins=bins, density=density, alpha=alpha)
    plt.xlabel('Valeurs')
    plt.ylabel('Fréquence')
    plt.title('Histogramme des données')
    plt.grid(True)


# ex 10
def polar_plot():
    theta = np.linspace(0, 2 * np.pi, 100)
    r1 = 1 + 0.5 * np.sin(6 * theta)
    r2 = 1 + 0.5 * np.cos(6 * theta)

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})
    ax1.plot(theta, r1, label='r = 1 + 0.5 * sin(6*θ)')
    ax2.plot(theta, r2, label='r = 1 + 0.5 * cos(6*θ)')
    for ax in [ax1, ax2]:
        ax.set_rticks([1, 2, 3, 4])
        ax.legend()
    ax1.set_title('Graphe Polaire 1')
    ax2.set_title('Graphe Polaire 2')

    plt.savefig("plot.png", dpi=600)


def inter_plot():
    # Générer des données
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x ** 2 + y ** 2))

    # Créer une figure 3D interactive
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(x, y, z, cmap='viridis')

    # Tracer la surface en 3D
    # ax.plot_surface(x, y, z, cmap='viridis')

    # Ajouter des étiquettes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Ajouter des outils de navigation interactive
    ax.view_init(elev=20, azim=45)  # Position initiale de la vue
    fig.colorbar(surf)  # Ajouter une barre de couleur pour indiquer la valeur de z


if __name__ == "__main__":
    inter_plot()
    plt.show()
