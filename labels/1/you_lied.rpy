    stop music
    play sound wa_022
    show rena se hi_a1 with fastdown
    a_r "Так ты не знаешь содержания Главы, значит{cps=*0.3}.........{/cps}{w=0.5}{nw}"
    $ renpy.pause(5.0)
    show rena se hii_a1 with fastdown
    play sound usoda
    a_r "{size=72}ВРУША!!!!!{/size}{w=0.2}{nw}"
    hide rena
    queue sound wa_015
    queue sound wa_005
    $ renpy.pause(1.0)
    scene ryuuketu with ryuuketu_efe
    queue sound wa_030
    $ renpy.pause(1.0)
    scene black with m1
    $ renpy.pause(2.0)
    $ renpy.full_restart()
