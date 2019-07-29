    $ _game_menu_screen = None
    $ unlock_prompt = True
    scene black
    show rena se def_a1 with fastdown
    a_r "День добрый."
    a_r "Стало быть, вы утверждаете, что знаете полное содержание первой арки?{nw}{w=1.0}"
    play sound lovely_laugh
    show rena se wa_a1 with fastdown
    $ renpy.pause(1.0)
    show rena se def_a1 with up
    a_r "Что же, посмотрим, сможете ли вы это подтвердить, ответив на три простых вопроса."
    a_r "Ответ на каждый вопрос — одно короткое существительное, начинающееся с заглавной буквы."
    a_r "Точку ставить не надо."
    a_r "Ну, значит..."
    show rena se wa_b1 with fastup
    play sound wa_011
    a_r "Поехали!{nw}{w=0.2}"
    $ question_1 = renpy.input("Предмет, использованный при наказании фотографа.", length=7)
    if question_1 == pass_onik_1:
        show rena se wa_a1 with fastdown
        a_r "Отлично!"
        a_r "Переходим ко следующему вопросу."
        show rena se bik_b1 with fastup
        $ question_2 = renpy.input("Уменьшительно-ласкательное название предмета, подаренного главным героем одной из девушек.", length=7)
        if question_2 == pass_onik_2:
            show rena se hau_a1 with fastdown
            a_r "Отлично... хау..."
            a_r "А теперь заключительный вопрос..."
            show rena se ko_a2 with fastdown
            $ question_3 = renpy.input("Предмет, которым была убита вышеупомянутая девушка.", length=7)
            if question_3 == pass_onik_3:
                play sound wa_012
                show rena se wa_a1 with fastup
                a_r "Отлично!"
                a_r "Вы доказали, что знаете содержание Первой Главы."
                hide rena with Dissolve(1.0)
                $ renpy.pause(1.0, hard=True)
                jump otsukaresama_onikakushi
            else:
                jump you_lied
        else:
            jump you_lied
    else:
        jump you_lied
