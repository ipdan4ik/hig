    stop music fadeout 1.0
    stop ambient fadeout 1.0
    play ambient lsys11
    scene bg 074 with dissolve_04
    show irie si def_a2 at sprava with right_03
    n "\"Не могли бы вы помочь, Шион-сан?\""
    show shion si wink_a1 at sleva with left_03
    n "\"Вы просите девушку помочь с перетаскиванием тяжестей?"
    extend " Вот потому-то у вас до сих пор и нет пары.\""
    nvl clear
    show irie si def_a1 with dissolve_02
    n "\"Э-э, знаете ли,"
    extend " эмм, это не ваше дело.\""
    show shion si wa_a1 with dissolve_02
    n "\"Аха-ха-ха-ха-ха-ха-ха-ха.\""
    nvl clear
    scene black with dissolve_04
    scene bg 151 zakat with fastup
    n "Для сегодняшнего пикника понадобился полный фургон всякой утвари."
    n "Помогавшие с уборкой родители начали понемногу расходиться."
    nvl clear
    show irie si def_a1 at sleva with left_03
    n "\"Что ж......"
    extend " Что теперь, Шион-сан?"
    extend " Как вы сюда добрались?"
    extend " Если на велосипеде, я могу вас подкинуть. Места в машине хватит.\""
    show shion si def_b1 at sprava with right_03
    n "\"Ничего, я на мотороллере приехала."
    extend " Но благодарю за заботу.\""
    nvl clear
    show irie si def_a2 with dissolve_02
    n "\"......Как хорошо, что вы сегодня пришли."
    extend " Без помощницы нам всё-таки не обойтись.\""
    show shion si aku_a1 with dissolve_02
    n "\"Неужели я до сих пор ей считаюсь?"
    extend " Я уже год как не приходила, вам следует уволить такого недобросовестного помощника.\""
    nvl clear
    show irie si warai with dissolve_02
    n "\"Хорошо,"
    extend " когда Шион-сан придёт и скажет, что хочет уйти, я мигом её уволю.\""
    show shion si to_b1 with dissolve_02
    n "\"Тьфу..."
    extend " Хитрите вы всё."
    show shion si wink_b1 with dissolve_02
    extend " ............Отпустили бы наконец бедную пташку на волю."
    extend " Сил больше нету отвечать на ваши звонки всякий раз, когда собираетесь провести матч.\""
    nvl clear
    show irie si def_a2 with dissolve_02
    n "\"Шион-тян, ты бы такой милой девчуркой была, будь у тебя поболее искренности."
    extend " Папочке грустно. Когда ты сбилась с правильного пути, скажи мне?!"
    extend " Ах, проснёшься ли ты от крепких объятий папочкиной любви?!"
    extend " Не надо робеть!!"
    play sound wa_029
    extend " Нуууу же-е~...\""
    nvl clear
    n "...Тренер валял дурака как мог, но Шион лишь улыбнулась, глядя куда-то вдаль."
    nvl clear
    scene black with dissolve_04
    scene bg 204 with dissolve_04
    n "\".........Ничто не меняется."
    extend " Тренер всё такой же чудак, остальные всё так же радуются жизни.\""
    n "\"...За исключением Сатоши-куна..."
    extend " Это вы хотели сказать?\""
    n "\"..................\""
    n "\"Он вернётся."
    extend " Я знаю."
    extend " Ведь его ждут.\""
    n "\".........Хм......"
    extend " Ай, говорите, что вам заблагорассудится.\""
    nvl clear
    n "\"Бессердечный он парень."
    extend " Как он мог уйти от такой милой девушки?\""
    n "\"Э-э?!"
    extend " Д-де-девушки?!!"
    extend " ВЫ ПРО КОГО?!"
    extend " ПРО КОГО?!"
    extend " ......А?!\""
    n "\"Пф-ф... хе-хе-хе, ха ха ха ха ха ха!\""
    nvl clear
    n "\"......Чё-ёрт... ну хватит!"
    extend " Вы прекратите смеяться или нет?!!"
    extend " ТРЕЕЕНЕЕЕЕР!!\""
    n "\"Ха-ха-ха!"
    extend " Уааах-ха-ха-ха-хааа!!\""
    n "{nw}"
    n "Тренер долго заливался смехом, держась за живот..."
    nvl clear
    scene bg 151 zakat
    show irie si def_a2 at sleva
    with fastup
    n "\"Что ж, до свидания."
    extend " Пожалуйста, приходите на игры хоть иногда.\""
    show shion si aku_a1 at sprava with dissolve_02
    n "\"Ну, ежели будет охота..."
    extend " Желания помогать у меня больше со-овсем нет.\""
    nvl clear
    show irie si def_a1 with dissolve_02
    n "\"...Как вам будет угодно."
    extend " Если не хочется, могу вычеркнуть из состава в любое время."
    extend " Не по душе мне кого-либо заставлять.\""
    show shion si wa_a1 with dissolve_02
    n "\"........................Тьфу..."
    extend " Ай, ладно, ладно!"
    extend " Простите, простите!"
    extend " Я проиграла."
    extend " Так и быть, приду поболеть, коли будет на то желание, только уж сегодня мне со счёта спишите.\""
    nvl clear
    show irie si def_a2 with dissolve_02
    n "\"Хе-хе-хе!"
    extend " Ох, время-то, время!"
    extend " Уже давно пора утварь вернуть!.."
    extend " Меня, наверное, заждались!"
    extend " Ладно, всё на сегодня!"
    extend " До встречи на следующей игре!\""
    show shion si wink_b1 with dissolve_02
    n "\"Ладно, если будет охота."
    extend " Счастливо, Тренер.\""
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_tata
    return
