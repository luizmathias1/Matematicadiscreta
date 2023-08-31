def linhas(arquivo):
    with open(arquivo, 'r') as texto:
        lines = texto.readlines()
    return [line.strip() for line in lines]

def união(set1, set2):
    return set1.union(set2)

def interseção(set1, set2):
    return set1.intersection(set2)

def diferença(set1, set2):
    return set1.difference(set2)

def produto_cartesiano(set1, set2):
    return [(item1, item2) for item1 in set1 for item2 in set2]

arquivo = "Texto.txt"
lines = linhas(arquivo)

set2 = set(lines[1].split())
set3 = set(lines[2].split())
set5 = set(lines[4].split())
set6 = set(lines[5].split())
set8 = set(lines[7].split())
set9 = set(lines[8].split())
set11 = set(lines[10].split())
set12 = set(lines[11].split())

result_union = união(set2, set3)
result_intersection = interseção(set5, set6)
result_difference = diferença(set8, set9)
result_cartesian_product = produto_cartesiano(set11, set12)

print("União - conjunto 1: {", lines[1],"}, conjunto 2: {", lines[2],"}. Resultado:", result_union)
print("\nInterseção - conjunto 1: {", lines[4],"}, conjunto 2: {", lines[5],"}. Resultado:", result_intersection)
print("\nDiferença - conjunto 1: {", lines[7],"}, conjunto 2: {", lines[8],"}. Resultado:", result_difference)
print("\nProduto Cartesiano - conjunto 1: {", lines[10],"}, conjunto 2: {", lines[11],"}. Resultado:", result_cartesian_product)
