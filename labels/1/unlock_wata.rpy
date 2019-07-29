    $ _game_menu_screen = None
    $ unlock_prompt = True
    $ wata_q = 5
    scene black
    show mion si def_a1 with down
    a_m "Здоров. Чё, пришёл попытать счастья?{w=0.5} Тады не станем нежности разводить, начали.{w=0.7} Даю пять вопросов, ответить правильно надо хотя бы на три."
    a_m "Ответ на каждый вопрос должен писаться с заглавной буквы, в именительном падеже и единственном числе.{w=1.5} Разумеется, ответ согласуется с вопросом."
    $ question_1 = renpy.input("Фамилия одного из парней, с которыми Кей-тян играл на большом соревновании в магазине игрушек, а потом не раз ещё с ними пересекался (их называют в основном по фамилиям).", length=10)
    if question_1 in pass_wata_1:
        play sound wa_011
        show mion si wink_a2 with m1_03
        a_m "Молодца! Давай дальше!"
    else:
        $ wata_q += -1
    $ question_2 = renpy.input("Любимая приправа учительницы Сатоко.", length=10)
    if question_2 == pass_wata_2:
        play sound wa_012
        show mion si wa_a1 with left_03
        a_m "Аха-ха-ха! Так держать!"
    else:
        $ wata_q += -1
    $ question_3 = renpy.input("Фамилия убийцы друзей главного героя?", length=10)
    hide mion with dissolve_04
    $ renpy.pause(2.0, hard=True)
    show mion ki sin_a1 with Dissolve(1.0)
    if question_3 != pass_wata_3:
        $ wata_q += -1
    a_m "Молодец. Ещё два вопроса."
    $ question_4 = renpy.input("Японское название здания, играющего ключевую роль в данной Главе.", length=10)
    if question_4 == pass_wata_4:
        play sound wa_012
    else:
        $ wata_q += -1
    show mion ki wink_a1 with dissolve_04
    a_m "И заключительный вопрос! Отвечай честно!"
    play sound wa_047
    a_m "И-и-и-и..."
    show mion ki wa_a1:
        xalign 0.5 yalign 1.0
        linear 0.5 xalign 0.15
    show mion se bik_b1 at sprava as real_mion with moveinright
    $ question_5 = renpy.input("Каков цвет нижнего белья сеструхи?", length=10, exclude='бух')
    if question_5 != pass_wata_5:
        $ wata_q += -1
    if wata_q >= 3 and question_5 not in failpass_wata_5:
        play sound wa_012
        show mion se hau_a1 as real_mion with Dissolve(1.0)
        show mion ki wa_a1 with dissolve_02
        a_m "Ну что ж! Поздравляю, ты прошёл экзамен!"
        show mion ki wink_a2 with dissolve_02
        a_m "Кстати говоря, трусы на сеструхе чёрные. Как у меня!"
        show mion se bik_b1 as real_mion with dissolve_04
        a_m "ШИОННННН!!! АХ ТЫ ЗАСРААААНКАААААА!!!!!!!"
        play sound wa_007
        scene black with Shake((0, 0, 0, 0), 0.5, dist=30)
        $ renpy.pause(0.4, hard=True)
        play sound wa_005
        $ renpy.pause(0.4, hard=True)
        play sound wa_005
        $ renpy.pause(0.4, hard=True)
        play sound wa_003
        $ renpy.pause(0.7, hard=True)
        play sound wa_008
        $ renpy.pause(0.4, hard=True)
        play sound wa_036
        with Shake((0, 0, 0, 0), 4.0, dist=70)
        $ renpy.pause(2.5, hard=True)
        show mion se bik_b1:
            zoom 1.5 xalign 0.25 yalign 0.1
        with dissolve_04
        a_m "Н-ну, как бы то ни было..."
        play sound wa_008
        $ renpy.pause(0.3, hard=True)
        play sound wa_006
        scene black with Shake((0, 0, 0, 0), 0.5, dist=30)
        $ renpy.pause(0.5, hard=True)
        play sound wa_018
        $ renpy.pause(0.2, hard=True)
        play sound wa_005
        $ renpy.pause(0.8, hard=True)
        play sound wa_005
        $ renpy.pause(0.3, hard=True)
        play sound wa_030
        $ renpy.pause(0.4, hard=True)
        play sound wa_007
        $ renpy.pause(0.5, hard=True)
        play sound wa_005
        $ renpy.pause(0.3, hard=True)
        play sound wa_012
        $ renpy.pause(0.9, hard=True)
        play sound wa_006
        with Shake((0, 0, 0, 0), 1.5, dist=30)
        $ renpy.pause(0.2, hard=True)
        play sound wa_010
        $ renpy.pause(0.5, hard=True)
        play sound wa_005
        $ renpy.pause(0.4, hard=True)
        play sound wa_012
        $ renpy.pause(0.6, hard=True)
        play sound wa_030
        $ renpy.pause(0.6, hard=True)
        play sound wa_018
        with Shake((0, 0, 0, 0), 0.5, dist=20)
        $ renpy.pause(2.8, hard=True)
        play sound wa_007
        with Shake((0, 0, 0, 0), 1.0, dist=10)
        $ renpy.pause(4.0, hard=True)
        show mion ki sin_a1 at central with left_03
        a_m "Аха-ха! Ладно, ладно, получай свою награду."
        show mion ki fu_a2:
            alpha 1.0
            0.3
            linear 0.7 alpha 0.0
        with dissolve_04
        $ renpy.pause(1.0, hard=True)
        jump otsukaresama_watanagashi
    elif question_5 in failpass_wata_5:
        jump evil_sisters
    else:
        jump sad_sister
