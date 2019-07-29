    $ _game_menu_screen = None
    $ unlock_prompt = True
    stop music fadeout 2.0
    scene black
    show satoko ts bik_a1
    a_s "А куда это вы полезть изволили без моего разрешения?!"
    if persistent.matsuri:
        play sound lsys28
        $ ui.timer(17.0, ui.jumps("eaten_by_satoko"))
        show satoko ts aku_a1:
            crop (0, 0, 224, 384)
            size (224, 384)
            linear 12.0 crop (0, 0, 224, 192) xzoom 2.0
            linear 5.0 zoom 2.0 yanchor 0.75
        a_s "А ну, назад, назад!"
    else:
        show satoko ts aku_a1 with dissolve_02
    stop sound fadeout 0.01
    $ renpy.pause(3.0, hard=True)
    scene black with dissolve_04
    show satoko ku aki_a1 with fastup
    a_s "Какая невоспитанность! Могли бы и подождать, пока я переоденусь!"
    play music msys05
    show satoko ku wa_a1 with dissolve_02
    a_s "Ладно, вы же пришли сюда открыть Главу, так?"
    show satoko ku def_a1 with dissolve_02
    a_s "Вам понадобится ответить на семь вопросов. На каждый надобно отвечать существительным в именительном падеже. Точку ставить не нужно."
    show satoko ku aku_a1 with dissolve_02
    a_s "Вопросов нет?{w=0.2} Вопросов нет, приступаем.{w=0.1}{nw}"
    show satoko ku wa_a1 with dissolve_02
    $ question_1 = renpy.input("Кто готовил ужин в доме семьи Маэбара в первый день?", length=9)
    if question_1 == pass_tata_1:
        play sound wa_011
        a_s "Весьма хорошо! Вижу, отсутствием памяти вы не страдаете!"
        show satoko ku aku_a1 with dissolve_02
        a_s "Переходим к следующему!{w=0.2}{nw}"
        play sound wa_007
        $ question_2 = renpy.input("Краткое название предмета, потрясая которым, Кейти-сан прибыл на спортивную площадку начальной школы посёлка Окиномия, думая, что там идёт драка.", length=9)
        if question_2 == pass_tata_2:
            play sound wa_007
            show satoko ku def_a1 with dissolve_02
            a_s "Неплохо, неплохо! Давайте дальше!"
            $ question_3 = renpy.input("Как зовут тренера Бойцов Хинамидзавы?", length=9)
            if question_3 in pass_tata_3:
                play sound wa_029
                show satoko ku aki_a1 with dissolve_02
                a_s "Согласна с вами, личность он престраннейшая."
                show satoko ku hau_a1 with dissolve_02
                a_s "Тем не менее и к нему можно привыкнуть."
                $ question_4 = renpy.input("Во что играли на упомянутой площадке школы Окиномия... до того как туда прибыл Кейти-сан?", length=9)
                if question_4 == pass_tata_4:
                    play sound wa_011
                    show satoko ku wa_a1 with dissolve_02
                    a_s "Не правда ли, здорово я его?"
                    show satoko ku aki_a1 with dissolve_04
                    a_s "Впрочем, подождите минутку, будьте столь добры."
                    a_s "У меня, видите ли, не так много выражений лица с ошейником, поэтому для заключительных вопросов мне понадобится его снять."
                    hide satoko with dissolve_04
                    show irie si warai at sleva with dissolve_04
                    a_i "А пока моя будущая {cps=*0.6}служаночка~{font=DejaVuSans.ttf}☆{/font}...{/cps} переодевается, мы продолжим наш увлекательный допрос!"
                    show irie si maji_a2 with dissolve_02
                    $ question_5 = renpy.input("Фамилия подозрительной личности, повстречавшейся Маэбаре-сану после закапывания трупа.", length=9)
                    if question_5 == pass_tata_5:
                        show irie si def_a1 with dissolve_02
                        a_i "Да, ответ правильный. Переходим к следующему."
                        $ question_6 = renpy.input("Предмет, которым главный герой намеревался повторно убить одного человека, менее чем достойного уважения, но который сослужил ему медвежью услугу.", length=9)
                        if question_6 == pass_tata_6:
                            play sound wa_005
                            show irie si maji_a1 with dissolve_02
                            a_i "Убийство — не выход. Но иногда бывает так, что совесть не позволяет мне осудить убийцу."
                            show satoko se mu_a2 at sprava with dissolve_04
                            a_s "............"
                            show irie si maji_a2 with dissolve_02
                            a_i "Заключительный вопрос."
                            $ question_7 = renpy.input("Название (вид) стратегического сооружения, где произошла развязка данной Главы.", length=9)
                            if question_7 == pass_tata_7:
                                play sound wa_041
                                a_s "Верно..."
                                show satoko se hn_b3 with fastup
                                a_s "И вы знаете, что со мной потом стало?"
                                show satoko se na_b1 with dissolve_02
                                a_s "{cps=*2.0}Всё вышло так, как и говорила Мион-саааан! Уаааааа!{/cps}{w=0.1}{nw}"
                                hide satoko with moveoutleft
                                a_i "............"
                                a_i "Н-да."
                                scene black with dissolve_04
                                $ renpy.pause(1.0)
                                jump otsukaresama_tatarigoroshi
                            else:
                                jump wrong_answer
                        else:
                            jump wrong_answer
                    else:
                        jump wrong_answer
                else:
                    jump wrong_answer
            else:
                jump wrong_answer
        else:
            jump wrong_answer
    else:
        jump wrong_answer
