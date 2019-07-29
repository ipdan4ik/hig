    stop music fadeout 1.0
    scene bg 241 with Dissolve(3.0)
    if renpy.loadable("music/Matsuri/17 - Soushitsu.ogg"):
        play music soushitsu
    else:
        play music silver_mirror
    n "{b}Татами{/b}."
    n "{nw}"
    n "Количеством циновок {i}татами{/i} японцы измеряют площадь комнат."
    n "Площадь обычных {i}татами{/i} — 90x180 сантиметров."
    nvl clear
    n "{b}Одзягайкэ{/b}."
    n "{nw}"
    n "Пруд неподалёку от Хинамидзавы."
    n "Есть в Японии на самом деле."
    nvl clear
    n "{b}Четвёртый отдел{/b}."
    n "{nw}"
    n "Один из отделов главного полицейского управления по борьбе с организованной преступностью (в масштабе страны)."
    n "Данный отдел занимается местечковыми якудза и предотвращением применения теми насилия."
    nvl clear
    n "{b}Хаори{/b}."
    n "{nw}"
    n "Лёгкая куртка, надеваемая поверх кимоно."
    n "Чаще всего можно увидеть в кино про самураев."
    nvl clear
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    n "{b}\"Она проклята, говорю вам! ПРОКЛЯТАААААА!!!\"{/b}{w=1.0}{nw}"
    nvl clear
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    call screen translation_notes
    return
