    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    scene bg 252 with Dissolve(1.0)
    play ambient lsys13
    n "\"Это полицейский участок Окиномия, Третий, вы на связи? Приём."
    extend " Третий, приём.\""
    n "\"На связи Третий."
    extend " Слышим вас хорошо.\""
    nvl clear
    n "\"Подмога в пути."
    extend " Оставайтесь на месте до дальнейших приказов."
    extend " Отбой.\""
    n "\"Это Третий, вас понял.\""
    nvl clear
    n "\"И не включайте проблесковые маячки."
    extend " Тише. Пожалуйста, тише.\""
    n "\"База, прибыл врач, желает переместить его для обследования."
    extend " Что делать?"
    extend " Приём.\""
    nvl clear
    n "\"Подтверждаем."
    extend " Следуйте указаниям врача.\""
    n "\"Принял."
    extend " Так точно."
    extend " ...А вот и подмога."
    extend " Может, сначала сделать снимки?"
    extend " ...Всё равно жертве уже ничем, думаю, не помочь.\""
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_onik
    return
