# Created by: Saad Shabir
# Created on: Aug 2017
# Created for: IC3U
# Daily Assignment - Unit 0-03
# This program displays Hello World through a click of a button

import ui

def hello_world_touch_up_inside(sender):
    #print ('Hello, World!')
    view['hello_world_label'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')


