"""manipulation de fichier"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
    # Supprimer le \n et transformer en entiers
    data = [[int(x) for x in line.strip().split(";")] for line in lines if line.strip()]
    return data

def get_list_k(data, k):
    """kieme element de l"""
    return data[k]

def get_first(l):
    """premier element de l"""
    return l[0]

def get_last(l):
    """dernier element de l"""
    return l[-1]

def get_max(l):
    """max element de l"""
    return max(l)

def get_min(l):
    """min element de l"""
    return min(l)

def get_sum(l):
    """somme elements de l"""
    return sum(l)


#### Fonction principale


def main():
    """fonction principale"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
