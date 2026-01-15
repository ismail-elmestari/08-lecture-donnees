#### Imports et définition des variables globales
"""
blablabla
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []

    with open(filename,mode='r',encoding='utf8') as f:
        for ligne in f :
            l2=[]
            for elem in ligne.strip().split(';'):
                l2.append(int(elem))
            l.append(l2)

    return l

def get_list_k(data, k):
    """
    blablabla
    """
    l = data[k]
    return l

def get_first(l):
    """
    blablabla
    """
    return l[0]

def get_last(l):
    """
    blablabla
    """
    return l[-1]

def get_max(l):
    """
    blablabla
    """
    return max(l)

def get_min(l):
    """
    blablabla
    """
    return min(l)

def get_sum(l):
    """
    blablabla
    """
    return sum(l)


#### Fonction principale


def main():
    """
    blablabla
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
