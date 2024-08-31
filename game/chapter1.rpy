label chap1:

    scene black with fade

    "..."
    define mys = Character("Mysterious Voice")
    mys "The power of the sword flows through you..."
    mc "What the... "
    mc "Who was that...? Where did that voice come from?"
    mys "RAISE YOUR SWORD!!!"
    "You feel a strange power course through your body..."
    "...and a sword appears in your hand!"


    jump battle_game_1

label chap1_1:

    scene white with blinds
    "*Shudders*"
    scene office with fade

    play music regular

    mc "Man, that was really scary."
    mc "Out of all the things in this world, why did I have to dream about that?"
    "Someone walks up to you..."

    show suzan

    s "Ermmmm hey there, [mc]~!"
    s "Hows it going??"
    mc "Erm... it's going-"
    s "Sooooo ermmmmmm yknow that skibbidy bar cafe that opened up nearby???~"
    s "Did you maybe wanna ermmm, go there together sometime??~"

    menu:
        "Sure?":
            jump chap1suzancafe

        "EWWWWWW! NO.":
            s "Boo hoo hoo hoy!"

    "Suzan runs off."
    mc "Heheheha!"

    jump chap2


label chap1suzancafe:
    s "Omg really??"

    s "W-wait I was joking anyways, ahaha!"

    s "Sorry BYE!"
    ##TODO add in story to get to cafe
    ##TODO make a cafe bg

    jump chap2