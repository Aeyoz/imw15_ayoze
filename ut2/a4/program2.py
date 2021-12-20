import random
nucleobases = "ATGC"

dna_length = 100

sequence = ''.join([random.choice(nucleobases) for i in range(dna_length)])

A = 0
T = 0
G = 0
C = 0

for i in sequence:
    if i == 'A':
        A = A + 1
    elif i == 'T':
        T = T + 1
    elif i == 'G':
        G = G + 1
    else:
        C = C + 1

print(f'Adenina: {A}')
print(f'Timina: {T}')
print(f'Guanina: {G}')
print(f'Citosina: {C}')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero