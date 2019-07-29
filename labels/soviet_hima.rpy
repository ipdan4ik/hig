    $ save_name = "Заседание Актёрского Состава.\nХимацубуси"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play music msys01
    scene bg 161 night
    show ooishi si wa_a1 at sprava
    with up
    a_o "\"Премного благодарим за прохождение игры «Когда плачут цикады — Глава о Потерянном Времени»."
    extend " Мхм-хм-хм-хм!\""
    show rika se wa_a1 at sleva with left_03
    a_f "\"......Мхм-хм-хммм~.\""
    a_o "\"Ну-ну, что ни говори, а на сей раз я блистал."
    extend " Мало того, какая к тому же классная джазовая тема!"
    extend " Если уж я здесь не посмеюсь, то где ж ещё? Н-а-ха-ха-ха-ха!!\""
    nvl clear
    show rika se ni_a1 with dissolve_02
    a_f "\"...Так или иначе..."
    extend " Ооиси, не слишком ли тебя много?\""
    show ooishi si def_a2 with dissolve_02
    a_o "\"Хм-м?"
    extend " Что вы хотите сказать,{w=1.5} Рика-са...\""
    nvl clear
    stop music fadeout 1.0
    play sound wa_008
    $ renpy.pause(0.2)
    scene white with Dissolve(0.1)
    play sound wa_005
    with vpunch
    scene furiker_a with Dissolve(0.1)
    play sound wa_005
    with hpunch
    scene furiker_b with Dissolve(0.1)
    play sound wa_006
    with Shake((0, 0, 0, 0), 0.3, dist=40)
    scene bg 000 with Dissolve(0.1)
    play sound wa_007
    with Shake((0, 0, 0, 0), 0.5, dist=50)
    scene black with dissolve_04
    play music msys02
    scene bg 161 night
    show mion se ika_a2 at sprava
    with right_03
    a_m "\"ИМЕННО ТО, ЧТО ОНА СКАЗА-А-АЛА-А-А!!!\""
    show satoko se bik_b1 at sleva with left_03
    a_s "\"Мало вам своей роли, так вам ещё и повыделяться потребно? Вам поистине следовало бы знать своё ме-есто-о-о!!!\""
    hide mion with left_03
    show rena se wa_a1 at sprava with right_03
    a_r "\"А... а-ха-ха-ха."
    extend " Кроме главной героини, Рики-тян, почти никто нынче не побывал на сцене... {font=DejaVuSans.ttf}☆{/font}\""
    nvl clear
    scene bg 165 night with left_03
    show mion se to_a1 at sleva with left_03
    a_m "\"Мне говорили, конечно, что это так, глава-добавка, но я и не думала, что главных героев настолько нагло пробойкотируют!\""
    show satoko se bik_b1 at sprava with right_03
    a_s "\"Не вам бы жаловаться, Мион-сан."
    extend " Уж вы-то пару раз появились."
    extend " А вот меня с Рэной-сан даже разок не показали.\""
    hide mion with right_03
    show rika se ni_a1 at sleva with left_03
    a_f "\"......Но Рэна ведь на обложках и всём остальном, так что ей ещё ничего же.\""
    nvl clear
    show satoko se hn_a1 with dissolve_02
    a_s "\"...То есть, значит......"
    extend " Меня одну оставили без каких-либо появлений... правильно?\""
    show rika se wa_a1 with dissolve_02
    a_f "\"..................Нипа-а~{font=DejaVuSans.ttf}☆{/font}.\""
    nvl clear
    show satoko se na_b1 with dissolve_02
    a_s "\"Хы-а-а-аааааааа!!"
    extend " Почему только ко мне так относятся-я-я?!!"
    extend " Уааааа!!\""
    a_f "\"......Бедненькая, бедненькая."
    extend " Думаю, к тебе будут относиться всё хуже и хуже и в конце концов ты наверняка станешь всего-навсего второстепенным персонажем.\""
    a_s "\"УА-А-А-А-А-А-А-А!!"
    extend " Нечестно-о-о-о!!\""
    nvl clear
    hide rika with left_03
    show rena se ko_a1 at sleva with right_03
    a_r "\"В-во-во-вовсе и нет..."
    extend " Сатоко-тян, тебя тоже многие любят."
    extend " Тебя никто не собирается обижать! Верно?\""
    show satoko se na_a1 with dissolve_02
    a_s "\"НЕ ХОЧУ, ЧТОБЫ КО МНЕ ТАК ОТНОСИИИЛИ-И-ИСЬ!!!"
    extend " УАА-А-А-ХНЫ-ААААА!!\""
    show rena se def_b1 with dissolve_02
    a_r "\"А, а-ха-ха-ха-ха..."
    extend " Ничего, в следующей главе тебя как раз ждёт большая роль, как мне кажется."
    extend " Кажется!"
    extend " Ну же, не унывай! {font=DejaVuSans.ttf}☆{/font}\""
    nvl clear
    scene bg 166 night with right_03
    show mion se to_a1 at sprava with right_03
    a_m "\"Ну, так иль иначе..."
    extend " Говорят, эта глава вроде как маленький подарок..."
    extend " Вот интересно, так ли оно?"
    extend " Мне чё-то кажется, что история здорово запуталась.\""
    show rika se ko_a1 at sleva with left_03
    a_f "\"......Такая сложная стала, что я ничего почти не поняла же.\""
    hide mion with left_03
    show rena se def_b1 at sprava with right_03
    a_r "\"М-м-м..."
    extend " Поверить не могу, что за год до Цепи загадочных смертей Рика-тян уже о них знала...\""
    nvl clear
    scene bg 165 night
    show mion se wink_b1 at sleva
    with right_03
    a_m "\"...Короче говоря..."
    extend " Глава показывает, что все происшествия были запланированы загодя, так?.."
    extend " Н-да... чертовски значительная наводка...\""
    show rika se wa_a1 at sprava with right_03
    a_f "\"......Я же мико, а значит, Оясиро-сама открыл мне будущее.\""
    nvl clear
    show mion se wa_a2 with dissolve_02
    a_m "\"Хмммм..."
    extend " Как стороннику «Человека», мне, ясно дело, не хочется с тобой соглашаться.\""
    hide rika with left_03
    show rena se ko_a1 at sprava with right_03
    a_r "\"А я верю в «Проклятие»... и считаю, что у Рики-тян, воплощения бога-покровителя Хинамидзавы Оясиро-сама, вполне могли быть сверхъестественные способности, мало ли?\""
    nvl clear
    show mion se tk_b1 with dissolve_02
    a_m "\"Э, ну-ка, не надо тут!"
    extend " Сторонники «Человека» ни за что не признают подобных дурацких выдумок!"
    extend " Всё сделали люди!"
    extend " Нет ни проклятия, ни колдовства, ни хитрых устройств, ни жульнических уловок!\""
    hide rena with right_03
    show rika se ni_a1 at sprava with dissolve_04
    a_f "\"......Было бы здорово, умей я колдовать, не правда ли?\""
    hide mion with right_03
    show rena se wa_b1 at sleva with left_03
    a_r "\"А-ха-ха-ха-ха-ха. {font=DejaVuSans.ttf}☆{/font}"
    extend " А что, Рике-тян бы вполне подошло, как мне кажется. Хау!\""
    nvl clear
    scene bg 166 night with left_03
    show mion se wink_a1 at central with dissolve_04
    a_m "\"Ну да ладно. Зато стороне «Человека» в самом-самом конце подкинули ух какую полезную наводку!"
    show mion se tk_b2 with dissolve_02
    extend " Начиная с первого происшествия и до убийства Рики-тян с катастрофой, всё — один сценарий."
    a_m "То бишь они — одно крупное дело, что существенно увеличивает нашу доказательную базу!\""
    nvl clear
    scene bg 161 night with right_03
    show rena se def_a1 at sprava with right_03
    a_r "\"По-моему... её пророчество доказывает, что Рика-тян обладает особой силой."
    show rena se def_b1 with dissolve_02
    extend " Иначе говоря — что в Хинамидзаве правда есть некая «странная сила»."
    extend " Я думаю, то подтверждает, что в происшествиях виноваты не только люди.\""
    show rika se ko_a1 at sleva with left_03
    a_f "\"......Я запуталась. Совсем ничего не понимаю.\""
    nvl clear
    hide rena with left_03
    show mion se wa_b1 at sprava with right_03
    a_m "\"Кстати, кстати, помните!"
    extend " То выражение на личике Рики-тян!"
    extend " Меня ажно жуть взяла-а!\""
    show rika se wa_a1 with dissolve_02
    a_f "\"......Ми-и.\""
    show rena se nande_a1 at central behind mion with right_03
    a_r "\"Угу, я тоже обомлела..."
    extend " Я и подумать не могла, что миленькая Рика-тян умеет так хихикать...\""
    nvl clear
    show mion se wink_a2 with dissolve_02
    a_m "\"Эй, слышь-слышь!"
    extend " А можешь ещё разок ту гримасу сделать?!\""
    a_f "\"......А вот фигушки же.\""
    show rena se bik_b1 with dissolve_02
    a_r "\"Н-не надо, я не хочу её видеть, кроме как по игре..."
    extend " Хау-у-у...\""
    nvl clear
    scene black with dissolve_02
    stop music fadeout 1.0
    a_r "\"А?!"
    extend " Ч-Что такое?!"
    extend " Свет отключился?!\""
    if renpy.loadable("music/Fascism.mp3"):
        play music torture
    else:
        play music cold_blood
    a_s "\"Так, всех попрошу замереть и не шевелиться!!"
    extend " Ежели вам вздумается совершить необдуманное движение, вас ожидает восхитительный набор ловушек: от маятника-лезвия до противопехотной мины, циркулярной пилы и электрического стула!!\""
    a_m "\"Са-Сатоко?!"
    extend " Ты чё творишь?!\""
    nvl clear
    stop music fadeout 1.0
    scene bg 165 night
    show tomi si_def at sleva
    show satoko se wa_b1 at central
    show takano si_def at sprava
    with dissolve_04
    play music msys03
    a_s "\"ХО-ХО-ХО-ХО-ХО!!"
    extend " С вашего позволения, мы, труппа оставшихся в стороне актёров, берём власть над сиим заседанием в свои руки!"
    extend " ООО-ХО-ХО-ХО!!\""
    show takano si_wa with dissolve_02
    a_y "\"Хи-хи-хи..."
    extend " Спасибо за роскошно обустроенное появление."
    extend " Позвольте же вас всех поприветствовать.\""
    show tomi si_wa with dissolve_02
    a_t "\"Ну и ну, вот так выход на сцену."
    extend " Здорово, совсем не ожидал."
    extend " Спасибо, Сатоко-тян.\""
    nvl clear
    scene bg 161 night with left_03
    show rena se wa_a1 at sprava with right_03
    a_r "\"О, здравствуйте!"
    extend " ...............Ай?!\""
    nvl clear
    play sound wa_029
    hide rena with left_03
    play sound wa_017
    with hpunch
    play sound wa_018
    with vpunch
    play sound wa_006
    scene white with Dissolve(0.01)
    with hpunch
    play sound wa_033
    with Shake((0, 0, 0, 0), 0.4, dist=40)
    scene black with dissolve_04
    scene bg 165 night
    show satoko se aku_b1 at sprava
    with dissolve_04
    a_s "\"Ай-яй-яй, ну я же говорила, что лучше не шевелиться?\""
    show chie si_ko at sleva with left_03
    a_c "\"...Рюгу-сан, вы в порядке?"
    extend " Ходзё-сан, мне кажется, вы слишком...\""
    show satoko se wa_a1 with dissolve_02
    a_s "\"Ох-хо-хо-хо!!"
    extend " Поистине страшна месть за отсутствие появлений на сцене!\""
    show rika se wa_a1 at central with left_03
    a_f "\"......Сатоко отыгрывается за своё отсутствие в основном сценарии же.\""
    nvl clear
    scene bg 166 night
    show mion se bik_b1 at sprava
    with right_03
    a_m "\"Месть за отсутствие?.."
    extend " Чёрт, и когда ты успела понаставить ловушек!..\""
    show satoko se aku_a1 at sleva with left_03
    a_s "\"Как только узнала, что заседание пройдёт здесь,"
    extend " так сразу и принялась за работу. А как же иначе-то?"
    extend " О-хо-хо-хо!..\""
    show mion se ika_a1 with dissolve_02
    a_m "\"......А-а-а... Так вот оно что!!..."
    extend " За тобой кто-то стоит и дёргает за ниточки, верно?!..."
    extend " Стоит, не так ли?!"
    extend " Покажись!!\""
    nvl clear
    scene bg 165 night with right_03
    play music the_mion
    show shion si wa_b1 at sleva with left
    a_h "\"...Хы-хы-хы-хы-хы!"
    extend " Приветик, {i}май систа-а{/i}."
    extend " Как делишки?\""
    show rena se wa_a1 at sprava with right_03
    a_r "\"О, Шии-тян, здравствуй!"
    extend " ..........Уай?!\""
    nvl clear
    play sound wa_029
    hide rena with left_03
    play sound wa_017
    with hpunch
    play sound wa_018
    with vpunch
    play sound wa_006
    scene white with Dissolve(0.01)
    with hpunch
    play sound wa_033
    with Shake((0, 0, 0, 0), 1.0, dist=100)
    scene black with dissolve_04
    scene bg 165 night
    show rika se wa_a1 at sprava
    with fastdown
    a_f "\"......Дважды пострадала от одной ловушки, бедненькая ты, бедненькая...\""
    show mion se ika_a2 at sleva with left_03
    a_m "\"Так и знала — Шиооон-н-н!!"
    extend " У тебя, значит, в следующей главе первая роль, и ты ещё тут буянишь?!"
    extend " ДА ТЫ ВАЩЕ ОБНАГЛЕЛА?!!\""
    nvl clear
    scene bg 166 night
    show shion si aku_a1 at sprava
    with right_03
    a_h "\"Хы-хы-хы..."
    extend " Пусть данная глава всего-навсего заключительный подарок перед главами Ответов, я не настолько добрая, чтобы отдать сцену одной сеструхе."
    extend " Ну~{font=DejaVuSans.ttf}☆{/font},"
    extend " вот я и подогрела Сатоко немножко.\""
    nvl clear
    show mion se to_b1 at sleva with left_03
    a_m "\"...У-у-у-у!!..."
    extend " Шион... на что ты рассчитываешь?!...\""
    show shion si wink_a1 with dissolve_02
    a_h "\"На закрепление успеха, пожалуй?"
    extend " А то видишь, сеструха, в последнее время за тебя голосуют всё больше и больше.\""
    hide mion with right_03
    show rena se wa_a1 at sleva with left_03
    a_r "\"Ага."
    extend " Нам часто присылают письма про то, какая милашка была Мии-тян в первой половине «Главы о Хлопковых Корабликах»!\""
    nvl clear
    scene bg 161 night with left_03
    show mion se fu_a1 at central with dissolve_02
    a_m "\"Хы-хы-хы!"
    extend " Просто твоя вредная сущность вскрылась, и товарищи игроки наконец-то заметили моё очарование."
    extend " Сатоко же привела к славе «Глава о Смертоносном Проклятии»."
    extend " А у Рэны и Рики-тян поклонники завсегда найдутся."
    extend " Никому ты давно уже не нужна-а-а!\""
    nvl clear
    scene bg 166 night
    show shion si wa_a1 at sprava
    with right_03
    a_h "\"Вот мне и думается:"
    show shion si wink_b1 with dissolve_02
    extend " а почему бы не подстрелить разом двух зайцев, то есть Сатоко и сестрицу, раз уж они тревожно быстро набирают голоса?"
    extend " Ну, вот я по-взрослому и подготовилась.\""
    nvl clear
    show satoko se bik_b1 at sleva with left_03
    a_s "\"......?!"
    extend " Шион-сан, что-что вы сказали?!"
    extend " Меня тоже хотите?!\""
    show shion si aku_a1 with dissolve_02
    a_h "\"А малявочка-то не особенно сообразительная!!"
    extend " На!!\""
    show satoko se hn_a1 with dissolve_02
    a_s "\"М-мя-мя-мя-мяяяуууууу!!!!\""
    nvl clear
    play sound wa_015
    hide satoko with left_03
    play sound wa_005
    with hpunch
    play sound wa_009
    with vpunch
    play sound wa_034
    scene white with Dissolve(1.0)
    play sound wa_033
    with Shake((0, 0, 0, 0), 0.5, dist=50)
    scene black with dissolve_04
    scene bg 166 night
    show shion si tk_a1 at central
    with dissolve_04
    if renpy.loadable("music/Fascism.mp3"):
        play music torture
    else:
        play music msys03
    a_h "\"Хы-хы-хы-хы!"
    extend " Прощайте, основной актёрский состав, да здравствуют второстепенные роли!"
    extend " Конец вам, главные героини!\""
    nvl clear
    scene bg 165 night with right_03
    show tomi si_uh at sprava with right_03
    a_t "\"...Ш-Шион-тян."
    extend " Тебе не кажется, что незачем так...\""
    show takano si_wa at sleva behind tomi with left_03
    a_y "\"Ну-ну, Дзиро-сан."
    extend " Весело же, пускай балуется."
    show takano si_fu with dissolve_02
    extend " Ведь мы двое теперь будем появляться намного чаще."
    extend " ......Вы и я, вместе...{w=1.5} неужели не хотите?\""
    show tomi si_wa with dissolve_02
    a_t "\"А...... А-ха-ха-ха-ха-ха-ха-ха!"
    extend " Д-д-да что вы, что вы, совсем нет!"
    extend " А-ха-ха!\""
    nvl clear
    scene black with left_03
    scene bg 161 night with left_03
    show rena se bik_a1 at sprava with right_03
    a_r "\"Тиэ-сэнсэээй!"
    extend " Неужто и вас Шии-тян подкупила?!\""
    show chie si_ko at sleva with left_03
    a_c "\"П... простите, Рюгу-сан..."
    extend "... Понимаете... Шион-тян сказала, что, начиная со следующей главы, будет выходить уголок под названием «Поучите нас! Тиэ-сэнсэй!»... ну и вот...\""
    nvl clear
    scene bg 165 night
    show shion si wink_a1 at sleva
    with dissolve_04
    a_h "\"Так-тааак."
    extend " Ну, с кого начать ПОЗОООРНУЮ казнь?"
    extend " Наверное, с Сатоко — в награду за то, что помогла устроить ловушку?\""
    nvl clear
    stop music fadeout 1.0
    play sound wa_015
    $ renpy.pause(0.3)
    play sound wa_015
    $ renpy.pause(0.3)
    play sound wa_015
    $ renpy.pause(0.3)
    a_n "\"НЕ ПОЗВОЛЮ!!!!{nw}"
    play sound wa_007
    play music msys04
    scene furiker_b with Shake((0, 0, 0, 0), 0.7, dist=40)
    scene black with dissolve_04
    extend ""
    extend " О-о!!!\"{nw}"
    play sound wa_009
    scene bg 166 night
    show irie si def_a1 at central
    with dissolve_04
    extend ""
    nvl clear
    scene bg 165 night
    show rena se wa_b1 at sprava
    with left_03
    a_r "\"Н-Начальник!!\""
    show satoko se wa_b1 at sleva with left_03
    a_s "\"Каким невиданно надёжным он кажется!!\""
    hide rena with left_03
    show irie si maji_a1 at sprava with right_03
    a_i "\"Я, Ириэ Кёсукэ, ни в коем случае не позволю обидеть Сатоко-тян."
    extend " Пускай я тоже второстепенный персонаж... но не думайте, что сможете меня усмирить!\""
    nvl clear
    scene bg 166 night
    show shion si aku_b1 at sprava
    with right_03
    a_h "\"Ой,"
    extend " неужели вы хотите отказаться от главной роли в фильме{w=1.0} {b}{cps=*20.0}«ЖИВАЯ СЪЁМКА!! Дрессировка горничной Сатоко, Глава о Переодевании»{/cps}{/b},{nw}"
    play sound wa_029
    extend " {w=0.6}который мы как раз после этого пойдём снимать?\""
    stop music fadeout 1.0
    play sound wa_029
    show irie si warai at sleva with left_03
    a_i "{b}\"...Шион-сама.{/b}"
    play music msys03_treat
    extend " {b}Я, ИРИЭ, ОБЯЗУЮСЬ БЫТЬ ВЕРЕН ВАМ ПО ГРОБ ЖИИИЗНИ-И-И-И-И!!!\"{/b}"
    hide shion with left_03
    show mion se to_a1 at sprava with right_03
    a_m "\"Вот и усмирила, глазом моргнуть не успели!!!!!\""
    nvl clear
    scene bg 161 night
    show shion si wink_a1 at central
    with right_03
    a_h "\"Что же..."
    extend " Теперь всё в моих руках!"
    extend " Отныне \nвсё — и заседания, и главы!"
    extend " — будет идти по моему хотению."
    extend " ...............Хм?"
    extend " Кого-то не хватает?\""
    nvl clear
    show irie si def_a2 at sprava with right_03
    a_i "\"......Шион-сама!"
    extend " Нет Рэны-сан!"
    extend " Она куда-то подевалась!..\""
    scene black with left_03
    scene bg 166 night
    show chie si_maji at sprava
    with left_03
    a_c "\"А, вот она."
    extend " Рюгу-сан!"
    extend " Вам же вроде бы сказали не двигаться!\""
    show tomi si_uh at sleva with left_03
    a_t "\"Рэна-тян!"
    extend " Поверь, тебе самой же лучше не сопротивляться!..\""
    nvl clear
    hide chie with left_03
    show rena se ko_a1 at sprava with right_03
    a_r "\"Извините... но я не думаю, что так можно делать!\""
    nvl clear
    scene bg 165 night
    show takano si_def at sleva
    with right_03
    a_y "\"...Что тебе надо?"
    extend " ......Выключатель?"
    show takano si_fu with dissolve_02
    extend " А, так ты собираешься предпринять что-то, когда зал покроется тьмой?"
    extend " Хи-хи-хи... Зря стараешься.\""
    show shion si aku_b1 at sprava with right_03
    a_h "\"Рэна-сан."
    extend " Мне кажется, вам лучше прекратить бессмысленное сопротивление и одуматься."
    extend " Разозлите меня, и худо придётся не только вам, но и сеструхе, и всем остальным.\""
    nvl clear
    scene bg 161 night with left_03
    show mion se bik_b1 at sprava with right_03
    a_m "\"......Вырубив свет, ничего не добьёшься..."
    extend " Рэна, жаль признавать, но лучше тебе подчиниться......\""
    show rena se okoru_b1 at sleva with left_03
    a_r "\"Ничего, не унывай."
    extend " Выключим свет... и устроим переворот в нашу пользу!\""
    show satoko se bik_b1 at central behind rena with dissolve_04
    a_s "\"...Переворот?!..."
    extend " У вас что, есть какой-то запасной план?!...\""
    nvl clear
    scene bg 166 night
    show shion si aku_a1 at sleva
    with right_03
    a_h "\"......АХА-ХА-ХА-ХА!!"
    extend " А вы умеете насмешить, Рэна-сан."
    extend " Ну так попробуйте?"
    extend " Покажите мне ваш переворот, прошу любезно.\""
    show rena se okoru_a1 at sprava with right_03
    a_r "\"......Капризная ты, Шии-тян."
    extend " Всего-то из-за того, что тебя недостаточно показали в сценарии, ты решила захватить Заседание... Какая же ты капризная.\""
    nvl clear
    show shion si fu_b1 with dissolve_02
    a_h "\"Когда это я капризничала?..\""
    show rena se okoru_b1 with dissolve_02
    a_r "\"Не понимаешь, Шии-тян..."
    extend " Пускай это лишь заседание, но ты-то появилась. Ты и в предыдущих главах то и дело мелькала, и ты ещё буянишь?"
    extend "..... Разве не слышишь, Шии-тян...{w=1.0} голоса, доносящегося из ада...{w=1.0} голоса, стенающего, что ни за что тебя не простит?..\""
    nvl clear
    scene bg 161 night with left_03
    show satoko se wa_a1 at sprava with right_03
    a_s "\"......П-понятно!"
    extend " Так вот оно что!!\""
    show mion se bik_a1 at sleva with left_03
    a_m "\"Поняла!!"
    extend " Кей-тян, да?!!!"
    show mion se wink_b2 with dissolve_02
    extend " Верно, Кей-тяна ни разу ещё не бывало на заседании!"
    extend " Он тебя не простит за то, что ты посмела захватить заседание, забыв про него!\""
    nvl clear
    scene bg 166 night
    show shion si fu_a1 at sprava
    with left_03
    a_h "\"Ясненько."
    extend " Ну и?"
    extend " Как же он появится, если у него и картинки-то нет?"
    extend " ......Только не говори, что её как раз вставляют в игру."
    extend " Хы-хы-хы!!...\""
    show rena se okoru_b1 at sleva with left_03
    a_r "\"Ох и зазнайка же ты, Шии-тян!!...\""
    nvl clear
    scene bg 165 night
    show takano si_def at sleva
    with right_03
    a_y "\"......Ах!!"
    extend " Чёрт!!"
    extend " Если она выключит свет!!!....."
    extend " Тиэ-сэнсэй, хватай Рэну-тян!!\""
    show chie si_ko at sprava with right_03
    a_c "\"Э?"
    extend " Э?\""
    scene bg 166 night
    show rena se wa_b1 at central
    with dissolve_02
    a_r "\"ПОЗДНО!!!!\""
    nvl clear
    stop music fadeout 1.0
    if persistent.matsuri:
        scene bg 166 night:
            xalign 0.5 yalign 0.5
            0.2
            ease 0.3 zoom 2.0
        show rena se wa_b1:
            xalign 0.5 yalign 1.0
            0.2
            ease 0.3 zoom 2.0 yalign 0.2
        $ renpy.pause(0.5, hard=True)
        scene black with Dissolve(0.1)
        scene cg renapan x1:
            zoom 1.6 xalign 0.3 yalign 0.4
            0.6
            easein 0.4 zoom 2.0
        with Dissolve(1.0)
        $ renpy.pause(0.4)
        scene aka1 with Dissolve(0.15)
    play sound wa_006
    scene black with dissolve_04
    a_r "{cps=*20.0}{b}\"......НА ПООООМООООЩЬ!! КЕЙТИ-КУУУУУУУН!!!!!\"{/b}{/cps}" with vpunch
    nvl clear
    play sound wa_032
    $ renpy.pause(1.0)
    a_k "{b}\"...Хе, хе, хе, хе...{/b}"
    extend " {b}УХА-ХА-ХА-ХА-ХА-ХА!!!!\"{/b}"
    nvl clear
    a_m "\"Э-это же голос...... Кей-тяна?!!!\""
    play music msys04
    a_k "\"Благодарю, Рэна!!"
    extend " Когда истинный мрак, оставленный даже луной, скрывает землю,"
    play sound wa_015
    extend "{w=0.3}{nw}"
    play sound wa_015
    extend "{w=0.3}{nw}"
    play sound wa_015
    extend " {w=0.3}на неё спускается дьявол чернее ночи — {b}МАЭБАРА КЕЙТИ!!!!{/b}\"{nw}"
    play sound wa_007
    scene furiker_b with Dissolve(0.1)
    with hpunch
    extend ""
    nvl clear
    scene black with dissolve_04
    a_s "\"Понятно, для этого картинки не надо.\""
    a_f "\"......Да, не нужны ни картинка с ним, ни задний план. Очень мило по отношению к разработчикам.\""
    nvl clear
    a_k "{b}\"ЫХ-ХАХ-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА!!!{/b}"
    extend " {b}ШИОООНННН!!{/b}"
    play sound wa_010
    extend " {b}Ты ведёшь себя как героиня трагедии, но какой же немыслимо смешной ты мне кажешься!!!{/b}"
    extend " {b}ПО-МОЕМУ, ТЫ ЗАРВАААЛАСЬ!!{/b}"
    play sound wa_029
    a_k "{b}Всякий раз, как устраивали Заседание Актёрского Состава!{/b}"
    extend " {b}Я, без картинки, не мог даже показаться — можешь представить себе мои{/b}{w=0.8}{nw}"
    play sound wa_005
    extend " {b}злость,{/b}{nw}"
    play sound wa_005
    extend " {b}{w=0.2}негодование{/b}{nw}" with vpunch
    play sound wa_006
    extend " {b}{w=0.2}и обиду!!!{/b}{nw}" with hpunch
    extend "" with vpunch
    play sound wa_007
    extend " {b}НУ, СЕЙЧАС Я ТЕБЕ ПОКАЖУУУУУ!!!\"{/b}{nw}"
    extend "" with Shake((0, 0, 0, 0), 0.4, dist=30)
    nvl clear
    a_r "\"К-Кейти-кун, т-ты словно воплощение зла.\""
    a_k "{b}\"Какое там воплощение — называй меня самим Дьяволом!!{/b}"
    extend " {b}И теперь этот мир, поглощённый истинной тьмой, переходит мне!!{/b}"
    extend " {b}В мире тьмы мне никто не соперник!!!!\"{/b}"
    nvl clear
    a_r "\"......Кейти-кун... ты какой-то страшный, хау...\""
    nvl clear
    a_k "\"Страшный?"
    extend " Уа-ха-ха-ха-ха!!!"
    play sound wa_010
    extend " Время страшных Цикад ушло!!"
    play sound wa_008
    extend "{w=0.3}{nw}"
    play sound wa_008
    extend "{w=0.3}{nw}"
    play sound wa_008
    extend " Отныне начинаются модные, пошлые, возбуждающие Цикады!!!!\"{nw}"
    play sound wa_006
    extend "" with Shake((0, 0, 0, 0), 0.5, dist=30)
    a_i "\"......Ч-ч-что-чтооо?!"
    play sound wa_011
    extend " Маэбара-сама!"
    play sound wa_029
    extend " ВОЗЬМИТЕ МЕНЯ С СОБОООЙ!!\""
    a_k "\"Гха-ха-ха-ха!!"
    extend " Гляжу, смекаешь суть, Начальник!!"
    extend " Ну тогда, врач-начальник, давай-ка мы с тобой посмотрим, на что я способен."
    extend " Хрммммм... {b}КАХ-Х-Х!!!{/b}\"{nw}"
    play sound wa_029
    extend ""
    nvl clear
    play sound wa_034
    scene white with Dissolve(1.0)
    scene black with dissolve_04
    a_y "\"...Ах?!"
    extend " Ч-что это?!\""
    play sound wa_006
    a_t "\"Та-Та... Такано-сан..... в халате медсестры... с мини-юбкоооой!!"
    play sound wa_005
    extend " И не розовом, как в неприличных играх!{nw}"
    play sound wa_005
    extend " {w=0.2}Да!!{nw}" with vpunch
    play sound wa_006
    extend " {w=0.2}Невинном, чисто-белом, как должно быть!!\"{nw}" with vpunch
    extend "" with Shake((0, 0, 0, 0), 0.4, dist=60)
    nvl clear
    a_k "\"Она, работая медсестрой, ни разу за всю игру ей не оделась — что за ересь!!"
    extend " Так-так..."
    extend " Кого бы следующей... {font=DejaVuSans.ttf}☆{/font}\""
    nvl clear
    a_m "\"...Рэ... РЭНА-А-А!!"
    extend " Это никакой не переворот!"
    extend " Теперь нас постигла другая беда!!!\""
    a_r "\"Хау-у-у!!"
    extend " Слишком темно, я ничего не могу подела-а-ать!\""
    nvl clear
    a_k "\"Ну, кого теперь переодеть и во что?"
    extend " Хм, почему бы не совместить"
    play sound wa_011
    extend " школьную форму,{w=0.8}{nw}"
    play sound wa_010
    extend " физкультурную{w=0.8}{nw}"
    play sound wa_006
    extend " и школьный купальник?!!!\""
    a_i "\"МАЭБАРА-САМА, ВЫ — ЛУЧШИЙ!!!!!"
    extend " А потом давайте девочку-зайчика или бадо-гару; нет-нет, ещё лучше — в одном нижнем белье оставим!!"
    extend " Нет-нет!!"
    extend " Я знаю — давайте разденем всех догола?!!!{nw}"
    play sound wa_012
    extend ""
    extend " Н-но, конечно, носочки оставим всенепременно!!!\""
    nvl clear
    a_k "\"О-О-О-О-О-О!!"
    extend " Прекрасно!!"
    extend " Вижу, ты знаешь толк!!"
    extend " Н... Начальник!!..."
    play sound wa_006
    extend " {cps=*10.0}Кажись, мы с тобой наконец-то понимаем друг друга!!!\"{/cps}{w=0.2}{nw}"
    extend "" with vpunch
    a_i "\"Нет-нет, Маэбара-сан."
    extend " {b}...То есть Кей{/b}."
    play sound wa_010
    extend " Отныне зови меня {b}«Ирий»{/b}."
    play sound wa_007
    extend " {b}Теперь я Доктор Ирий{/b}!!!\""
    nvl clear
    play sound wa_015
    $ renpy.pause(0.3)
    play sound wa_015
    $ renpy.pause(0.3)
    play sound wa_015
    $ renpy.pause(0.3)
    a_t "\"КЕ-Е-Е-Е-ЕЙ!!"
    extend " Что ж ты о нас-то забыл!!\""
    a_o "\"Мхм-хм-хм!"
    extend " Томми с Клаудом никогда Кея не бросят!!"
    extend " Мм-хм-хм-хм!!\""
    a_k "\"Томми!!"
    extend " Клауд!!"
    extend " ...Наконец-то мы вместе..."
    play sound wa_015
    extend "{w=0.25}{nw}"
    play sound wa_015
    extend "{w=0.25}{nw}"
    play sound wa_015
    extend " {w=0.25}{b}Внемлите — Четыре Короля в сборе!!!{/b}\"{nw}"
    scene white with fade_010
    play sound wa_007
    scene furiker_a with Shake((0, 0, 0, 0), 0.3, dist=50)
    scene black with dissolve_04
    extend ""
    nvl clear
    t "{b}Наконец-то...{/b}"
    extend " {b}Четыре злобных Царя с Кеем во главе собрались в одном месте.{/b}"
    t "{nw}"
    t "{b}На окутанную мраком землю в кои-то веки спустился дьявол чернее ночи, Маэбара Кейти.{/b}"
    t "{nw}"
    t "{b}С его колдовской мощью не сравнится ничто!!{/b}"
    extend " {b}В такой тьме... никто ему не соперник!!{/b}"
    extend " {b}Остаётся только капитулировать!!!{/b}"
    nvl clear
    t "{b}Ах, героини не в состоянии выбраться из темноты и вынуждены одеваться в один постыдный наряд за другим, как захочется Дьяволам.{/b}"
    extend " {b}Неужели они всю оставшуюся жизнь будут служить манекенами?!!{/b}"
    n "{nw}"
    play sound wa_029
    n "{b}Потрясающе, давай ещё!!{/b}"
    play sound wa_010
    n "{b}Да, кстати, купальник, надеюсь, правильный — старого типа?!{/b}"
    play sound wa_006
    n "{b}Если соревновательный, то ух я тебе задааааам!!!{/b}{nw}"
    extend "" with Shake((0, 0, 0, 0), 0.4, dist=50)
    nvl clear
    a_m "\"......Тьфу!!"
    extend " Шион!!"
    extend " Всё из-за тебя, вот ты и придумай что-нибудь!!!\""
    a_h "\"Не волнуйся, сестричка."
    extend " В темноте истинная сила просыпается не у одного Кей-тяна.\""
    a_s "\"......Э-э?"
    extend " А что, у нас тут найдётся такой друг?\""
    nvl clear
    a_k "\"Гха-ха-ха-ха-ха!!"
    extend " Ну и наглая ты, Сонодзаки Шион!!"
    extend " Между прочим, если ты про директора, брось надежду!!"
    extend " «Парни наконец-таки дорвались до своей давней мечты!"
    play sound wa_011
    extend " Истинный муж ни за что не сдастся!» — дал он своё благословение!!!"
    a_k "Разумеется, нечего рассчитывать и на новенького, Акасаку-сана!"
    a_k "Он, как сказали, ещё вчера уехал на горячие источники вместе с женой, оставив дочку родным."
    play sound wa_011
    extend " А значит!"
    play sound wa_006
    extend " Выхода НЕТ!!\"{nw}"
    extend "" with Shake((0, 0, 0, 0), 0.4, dist=50)
    nvl clear
    a_h "\"...Эх, глупый Кей-тян..."
    extend " Видишь ли, даже среди персонажей с картинками могут найтись те, чьё истинное лицо открывается лишь в темноте."
    play sound wa_012
    extend " .........ТИЭ-СЭНСЭЙ!!!\""
    stop music fadeout 1.0
    a_c "{b}\".........Так вот, Маэбара-кун...\"{/b}"
    nvl clear
    play music lsys11
    a_s "\"......Слишком темно, чтобы что-либо разглядеть, но платье на Тиэ-сэнсэй стало другим."
    extend " ...Ой, а это что?"
    extend " Сколько мечей у неё в руках......"
    extend " Б-Быть не может!!"
    extend " Чёрные... м-м-м!!!.....\""
    a_f "\"{b}......Молчание — золото.{/b}"
    extend " Нипа-а~{font=DejaVuSans.ttf}☆{/font}.\""
    nvl clear
    a_c "{b}\"...Маэбара-кун?{/b}"
    extend " {b}...Кажется, ты немного зарвался.{/b}"
    extend " {b}Больше твоих злодейств Церковь не потерпит.\"{/b}"
    nvl clear
    play music msys03_treat
    a_k "\"Т-так,{w=0.8} так, секундочку,{w=0.6} т-т-{w=0.8}так нельзя делать,{w=0.8} это нечестно,{w=0.6} не по правилам!!!!"
    extend " Эй, так ведь нельзя?!!!"
    extend " О, о, эй, чёрт, что это за здоровая дура?!!!"
    extend " ЧТО-О-О?!"
    extend " Приём с неуязвимостью?!"
    extend " Седьмое пи-{b}аААаАААЙ!!!{/b}"
    extend " {b}АААааыаЫАЫааыарррх!!!!{/b}\""
    nvl clear
    play sound wa_033
    $ renpy.pause(0.3)
    play sound wa_015
    $ renpy.pause(0.3)
    call key_hit
    call key_hit
    call key_hit
    call key_hit
    call key_hit
    call key_hit
    call key_hit
    call key_hit
    call key_hit
    call key_hit
    play sound wa_006
    $ renpy.pause(0.2)
    play sound wa_006
    with hpunch
    scene bg 000 with fade_050
    play sound wa_007
    with Shake((0, 0, 0, 0), 0.7, dist=50)
    scene white with Dissolve(5.0)
    show cinema with x_15
    show title02 with Dissolve(3.0)
    $ renpy.pause(2.0)
    show black behind title02 with Dissolve(3.0)
    $ renpy.pause(1.0)
    scene black with right
    stop music fadeout 1.0
    scene bg 166 night
    show rena se wa_a1 at central
    with dissolve_04
    play music msys05
    a_r "\"А-ха-ха-ха..."
    extend " Позвольте снова вас поприветствовать."
    extend " Огромнейшее вам спасибо за прохождение игры «Когда плачут цикады — Глава о Потерянном Времени»!\""
    nvl clear
    show rena se def_a1 with dissolve_02
    a_r "\"Полагаю, вы и так уже знаете, что «Когда плачут цикады» — sound novel, иначе говоря, звуковой роман с отсутствием выбора."
    a_r "Мне кажется, по сравнению с «приключенческими» романами — теми, где игрок может повлиять на ход истории, — Цикады больше похожи на книгу или кинофильм."
    extend " Иногда нам пишут, что их из-за этого даже игрой называть не стоит.\""
    nvl clear
    a_r "\"Если бы «Цикад», подобно книге или кино, можно было только смотреть или читать, тогда они не игра."
    extend " ......Но, как вы сами знаете, в них полным-полно загадок."
    extend " Вот когда вы пытаетесь их разгадать, тогда Цикады игрой и становятся.\""
    nvl clear
    show rena se wa_b1 with dissolve_02
    a_r "\"Вам, игрокам, предоставляется почётное право рассмотреть эту полную загадок историю с любых точек зрения."
    a_r "К примеру, вы можете самостоятельно находить объяснения всем загадкам, делиться ими да обсуждать с остальными. И это далеко не единственный способ получить от игры удовольствие.\""
    nvl clear
    show rena se def_b1 with dissolve_02
    a_r "\"Авторы создали отдельный форум для обсуждения загадок и ответов на них на японском, называющийся «форум Мии», однако тот, к сожалению, закрылся 15 ноября 2011 года."
    a_r "Сайт авторов по-прежнему можно найти (по состоянию на ноябрь 2013 года) по адресу \n{a=http://07th-expansion.net/}07th-expansion.net{/a}.\""
    nvl clear
    a_r "\"Как авторы, так и переводчик будут рады присланным мнениям. Авторы — у себя на сайте (на японском), переводчик — на {a=http://iichan.hk/hau/}IIchan.hk{/a} и {a=http://dobrochan.com/hau/}Dobrochan.ru{/a}.\""
    nvl clear
    show rena se def_a1 with dissolve_02
    a_r "\"Ну что ж... Со следующей Главы наконец-то начинаются Главы ответов."
    a_r "Её название — Мэакаси-хэн (Глава о Раскрытии Тайны)."
    a_r "......Но, к сожалению, ответ на загадку — такая штука, которая, будучи раскрытой, разом сводит все воображаемые решения на нет.\""
    nvl clear
    a_r "\"И поэтому, мне кажется... можно сказать, сейчас вы находитесь в той самой точке, в которой интерес от Цикад больше всего.\""
    a_r "\"Надо отметить, что переводчик с данным мнением не согласен и утверждает, что дальше будет лишь интереснее, хотя, безусловно, в другом плане.\""
    nvl clear
    show rena se def_b1 with dissolve_02
    a_r "\"Ну а если Глава о Раскрытии Тайны у вас уже есть,"
    extend " советую поразмыслить над всеми загадками и насладиться поиском объяснений, прежде чем приметесь за её чтение."
    extend " Ведь так всего интереснее.\""
    nvl clear
    show rena se wa_a1 with dissolve_02
    a_r "\"......А-ха-ха..."
    extend " Прошу прощения за бесстыдство."
    extend " Если Цикады вам понравились, то большего счастья для всех нас нет и быть не может.\""
    nvl clear
    show rena se def_b1 with dissolve_02
    a_r "\"Что ж — счастливого вечера!.."
    extend " Жду вас в Хинамидзаве!.."
    show rena se hau_b1 with dissolve_02
    extend " А если захотите поиграть с Рэной... то давайте пойдём вместе искать сокровища!"
    extend " Хау! {font=DejaVuSans.ttf}☆{/font}\""
    nvl clear
    scene black with Dissolve(1.0)
    $ renpy.pause(2.0)
    scene staff:
        xalign 0.5 yalign 0.0 zoom 1.0
        linear 120.0 yalign 1.0
    with Dissolve(1.0)
    play music msys01
    $ renpy.pause(120.0)
    stop music fadeout 3.0
    $ renpy.pause(4.0)
    scene black with Dissolve(7.0)
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
