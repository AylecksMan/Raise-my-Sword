define m = Character("You")

screen simple_stats_screen_3:
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
            text "boss" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value boss_hp
                    range boss_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[boss_hp] / [boss_max_hp]" size 16

    text "You vs. boss" xalign 0.5 yalign 0.05 size 30

label battle_game_3:
    $ boss_max_hp = 100
    $ mc_max_hp = 75
    $ boss_hp = boss_max_hp
    $ mc_hp = mc_max_hp
    $ health_potions = 13

    scene black with fade

    jump battle_3_loop

label battle_3_loop:

    play music boss

    scene airman with squares

    mc "IT WAS AIRMAN ALL ALONG?"

    am "MWEHEHEHE YEAS IT WAS I, AIRMAN"

    am "And as the saying goes, {w}YOU CAN'T DEFEAT AIRMAN!"

    #show monster

    show screen simple_stats_screen_3
    while (boss_hp > 0) and (mc_hp > 0):

        menu:
            "Attack":
                $ boss_hp -= 4
                mc "K-y-aaa!!!11 (damage dealt - 2hp)"

            "Restore Health ([health_potions] health potions left)" if health_potions > 0:
                $ mc_hp = min(mc_hp+6, mc_max_hp)
                $ health_potions -= 1
                mc "Mmm, tasty... (restore 5hp)"

            "Use lucky ultimate!":
                if renpy.random.randint(1, 4) > 3:
                    $ boss_hp -= 20
                    "You damage the boss."
                else:
                    "You miss your ultimate."
            "Flip a coin (Heads = win; tails = lose)":
                if (renpy.random.randint(1, 2)) > 1:
                    "Tails!"
                    $ mc_hp -= 1000000
                    "You lose..."
                    "Recommencing battle."
                    jump battle_game_3
                else:
                    "Heads!"
                    $ boss_hp -= 1000000
                    "You win!"
                    jump credits

        $ boss_damage = renpy.random.randint(1, 5)

        $ mc_hp -= boss_damage

        "{i}*The boss slaps you*{/i} (damage dealt - [boss_damage]hp)"
    #
    ####

    hide screen simple_stats_screen_3

    if boss_hp <= 0:
        if mc_hp <= 0:
            "Double KO"
            "Recommencing battle..."
            jump battle_game_3

        else:

            "([health_potions] health potions left)"

    else:
        "{i}*The boss creatures wins.*{/i}"
        "Recommencing battle..."
        jump battle_game_3




    jump credits
