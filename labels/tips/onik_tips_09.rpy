    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    scene bg 181 with Dissolve(1.0)
    play music silver_mirror
    n "XX июня 55 года Сёва. Вечерний выпуск."
    n "{nw}"
    n "XX числа, примерно в 2 часа пополудни, конторский служащий XXX-сан и его жена XXXX-сан, жители деревни Хинамидзава, входящей в X район города Шишибонэ..."
    extend " находясь на смотровой площадке природного парка Сиракава, упали с высоты 27 метров в горную реку."
    n "После проведённого полицейским и пожарным отрядами поиска ниже по течению примерно в 7 часов вечера обнаружено тело XXX-сана."
    n "Тело жены, XXXX-сан, всё ещё не найдено."
    n "{nw}"
    n "Уровень воды поднялся из-за тайфуна №3, прошедшего здесь несколькими днями раньше, что сильно затруднило поиски."
    nvl clear
    n "Предположительно, когда супружеская чета облокотилась на перила, те подломились."
    n "Так как состояние перил оставляет желать лучшего, полиция допрашивает заведующих парком по поводу халатности в отношении обслуживания парковых принадлежностей."
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_onik
    return
