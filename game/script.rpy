# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("bottom", screen="say_bottom")
define t = Character("Top", screen="say_top")
define l= Character("left", screen="say_left")
define r = Character("right", screen="say_right")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image backgroundgif = Movie(size=(1920,1080),channel="movie_dp", play="images/well.webm")

    show backgroundgif
    show screen say_top("Top", "top speaker")
    show screen say_left("left", "left speaker")
    show screen say_right("right", "right speaker")
    show screen say_bottom("bottom", "bottom speaker")
    # These display lines of dialogue.

    b "check bottom"
    t "does this show in the top properly?"
    l "check left"
    r "check right"

    b "check bottom"
    t "does this show in the top properly?"
    l "check left"
    r "check right"



    # This ends the game.
    return
