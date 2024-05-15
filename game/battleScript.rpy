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
            text "gronk" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value gronk_hp
                    range gronk_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[gronk_hp] / [gronk_max_hp]" size 16

    text "Red Hood vs. gronk" xalign 0.5 yalign 0.05 size 30

# The game starts here.
label battle_game_1:
    #### Some variables that describes the game state.
    $ gronk_max_hp = 30
    $ mc_max_hp = 50
    $ gronk_hp = gronk_max_hp
    $ mc_hp = mc_max_hp
    $ health_potions = 13

    scene black

    "You feel power surge though your BALLS..."
    "and then..."
    "You RAISE YOUR SWORD!!!"

    jump battle_1_loop


label battle_1_loop:
    scene alley with fade
    #### Let's show the game screen.
    #
    show screen simple_stats_screen

    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    while (gronk_hp > 0) and (mc_hp > 0):

        menu:
            "Attack":
                $ gronk_hp -= 2
                mc "K-y-aaa!!!11 (damage dealt - 2hp)"

            "Restore Health ([health_potions] health potions left)" if health_potions > 0:
                $ mc_hp = min(mc_hp+5, mc_max_hp)
                $ health_potions -= 1
                mc "Mmm, tasty... (restore 5hp)"

            "Use lucky ultimate!":
                if renpy.random.randint(1, 4) > 3:
                    $ gronk_hp -= 10
                    g "Owie!!!"
                else:
                    g "haha u missed :p"

        $ gronk_damage = renpy.random.randint(1, 6)

        $ mc_hp -= gronk_damage

        g "RrrrrRRrrrr! {i}*gronk bites you*{/i} (damage dealt - [gronk_damage]hp)"
    #
    ####

    hide screen simple_stats_screen

    if gronk_hp <= 0:
        if mc_hp <= 0:
            "Double KO"

        else:
            mc "night-night gronky-poo"
            mc "erm, what the sigma"
            "([health_potions] health potions left)"

    else:
        g "Om-nom-nom-nom {i}*gronk ate you all up*{/i} (along with the basket, of course...)"

    jump battle_1_ending

label battle_1_ending:
    jump chap1_1
