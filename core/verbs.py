from random import randint
from copy import copy
import csv

def download_verbs(path: str) -> list[list[str]]:
    file = open(path, "r")
    content = file.readlines()
    file.close()
    lista = [line.split(";") for line in content]
    lista.pop(0)
    return lista

def upload_verb(path: str, verb_string: str):
    file = open(path, 'r')
    content = file.readlines()
    file.close()
    
    header = content.pop(0)
    content.append(verb_string)
    content.sort()
    content.insert(0, header)
    file = open(path, 'w')
    file.write(''.join(content))
    file.close()

def consult_verb(path: str, verb: str) -> str:
    with open(path, 'r') as csvfile:
        for row in csvfile:
            if verb == row.split(";")[0]:
                return row
    return None



def get_verb(verbs_list: list[str]) -> str:
    """Función que recibe una lista de verbos y retorna un verbo aleatoriamente, así mismo este verbo es eliminado de la lista."""
    max_size = len(verbs_list) - 1
    return verbs_list.pop(randint(0, max_size))

if __name__ == "__main__":
    verbs = ["fly", "read", "eat", "sing", "listen", "break"]
    resultado = [get_verb(verbs) for verb in copy(verbs)] 
    print(*resultado, '\n')
