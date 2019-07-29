    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play ambient lsys12
    n "\"Зуб даю,"
    extend " в здешних горах Сатоко спокойно даст бой хоть целой пехотной дивизии.\""
    n "\"Знаю,"
    extend " она как-то приезжала в одну страну обучать партизан ставить ловушки в составе группы советских военных инструкторов.\""
    n "\"Хватит говорить о глупостяяях... Лучше помогиииитеееее!!\""
    nvl clear
    stop ambient fadeout 1.0
    scene bg 205 with dissolve_04
    play music msys02
    n "И как же...... нас так угораздило..."
    nvl clear
    n "Мион провалилась в узкую ямку, и над землёй торчала одна её голова."
    n "{nw}"
    n "На голову Рэны плотно нахлобучено лужёное ведёрко, и снять его у ней никак не получается."
    n "{nw}"
    n "...Да, видок у обеих смешной донельзя,"
    extend " но они хотя бы чуют ногами землю."
    nvl clear
    scene bg 142 with left_03
    play ambient lsys12
    n "\"......И как та-ам, наверху-у, а, Кей-тян?"
    extend " Спуститься могё-ёшь?"
    extend " Давай спускайся, вытаскивай Дядьку-у скоре-е.\""
    n "\"Это ты давай вылезай и снимай меня!"
    extend " Как я, чёрт побери, слезу, закутанный в бамбуковую циновку?!\""
    nvl clear
    n "...Я, вместе с конечностями стянут бамбуковою циновкой, вишу на высоте где-то двух метров от земли."
    n "{nw}"
    n "Рррр... Ну и что это за ловушка?"
    extend " А-а?!"
    extend " Сатоко!"
    nvl clear
    scene black with Dissolve(1.0)
    n "Началось всё с того, что меня, городского мальчика, решили поближе познакомить с природой и предложили сходить погулять в горах."
    nvl clear
    stop ambient fadeout 1.0
    scene bg 108 with fastup
    show rena se def_a1 at sprava with right_03
    n "\"М-м-м, Рэна тоже не очень хорошо знает горы вокруг деревни."
    show rena se hau_b1 with dissolve_02
    extend " Рэна может потеряться."
    extend " Хау.\""
    show mion se to_a1 at sleva with left_03
    n "\"Горы вокруг деревни, говоришь..."
    extend " Я как-то лазала там, когда была маленькой... но с тех пор столько лет прошло."
    extend " Примешь не туда, в два счёта заблудишься.\""
    nvl clear
    scene bg 109 with left_03
    show satoko se wa_a1 at sleva with left_03
    n "\"Если желаете гор, то можете на нас положиться!"
    extend " Как-никак они все — наша с Рикой игровая площадка."
    extend " Да-а, Рика-а?\""
    show rika se wa_a1 at sprava with right_03
    n "\"......Ми-и!\""
    nvl clear
    n "\"Ого,"
    extend " звучит обнадёживающе."
    extend " Ну что ж, почему бы и не походить по горам под вашим чутким руководством!\""
    hide satoko with right_03
    show rena se ko_a1 at sleva with left_03
    n "\"Но, Кейти-кун..."
    extend " В школьной памятке по проведению летних каникул написано, что не надо туда ходить, там легко потеряться.\""
    show rika se ni_a1 with dissolve_02
    n "\"......Ничего-ничего, летние каникулы ещё не наступили же."
    extend " А тропки мы знаем, так что не беспокойтесь.\""
    nvl clear
    show satoko se wa_b1 at central with dissolve_04
    n "\"Мы уже давно там играем!"
    extend " Они нам как собственный дворик!"
    extend " Нам там знакомы все тропинки да обходные пути!\""
    nvl clear
    scene black with Dissolve(1.0)
    n "......И действительно, там они всё знали как свои пять пальцев."
    n "Благодаря им я в полной мере мог насладиться природой, отличным видом, которых не найдёшь в самой деревне, и, помимо того, свежайшим воздухом."
    n "{nw}"
    n "Но потом начались всякие странности!!"
    nvl clear
    stop music fadeout 1.0
    scene bg 143
    show satoko si aku_a1 at sprava
    with dissolve_04
    play ambient lsys12
    n "\"Так,"
    extend " уважаемые."
    extend " Дальше прошу идти след в след за мной.\""
    n "\"Э-э?.."
    extend " Чего это ты вдруг?\""
    show rika si ni_a1 at sleva with left_03
    n "\"......Послушаться Сатоко будет намного умнее и полезнее для тебя же.\""
    nvl clear
    hide rika
    hide satoko
    with dissolve_04
    show rena si wa_a1 at central with dissolve_04
    n "\"Ой-ой,"
    extend " Мии-тян, глянь сюда."
    extend " Что это ещё такое?"
    show rena si wa_b1 with dissolve_02
    extend " Надо, наверное, потянуть?"
    extend " Потянуть?\""
    nvl clear
    scene black with fade_050
    n "*Дёрг*."
    play sound wa_029
    extend " .......*Тпруньк*..."
    extend " *Вшах*!!!!"
    nvl clear
    play sound wa_015
    $ renpy.pause(0.1)
    play sound wa_015
    $ renpy.pause(0.15)
    play sound wa_015
    $ renpy.pause(0.2)
    play sound wa_015
    $ renpy.pause(0.2)
    play sound wa_002
    $ renpy.pause(0.15)
    play sound wa_004
    $ renpy.pause(0.15)
    play sound wa_003
    $ renpy.pause(0.1)
    play sound wa_002
    $ renpy.pause(0.15)
    play sound wa_015
    $ renpy.pause(0.2)
    play sound wa_004
    $ renpy.pause(0.15)
    n "Рэна потянула за некую верёвочку, и сверху тотчас посыпались, застучав по земле, бесчисленные бамбуковые колья, бывшие до того привязанными к ветке над её головой!!"
    nvl clear
    scene bg 143 with dissolve_04
    show mion si bik_a2 at sprava with dissolve_04
    play music msys03_treat
    n "\"Ооооооо!!"
    extend " О-О-О-О-О!!"
    extend " Это ещё что?!{w=0.5}{nw}"
    play sound wa_015
    extend " Что за?!{w=0.4}{nw}"
    play sound wa_015
    extend " ЧТО ЗА?!{w=0.4}{nw}"
    play sound wa_015
    extend " {b}АААААААА!!{/b}\"{nw}"
    play sound wa_004
    extend "{w=0.2}{nw}"
    play sound wa_003
    extend "{w=0.1}{nw}"
    play sound wa_002
    extend "{w=0.2}{w=1.0}"
    show rika si wa_a1 at sleva with left_03
    n "\"......Старая штучка же."
    extend " Сатоко сделала её, помнится, на втором году обучения, во втором полугодии.\""
    nvl clear
    hide mion with left_03
    show satoko si yare_a1 at sprava with right_03
    n "\"Вам повезло."
    extend " Наконечники кольев обмазаны собачьим помётом, посему рана быстро загниёт, если её не обработать.\""
    n "{b}\"С-С КАКИХ ЭТО ПОР У НАС ТУТ ВЬЕТНА-А-А-А-АМ?!!\"{/b}"
    nvl clear
    hide rika
    hide satoko
    with dissolve_04
    n "......Как объяснили Сатоко и Рика-тян..."
    n "В младших классах ловушки для Сатоко были главной отрадой — и она все горы ими обставила."
    nvl clear
    show rena si ko_b1 at sprava with right_03
    n "\"...Кейти-кун, а может...... сюда запрещено ходить вовсе не из-за опасности потеряться... а из-за ловушек?..\""
    n "Как я, так и Мион выразили полнейшее согласие с предположением Рэны."
    nvl clear
    show satoko si aku_a1 at sleva with left_03
    n "\"Ладно!"
    extend " Давайте поторапливаться уже."
    extend " А то до темноты не успеем."
    extend " В темноте мне и самой опасно тут ходить.\""
    n "{b}Н-НУ И ЗАЧЕМ ВЫ МЕНЯ ПРИТАЩИЛИ НА ЭТИ ПОЛНЫЕ ОПАСНОСТЕЙ ГОРЫ-Ы-Ы-Ы?!!{/b}"
    n "{nw}"
    n "Какого чёрта мне, обычному парню-японцу среднего телосложения, приходится рисковать своей жизнью посреди скопища ловуше-ек?!"
    nvl clear
    scene black with dissolve_04
    n "......А потом..."
    extend "... в тот же миг, как потеряли Рику-тян и Сатоко из вида, мы трое разом попались..."
    nvl clear
    scene bg 205 with Dissolve(1.0)
    play ambient lsys12
    n "\"......Вытащите меня, люди-и-и!"
    extend " Дядюшка хочет в кустики-и-и!!\""
    n "\"Подождё-ёшь!"
    extend " Сначала снимите с меня ведёрышко-о!!"
    extend " Не вижу ничегошеньки-и!"
    extend " Хау-у-у!!\""
    n "\"Слышь, Рэна, хватит беситься..."
    extend " Т-трусы видать...\""
    nvl clear
    n "\"Х-ХААААУУУУУУ!!!"
    extend " Ты их видел?!"
    extend " Видел?!"
    extend " Кейти-кун видел!!"
    extend " Хаааууууууууу!!!\""
    nvl clear
    play sound wa_015
    scene white with fade_010
    scene furiker_a with fade_050
    play sound wa_005
    with Shake((0, 0, 0, 0), 0.5, dist=30)
    scene furiker_b with fade_050
    play sound wa_006
    with hpunch
    scene furiker_a with fade_050
    with Shake((0, 0, 0, 0), 0.5, dist=30)
    scene black with fade_010
    n "{b}*БА-БА-БА-БА-БА-БА*, *БА-БА-БА-БА-БА*, *БА-БА-БА-БААААМММ*!!!{/b}"
    nvl clear
    n "\"Д-Да ты же всё равно видишь!!"
    extend " Хоть у тебя на голове и ведёрко...{nw}"
    play sound wa_005
    extend " Гха,{w=0.2}{nw}"
    play sound wa_005
    extend " кхо!!{w=0.4}{nw}"
    play sound wa_006
    extend " Гхве-е-е!!\""
    nvl clear
    scene bg 142 with dissolve_04
    n "Я временно превратился в личную боксёрскую грушу Рэны Ведёрко-На-Голове. Мион протяжно захныкала."
    nvl clear
    show rika si wa_a1 at sprava with right_03
    n "\"......Не можешь выбраться, бедненькая ты, бедненькая.\""
    show satoko si yare_b1 at sleva with right_03
    n "\"Тьфу, я что, не говорила вам?"
    extend " Идите след в след и не отрывайтесь от меня ни на шаг!\""
    nvl clear
    n "Только тогда я понял......"
    n "Сатоко так сильно хотела затащить нас на здешние горы... лишь затем, чтоб похвастаться старыми ловушками."
    n "{nw}"
    n "......А могла бы просто показать..."
    extend " а не делать так, чтобы нам пришлось испытать их действие на своей шкуре!!"
    nvl clear
    n "Рика-тян по очереди гладила наши макушки, выглядя при сём небывало довольной..."
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_tata
    return
