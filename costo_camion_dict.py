import csv
import sys

def costo_camion(path):
    data = open(path, 'rt')
    rows = csv.DictReader(data)

    costo_total = 0.0
    for row in rows:
        try:
            costo_total += int(row['cajones']) * float(row['precio'])
        except ValueError:
            print('Warning')

    return costo_total

print(sys.argv[0])
print(sys.argv[1])

costo_total = costo_camion(sys.argv[1])
print('El costo total es: ', costo_total)
