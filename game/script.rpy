label splashscreen:
    scene black
    with Pause(1)


    show acceleratestudios with dissolve
    play sound splash
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return





# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    $ config.rollback_enabled = False

    jump beginning

    label nameMC:
            $ mc = renpy.input("Only one person can do this, and their name is:", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=15)
            if mc == "":
                "Try again."
                jump nameMC
            else:
                menu:
                        "Your name is, \"[mc]\", {w}correct?"

                        "Yes":
                            stop music fadeout 1.0
                            jump aftername

                        "Let me rethink this...":
                            jump nameMC
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
label credits:

    scene bg room

    "yeah this is credits i swear"

    "test Balls"


    return
