    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with spiral2
    play music lsys23
    t "XX год эры Сёва.{w=2.0}{nw}"
    t "Статистика распределения обидчиков (по докладу Министерства Здравоохранения)."
    nvl clear
    show satoko se mu_a1 gray at sprava with Dissolve(1.0)
    t "Всего: 5 тысяч 352 случая.{w=2.0}{nw}"
    extend "\n{nw}"
    t "Родных матерей:{w=2.0}{nw}"
    t "{space=100}2 943 (55,0%%){w=2.0}{nw}"
    extend "\n{nw}"
    t "Приёмных матерей:{w=2.0}{nw}"
    t "{space=100}203 (3,8%%){w=2.0}{nw}"
    extend "\n{nw}"
    t "Родных отцов:{w=2.0}{nw}"
    t "{space=100}1 445 (27,0%%){w=2.0}{nw}"
    extend "\n{nw}"
    t "Приёмных отцов:{w=2.0}{nw}"
    t "{space=100}488 (9,1%%)"
    nvl clear
    t "XX год эры Сёва.{w=2.0}{nw}"
    t "Количество заявлений о жестоком обращении с детьми по категориям (по докладу Министерства Здравоохранения).{w=2.0}{nw}"
    t "Всего: 5 тысяч 352 случая.{w=2.0}{nw}"
    t "{nw}"
    t "Физическое насилие:{w=2.0}{nw}"
    t "{space=100}2 780 (51,9%%){w=2.0}{nw}"
    t "{nw}"
    t "Оставление без присмотра (отказ от обязанностей по воспитанию ребёнка):{w=2.0}{nw}"
    t "{space=100}1 728 (32,3%%)"
    nvl clear
    t "Психологическое насилие:{w=2.0}{nw}"
    t "{space=100}458 (8,6%%){w=2.0}{nw}"
    t "{nw}"
    t "Запреты на посещение школы:{w=2.0}{nw}"
    t "{space=100}75 (1,4%%){w=2.0}{nw}"
    t "{nw}"
    t "Изнасилования:{w=2.0}{nw}"
    play sound wa_026
    t "{space=100}311 (5,8%%){w=2.0}{w=2.0}"
    nvl clear
    scene black with Dissolve(3.0)
    $ renpy.pause(1.0)
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    call screen tips_tata
    return
