    $ unlock_prompt = True
    $ save_name = "У, фулюганы!\nНеча тут сохранятися!"
    scene cg_haikei with dissolve
    $ renpy.pause(0.2)
    if tips == "mainmenu_onik":
        call screen tips_onik
    elif tips == "mainmenu_wata":
        call screen tips_wata
    elif tips == "mainmenu_tata":
        call screen tips_tata
    elif tips == "mainmenu_hima":
        call screen tips_hima
    return
