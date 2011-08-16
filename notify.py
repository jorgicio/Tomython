# Code made originally for the notifications using pynotify
# Thanks to http://ubuntuforums.org/showthread.php?t=887173
# I modified the code for using a custom icon

import gtk
import gobject
import pynotify
import os

icon=None
notify=None

dir_actual = os.getcwd()
dir_img = os.path.join(dir_actual,"img/pomodoroicon.png")


def create_icon(title, text=""):
    global icon
    pynotify.init("pymodoro")
    icon=gtk.status_icon_new_from_file(dir_img)
    icon.set_visible(False)
    icon.connect('activate', quit)
    icon.set_tooltip("%s\n(%s)" % (title,text))
    icon.set_visible(True)
    ui_idle()
    gobject.timeout_add (1,show_notification,(title,text,icon))

def show_notification(data):
    global notify
    (title, text, icon) = data
    notify = pynotify.Notification(title,text,dir_img)
    notify.set_urgency(pynotify.URGENCY_NORMAL)
    notify.set_timeout(5000)
    notify.show()

def ui_idle():
    while gtk.events_pending():
        gtk.main_iteration(False)

def quit(data):
    gtk.main_quit()
    notify.close()
