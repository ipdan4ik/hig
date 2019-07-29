    scene ryuuketu with ryuuketu_efe
    queue sound wa_030
    $ renpy.pause(1.0)
    scene black with m1
    $ renpy.pause(2.0)
    "Тебя съела Сатоко.{w=1.0}{nw}"
    $ persistent.chapter = False
    $ persistent.chapter_onik = False
    $ persistent.chapter_wata = False
    $ persistent.chapter_tata = False
    $ persistent.chapter_hima = False
    "Воистину, печальный конец.{w=1.0}{nw}"
    $ renpy.full_restart()
