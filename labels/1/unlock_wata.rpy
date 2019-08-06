$ _game_menu_screen = None
$ unlock_prompt = True
$ wata_q = 5
scene black
show mion si def_a1
a_m "Здоров. Чё, пришёл попытать счастья?{w=0.5} Тады не станем нежности разводить, начали.{w=0.7} Даю пять вопросов, ответить правильно надо хотя бы на три."
a_m "Ответ на каждый вопрос должен писаться с заглавной буквы, в именительном падеже и единственном числе.{w=1.5} Разумеется, ответ согласуется с вопросом."
$ question_1 = renpy.input("Фамилия одного из парней, с которыми Кей-тян играл на большом соревновании в магазине игрушек, а потом не раз ещё с ними пересекался (их называют в основном по фамилиям).", length=10)
if question_1 in pass_wata_1
show mion si wink_a2
a_m "Молодца! Давай дальше!"
else
$ wata_q += -1
$ question_2 = renpy.input("Любимая приправа учительницы Сатоко.", length=10)
if question_2 == pass_wata_2
show mion si wa_a1
a_m "Аха-ха-ха! Так держать!"
else
$ wata_q += -1
$ question_3 = renpy.input("Фамилия убийцы друзей главного героя?", length=10)
hide mion
show mion ki sin_a1
if question_3 != pass_wata_3
$ wata_q += -1
a_m "Молодец. Ещё два вопроса."
$ question_4 = renpy.input("Японское название здания, играющего ключевую роль в данной Главе.", length=10)
if question_4 == pass_wata_4
else
$ wata_q += -1
show mion ki wink_a1
a_m "И заключительный вопрос! Отвечай честно!"
a_m "И-и-и-и..."
show mion ki wa_a1
show mion se bik_b1 at sprava as real_mion
$ question_5 = renpy.input("Каков цвет нижнего белья сеструхи?", length=10, exclude='бух')
if question_5 != pass_wata_5
$ wata_q += -1
if wata_q >= 3 and question_5 not in failpass_wata_5
show mion se hau_a1 as real_mion
show mion ki wa_a1
a_m "Ну что ж! Поздравляю, ты прошёл экзамен!"
show mion ki wink_a2
a_m "Кстати говоря, трусы на сеструхе чёрные. Как у меня!"
show mion se bik_b1 as real_mion
a_m "ШИОННННН!!! АХ ТЫ ЗАСРААААНКАААААА!!!!!!!"
scene black
show mion se bik_b1
a_m "Н-ну, как бы то ни было..."
scene black
show mion ki sin_a1 at central
a_m "Аха-ха! Ладно, ладно, получай свою награду."
show mion ki fu_a2
alpha 1.0
0.3
linear 0.7 alpha 0.0
jump otsukaresama_watanagashi
elif question_5 in failpass_wata_5
jump evil_sisters
else
jump sad_sister
