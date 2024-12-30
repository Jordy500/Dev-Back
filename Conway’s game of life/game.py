import numpy

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

"""
 Cette fonction prend en entrée la matrice avec bordure et
 renvoie le nombre de cellules voisines vivantes.
"""

def compute_number_neighbors(paded_frame, index_line, index_column):

    number_neighbors = 0
    for i in range(index_line - 1, index_line + 2):
        for j in range(index_column - 1, index_column + 2):
            if i == index_line and j == index_column:
                continue
            number_neighbors += paded_frame[i][j]

    return number_neighbors
    
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
    """
def compute_next_frame(frame):
    
        next_frame = numpy.zeros(frame.shape)  # initialisation de la frame suivante

        paded_frame = numpy.pad(frame, 1, mode="constant")  # zero padding

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

# Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) element par element.
# Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)
                                                      

    # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)

    # L'étape 2 et 3 se font au cours de la même itération (attention à l'indentation !)

        for i in range(1, paded_frame.shape[0] - 1):
            for j in range(1, paded_frame.shape[1] - 1):
                 number_neighbors = compute_number_neighbors(paded_frame, i, j)
                 if paded_frame[i][j] == 1:
                     if number_neighbors < 2 or number_neighbors > 3:
                         frame[i - 1][j - 1] = 0
            else:
                         frame[i - 1][j - 1] = 1
        else:
            if number_neighbors == 3:
                         frame[i - 1][j - 1] = 1
   
    # Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
    # On fait appelle à la fonction (compute_number_neighbors)


    # Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
    # si il y a des modifications à faire.
    # Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice utilisé ! )
