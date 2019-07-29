    $ _game_menu_screen = None
    $ unlock_prompt = True
    scene black
    show ooishi yukata def_a1
    a_o "Ваши документики?{w=1.0}{nw}"
    show ooishi yukata wa_a1 with dissolve_02
    a_o "Шучу, шучу. Мм-хм-хм-хм!"
    show ooishi yukata def_a1 with dissolve_02
    a_o "Полагаю, вы пришли сюда открыть четвёртую главу. Что ж, для этого вам придётся ответить на семь вопросов по её содержанию."
    a_o "Все ответы начинаются с заглавной буквы (все остальные буквы — строчные) и согласуются с вопросом. Точку ставить не нужно."
    show ooishi yukata def_a2 with dissolve_02
    a_o "Вы готовы? Тогда поехали."
    show ooishi yukata def_a1 with dissolve_02
    $ question_1 = renpy.input("Какова фамилия министра, связанного с делом о похищении, вокруг которого вертится сия Глава?", length=8)
    if question_1 in pass_hima_1:
        play sound wa_012
        show ooishi yukata wa_a1 with dissolve_02
        a_o "Отлично! Продолжим же?"
        $ question_2 = renpy.input("Имя жены следователя, занимавшегося данным делом и подружившегося в его ходе с Ооиси?", length=8)
        if question_2 == pass_hima_2:
            play sound wa_044
            show ooishi yukata def_a1 with dissolve_02
            a_o "Верно."
            $ question_3 = renpy.input("Игра, в которую играл главный герой вечером второго дня с Ооиси?", length=8)
            if question_3 in pass_hima_3:
                show ooishi yukata aku_a1 with dissolve_02
                play sound wa_010
                $ renpy.pause(0.3)
                play sound wa_011
                show ooishi yukata def_a2 with dissolve_04
                a_o "Эх, славная была партейка! Вот бы сыграть ещё хоть разок!"
                $ question_4 = renpy.input("Ключевая улика, позволившая завершить дело и спасти похищенного?", length=8)
                if question_4 in pass_hima_4:
                    play sound wa_011
                    a_o "Совершенно верно."
                    show ooishi yukata def_a1 at sleva with move
                    show rika hima de_a1 at sprava with dissolve_04
                    a_f "Ми-и."
                    show ooishi yukata wa_a1 with dissolve_04
                    a_o "О, Рика-сан? Добрый день, добрый день, мм-хм-хм!"
                    a_f "Добрый день же, Ооиси. Дальше вопросы буду задавать я."
                    show ooishi yukata def_a2 with dissolve_02
                    a_o "Что ж, прошу любезно."
                    show ooishi yukata def_a1 with dissolve_02
                    $ question_5 = renpy.input("Оружие, которым угрожали Акасаке, чтобы тот отдал спасённого.", length=8)
                    if question_5 == pass_hima_5:
                        play sound wa_012
                        show rika hima wa_a1 with dissolve_02
                        a_f "Нипа-а~{font=DejaVuSans.ttf}☆{/font}. Верно!"
                        show rika hima ko_a1
                        show ooishi yukata aku_a1
                        with fastdown
                        $ question_6 = renpy.input("Кто перерезал провода?", length=8)
                        if question_6 in pass_hima_6:
                            play sound wa_012
                            show rika hima wa_a1 with dissolve_02
                            a_f "Ми-и!{w=0.8}{nw}"
                            show ooishi yukata wa_a1 with left_03
                            a_o "Мм-хм-хм-хм-хм..."
                            show rika hima ni_a1 with dissolve_02
                            $ question_7 = renpy.input("Ми-и?", length=7, exclude="~!.")
                            if (question_7.find(pass_hima_7[0]) != -1) or (question_7.find(pass_hima_7[1]) != -1) or (question_7.find(pass_hima_7[2]) != -1):
                                play sound wa_029
                                $ renpy.pause(0.2)
                                play sound wa_029
                                show rika hima wa_a1 with dissolve_02
                                a_f "Нипа-а-а! ~{font=DejaVuSans.ttf}☆{/font}"
                                show ooishi yukata def_a1 with dissolve_02
                                a_o "Поздравляю! Вы открыли четвёртую Главу!"
                                scene black with Dissolve(1.0)
                                $ renpy.pause(1.0)
                                jump otsukaresama_himatsubushi
                            else:
                                jump bad_answer
                        else:
                            jump bad_answer
                    else:
                        jump bad_answer
                else:
                    jump bad_answer
            else:
                jump bad_answer
        else:
            jump bad_answer
    else:
        jump bad_answer
