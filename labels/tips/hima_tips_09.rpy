    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play music days_of_children
    n "Думаете, в жизни бывает выбор?"
    n "Некоторые часто жалуются."
    n "Будь у них, мол, на ключевых точках жизни очевидный выбор, они бы могли выбирать лучшее будущее."
    n "{nw}"
    n "Слыша подобные жалобы, я всякий раз думаю: до чего же мелочные у них заботы."
    n "Какая, в сущности, разница, есть ли выбор — не бывает ничего такого, что поможет пройти к лучшему будущему."
    nvl clear
    n "......Не понимаете?"
    scene aka1 with Dissolve(1.0)
    n "Хорошо, тогда давайте представим, что \nперед вами — две загадочные коробки."
    n "{nw}"
    n "Можно выбрать лишь из двух вариантов."
    n "Или вы откроете красную, или вы откроете синюю."
    nvl clear
    n "Должно быть, вас охватят сомнения."
    n "{nw}"
    n "Раз надо выбрать коробку, то вам, естественно, захочется открыть ту, чьё открытие принесёт вам больше пользы."
    n "Вы оцените форму коробок, всяческие ощущения от каждой из них и, наконец, выберете одну — красную или синюю."
    n "{nw}"
    n ".........Так какую же?"
    nvl clear
    n "Красную или синюю?"
    n "Если счесть, что цвета коробок следуют тем же правилам, что цвета светофора, тогда красный означает опасность."
    n "Только это ещё не значит, что синяя безопасна."
    n "А возможно, тут как раз ловушка — заставить остерегаться красной, чтоб подтолкнуть к синей."
    nvl clear
    n "Ловушка?"
    n "...А если там то, что вам совершенно не нужно, а если там то, что принесёт вам вред?.."
    n "{nw}"
    n "Ага, ага... вот вы и запутались."
    n "Вы в замешательстве, какую же выбрать... Несомненно, теперь вам хочется и третьего варианта: уйти, не открывая ни одной из коробок."
    nvl clear
    n "А вот фигушки."
    extend " Вы обязаны открыть одну из них — либо красную, либо синюю."
    n "А, забыла сказать: когда вы сделаете выбор, другая исчезнет."
    n "И вы так и не узнаете, что в ней лежало."
    extend " Просто знайте, ладно?"
    nvl clear
    n "Ну же."
    extend " Что выберете?"
    n "Красную, синюю ли."
    n "{nw}"
    n "Не волнуйтесь — ни в одной нет ничего, что вам повредило бы."
    extend " Давайте."
    nvl clear
    play sound wa_044
    menu:
        "Открыть красную коробку":
            $ asobi_box = 1
            nvl clear
        "Открыть синюю коробку":
            $ asobi_box = 2
            nvl clear
    n "Вы хорошо подумали?"
    n "Стало быть, выбираете эту?"
    n "{nw}"
    n "В тот же миг, как вы приняли решение, другая коробка — пуф! — бесследно исчезла."
    n "Перестаньте думать о том, что в ней лежало, ладно?"
    n "Таково правило."
    n "{nw}"
    n "Ну что ж, давайте откроем выбранную вами коробку."
    nvl clear
    if asobi_box == 1:
        n "В ней лежит...{w=1.0} одна карамелька."
    elif asobi_box == 2:
        n "В ней лежит...{w=1.0} одна жевательная резинка."
    nvl clear
    if persistent.hima_asobi == asobi_box or not persistent.hima_asobi:
        jump hima_tips_09_first
    else:
        jump hima_tips_09_final
