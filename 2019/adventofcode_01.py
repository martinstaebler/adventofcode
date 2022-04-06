import math

gesamtsprit = 0

def berechne_sprit(gewicht):
    modulsprit = math.floor(gewicht / 3) - 2
    zusatzsprit = modulsprit
    while zusatzsprit > 0:
        zusatzsprit = math.floor(zusatzsprit / 3) - 2
        if zusatzsprit > 0:
            modulsprit += zusatzsprit

    return modulsprit

with open('./modules.txt') as file:
    for line in file:
        gesamtsprit += berechne_sprit(int(line))

print(gesamtsprit)

