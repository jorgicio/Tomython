# Code that throws notifications for the Pomodoro Style.
# -*- coding:utf-8 -*-
import notify
import gtk
import os
import player



dir_actual = os.getcwd()    #Gets the current directory
sonido = os.path.join(dir_actual,"sounds/CLOCK1.mp3") #The Full path for the sound file

def pomodoro_inicio(tarea):
    mensaje = "Debe realizar la labor %s" % tarea
    mensaje2 = "Tiene 25 minutos"
    notify.create_icon(mensaje,mensaje2)
    gtk.main()

def pomodoro_termino(tarea):
    player.play(sonido)
    mensaje3 = "Ya pasaron 25 minutos"
    mensaje4 = "Ya debió terminar: %s" % tarea
    notify.create_icon(mensaje3,mensaje4)
    gtk.main()
