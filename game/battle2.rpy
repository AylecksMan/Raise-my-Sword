define m = Character("You")

screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text mc size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value mc_hp
                    range mc_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[mc_hp] / [mc_max_hp]" size 16


    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "unknown" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value unknown_hp
                    range unknown_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[unknown_hp] / [unknown_max_hp]" size 16

    text "You vs. unknown" xalign 0.5 yalign 0.05 size 30

label battle_game_2:
    $ unknown_max_hp = 50
    $ mc_max_hp = 75
    $ unknown_hp = unknown_max_hp
    $ mc_hp = mc_max_hp
    $ health_potions = 13

    scene black with fade

    mc "..."
    mc "I guess it's that time again."

    jump battle_2_loop

label battle_2_loop:

    scene black with squares

    #show monster

    show screen simple_stats_screen
    while (unknown_hp > 0) and (mc_hp > 0):

        menu:
            "Attack":
                $ unknown_hp -= 2
                mc "K-y-aaa!!!11 (damage dealt - 2hp)"

            "Restore Health ([health_potions] health potions left)" if health_potions > 0:
                $ mc_hp = min(mc_hp+5, mc_max_hp)
                $ health_potions -= 1
                mc "Mmm, tasty... (restore 5hp)"

            "Use lucky ultimate!":
                if renpy.random.randint(1, 4) > 3:
                    $ unknown_hp -= 15
                    "You damage the unknown creature."
                else:
                    "You miss your ultimate."

        $ unknown_damage = renpy.random.randint(1, 5)

        $ mc_hp -= unknown_damage

        "{i}*unknown slashes you*{/i} (damage dealt - [unknown_damage]hp)"
    #
    ####

    hide screen simple_stats_screen

    if unknown_hp <= 0:
        if mc_hp <= 0:
            "Double KO"
            "Recommencing battle..."
            jump battle_game_2

        else:

            "([health_potions] health potions left)"

    else:
        "{i}*The unknown creatures wins.*{/i}"
        "Recommencing battle..."
        jump battle_game_2


    jump credits

