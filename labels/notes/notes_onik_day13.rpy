    scene bg 115 with fade
    n "{b}Гостевая? Кухня?{/b}"
    n "{nw}"
    n "Пожалуй, следует прояснить устройство дома семьи Маэбара."
    $ renpy.pause(2.0)
    if persistent.matsuri:
        scene bg 115 _ohagi with dissolve_04
    $ renpy.pause(2.0)
    scene bg 210 _lamp with fade
    $ renpy.pause(2.0)
    scene bg 170 with fade
    n "Насколько понял переводчик, это всё — одно и то же помещение.\nВидимо, в гостиной есть кухонный закуток, в котором стоит обеденный стол.\nВ гостиной стоят, как вы видите, два дивана.\nИначе никак не объяснить, что к чему (кроме ошибки в задних планах первоисточника)."
    nvl clear
    scene bg 117 zakat with Dissolve(1.0)
    $ renpy.pause(2.0)
    scene bg 118 with Dissolve(7.0)
    play music msys07
    n "{b}Каждое подозрение рождает демонов{/b}."
    n "{nw}"
    n "Иносказание, рождённое пословицей в четыре \nиероглифа, читающейся как {i}«гисинъ-анки»{/i} \n(паранойя), что значит: «Заподозришь что-то — подозрительным станет выглядеть всё». Данное высказывание хорошо подытоживает всю первую Главу."
    n "Нынешний вариант как нельзя ладно увязывается с историей Хинамидзавы и Оникакуси."
    nvl clear
    stop music fadeout 2.5
    $ renpy.pause(1.0)
    scene black with down
    scene bg 080 _door with up
    $ renpy.pause(3.0)
    scene bg 082 night with Dissolve(6.0)
    scene black with Dissolve(8.0)
    $ renpy.pause(2.0)
    play sound wa_008
    $ renpy.pause(0.5)
    play sound wa_030
    scene ryuuketu with ImageDissolve("efe/ryuuketu_efe.png", 0.3, 50, reverse=True)
    play sound wa_007
    scene bg 082 night with Shake((0, 0, 0, 0), 2.0, dist=30)
    scene black with Dissolve(3.0)
    call screen translation_notes
    return
