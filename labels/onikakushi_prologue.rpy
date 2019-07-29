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
    n "Если уж страданий не избежать..."
    n ""
    n "То пусть лучше страдает тело."
    nvl clear
    n "Я верил."
    call dead_end
    n ""
    n "Нет... верю."
    call dead_end
    n ""
    n "Даже сейчас верю."
    nvl clear
    call dead_end
    n "Но уже начинаю осознавать."
    n "Я верю лишь потому, что не хочу признавать правду."
    call dead_end
    n ""
    n "Я пытаюсь себя убедить..."
    n "Но как же дурацки звучит этот плачущий голос..."
    call dead_end
    n ""
    n "Пропитывая лицо, из моих глаз вытекают слёзы..."
    nvl clear
    n "Мои однообразные движения прекратились, и в комнате стихло."
    nvl clear
    scene bg 204 with center
    n "Всё, что я слышу, — отвратительно громкий плач вечерних цикад..."
    n ""
    n "Кажется..."
    n "Я всё ещё слышу её..."
    n ""
    n "...Да нет, не может быть такого."
    n "Она уж ничего не произносит."
    nvl clear
    n "Рыдал один я."
    n ""
    n "Она же не проронила и слезинки."
    nvl clear
    n "Когда она повторяла одно и то же, её лицо не выражало ничего, никаких эмоций."
    n "Раз у неё нет слёз для меня..."
    extend " тогда и с моей стороны их не будет."
    n ""
    n "Не стоит по ним плакать."
    nvl clear
    n ""
    n "Но... почему сердцу так больно, а в глазах стоят слёзы?...."
    n ""
    n "Потому что... я хочу верить, что до сих пор не со всем порвал."
    nvl clear
    n "Может быть, хватит?"
    n ""
    n "Внутри моего сердца прозвучал мягкий голос..."
    nvl clear
    n "Ты достаточно настрадался."
    n ""
    n "Снова и снова мне хотелось избавиться от своего саднящего сердца."
    n ""
    n "И всё-таки... я упрямо не хотел от него отказываться."
    nvl clear
    n "Без этих страданий было бы много легче..."
    n ""
    n "Даже зная это, разве не выбрал я верить?"
    n "Только я знаю, насколько такое трудно, и только меня можно за это вознаградить."
    nvl clear
    n "Эй, «я»."
    n "Ты сделал всё, что смог."
    n "Я знаю..."
    n ""
    n "Так, может..."
    n "Не хватит ли себя истязать?.."
    nvl clear
    n "К тому же...... я не выбрасываю свою боль."
    n "Я оставлю её тут, с нею."
    n ""
    n "Как возлагают цветы..."
    nvl clear
    n "Итак..."
    n "Успокойся..."
    n ""
    n "Правая рука налилась свинцом..."
    n "Но подними её ещё раз."
    n ""
    n "С каждым взмахом я забываю."
    nvl clear
    call dead_end
    n "Как радовался твоей доброте."
    n ""
    call dead_end
    n "Как наслаждался твоей милой улыбкой."
    n ""
    call dead_end
    n "Я любил гладить тебя по голове."
    n ""
    call dead_end
    n "Любил эту твою застенчивость."
    call dead_end
    $ renpy.pause(0.3)
    queue sound wa_030
    nvl clear
    n ""
    n "Это последний взмах."
    n ""
    n "После него я всё забуду."
    n ""
    n "Это для тебя..."
    n ""
    n "Мой первый и последний......"
    extend " букет цветов."
    nvl clear
    $ renpy.pause(2.0)
    scene black with Dissolve(3.0)
    n "Не знаю точно..."
    extend " Но, кажется..."
    n ""
    n ""
    play sound wa_015
    n ""
    extend "я любил тебя."
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
