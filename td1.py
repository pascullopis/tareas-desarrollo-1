# -*- coding: utf-8 -*-

print ""
print ""
print "IMPRIMIR PARÁMETROS DE ENTRADA DE EJECUCIÓN"
print ""
print "se ejecuta así:   $ python exParametros.py parametro1 parametro2 parametro3"
print ""

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
