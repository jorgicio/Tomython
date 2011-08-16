#!/usr/bin/python2
# -*- coding:utf-8 -*-

import notify
import gtk
import pygtk
import os
import player
import sys
import tomython
import countdown
import time

class SinParametro(Exception):
    def __str__(self):
        return "No se pasó ningún parámetro. El uso del programa es %s archivoentrada" % sys.argv[0]

class ExcesoDeParametros(Exception):
    def __str__(self):
        return "Demasiados parámetros. El uso del programa es %s archivoentrada" % sys.argv[0]

try:
    if len(sys.argv) < 2:
        raise SinParametro
    elif len(sys.argv) > 2:
        raise ExcesoDeParametros
    else:
        if not(os.path.exists(sys.argv[1])):
            raise IOError
        else:
            archivo = open(sys.argv[1],'r')
            counter = 0
            salida = open('%s_realizadas' % sys.argv[1],'a')
            salida.write("Labores realizadas a las %s el día %s:\n" % (time.strftime("%H:%M:%S"),time.strftime("%d-%m-%Y")))
            for linea in archivo.readlines():
                if not linea:
                    break
                
                if (counter % 4 == 0) and (counter != 0): # Cada 4 pomodoros, hacer una pausa larga, si no, se hace pausa corta
                    print "Haciendo pausa larga..."
                    countdown.countdown(1200) # Pausa larga de 20 minutos
                elif counter != 0:
                    print "Haciendo pausa corta..."
                    countdown.countdown(300) # Pausa corta de 5 minutos
                
                tomython.pomodoro_inicio(linea)
                countdown.countdown(1500) # 25 minutos para desarrollar actividades
                tomython.pomodoro_termino(linea)
                salida.write(linea+" [x]\n")
                counter = counter + 1
            archivo.close()
            salida.close()
            os.remove(sys.argv[1])
            archivo_vacio = open(sys.argv[1],'w')
            archivo_vacio.close()
except SinParametro, a:
    print a
except ExcesoDeParametros, b:
    print b
except IOError:
    print "El archivo %s no existe" % sys.argv[1]
finally:
    print "Me voooooooy xD"
