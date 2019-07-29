    $ save_name = "Пролог"
    $ mouse_visible = False
    scene black
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    $ renpy.pause(2.0)
    play music nageki_musicbox
    scene si_onikakusi with dissolve_02
    $ renpy.pause(20.0, hard=False)
    if persistent.matsuri:
        scene black with Dissolve(4.0)
        show text "{font=times.ttf}Вначале было лишь лёгкое беспокойство.{/font}" at truecenter with Dissolve(1.0)
        play sound oni001
        $ renpy.pause(2.0)
        hide text with Dissolve(1.0)
        show text "{font=times.ttf}Он и не думал причинять кому-либо зла.{/font}" at truecenter with Dissolve(1.0)
        play sound oni002
        $ renpy.pause(3.0)
        hide text with Dissolve(1.0)
        show text "{font=times.ttf}Но из беспокойства родилось одиночество,{/font}":
            xalign 0.5 yalign 0.45
        with Dissolve(1.0)
        play sound oni003
        $ renpy.pause(2.0)
        show text "{font=times.ttf}перешедшее затем в подозрение.{/font}" as text2:
            xalign 0.5 yalign 0.55
        with Dissolve(1.0)
        $ renpy.pause(2.0)
        hide text
        hide text2
        with Dissolve(1.0)
        show text "{font=times.ttf}Вскоре тёмные, кровожадные мысли поработили сердце.{/font}" at truecenter with Dissolve(1.0)
        $ renpy.pause(4.0)
        hide text with Dissolve(1.0)
        show text "{font=times.ttf}К прежней жизни уже не вернуться.{/font}":
            xalign 0.5 yalign 0.45
        with Dissolve(1.0)
        play sound oni004
        $ renpy.pause(1.0)
        show text "{font=times.ttf}Парень ступает всё дальше.{/font}" as text2:
            xalign 0.5 yalign 0.55
        with Dissolve(1.0)
        $ renpy.pause(2.0)
        hide text
        hide text2
        with Dissolve(1.0)
        show text "{font=times.ttf}Даже не замечая разверстого впереди колодца в ад.{/font}" at truecenter with Dissolve(1.0)
        play sound oni005
        $ renpy.pause(4.0)
    scene chapter 1 with Fade(3.0, 0.5, 1.0)
    play sound oni006
    $ renpy.pause(2.0)
    scene chapter onik_1 with Dissolve(2.0)
    $ renpy.pause(0.5)
    scene chapter onik_2 with Dissolve(2.0)
    play sound oni007
    $ renpy.pause(2.0)
    scene black with Dissolve(3.0)
    if persistent.matsuri:
        show text "{font=times.ttf}Трагедия, порождённая желанием верить.{/font}" at truecenter with Dissolve(1.0)
        play sound "sound/oni008.ogg"
        $ renpy.pause(2.0)
        hide text with Dissolve(1.0)
        show text "{font=times.ttf}Льющиеся слёзы — слёзы раскаяния, обиды ли?{/font}" at truecenter with Dissolve(1.0)
        play sound "sound/oni009.ogg"
        $ renpy.pause(5.0)
        hide text with Dissolve(2.0)
        $ renpy.pause(2.0)
    play sound wa_015
    $ renpy.pause(1.0)
    play sound wa_005
    scene tyuui_disclaimer with Dissolve(0.2)
    $ renpy.pause(0.5)
    scene black with Dissolve(4.0)
    play sound wa_015
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    play sound wa_005
    scene tyuui_s58 with Dissolve(0.2)
    scene black with Dissolve(4.0)
    play sound wa_015
    $ renpy.pause(1.0)
    play sound wa_005
    $ renpy.pause(0.35)
    scene black
    play sound wa_030
    $ renpy.pause(3.0)
    $ mouse_visible = True
    play ambient lsys11
    n "\n\n\n\nЕсли уж страданий не избежать...{nw}{w=2.0}"
    n "{nw}"
    n "То пусть лучше страдает тело.{nw}{w=4.0}"
    nvl clear
    n "\n\nЯ верил.{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Нет...{w=0.5} верю.{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Даже сейчас верю.{nw}{w=2.0}"
    nvl clear
    call dead_end
    n "\n\nНо уже начинаю осознавать.{nw}{w=2.0}"
    n "Я верю лишь потому, что не хочу признавать правду.{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Я пытаюсь себя убедить...{nw}{w=2.0}"
    n "Но как же дурацки звучит этот плачущий голос...{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Пропитывая лицо, из моих глаз вытекают слёзы...{nw}{w=2.0}"
    nvl clear
    n "\n\n\n\nМои однообразные движения прекратились, и в комнате стихло.{nw}{w=4.0}"
    nvl clear
    scene bg 204 with center
    n "\n\n\nВсё, что я слышу, — отвратительно громкий плач вечерних цикад...{nw}{w=2.0}"
    n "{nw}"
    n "Кажется...{nw}{w=1.5}"
    n "Я всё ещё слышу её...{nw}{w=2.0}"
    n "{nw}"
    n "...Да нет, не может быть такого.{nw}{w=2.0}"
    n "Она уж ничего не произносит.{nw}{w=4.0}"
    nvl clear
    n "\n\n\n\nРыдал один я.{nw}{w=2.0}"
    n "{nw}"
    n "Она же не проронила и слезинки.{nw}{w=4.0}"
    nvl clear
    n "\nКогда она повторяла одно и то же, её лицо не выражало ничего, никаких эмоций.{nw}{w=2.0}"
    n "Раз у неё нет слёз для меня...{nw}{w=1.0}"
    extend " тогда и с моей стороны их не будет.{nw}{w=2.0}"
    n "{nw}"
    n "Не стоит по ним плакать.{nw}{w=4.0}"
    nvl clear
    n "{nw}"
    n "\nНо... почему сердцу так больно, а в глазах стоят слёзы?....{nw}{w=2.0}"
    n "{nw}"
    n "Потому что... я хочу верить, что до сих пор\nне со всем порвал.{nw}{w=4.0}"
    nvl clear
    n "\n\n\nМожет быть, хватит?{nw}{w=2.0}"
    n "{nw}"
    n "Внутри моего сердца прозвучал мягкий голос...{nw}{w=4.0}"
    nvl clear
    n "\n\n\nТы достаточно настрадался.{nw}{w=2.0}"
    n "{nw}"
    n "Снова и снова мне хотелось избавиться от своего саднящего сердца.{nw}{w=2.0}"
    n "{nw}"
    n "И всё-таки... я упрямо не хотел от него отказываться.{nw}{w=4.0}"
    nvl clear
    n "\nБез этих страданий было бы много легче...{nw}{w=2.0}"
    n "{nw}"
    n "Даже зная это, разве не выбрал я верить?{nw}{w=2.0}"
    n "Только я знаю, насколько такое трудно, и только меня можно за это вознаградить.{nw}{w=4.0}"
    nvl clear
    n "\n\nЭй, «я».{nw}{w=2.0}"
    n "Ты сделал всё, что смог.{nw}{w=2.0}"
    n "Я знаю...{nw}{w=2.0}"
    n "{nw}"
    n "Так, может...{nw}{w=2.0}"
    n "Не хватит ли себя истязать?..{nw}{w=4.0}"
    nvl clear
    n "\n\n\n\nК тому же...... я не выбрасываю свою боль.{nw}{w=2.0}"
    n "Я оставлю её тут, с нею.{nw}{w=2.0}"
    n "{nw}"
    n "Как возлагают цветы...{nw}{w=4.0}"
    nvl clear
    n "\n\nИтак...{nw}{w=2.0}"
    n "Успокойся...{nw}{w=2.0}"
    n "{nw}"
    n "Правая рука налилась свинцом...{nw}{w=2.0}"
    n "Но подними её ещё раз.{nw}{w=2.0}"
    n "{nw}"
    n "С каждым взмахом я забываю.{nw}{w=4.0}"
    nvl clear
    call dead_end
    n "\n\nКак радовался твоей доброте.{nw}{w=2.0}"
    n "{nw}"
    call dead_end
    n "Как наслаждался твоей милой улыбкой.{nw}{w=2.0}"
    n "{nw}"
    call dead_end
    n "Я любил гладить тебя по голове.{nw}{w=2.0}"
    n "{nw}"
    call dead_end
    n "Любил эту твою застенчивость.{nw}{w=2.0}"
    call dead_end
    $ renpy.pause(0.3)
    queue sound wa_030
    nvl clear
    n "{nw}"
    n "Это последний взмах.{nw}{w=2.0}"
    n "{nw}"
    n "После него я всё забуду.{nw}{w=2.0}"
    n "{nw}"
    n "Это для тебя...{nw}{w=2.0}"
    n "{nw}"
    n "Мой первый и последний......{nw}{w=1.0}"
    extend " букет цветов.{nw}{w=4.0}"
    nvl clear
    $ renpy.pause(2.0)
    scene black with Dissolve(3.0)
    n "\n\n\nНе знаю точно...{nw}{w=1.0}"
    extend " Но, кажется...{nw}{w=2.0}"
    n "{nw}"
    n "{nw}"
    play sound wa_015
    n "{cps=*0.4}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{/cps}{nw}{w=1.0}"
    extend "я любил тебя.{nw}{w=3.0}"
    nvl clear
    play sound wa_005
    scene aka1
    show title at truecenter
    with Dissolve(0.01)
    $ renpy.pause(3.0)
    show black behind title with Dissolve(3.0)
    $ renpy.pause(2.0)
    scene black with Dissolve(2.0)
    jump onik_day0
