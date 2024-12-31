import numpy
import time


# Initialisation de la frame (matrice) avec des 0 et des 1
# 0 pour une cellule morte et 1 pour une cellule vivante
frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])


# Cette fonction prend en entrée la matrice avec bordure et renvoie le nombre de cellules voisines vivantes.
def compute_number_neighbors(paded_frame, index_line, index_column):

    number_neighbors = 0
    if index_line != 0:
        if index_column != 0:
            if paded_frame[index_line - 1][index_column - 1] > 0: number_neighbors += 1
        if paded_frame[index_line - 1][index_column + 0] > 0: number_neighbors += 1
        if index_column != (len(paded_frame[0]) - 1):
            if paded_frame[index_line - 1][index_column + 1] > 0: number_neighbors += 1

    if index_column != 0:
        if paded_frame[index_line + 0][index_column - 1] > 0: number_neighbors += 1
    if index_column != (len(paded_frame[0]) - 1):
        if paded_frame[index_line + 0][index_column + 1] > 0: number_neighbors += 1

    if index_line != len(paded_frame) - 1:
        if index_column != 0:
            if paded_frame[index_line + 1][index_column - 1] > 0: number_neighbors += 1
        if paded_frame[index_line + 1][index_column + 0] > 0: number_neighbors += 1
        if index_column != (len(paded_frame[0]) - 1):
            if paded_frame[index_line + 1][index_column + 1] > 0: number_neighbors += 1

    return number_neighbors

# Cette fonction prend en entrée une frame et calcule la frame suivante
# à partir des règles du jeu de la vie
def compute_next_frame(frame):

    next_frame = numpy.zeros(frame.shape)  
    # zero padding
    paded_frame = numpy.pad(frame, ((1, 1), (1, 1)), mode="constant")  

    for i in range(1, paded_frame.shape[0] - 1):
        for j in range(1, paded_frame.shape[1] - 1):
            number_neighbors = compute_number_neighbors(paded_frame, i, j)
            if paded_frame[i][j] == 1:
                if number_neighbors < 2 or number_neighbors > 3:
                    next_frame[i - 1][j - 1] = 0
                else:
                    next_frame[i - 1][j - 1] = 1
            else:
                if number_neighbors == 3:
                    next_frame[i - 1][j - 1] = 1

    return next_frame

# Fonction pour compter le nombre de cellules vivantes
def count_alive_cells(frame):
    return numpy.sum(frame)

# Fonction pour mesurer la complexité (par exemple, le nombre de changements entre deux frames)
def measure_complexity(frame, next_frame):
    return numpy.sum(frame != next_frame)

# Exemple d'utilisation des outils d'analyse
while True:
    print("frame:")
    print(frame)
    alive_cells = count_alive_cells(frame)
    print(f"Number of living cells: {alive_cells}")
    
    next_frame = compute_next_frame(frame)
    complexity = measure_complexity(frame, next_frame)
    print(f"number of changes: {complexity}")
    
    frame = next_frame
    time.sleep(0.5)

# Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
# On fait appelle à la fonction (compute_number_neighbors)

# Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
# si il y a des modifications à faire.
# Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice utilisé ! )

# Étape 4 : Affichez la frame actuelle et passez à la suivante (frame suivante = frame calculée à l'étape 3)

# Étape 5 : Répétez les étapes 2 à 4 à l'infini (boucle infinie)

# Étape 6 : Arrêtez le script en appuyant sur ctrl + c


