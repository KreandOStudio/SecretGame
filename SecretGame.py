#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret = 11

print "Bienvenidos a Secret Game!"

guess = int(raw_input("Introduzca el número a adivinar, ¿lo adivinarás? Tiene que ser del 0 al 20. ¡ADELANTE!: "))

if guess <= 20:
    if guess == secret:
        print "¡ACERTASTE! INCREIBLE!!"
    else:
        print "OOOOHHHH! PO VA SER QUE NO..."
else:
    print "¿Crees que son pocos numeros? No te preocupes, trabajaremos para poner mas, de momento es hasta 20. Lo siento."

