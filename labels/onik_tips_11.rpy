    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    scene bg 180 with Dissolve(1.0)
    play ambient lsys13
    centered "{space=24}(Газетной статьи не напечатано......){w=1.0}{nw}"
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_onik
    return
