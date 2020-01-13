# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#invites
define mango = Character("Mango")
define amsa = Character("Amsa")
define wizz = Character("Wizzrobe")
define plup = Character("Plup")
define leffen = Character("Leffen")
define axe = Character("Axe")
define hbox = Character("Hungrybox")

#commentators
define hugs = Character("Hugs")
define lovage = Character("Lovage")
define scar = Character("Scar")
define webs = Character("Webs")
define vish = Character("Vish")
define toph = Character("Toph")
define m = Character("Mango")


# The game starts here.

label start:

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

    # These display lines of dialogue.

    m "suh dude"

    m "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
