    stop music fadeout 1.0
    stop ambient fadeout 1.0
    play music msys02
    scene bg 027 with Dissolve(1.0)
    show satoko se bik_a1 at central with right_03
    n "\"А?"
    extend " Семья Мион-сан?\""
    n "\"Ага."
    extend " Есть у неё братья там, сёстры?\""
    nvl clear
    n "Я подумал: а может, и вправду есть младшая сестра по имени Шион..."
    extend " и, не сдержав любопытства, тайком спросил Сатоко."
    nvl clear
    show satoko se aki_a1 with dissolve_02
    n "\"...Хммм..."
    extend " Боюсь, не помню..."
    extend " Не могу точно сказать...\""
    n "Проговорила она невнятно."
    n "...Разве Сатоко не заходила к Мион погостить?"
    nvl clear
    n "\"Как я понимаю... ты её не встречала.\""
    show satoko se def_a1 with dissolve_02
    n "\"Угу."
    extend " Никого не знаю, за исключением бабушки.\""
    n "С таким ответом... понятно, что над предположением о подлинности Шион сгустились грозовые тучи."
    nvl clear
    n "\"Такого рода вещи ведомы Рике."
    extend " Почему бы тебе не спросить её?\""
    nvl clear
    scene bg 028
    show rika se de_a1 at sleva
    with left_03
    n "Сатоко замахала Рике-тян, которая грелась в лучах солнышка."
    nvl clear
    show satoko se def_a1 at sprava with right_03
    n "\"Рика-а."
    extend " Не знаешь ли ты чего про семью Мион-сан?\""
    n "Не ожидавшая такого вопроса Рика-тян удивлённо на нас поглядела."
    nvl clear
    show rika se ni_a1 with dissolve_02
    n "\"......У Мии очень много родни, так что всех я \nне знаю.\""
    n "\"И впрямь так много?.."
    extend " А, например,"
    extend " ммм,"
    extend " есть ли в её семье Сонодзаки Шион?"
    extend " Понимаешь... может, я не расслышал, но мало ли, вдруг она и впрямь есть...\""
    nvl clear
    show rika se de_a1 with dissolve_02
    n "\"Ты про Шии?"
    extend " Да, Шион есть.\""
    n "Э?"
    n "Ну дела."
    extend " Она есть взаправду!.."
    nvl clear
    show satoko se aku_a1 with dissolve_02
    n "\"Хммм?"
    extend " Какое созвучное имя."
    extend " Как бы язык не сломать от путаницы.\""
    n "\"......Я слышала, что Мии она приходится младшей близняшкой, но сама её видела мало.\""
    n "{nw}"
    n "Хотя Рика-тян её знает, виделись они всё же мало."
    nvl clear
    n "\"......Кажется, видела её на поминальной службе несколько лет назад.\""
    n "\"Если она не ходит в наш класс, тогда она ходит во школу в Окиномии?\""
    show satoko se def_a1 with dissolve_02
    n "\"Вполне может статься, что в Окиномии она и живёт."
    extend " Потому что Мион-сан живёт со своей бабушкой отдельно от всей семьи.\""
    n "Живёт раздельно с родителями?"
    extend " Странно как-то."
    extend " На то есть причины?"
    nvl clear
    show rika se ko_a1 with dissolve_02
    n "\"......Её семья очень запутанная, видишь ли.\""
    show satoko se wa_b1 with dissolve_02
    n "\"У неё столько родственников."
    extend " Уверена, причины какие-то есть.\""
    n "Ну, теперь я хоть знаю, что есть младшая сестра-близнец по имени Шион, однако семья её не менее загадочна, чем она сама..."
    nvl clear
    hide satoko with left_03
    show mion se wink_b1 at sprava with right_03
    n "\"Эй, о чём вы там втроём сплетничаете?"
    extend " Дядька Мион с вами-и!\""
    hide rika with right_03
    show satoko se wa_a1 at sleva behind mion with left_03
    n "\"Ох, Мион-сан, вы как раз вовремя!"
    extend " Мион-сан, правда ли, что у вас есть младшая сестра-близняшка?\""
    n "Ах... Мион... вот чёрт..."
    nvl clear
    show mion se bik_a1 with dissolve_02
    n "\"...С... сестра?!..."
    show mion se hau_a1 with dissolve_02
    extend " А, э......... у-угу."
    extend " Есть...\""
    n "Мион, совсем не походя на себя, разнервничалась и залилась краской."
    n "Такое чувство, что меня проверяет......"
    nvl clear
    show satoko se aku_b1 with dissolve_02
    n "\"Ого-о-о!"
    extend " Я и не ведала!"
    extend " На кого же она похожа..."
    extend " Мне обязательно надо на неё поглядеть!!\""
    show mion se bik_b1 with dissolve_02
    n "\"Нет, лучше не стоит!"
    extend " О-Она совсем не мила!"
    extend " И развязна вдобавок!"
    extend " Я иногда разговариваю с ней по телефону... но и сама уже давненько не видела!..\""
    nvl clear
    n "......Почему она так расстроилась, хотел бы я знать?.."
    n "Она будто бы заявляет, что вчерашняя Шион — поддельная..."
    n "{nw}"
    n "Пока оставлю всё на своих местах — так забавнее."
    nvl clear
    n "...Иная Мион, прозывающаяся Шион."
    n "...Встречу ли я её снова, если снова зайду в ресторан?"
    n "{nw}"
    n "Хоть я и знал, что видел Мион, всё же было такое чудное чувство, будто завожу совершенно нового друга."
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_wata
    return