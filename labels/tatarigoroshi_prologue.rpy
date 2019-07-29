    $ save_name = "Глава о Смертоносном Проклятии.\nПролог"
    $ mouse_visible = False
    $ _game_menu_screen = None
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black
    $ renpy.pause(2.0)
    play music nageki_musicbox
    scene si_tatarigorosi with dissolve_02
    $ renpy.pause(20.0, hard=False)
    if persistent.matsuri:
        scene black with Dissolve(4.0)
        show text "{font=times.ttf}В стремлении защищать не было лжи.{/font}" at truecenter with Dissolve(1.0)
        play sound tata001
        $ renpy.pause(2.5)
        hide text with Dissolve(1.0)
        show text "{font=times.ttf}Желанию ценить и беречь не должно было быть равных.{/font}" at truecenter with Dissolve(1.0)
        play sound tata002
        $ renpy.pause(3.5)
        hide text with Dissolve(1.0)
        show text "{font=times.ttf}Но заботливость породила тёмное чувство,\nставшее жаждой убийства,{/font}":
            xalign 0.5 yalign 0.45
        with Dissolve(1.0)
        play sound tata003
        $ renpy.pause(5.0)
        show text "{font=times.ttf}и когда-то белоснежные мысли\nокрасились в красный и чёрный.{/font}" as text2:
            xalign 0.5 yalign 0.6
        with Dissolve(1.0)
        $ renpy.pause(4.5)
        hide text
        hide text2
        with Dissolve(1.0)
        show text "{font=times.ttf}При этом он понимал, что разрушает мирную жизнь,{/font}":
            xalign 0.5 yalign 0.45
        with Dissolve(1.0)
        play sound tata004
        $ renpy.pause(2.5)
        show text "{font=times.ttf}которую хотел уберечь.{/font}" as text2:
            xalign 0.5 yalign 0.55
        with Dissolve(1.0)
        $ renpy.pause(2.0)
    scene chapter 3 with Fade(3.0, 0.5, 1.0)
    play sound tata005
    $ renpy.pause(2.0)
    scene chapter tata_1 with Dissolve(2.0)
    $ renpy.pause(0.5)
    scene chapter tata_2 with Dissolve(2.0)
    play sound tata006
    $ renpy.pause(2.0)
    scene black with Dissolve(1.0)
    if persistent.matsuri:
        show text "{font=times.ttf}Что же пошло не так?{/font}" at truecenter with Dissolve(1.0)
        play sound tata007
        $ renpy.pause(0.5)
        hide text with Dissolve(1.0)
        show text "{font=times.ttf}В поисках ответа трагедия идёт дальше.{/font}" at truecenter with Dissolve(1.0)
        play sound "sound/tata008.ogg"
        $ renpy.pause(4.5)
        hide text with Dissolve(2.0)
        $ renpy.pause(2.0)
    scene tyuui_disclaimer with Dissolve(1.0)
    scene black with Dissolve(4.0)
    scene tyuui_s58 with Dissolve(1.0)
    scene black with Dissolve(4.0)
    $ _game_menu_screen = "game_menu"
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ renpy.pause(3.0)
    $ mouse_visible = True
    play ambient lsys12
    scene white with m1_03
    scene bg 203 with up
    n "Жара..."
    nvl clear
    n "Даже малейшего ветерка нет... и мало жарищи, так ещё и лето выдалось на редкость влажное."
    n "На многих окнах висит, просушиваясь, бельё, но свежестью от него не веет — наоборот, его унылый вид раздражает."
    nvl clear
    scene black with fastdown
    n "С обеих сторон улочку обступили скособочившиеся частные домишки вперемежку с невысокими многоквартирными."
    n "{nw}"
    n "И без того узенькая дорога становилась ещё уже, муторнее и жарче от клумб и горшков с никнущими цветами, от велосипедов, мотороллеров и мотоциклов."
    nvl clear
    n "Никому бы не захотелось побывать в подобном местечке в такое время."
    n "...И всё же как раз тогда, после обеда, по дороге проехал мотоцикл..."
    nvl clear
    scene bg 133 with fastup
    n "Он затормозил у двухэтажного многоквартирного дома, который даже из лести нельзя было назвать ухоженным."
    nvl clear
    n "С мотоцикла слез мужчина весьма почтенного возраста. Лицо его избороздили морщины."
    n "...Приметив его, развешивавшая бельё хозяйка поздоровалась."
    nvl clear
    n "\"А-а, здоровенько-о!"
    extend " Страх жарко-то нонче, ага?\""
    n "\"Да-а, есть такое дело!"
    extend " Мене будто прям живьём варять."
    extend " Хе-хе-хе!\""
    nvl clear
    n "\"Ах да, гражданин управляющий,"
    extend " я вам кой-шо сказать хотела.\""
    n "\"Ээээ, да-да, знаю, знаю!"
    extend " Ртутные светильники, так?"
    extend " Совсем запамятовал!"
    extend " Э-хе-хе!\""
    n "\"Та ни, вы шо, не слышите?"
    extend " С самого утра"
    extend " чем-то несёт, я уж не можу больше.\""
    n "\".........Ох, ну и ну."
    extend " И верно, шо за вонь!"
    extend " Видать, канал-от опять засорился.\""
    nvl clear
    n "\"Будьтя ласка, сделайте шо-нить."
    extend " С утра нос коробится.\""
    n "\"Хе-хе-хе!"
    extend " Ну, вы от того токмо красивше выйдете, хе-хе-хе!\""
    nvl clear
    scene black with left_03
    n "Позади дома шла сточная канава."
    n "{nw}"
    n "Её решётку забивали опавшие листья и ветки, собиравшие собой мусор и летом жутко вонявшие."
    nvl clear
    n "\"Вот, можа, побалакаете с чановниками об этом?"
    extend " Нехай вообще усю канаву закапывают!\""
    n "\"Н-да-а."
    extend " Решётку совсем забило."
    extend " Палкой бы какой потолкать, глядишь, снова вода пойдёт.\""
    n "{nw}"
    n "Мужчина перебрался через заборчик, ограждавший канаву, и поднял с земли валявшуюся рядом палку для развешивания белья."
    n "Никак, попробует расчистить ею решётку."
    nvl clear
    scene bg 203 with dissolve_04
    n "\"Э-эй, э-эй, постойте!"
    extend " Оно ишшо сильнее вонять почнёт,"
    extend " ежли разворошить!\""
    n "\"Э-хе-хе, дак оно воняет и кады забивает канаву, и коли его шевелить."
    extend " Шо ж мене остаётся?"
    extend " Хе-хе-хе!\""
    n "Он ткнул палкой в кучу мусора, скопившуюся у решётки."
    n "......Нечего и говорить, что с накопившимся мусором от этого ничего не сделалось."
    nvl clear
    n "\"О-ох..."
    extend " Гляньте-ко, мёртвая кошка."
    extend " Надоть отдел охраны здоровья сюды привлечь.\""
    n "\"Мёртвые кошки-собачки дюже на вонь здоровы..."
    extend " Не знаю, шо тут с одной палкой поделаю.\""
    nvl clear
    n "\"Эвона понакидали — мусорные мешки, одёжка старая..."
    extend " Ишшо и горшок-уточка для детишков?"
    extend " ...Таперь понятно, чего такая вонища."
    extend " Шо ж за люди-то!\""
    nvl clear
    scene black with dissolve_04
    n "Какая разница — добавить мусора, не добавить, — канал и так уж давно как помойка."
    n "{nw}"
    n "...Многие нерадивые люди так думают, вот благодаря им канава и стала помойкой."
    nvl clear
    n "Палка ткнулась в кучу старых вещей, плававшую в грязной водице, и та, испустив облачко чёрного дыма, немного разошлась."
    n "{nw}"
    n "От открывшегося взору непонятного и жуткого зрелища оба непроизвольно нахмурились..."
    nvl clear
    n "\"О-о... глядитя-ка, личинки так и кишать."
    extend " Верно, еду кто-то выкинул...\""
    n "\"Ох...... г-гражданин управляющий..."
    extend " Ш-што там такое?\""
    nvl clear
    n "\"Э, шо только не выбрасывають......\""
    n "\"......В-вы... вы поглядите... это же!!.....\""
    play music lsys28
    n "\"М-м{w=1.0}......... Ох.{w=0.8} ......ОООООО-О-О-ОХ ЖЕЕЕ Ж!!\""
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    play sound wa_013
    scene white with fade_010
    scene bg 133 with dissolve_04
    play sound wa_013
    $ renpy.pause(0.2)
    play sound wa_013
    $ renpy.pause(0.15)
    play sound wa_013
    $ renpy.pause(1.5, hard=True)
    play sound wa_013
    $ renpy.pause(0.1)
    play sound wa_013
    $ renpy.pause(0.2)
    play sound wa_013
    $ renpy.pause(0.15)
    play sound wa_013
    play ambient lsys12
    n "\"А, проходите!"
    extend " Здравия желаю.\""
    n "\"Ох-х, ну и вонища!"
    extend " Эй!"
    extend " Сверху тоже простынкой накройте!"
    extend " Со второго этажа всё видно!\""
    nvl clear
    n "\"Личность пока не установили."
    extend " Пол женский."
    extend " Возраст — от двадцати пяти до сорока."
    extend " Предполагаю, скончалась два-три дня тому назад."
    extend " \nА потом кто-то бросил её труп сюда.\""
    n "\"Причём голой."
    extend " Да уж, легко мы её не опознаем."
    extend " Посмотрите, не приходило ли в управление жизнеобеспечения объявление о пропаже.\""
    nvl clear
    n "\"Скорее всего, в канал её скинули с привязанным грузом."
    extend " Похоже, груз отвязался, вот она и всплыла."
    extend " ...Только почему её решили кинуть сюда, в сточную канаву?"
    extend " Могли бы и получше-то место выбрать — где-нибудь под автострадой, ну, в горах, что ли.\""
    n "\"Хочешь сказать, лучше бы тело нашли не на нашем участке?"
    extend " Ну, кто бы это ни совершил, прятать тело точно не собирался.\""
    nvl clear
    n "\"Значит, убийца {i}рассчитывал{/i}, что тело найдут, — хотел преподать кому-то какой-то урок?\""
    nvl clear
    scene black with dissolve_04
    n "\"У неё живот разодран, и я не думаю, что здесь водится настолько зубастая рыба."
    extend " Кто-то вспорол ей живот и вытащил внутренности."
    extend " Перед убийством её жестоко пытали."
    extend " Прямо как старые порядки китайской мафии, правда?"
    extend " Поспрошай Сигэ-сана из четвёртого отдела, не знает ли он о каких волнениях, связанных с бандами.\""
    n "\"Есть!\""
    nvl clear
    n "\"Всё-таки... вот уж труп так труп."
    extend " Поглядите-ка на эти кишки, они вам не напоминают о салате в Кёя?"
    extend " Вон, глянь-ка, оттуда словно лапша вылезет, если палочками поворошить, не так ли?\""
    scene ryuuketu with efe_aa
    n "\"......М-м!"
    extend " П-пожалуйста, перестаньте...\""
    nvl clear
    n "\"Кха-ха-ха-ха!"
    extend " Итак, живот выпотрошен, уши с носом отрезаны."
    extend " Никому бы не понравилось так умирать."
    extend " А особенно неприятный видок у пальцев."
    extend " По нескольку здоровых гвоздей в каждом пальце на обеих руках."
    extend " Что ж это за пытка такая?\""
    nvl clear
    scene black with Fade(0.07, 0.01, 0.02)
    show title at truecenter
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    $ renpy.pause(3.0)
    scene black with Dissolve(5.0)
    $ renpy.pause(2.0)
    jump tata_day01
