﻿# The script of the game goes in this file.
from repeatingtimer import RepeatingTimer
from threading import Timer
def img_up():
def img_down():
def cncl_down():
    down_tmr.cancel()
def cncl_up():
    up_tmr.cancel()
def bounce():
    down_tmr = RepeatingTimer(.01, img_down)
    up_tmr = RepeatingTimer(.01, img_up)
    down_cncl_tmr = Timer(.25, cncl_down)
    up_cncl_tmr = Timer(.25, cncl_down)
    down_tmr.start()
    up_tmr.start()
    down_cncl_tmr.start()
    up_cncl_tmr.start()
# Declare characters used by this game. The color argument colorizes the
# name of the character.
#invites
define mango = Character("Mango")
define amsa = Character("Amsa")
define wizz = Character("Wizzrobe")
define plup = Character("Plup")
define leff = Character("Leffen")
define axe = Character("Axe")
define hbox = Character("Hungrybox")

#commentators
define hugs = Character("Hugs")
define lovage = Character("Lovage")
define scar = Character("Scar")
define webs = Character("Webs")
define vish = Character("Vish")
define toph = Character("Toph")

#bruh

# The game starts here.

label start:
    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg fd:
        zoom 0.8

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show mango happy:
        xpos 10 ypos 160
        zoom 0.5
    mango "what's up"


    show mango angry at bounce:
        xpos 10 ypos 160
        zoom 0.5
    mango "ay woah"



    # These display lines of dialogue.

    hide mango

    show wizz sweat at bounce:
        xpos -50 ypos 160
        zoom 0.5
    wizz "ok"

    # This ends the game.

    return
