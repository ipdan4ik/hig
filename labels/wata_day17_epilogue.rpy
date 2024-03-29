    $ save_name = "Глава о Хлопковых Корабликах.\nЭпилог. Конец происшествия"
    scene black
    t "\n\n\n\n{space=120}28 июня 58 года эры Сёва.{w=2.0}{nw}"
    t "{nw}"
    t "В деревне Хинамидзава, входящей в состав города Шишибонэ префектуры XX, произошло нападение с причинением тяжкого вреда здоровью.{w=2.0}{nw}"
    nvl clear
    scene bg 120 with Dissolve(1.0)
    t "\nПострадал Маэбара Кейти, ранее выживший в происшествии с несколькими пропавшими без вести.{w=2.0}{nw}"
    extend "\n{nw}"
    t "Около двух часов утра его ударила ножом в живот подозреваемая в упомянутом происшествии с пропавшими без вести (Сонодзаки Мион), пришедшая к его дому.{w=2.0}{nw}"
    extend "\n{nw}"
    t "Семья обнаружила его утром, после чего сразу же доставила его в клинику.{w=2.0}{nw}"
    extend " Жизнь пострадавшего удалось спасти.{w=2.0}{nw}"
    t "{nw}"
    t "Подозреваемая сбежала с места преступления.{w=4.0}{nw}"
    nvl clear
    scene bg 131 with Dissolve(1.0)
    t "\n\n\n\n{space=80}Примерно в то же время того же дня.{w=2.0}{nw}"
    t "{nw}"
    t "С балкона одного из высотных домов частного владения в Камииссики, что в городе Шишибонэ префектуры XX, произошло падение жилицы.{w=2.0}{nw}"
    extend "\n{nw}"
    t "Пострадала Сонодзаки Шион, ранее выжившая в происшествии с несколькими пропавшими без вести.{w=4.0}{nw}"
    nvl clear
    t "\nПоздней ночью сосед по лестничной клетке услышал доносившуюся из её квартиры громкую перебранку жертвы с кем-то, после чего уведомил вахтёра.{w=2.0}{nw}"
    t "{nw}"
    t "Вахтёр, открыв своим ключом дверь, обнаружил, что жертва разбилась насмерть, упав с балкона восьмого этажа.{w=4.0}{nw}"
    nvl clear
    scene black with Dissolve(1.0)
    t "Комната была в беспорядке — похоже, в ней произошла драка.{w=2.0}{nw}"
    t "{nw}"
    t "По словам соседа, хорошо и давно знавшего семью Сонодзаки, доносившиеся из квартиры звуки ударов и взаимная ругань были точь-в-точь такими же, как если бы сёстры друг с другом ссорились.{w=2.0}{nw}"
    t "{nw}"
    t "Полиция усматривает в данном происшествии некую связь с нападением, произошедшим в Хинамидзаве той же ночью,{w=2.0}{nw}"
    extend " однако же обыск жилого помещения не выявил никаких следов кого-либо помимо жертвы.{w=4.0}{nw}"
    nvl clear
    t "\nЖертва упала в посаженный под балконом кустарник.{w=2.0}{nw}"
    extend " От перелома шеи смерть наступила мгновенно.{w=2.0}{nw}"
    t "{nw}"
    t "Её одежда оказалась мятой, со следами борьбы.{w=2.0}{nw}"
    t "{nw}"
    t "Однако, учитывая её душевное состояние после предыдущего происшествия, также рассматривается возможность самоубийства на почве нервного потрясения.{w=2.0}{nw}"
    t "Полицией отрабатываются обе версии — как самоубийства, так и уголовного преступления...{w=4.0}{nw}"
    nvl clear
    show cinema with x_15
    show title02 with Dissolve(3.0)
    $ renpy.pause(2.0)
    show black behind title02 with Dissolve(3.0)
    $ renpy.pause(1.0)
    scene black with right
    stop music fadeout 1.0
    play ambient lsys12
    scene bg 132 with Dissolve(1.0)
    $ renpy.pause(2.0)
    scene bg 186 with Dissolve(1.0)
    n "\"Всего лишь на пять минут, хорошо?"
    extend " Только не надо его волновать, пожалуйста.\""
    n "\"Угу, угу. Знаю.\""
    nvl clear
    n "Лязг."
    n "Дверь открылась... и, не обманув ожиданий, зашёл Ооиси-сан."
    nvl clear
    stop ambient fadeout 1.0
    show ooishi si wa_a1 at central with dissolve_04
    play music msys06
    n "\"Дообрый деень, добрый дееень, Маэбара-сан."
    extend " Давненько же мы не виделись."
    extend " Как поживаете?\""
    n "\"......Ну, врач говорит, что поправляюсь я после операции не по дням, а по часам... только вот погляжу на вашу рожу, и рана хуже затягиваться начинает.\""
    n "\"Н-а-ха-ха-ха-ха-ха! Сурово ты, брат.\""
    nvl clear
    n "Ооиси-сан, басовито похохатывая, вручил маме пакетик сладостей — явно купленных в магазинчике для передачек, что на первом этаже больницы."
    nvl clear
    show ooishi si def_a1 with dissolve_02
    n "\"Премного прошу простить, милейшая,"
    extend " но не мог бы я немного потолковать с вашим Кейти-куном?\""
    n "{nw}"
    n "Мамане явно не нравилось, что полиция хочет говорить с её сыном без присутствия родителей."
    n "Однако я тоже сказал ей......"
    nvl clear
    n "\"Мам,"
    extend " извини, мы недолго."
    extend " За пять минут управимся.\""
    n "Она с неохотой вышла."
    n "{nw}"
    n "Когда дверь закрылась, Ооиси-сан, усмехаясь, оглядел палату."
    nvl clear
    show ooishi si wa_a1 with dissolve_02
    n "\"Экая роскошь — лежать в личной палате!"
    extend " Моя-то старушка всегда лежит с кем-то ещё, знаете?"
    extend " Ну, и веселее там тоже, да."
    extend " Видать, в таких заведениях тяжесть болезни определяет твоё положение."
    extend " Чем серьёзнее ты нездоров, тем больше тебе почёта...\""
    nvl clear
    n "\"Пять минут, Ооиси-сан."
    extend " И, надеюсь, они станут последними пятью минутами."
    n "......К Хинамидзаве я больше никак не отношусь... да и не в Хинамидзаве-то мы.\""
    n "\"Ну конечно, в Окиномии же нет общей больницы......"
    extend " Не позволите ли мне присесть?.."
    extend " Ох-хо.\""
    nvl clear
    n "Мы находимся в большой университетской клинике города Шишибонэ."
    n "{nw}"
    n "И потрясающий, скажу вам, город — совсем не то, что Хинамидзава с Окиномией."
    n "С трудом верится, что Хинамидзава — его же частичка."
    nvl clear
    show ooishi si def_a1 with dissolve_02
    n "\"Когда же вы собираетесь переехать?\""
    n "\"Кто знает..."
    extend " Лично мне всё равно, я всегда готовый.\""
    n "{nw}"
    n "Из-за моего ранения переезд слегка откладывается."
    n "Правда, родители уже выехали из дома в Хинамидзаве — под новой крышей теперь живут."
    n "А я тоже переберусь потом — дай только получше окрепнуть — в больницу моего нового города."
    nvl clear
    n "\"...Прошу не навещать меня в новой больнице."
    extend " Мне действительно хуже становится.\""
    n "\"Эх... неужто я так не мил?"
    extend " Ну, что поделать, приходится по долгу службы."
    extend " Ладно, чтоб искупить вину, я вам принёс нынче кое-что славное.\""
    nvl clear
    n "\".........Печенье можно было и не приносить.\""
    n "\"В общем-то..."
    extend " Там внутри не печенье."
    extend " Погля~ди~те-ка!\""
    nvl clear
    n "Ооиси-сан открыл жестянку с печень{cps=4.0}......{/cps} С ЧЕЕЕМ?!"
    extend " Оооххх, шрам растянулся..."
    nvl clear
    show ooishi si wa_a1 with dissolve_02
    n "\"Не знал, каковы предпочтения Маэбары-сана, посему пришлось принести кучу всякого-разного."
    extend " Тут на любой вкус найдётся — от взрослых заокеанских комиксов до довольно-таки даже милых!"
    extend " Надо же, нынче и такое рисуют. На девочек, видать, рассчитано.\""
    n "\"Ннн-не-не-не п-приносите сюда всякую порнографию, прошу вас!!!"
    extend " С собой её заберите, с собооой!!"
    extend " Оооооххххх!!...\""
    nvl clear
    n "\"Мм-хм-хм-хм!"
    extend " Молодому, здоровому парню, да чтоб сидеть столько в неволе, — подумал, сподручно будет."
    extend " Хотя, может, вы нынче к медсёстрам неровно дышать стали?"
    n "Но поймите, в мире куда больше прекрасного, чем одни медсестрички!"
    extend " Не зацикливайтесь на одном, шире мыслью летите!"
    extend " Будьте же многосторонни."
    extend " Мм-хм-хм-хм-хм-хм!!\""
    nvl clear
    n "В ответ непристойному смеху Ооиси-сана я криво усмехнулся."
    n "...Но сам знал."
    n "{nw}"
    n "Когда Ооиси-сан заводит разговор в таком духе{w=1.0}...... значит, рассказать собирается что-то важное."
    nvl clear
    stop music fadeout 1.0
    play ambient lsys12
    show ooishi si def_a1 with dissolve_02
    n "\".........Искренне сожалею насчёт Шион-сан.\""
    n "\"..........................................\""
    nvl clear
    n "В ту же ночь, как Мион ткнула меня ножом."
    n "Шион разбилась насмерть, упав с балкона."
    n "{nw}"
    n "Полицейские сказали, что расследуют все возможности — несчастного случая, самоубийства и убийства... хотя ничем, кроме работы Мион, оно быть не могло..."
    n "{nw}"
    n "Мион узнала, где прячется Шион... и убила, столкнув с балкона."
    extend " Об ином я и не задумываюсь."
    nvl clear
    n "\".........Никакой то не случай."
    extend " ......Мион её столкнула."
    extend " ...Точно.\""
    n "\"......Наши следователи говорят, что всё указывает на самоубийство. Но я разделяю вашу точку зрения, Маэбара-сан."
    extend " Она столкнула Шион-сан и пропорола вам живот"
    extend " за одну ночку.\""
    n "\"{cps=*0.4}..................{/cps}Мион{w=1.0}... ещё не нашли?\""
    nvl clear
    n "\"Ах да."
    extend " Я ж зачем пришёл-то..."
    extend " Да."
    play sound wa_024
    extend " Вот именно, что нашли.\""
    n "\"ЧТО-О?!"
    extend " .........Ой-ёй-ёй-ёй...\""
    nvl clear
    n "Какое-то... странное ощущение."
    n "{nw}"
    n "Вроде и рад я, что дело наконец-таки действительно кончилось... но в то же время — жаль, что лучшего друга в конце концов поймали."
    extend " И ещё самые разные чувства переполняют меня..."
    extend " Сложное, короче, ощущеньице."
    nvl clear
    show ooishi si wa_a1 with dissolve_02
    n "\"И не только."
    extend " В подземном доме семьи Сонодзаки..."
    extend " мы нашли потайной колодец."
    n "Как вы и сказывали, тела всех жертв оказались на его дне.\""
    n "\"..................Вот{w=0.8}...... значит, как...\""
    n "{nw}"
    n "Доныне я душой и сердцем надеялся, что Рика-тян и Сатоко, может быть, живы ещё, раз их тела не нашли... Теперь...{w=1.0} надежды не стало."
    nvl clear
    scene bg 196 with Dissolve(1.0)
    n "\"Запрятали его, надо сказать, с умом."
    extend " Нет, скажем так, в самой непросматриваемой точке слепого пятна."
    n "Отвесный туннель, весьма-таки похожий на колодец."
    extend " Лестница во всю длину, а почти в самом низу — горизонтальное ответвление."
    extend " Проползёшь пару сотен метров на карачках, и — нате вам! — выход наружу через древний колодец в горах.\""
    nvl clear
    scene bg 186
    show ooishi si wa_a1 at central
    with Dissolve(1.0)
    n "\".........Полагаю, тайный подземный ход, сделанный для побега кого-то из предыдущих глав семьи Сонодзаки.\""
    n "\"Видимо, так и есть..."
    extend " Сделали, думаю, где-то после начала эпохи Мэйдзи."
    extend " Да уж... продуманность впечатляет.\""
    nvl clear
    n "\"{cps=*0.6}...............{/cps}Тела.........{w=0.8} нашлись внизу?..\""
    show ooishi si def_a1 with dissolve_02
    n "\"Да."
    extend " Ниже ответвления — лужа густой, как дёготь, грязи."
    extend " Трупы туда просто скидывали."
    n "Сбрасывали с приличной высоты, так что тела полностью зарывались в грязь..."
    extend " Нелегко было поднять их оттуда.\""
    nvl clear
    n "\"{cps=*0.6}..............................{/cps}Вы нашли{w=0.8} всех?\""
    n "Я надеялся... хотя бы Рику-тян и Сатоко там не найдут."
    n "{nw}"
    n "Надеялся что было силы, но с его следующими словами надежда мигом погибла."
    nvl clear
    n "\"Да."
    extend " Всех."
    extend " Честно говоря, мы нашли даже такие кости, которые там лежали уже с целый десяток лет."
    extend " Костей там хватит по крайней мере на троих."
    extend " ......Вот тебе и тёмная сторона прошлого Хинамидзавы."
    extend " И кто знает, сколько ещё найдём, когда выкопаем всю грязь..."
    extend " Подумать жутко......\""
    n ".........И весь этот груз Мион взвалила на плечи......"
    n "{nw}"
    n ".........Мион{w=2.0}................................."
    nvl clear
    n "\"Мы пересматриваем все дела о пропавших без вести в Шишибонэ за несколько десятилетий."
    extend " Может быть, закроем наконец кучу нерешённых дел.\""
    n "\"............................\""
    n "{nw}"
    n "Помолчавши...... я тяжело вздохнул..."
    nvl clear
    n "Ооиси-сан потянул было из пачки сигарету, но вспомнил, что здесь не курят, и со вздохом убрал её в нагрудный карман."
    nvl clear
    n "\"Кстати..."
    extend " Есть у меня к вам попутный вопрос......"
    extend " Вы ведь знали Фурудэ Рику-сан?\""
    n "\"Ясен пень......"
    extend " Дружили же.\""
    n "\"Вы не слыхали, чтоб ей приходилось делать частые уколы — инсулина, скажем, от диабета?\""
    n "............Чё??......"
    extend " Рика-тян — диабетичка???"
    extend "\nО чём он?"
    nvl clear
    scene black with fastdown
    show sepia_rika se de_a1 at sleva with left_03
    n "\"Видите ли, у неё в кармашке юбки"
    play sound wa_026
    extend " нашёлся шприц."
    extend " Он разбился, поэтому мы не смогли определить, \nиз-под чего тот."
    extend " ......Но нам стало любопытно — \nчто же он делал в её кармане-то."
    extend " Вам точно ничего не известно?\""
    n "{nw}"
    n "......Никогда не слышал, чтоб Рика-тян таскала с собой шприц."
    nvl clear
    n "\"Семья Сонодзаки занимается{w=1.0}... ай, в общем, якудза они."
    extend " Так вот, ходит слух, приторговывают они психостимулирующими наркотиками."
    extend " Вот и подумалось — а нет ли тут какой-нибудь связи.\""
    n "\".........Хотите сказать... Рика-тян употребляла наркотики?!...\""
    nvl clear
    n "\"Нет-нет... Ни в коем случае."
    n "...Просто, видите ли, не совсем понятно, зачем ей шприц, коли она шла за соевым соусом.\""
    n "...............Ничего...... не понимаю..."
    n "{nw}"
    n "Голова закружилась..."
    extend " Тошнит..............."
    nvl clear
    scene black with Dissolve(1.0)
    scene bg 186 with Dissolve(1.0)
    show ooishi si def_a1 at central with left_03
    n "\"Вам нехорошо?"
    extend " Позвать медсестру?\""
    n "\"Н...... нет, я в порядке."
    extend " ......Досказывайте...\""
    n "\"Ну, по шприцу более рассказать нечего."
    extend " Исключительно в личных целях полюбопытствовал.\""
    n "{nw}"
    n "...............Рика-тян..."
    nvl clear
    n "\"...Как понимаю, Рика-сан почиталась в деревне за талисман,"
    extend " поэтому там сейчас беспокойно."
    extend " Старики, слепо верившие в её святость, едва ль не порвать готовы семью Сонодзаки за убийство."
    n "...Да и от госанке, правивших твёрдой рукой, практически ничего не осталось."
    n ".........Всплыви сейчас разговор о постройке плотины — и на сей раз деревня не сдюжит.\""
    n "\"......Я с Хинамидзавой... больше никак не связан.\""
    nvl clear
    n "Что не совсем правда."
    n "Я, надеясь оборвать разговор, сказал так лишь потому... что не хотел ничего слышать об опустении Хинамидзавы."
    nvl clear
    n "Стук в дверь."
    nvl clear
    n "Приоткрывши дверь, мама поинтересовалась, наговорились ли мы."
    nvl clear
    show ooishi si wa_a1 with dissolve_02
    n "\"Ох же ж!"
    extend " Вот заговорился-то!.."
    extend " Ну и дела!\""
    n "...............Я поглядел на часы."
    extend " Пять минут уже давно как прошли."
    n "{nw}"
    n "Но всё же мне надо было кое о чём его расспросить, и я сказал матери подождать ещё чуть."
    nvl clear
    n "\"......Вот как?"
    extend " Только быстро.\""
    n "Очевидно, мать не переставала ломать голову, что же такое надо полиции от её мальчика."
    nvl clear
    show ooishi si def_a1 with dissolve_02
    n "\".........Может, мне как-нибудь потом прийти...\""
    n "\"Эмм... Ооиси-сан..."
    extend " Мион.........{w=1.0} как там она?..\""
    n "Как ответит, сразу же попрошу его покинуть палату."
    nvl clear
    n "\"..................Прежде чем расскажу, Маэбара-сан,"
    extend " хотел бы получить от вас честный ответ на один вопрос.\""
    n "\"......Что за вопрос?\""
    nvl clear
    show ooishi si wa_a1 with dissolve_02
    n "\"...............Отвечайте только со всей серьёзностью."
    extend " Ляпнете что-нибудь неумное — могу расценить как воспрепятствование ходу расследования.\""
    n "...И опять Ооиси-сан решил-таки мне угрожать."
    n "{nw}"
    n "Что же у него за вопрос такой......"
    nvl clear
    show ooishi si def_a1 with dissolve_02
    n "\"......Маэбара-сан..."
    extend " Кто, по-вашему, столкнул Шион-сан с балкона?\""
    n "\"..............................Мион, само собой, кто ж ещё-то?\""
    n "\"Тогда кто ткнул вас ножом?\""
    n "\"..............................Да сколько раз мне вам повторять?....."
    extend " Мион же......"
    extend " Сонодзаки Мион.\""
    nvl clear
    n "......С кривой усмешкой Ооиси-сан вытер платком выступившую на лбу испарину."
    n "Похоже, ждал он именно таких слов, однако радости они ему не доставили."
    nvl clear
    n "\"Она скинула Шион с балкона и ткнула меня ножом."
    extend " Ооиси-сан, вы же сами сказали только что — Мион виновата.\""
    nvl clear
    n "\"...Основание считать её убийцей Шион-сан одно — показания того соседа."
    n "А он, кстати, входит в бандитскую группировку Сонодзаки. Проще говоря, он был у Шион-сан за телохранителя."
    extend " Знал сестёр Сонодзаки с младенчества и относится к ним с большим сочувствием.\""
    nvl clear
    scene black with down
    n "По его, соседа, словам..."
    n "{nw}"
    n "Из-за стены доносился шум, очень похожий на тот шум, какой подымали сёстры, когда они, ещё живя вместе, часто ссорились."
    extend " ......Впрочем, нет, шум был как раз тот же самый."
    n "{nw}"
    n "Он услышал, что Мион да Шион ругаются и дерутся."
    nvl clear
    n "Поначалу он не обращал внимания, думая, что пострадавшая бредит."
    n "{nw}"
    n "......Всё-таки такой шум она каждую ночь подымала."
    n "{nw}"
    n "Однако той ночью гам долго не прекращался, и он решил дать ей успокоительного."
    nvl clear
    n "К тому времени, как пришёл вахтёр с ключом, гомон успел затихнуть."
    n "Но, подумав, что надо бы всё-таки её проверить, он позвонил в дверь и, когда ответа не последовало, решил всё-таки зайти без разрешения."
    nvl clear
    n "Комната оказалась в беспорядке."
    n "...Шион лежала на земле под балконом, вот он и подумал, что Мион её скинула..."
    extend " Как-то так вот."
    nvl clear
    scene bg 186
    show ooishi si def_a1 at central
    with fastdown
    n "\"В общем, он только слышал то, что доносилось из-за стены."
    extend " А в том доме, к слову, почти никто не живёт из-за рода деятельности хозяев,"
    extend " так что возню слышал он один."
    extend " ......И, вдобавок, Сонодзаки Мион совершенно никто не видел.\""
    n "\"Не видел...... да какая разница, ясно же, что Мион виновата!..\""
    nvl clear
    show ooishi si wa_a1 with dissolve_02
    n "\"Ну, ну..."
    extend " Так вот, что я хочу сказать-то..."
    extend " \nВы — единственный, кто несомненно видел Сонодзаки Мион той ночью."
    extend " Потому как другая свидетельница, Шион-сан, мертва.\""
    n "\".........Ооиси-сан, я вас{w=0.8} не понимаю...\""
    nvl clear
    n "Ооиси-сан примолк."
    nvl clear
    n "По-видимому, он позабыл, что тут запрещено курить, потому как вновь достал сигарету из пачки."
    n "Щёлкнул зажигалкой, подпалил сигарету......"
    extend " Выдохнул сизое облако..."
    nvl clear
    show ooishi si def_a1 with dissolve_02
    n "\".........Вы уверены, что вас пырнула ножом Сонодзаки Мион?\""
    n "\"Да."
    extend " ............Не сомневаюсь.\""
    n "\"..........................................\n.........................................\""
    n "{nw}"
    n "Исторгнутый Ооиси-саном дым поплыл по палате грозовой тучей, несомой ветром."
    nvl clear
    n "\".........Ооиси-сан, здесь нельзя курить..."
    extend " Медсёстры рассердятся.\""
    nvl clear
    scene black with dissolve_04
    stop ambient fadeout 1.0
    n "\"Вообще-то Сонодзаки Мион{nw}"
    $ renpy.pause(1.5)
    play sound wa_026
    extend "... тоже лежала на дне колодца.\""
    play ambient lsys15
    n "\"...............Э...\""
    nvl clear
    n "\"Разбилась насмерть."
    extend " Оступилась, видимо, при побеге, спускаясь по лестнице,"
    extend " полетела вниз"
    extend " и погибла от перелома шеи."
    extend " Да."
    extend " Точно так же, как и Шион-сан."
    extend " Сломала шею.\""
    n "\"......Ну... и......{w=1.0}............... а?.....\""
    nvl clear
    scene bg 196 with dissolve_04
    n "\"В тот день Сонодзаки Мион, после того как вас вырубила, попыталась сбежать через потайной колодец..."
    extend " Где, оступившись, погибла."
    n "...Словно бы все мертвецы внизу тянули её за ноги.\""
    n "\"{cps=*0.4}...........................{/cps}Как-то{w=0.8}...... не вяжется...\""
    nvl clear
    n "\"Вскрытие безоговорочно подтвердило — так и есть, умерла в тот же день."
    n "И она не возвращалась туда после того, как напала на тебя и на Шион-сан."
    play sound wa_023
    extend " ......Ведь она уже была мертва.\""
    n "{nw}"
    n "Челюсть моя отвисла...... и так и осталась."
    n "......Да быть... не может..."
    n "......Меня же Мион ударила...... да, самая настоящая Мион."
    n "......Ну да...... никто же больше не мог............"
    nvl clear
    scene black with dissolve_04
    n "\"Т{w=0.8}...... тогда...{w=0.6}{nw}"
    extend " к-кто напал на меня с Шион?!..."
    extend " КТО?!!.....\""
    n "\"Вас ударила...... Сонодзаки Мион, {b}которая на деле вовсе не Сонодзаки Мион{/b}. Вот кто.\""
    n "{nw}"
    n ".........Голова отказывается работать... Ничего не соображу..."
    nvl clear
    stop sound fadeout 1.0
    stop ambient fadeout 1.0
    play music mysterious
    n "\"......Помните ли вы, как погибла Такано Миё-сан?\""
    n "\"А?....."
    extend " Такано-сан?"
    extend " Ах...... да."
    n "......Слышал, её сожгли живьём где-то в горах...\""
    nvl clear
    show sepia_takano si_def at sprava with right_03
    n "\"По нашим сведениям, её сначала придушили, а потом только сожгли."
    extend " Вскрытие проводила полиция префектуры Гифу."
    extend " Но кое-что у них вышло странновато."
    n "Сначала вскрытие показало, что со времени смерти прошло двадцать четыре часа."
    extend " Они глянули, \nсмотрят — что за хрень? — ну, и тут же добавили ко времени смерти сутки, чтоб вышло, как будто та умерла тем днём.\""
    nvl clear
    n "......В деле Мион и так несуразицы более чем достаточно......"
    extend " Что ещё он...... хочет мне поведать?....."
    n "{nw}"
    n "............Вот никак я не понимаю запутанных речей Ооиси-сана..."
    nvl clear
    n "\"Только говорит мой знакомый старикан-судмедэксперт — те самые итоги вскрытия, по которым вышло, что умерла она двадцать четыре часа назад,"
    extend " есть штука, доверия очень даже достойная."
    extend " ......Что это значит?"
    n "Много же раз я вас про то спрашивал......"
    extend " но вы ж видели ночью Ватанагаси"
    extend " Такано Миё-сан?\""
    n "\".........Видел.\""
    nvl clear
    n "\"И на подготовке к фестивалю, что шла накануне вечером, вы её тоже встречали?"
    extend " Я сам вас тогда наблюдал.\""
    n "\"Ага......"
    extend " Встречал.\""
    nvl clear
    n "\"Если она правда погибла сутками ранее...{w=1.0} значит, в ночь перед фестивалем она уже была мертва.\""
    n "\".........Ха-ха{w=0.9}... да как такое...\""
    n "\"......Она была ещё жива в тот вечер, когда готовились к фестивалю."
    n "Но... когда вы вместе пробирались в хранилище{w=1.0}... Такано-сан в живых уже не было.\""
    nvl clear
    n "В самом начале."
    extend " Когда всё пошло-поехало."
    n "{nw}"
    n "Когда мы пробрались, о чём я впоследствии много раз пожалел... в Сайгудэн."
    n "Подговорила нас{cps=*0.6}.......................................{/cps} Такано-сан."
    n "{nw}"
    n "Когда она...... приглашала нас внутрь Сайгудэна......... её на свете...... уж не было..."
    nvl clear
    scene black with Dissolve(1.0)
    scene bg 186
    show ooishi si def_a1 at central
    with fastup
    n "\"Многовато у нас нынче летом трупов разгуливает..."
    extend " Н-а-ха-ха...\""
    n "{nw}"
    n "............Одна мёртвая начала дело{w=1.0}...... и другая{w=1.0}... его закончила."
    nvl clear
    stop music fadeout 1.0
    play ambient lsys11
    n "\"...От нас требуют, чтоб мы изменили время смерти Сонодзаки Мион на ту ночь, в которую она вас пырнула......"
    extend " По-видимому, некие заинтересованные личности пытаются замять дело как можно скорее..."
    extend " Так что, надеюсь, вы не вздумаете никому о нашем разговоре болтать.\""
    nvl clear
    n "Затушив сигарету о ботинок, Ооиси-сан поднял со стула свою куртку и замахал рукой, пытаясь развеять табачный дым."
    nvl clear
    n "\"Что-то я задержался..."
    n "Пришёл-то с желанием помочь вам покончить с делом......"
    extend " но, похоже, только напустил дыму.\""
    n "Искоса поглядывая на меня, ошеломлённо пялившегося перед собой, он пошёл ко двери."
    nvl clear
    n "\".........Если{w=1.0}... когда-нибудь захотите со мной поговорить, прошу звонить в любое время."
    extend " Моя визитная карточка — в банке с гостинцами."
    show ooishi si wa_a1 with dissolve_02
    extend " И тогда я приду к вам ещё раз... и снова принесу добрый подарок."
    extend " Мм-хм-хм-хм!\""
    n "{nw}"
    n "Ооиси-сан...... думает, что я всё ещё что-то скрываю."
    n "И что же... мне осталось... скрывать?.."
    n "Сам не знаю."
    extend " ...И хочу знать."
    nvl clear
    n "\"Что же, до встречи."
    extend " Берегите себя.\""
    nvl clear
    hide ooishi with Dissolve(2.5)
    n "Бах."
    nvl clear
    n "Слушая щелчки ботинок Ооиси-сана по коридору..."
    extend " я так и пребывал в ошеломлении."
    nvl clear
    scene black with Dissolve(1.0)
    n "Помочь мне покончить с делом?.."
    n "В каком смысле — покончить?"
    n "Ничего ж ещё не закончено."
    n "{nw}"
    n "...Дело...{w=0.8} до сих пор...{w=1.0} не окончено..."
    nvl clear
    stop ambient fadeout 1.0
    call toketu
    n ".........И тогда-то я увидал окровавленную руку...{w=0.6} высовывающуюся из-под кровати."
    n "{nw}"
    n "Не удивлён..."
    n "......Ведь это... морок, привидевшийся мне со страха......"
    nvl clear
    n "{font=CourierNew.ttf}{i}{b}......Кей-тян{w=0.6}...... я же тебе говорила......{/b}{/i}{/font}"
    n "{nw}"
    n "Из-под кровати... раздался сиплый голос......"
    extend " Впрочем, я всё равно узнал в нём голос Мион."
    nvl clear
    n "\"...Что, Мион?....."
    extend " Что ты сказала?..\""
    n "{nw}"
    n "{font=CourierNew.ttf}{i}{b}......Я{w=0.8}...... предупреждала тебя тогда...{/b}{/i}{/font}"
    n "{font=CourierNew.ttf}{i}{b}......Отныне......{w=0.9} хоть раз ещё увидишь меня{w=0.7}...... то буду не я{w=0.8}...... а демон в моём мёртвом теле.........{/b}{/i}{/font}"
    nvl clear
    n "\"...А ха ха ха ха{w=0.8}... верно... говорила ты."
    extend " Извини..."
    extend " Не хватило, понимаешь, внимательности......"
    extend " Видно, за то и ножом получил..."
    extend " А ха ха ха ха ха......\""
    n "{nw}"
    n "Некоторые ногти у неё поломаны, того и гляди — \nотвалятся..."
    extend " Должно быть, от падения с лестницы..."
    nvl clear
    n "Рука... медленно поползла по кровати, пытаясь отыскать мою руку..."
    nvl clear
    n "\"А... а знаешь,{w=0.7} Мион..."
    extend " Я{w=0.5} вот подумал сейчас{w=0.5} кое о чём смешном."
    extend " Хочешь... расскажу?\""
    n "{nw}"
    n "..............................Ответа из-под кровати не последовало."
    nvl clear
    play music lsys11
    n "\"С... скажем...{w=0.8}...... вот я помру сегодня{w=1.0}...... вот прямо тут."
    extend " Но завтра...... завтра я всё равно тут буду, живой... и живущий обычной жизнью......"
    extend " И...... этот Ооиси прознает...{w=0.9} и снова поймёт, что время смерти не совпадает."
    extend " И вот... мертвецы ходят как живые и поднимают переполох..."
    extend " Такано-сан, Мион, потом я — третий..."
    extend " {b}Ну?!{/b}"
    extend " {b}Весело же?{/b}"
    extend " {b}Смешно, да?{/b}"
    extend " {b}Ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха-ха!.....{/b}\""
    n "{nw}"
    n "{font=CourierNew.ttf}{i}{b}............Кей-тян............{/b}{/i}{/font}"
    nvl clear
    n "\"Ну, смейся..."
    extend " Чё, совсем не смешно, что ли?..\""
    n "{nw}"
    play ambient lsys25
    n "Окровавленная рука Мион...... отыскала... моё запястье."
    n "И её пальцы... пусть с отломанными ногтями... крепко в него вцепились, стискивая руку до боли......"
    nvl clear
    n "\"О... ой-ёй-ёй-ёй-ёй{w=0.7}...... х-хватит, слышь......{w=1.0} бо... больно же...\""
    nvl clear
    n "{font=CourierNew.ttf}{i}{b}......Кей-тян...{w=1.0} ...............Я пришла за тобой.........{/b}{/i}{/font}"
    nvl clear
    n "Она с невероятной силищей меня схватила... Я попытался стряхнуть её руку, но не смог."
    n "Она же вроде только запястье держит... но даже дёрнуться почему-то не может всё тело."
    nvl clear
    n "...Ни на волосок."
    n "Даже пальцы в кулак собрать не могу......"
    n ".........Вспомнился...... пыточный стол, где я... не мог даже кулак сжать!..............."
    nvl clear
    scene white with center_03
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    n "..........Ох!!!!..................."
    n "{nw}"
    n "На кончике левого мизинца... ощутился укол гвоздя."
    n "Прямо передо мной появилось ухмылявшееся лицо Мион, разделённое надвое сбегавшей со лба струйкой крови...{w=1.0} Появилось пред самым носом..."
    nvl clear
    play ambient lsys11
    scene black with Dissolve(1.0)
    n "......Ничего ещё не закончилось......"
    extend " Ничего ещё не закончилось."
    n "{nw}"
    n "{b}Дело до сих пор ни в чём не окончено...{/b}"
    n "{b}И до сих пор идёт.{/b}"
    n "{b}И продолжается, и ещё долго будет продолжаться.{/b}"
    nvl clear
    n "{b}Пожалуйста, пусть кто-нибудь закончит его.{/b}"
    n "{b}Пожалуйста, пусть кто-нибудь завершит......{w=1.0} это жестокое, безжалостное, несчастное и печальное дело.{/b}"
    n "{nw}"
    n "{b}\"Это......{w=1.0} всё, чего я желаю...\"{/b}"
    nvl clear
    n "{b}\"Я ведь{w=1.0} уже раз исполнила твоё желание?{/b}"
    extend " {b}Больше — не мечта-ай.{/b}"
    extend " {b}......АХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА ХА!!!\"{/b}"
    n "{nw}"
    n "Мион резко придавила мизинец гвоздём."
    n "{nw}"
    n "{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}И{w=0.3} {w=0.3}м{w=0.3}е{w=0.3}д{w=0.3}л{w=0.3}е{w=0.3}н{w=0.3}н{w=0.3}о{w=0.3} {w=0.3}з{w=0.3}а{w=0.3}н{w=0.3}е{w=0.3}с{w=0.3}л{w=0.3}а{w=0.3} {w=0.3}н{w=0.3}а{w=0.3}д{w=0.3} {w=0.3}г{w=0.3}о{w=0.3}л{w=0.3}о{w=0.3}в{w=0.3}о{w=0.3}й{w=0.3} {w=0.3}м{w=0.3}о{w=0.3}л{w=0.3}о{w=0.3}т{w=0.3}о{w=0.3}к{w=0.3},{w=0.3} {w=0.3}ч{w=0.3}т{w=0.3}о{w=0.3} {w=0.3}д{w=0.3}е{w=0.3}р{w=0.3}ж{w=0.3}а{w=0.3}л{w=0.3}а{w=0.3} {w=0.3}в{w=0.3} {w=0.3}д{w=0.3}р{w=0.3}у{w=0.3}г{w=0.3}о{w=0.3}й{w=0.3} {w=0.3}р{w=0.3}у{w=0.3}к{w=0.3}е{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
    nvl clear
    stop ambient fadeout 1.0
    play sound wa_015
    $ renpy.pause(1.5)
    scene white with fade_050
    play sound wa_036
    scene end_1 with Dissolve(0.5)
    scene end_2 with Dissolve(1.5)
    scene end_3 with Dissolve(2.5)
    $ renpy.pause(1.0)
    scene black with Dissolve(4.0)
    jump otsukaresama_watanagashi
