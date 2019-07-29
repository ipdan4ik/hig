    stop music
    play sound wa_024
    show mion ki hi_a1
    show mion se hi_a2 as real_mion
    with Dissolve(3.0)
    $ renpy.pause(2.0, hard=True)
    play sound wa_015
    $ renpy.pause(0.5)
    play sound wa_030
    scene ryuuketu with efe_aa
    $ renpy.pause(1.0)
    scene black with down_30
    $ renpy.pause(2.0)
    "Эх, дуралей...{w=2.0}{nw}"
    $ persistent.chapter = False
    $ persistent.chapter_onik = False
    $ persistent.chapter_wata = False
    $ persistent.chapter_tata = False
    $ persistent.chapter_hima = False
    "Никогда не говори, что знаешь цвет нижнего белья цундере, при ней. Никогда.{w=3.0}{nw}"
    $ renpy.full_restart()
