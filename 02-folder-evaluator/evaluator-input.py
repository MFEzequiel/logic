# -*- coding: utf-8 -*-

rc = float(input('Número de respuestas correctas'))
ri = float(input('Número de respuestas incorrectas'))
rb = float(input('Número de respuestas en Blanco'))

prc = rc * 3
pri = ri * -1
prb = rb * 0

pf = prc + pri + prb

print(prc)
print(pri)
print(prb)