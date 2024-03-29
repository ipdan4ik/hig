    scene black with center_03
    n "{b}Рис карри{/b}."
    n "{nw}"
    n "Как можно догадаться, представляет собой рис, приправленный соусом карри.\nСоус карри пошёл от индийской приправы карри.{w=0.7} Очень острой."
    n "{b}Нан{/b}, который, как утверждает главный герой, едят с карри, — индийский хлеб-лепёшка. Подобен лавашу, но внутри тмин."
    nvl clear
    n "{b}Кацура-муки{/b}."
    n "{nw}"
    n "Отличный поварской способ выпендриться. Как можно понять, подразумевает собой срезание кожуры (или верхнего слоя) с овощей одним куском. Следует учитывать ширину лезвия, которое не должно быть слишком узким."
    n "Срезанную кожуру можно использовать для самых различных целей.{w=0.2} Например, сделать из неё змейку, чему научила нас мудрая Рика-тян."
    nvl clear
    n "{b}Кото{/b}."
    n "{nw}"
    n "Японские гусли. Ударение на втором слоге."
    n "Традиционный щипковый музыкальный инструмент."
    nvl clear
    n "{b}Световолновая пушка{/b}."
    n "{nw}"
    n "Орудие космического линкора Ямато из вселенной {b}Gundam{/b}. См. TIPS.doc для прочтения настоящего названия."
    n "По-английски будет {i}wave motion gun{/i}."
    nvl clear
    n "{b}Пинок в голову{/b}."
    n "{nw}"
    n "Удар исполняла Харухи в отношении президента компьютерного сообщества в рассказе «День Стрельца».{w=2.0} Не пытайтесь повторить. За отсутствием специальной подготовки вместе с ножными мышцами как у кенгуру и быстротой колибри это невозможно."
    n "Потому что для выполнения пинка требуется сначала разогнаться, затем сделать прыжок на высоту несколько выше цели, в полёте перевернуться подошвами в сторону головы цели, более-менее сохранив импульс и вектор движения, точно попасть в заданную цель обеими ногами, сгруппироваться, чтобы приземлиться на обе ноги после поражения цели... Словом, лучше не пытайтесь.\n{w=5.0}На практике удар из-за вышеописанных сложностей полезен исключительно на десантной показухе."
    nvl clear
    n "{b}Онигири{/b}."
    n "{nw}"
    n "Очень распространённое в Японии угощение. Состоит из риса, сжатого ладонью в более-менее округлый комочек. Важно не сдавить его слишком сильно, иначе будет невкусно."
    n "Внутрь кладётся начинка, комочек оборачивается листом водоросли."
    nvl clear
    n "{b}Список Мишлен{/b}."
    n "{nw}"
    n "«Красный путеводитель Мишлен», который ведёт французская автомобильная компания Мишлен. Представляет собой карту различных местечек, созданную для автомобильных путешественников."
    n "Попасть в него — весьма круто. Три звезды — совсем круто."
    nvl clear
    n "{b}Монолог учительницы{/b}."
    n "{nw}"
    n "{b}Ашока Великий{/b} — индийский царь. {b}Великие речные державы{/b} — по убеждениям чужеземных историков, первыми достигшие величия (оседлав плодородные реки) цивилизации — Китай, Индия, Египет, Месопотамия."
    n "{b}Капилавасту{/b} — столица одной из древних индийских династий. {b}Куркума{/b} — жёлтый краситель для карри."
    nvl clear
    n "{b}Табаско{/b}."
    n "{nw}"
    n "Очень острый мексиканский соус на основе кайенского перца."
    n "Ну а то из чего ещё делают острые соусы."
    nvl clear
    show mion se def_a2 at sleva
    show satoko se aku_a1 at sprava
    with dissolve_04
    n "\"Не понимаю, как она может постоянно его есть.\""
    n "\"Ваша правда, Мион-сан, карри такое невкусное!\""
    $ renpy.pause(0.2)
    show chie si_maji at central behind mion with down
    show mion se bik_a1
    show satoko se hn_a1
    with dissolve_02
    n "\"Карри!\""
    play sound wa_005
    $ renpy.pause(0.3)
    play sound wa_030
    show ryuuketu with ryuuketu_efe
    hide mion
    hide satoko
    hide ryuuketu
    show chie si_def
    with Dissolve(1.0)
    n "\"Карри~{font=DejaVuSans.ttf}☆{/font}...\""
    nvl clear
    if persistent.matsuri:
        show inverse_chie si_maji at central as chie:
            0.5
            linear 0.2 xalign 0.5 yalign 0.1 zoom 3.0
        with dissolve_02
        $ renpy.pause(0.5, hard=True)
        play sound wa_005
    scene black with Shake((0, 0, 0, 0), 1.0, dist=30)
    call screen translation_notes
    return
