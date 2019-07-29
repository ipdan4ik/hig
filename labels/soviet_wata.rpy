    $ save_name = "Заседание Актёрского Состава\nВатанагаси"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    scene bg 161 with Dissolve(1.0)
    play music msys01
    show rena se wa_a1 at sprava with right_03
    a_r "\"Огромнейшее спасибо вам за прохождение игры «Когда плачут цикады — Глава о Хлопковых Корабликах»!"
    extend " И как вам эта глава?"
    extend " Надеемся, вам хоть немного понравилось.\""
    nvl clear
    scene bg 166 with right_03
    show satoko se bik_b1 at sleva with left_03
    a_s "\"Немного? Да какое там немного!"
    extend " Опять"
    extend " концовка фиговая-префиговая?!"
    extend " Как бы уважаемые игроки не рассердились?!\""
    show rika se ni_a1 at sprava with right_03
    a_f "\"......Я вот сердитая же.\""
    nvl clear
    scene bg 165 with left_03
    show mion se wink_a1 at sprava with right_03
    a_m "\"Э-эй, ребята-а, славно сыграли!!"
    extend " Эй, чего вы?"
    extend " Ну да, концовочка так себе, зато мы прошли, можно сказать, «Главу о Мион», ага?"
    extend " Мне сплошное удовольствие играть в такой! Ня-ха-ха-хаа!\""
    nvl clear
    show satoko se bik_a1 at sleva with left_03
    a_s "\"Н-Н-Не смейте так говорить — «сплошное удовольствие»!!"
    extend " Меня ведь с Рикой убили, не забыли вы?!\""
    hide mion with left_03
    show rika se de_a1 at sprava with right_03
    a_f "\"......И Сатоко притом случайно под горячую руку попала.\""
    show satoko se na_b1 with dissolve_02
    a_s "\"УУУЫЫЫЫААААААаааААаАА!!!"
    extend " Не хочууу тааак умираааать!!\""
    hide rika with left_03
    show rena se bik_b1 at sprava with right_03
    a_r "\"Ну-у-у, не реви!"
    extend " Есть же рассказ, где Мии-тян главная героиня, значит, будет и рассказ, где главная героиня — Сатоко-тян."
    extend " Поскорее бы!\""
    nvl clear
    show mion se aku_a1 at central behind rena with dissolve_04
    a_m "\"Ага, и в конце — зуб даю — Сатоко замучают до смерти какие-то странные личности.\""
    show satoko se na_a1 with dissolve_02
    a_s "\"УААаААААААААААААаААА!!"
    extend " НЕ ХОЧУУУУУУ!!!"
    extend " УааааААааААаааАА!!\""
    nvl clear
    play sound wa_015
    scene white with dissolve_02
    play sound wa_005
    if not persistent.matsuri:
        show furiker_b
        with Shake((0, 0, 0, 0), 1.0, dist=50)
    else:
        show cg renapan_rika x1
        with Shake((0, 0, 0, 0), 1.0, dist=50)
        queue sound wa_005
        $ renpy.pause(0.2)
        show cg renapan_rika x7
        with Shake((0, 0, 0, 0), 1.0, dist=50)
    scene bg 161
    show rena se wa_b1 at sprava
    with fastup
    a_r "\"Мииии-тяяян,"
    extend " ты хочешь, чтобы я разозли-и-ила-ась?\""
    show rika se wa_a1 at sleva with left_03
    a_f "\"......Мии стала совсем плоская же."
    extend " Я даже не пойму, где у неё голова, чтоб погладить...\""
    hide rena with left_03
    show satoko se def_a1 at sprava with right_03
    a_s "\"А, вот заново надувается."
    show satoko se aki_a1 with dissolve_02
    extend " ...Какое непостоянство...\""
    nvl clear
    play sound wa_013
    scene white with fade_010
    scene black with Fade(0.002, 0.003, 0.2, color="#fff")
    scene bg 165
    show tomi si_def at sprava
    with dissolve_04
    play music msys02
    a_t "\"Эй, ребята-а!"
    extend " Классно сыграли!\""
    show ooishi si def_a1 at sleva behind tomi with left_03
    a_o "\"И вновь прошу прощения за опоздание. Мм-хм-хм-хм!\""
    nvl clear
    scene bg 166
    show rena se wa_a1 at sprava
    with left_03
    a_r "\"Томитаке-сан, Ооиси-сан!"
    extend " Большое спасибо за ваши труды."
    extend " Хм?"
    extend " А где же Такано-сан и Шион-тян, они задерживаются?\""
    show shion si def_b1 at sleva with dissolve_04
    a_h "\"Не извольте переживать, мы уже тут."
    extend " Спасибо вам огромное за приглашение."
    extend " ...Можно тут присесть?\""
    show satoko se wa_a1 at central with dissolve_04
    a_s "\"Ага, будьте так добры!\""
    nvl clear
    scene black with Dissolve(1.0)
    scene bg 165 with Dissolve(1.0)
    show takano si_def at sprava with right_03
    a_y "\"Как же восхитительно видеть всех в сборе."
    extend " Что ж, прошу любить и жаловать.\""
    show rena se def_b1 at sleva with left_03
    a_r "\"Ладно, начинаем?"
    extend " Все пришли?\""
    hide takano with left_03
    show rika se de_a1 at sprava with right_03
    a_f "\"......Все, кроме Кейти же.\""
    hide rena with right_03
    show ooishi si def_a1 at sleva with left_03
    a_o "\"Ах да... Маэбара-кун, как обычно, не имея своего изображения, начал уже почитывать следующий сценарий?..\""
    nvl clear
    scene bg 163 with dissolve_04
    show takano si_fu at sprava with right_03
    a_y "\"Ах, как жаль."
    extend " Так неприятно без него веселиться.\""
    show shion si wink_a1 at sleva with left_03
    a_h "\"Миё-сан, да не беспокойтесь вы."
    extend " Давайте просто веселиться — уверена, он сам того хочет.\""
    hide takano with left_03
    show satoko se wa_a1 at sprava with right_03
    a_s "\"Воистину!!"
    extend " Мы с таким трудом смогли тут собраться, ну так нечего пребывать в унынии!!\""
    hide shion with right_03
    show tomi si_uh at sleva with left_03
    a_t "\"Т-ха-ха-ха..."
    extend " Что ж... извини, Кейти-кун... Придётся нам без тебя!\""
    nvl clear
    scene bg 165 with left_03
    show mion se wa_a1 at sprava with right_03
    a_m "\"Так, значит, решено!!"
    extend " А теперь все взяли стаканы!"
    extend " Есть такие, кто газировку не переносит?\""
    show ooishi si wa_a1 at sleva behind mion with left_03
    a_o "\"А у взрослых есть и спиртное. Мм-хм-хм-хм!\""
    hide mion with left_03
    show tomi si_wa at sprava with right_03
    a_t "\"Рика-тян, а чего хочешь ты?"
    extend " Кока-колы?"
    extend " Сока?\""
    hide ooishi with left_03
    show rika se ni_a1 at sleva with left_03
    a_f "\"...Ми-и-и-и..."
    extend " Я хочу того ячменного чаю с пузыриками, что у Томитаке.\""
    show rena se okoru_a1 at central with dissolve_04
    a_r "\"Эй!"
    extend " Рика-тян, тебе нельзя пить спиртное!\""
    nvl clear
    scene bg 161 with dissolve_04
    show satoko se wa_b1 at sprava with right_03
    a_s "\"Все ли взяли себе по стакану?"
    extend " Сок тёплый станет, если скоро тост не поднимем!\""
    show shion si def_b1 at sleva with left_03
    a_h "\"Кто здравицу-то произнесёт, а, сестрица?\""
    hide satoko with left_03
    show mion se wink_b2 at sprava with right_03
    a_m "\"А почему бы не Рэна?"
    extend " Давай, Рэна, говори!\""
    nvl clear
    hide shion
    hide mion
    with dissolve_04
    show rena se wa_a1 at central with dissolve_04
    a_r "\"Э-э... Кхм!"
    extend " Все, кто довёл до конца «Главу о Хлопковых Корабликах», — отличная работа, все молодцы!!\""
    a_n "{nw}"
    play music msys01
    a_n "\"\"\"ОТЛИИИИЧНООО!!!!\"\"\""
    a_n "{nw}"
    a_n "УРААААА!!! Хлоп-хлоп-хлоп-хлоп!!!!"
    nvl clear
    scene bg 166 with left_03
    show tomi si_wa at sprava with right_03
    a_t "\"Ну и, раз уж мы собрались!"
    extend " Давайте, что ль, опять главу обсудим?\""
    show rena se def_b1 at sleva with left_03
    a_r "\"Конечно."
    extend " Давайте поговорим."
    extend " У кого какое мнение-е?!\""
    nvl clear
    scene bg 163 with left_03
    play music msys04
    show satoko se aku_a1 at sprava with dissolve_04
    a_s "\"Ну какое может быть мнение — разве не очевидно же?"
    extend " Виновна Мион-сан!"
    extend " А главные негодяи — семья Сонодзаки!"
    extend " Вот и всё, и спорить тут не о чем.\""
    show rena se nande_b1 at sleva with left_03
    a_r "\"Хммм... да, ты права."
    extend " Но я всегда верила... что Мии-тян уж точно не виновна...\""
    hide satoko with left_03
    show shion si aku_a1 at sprava with right_03
    a_h "\"Ну и добрая же вы душа!"
    extend " Уже по прохождении предыдущей Главы, «О Похищенных Демонами», было совершенно всё ясно!"
    extend " Более того, разве не так получилось, как все ожидали?\""
    nvl clear
    hide rena with right_03
    show ooishi si def_a1 at sleva behind shion with left_03
    a_o "\"Правда ваша."
    extend " Полагаю, большинство прошедших предыдущую главу ожидали чего-то такого.\""
    hide shion with left_03
    show rika se ni_a1 at sprava with right_03
    a_f "\"......Видимо, все ждали такого хода событий.\""
    nvl clear
    scene bg 161 with right_03
    show rena se nande_b1 at sprava with right_03
    a_r "\"Значит... серия игр «Хигураси но Наку Коро Ни»... практически кончилась?.."
    extend " Всему виной Мии-тян и семья Сонодзаки... вот и конец, значит?..\""
    show takano si_def at sleva with left_03
    a_y "\"Но как знать?"
    extend " Вообще-то я... пришла к выводу, что предположение «виновник есть род Сонодзаки» начинает терять в убедительности.\""
    hide rena with left_03
    show mion se def_a1 at sprava with right_03
    a_m "\"А, Миё-сан, вы тоже так думаете?"
    extend " Согласна."
    extend " ...Я не верю ни в какие проклятия."
    extend " Однако и вероятность того, что подлинные виновники — Сонодзаки, по крайней мере ослабла.\""
    nvl clear
    hide takano with right_03
    show rena se bik_a1 at sleva with left_03
    a_r "\"А?"
    extend " Но почему?.."
    extend " Мии-тян же признала, что всех прикончила, так?..\""
    hide mion with left_03
    show satoko se bik_a1 at sprava with right_03
    a_s "\"Именно."
    extend " Она убила меня с Рикой — и вы после этого смеете считать её невиновной??\""
    nvl clear
    hide rena with right_03
    show mion se maji_b1 at sleva with left_03
    a_m "\"Я не то чтобы навожу туман,"
    extend " просто как-то не очень разумно подозревать меня, Мион, во всём."
    extend " Если подумаете немного, поймёте сами.\""
    hide satoko with left_03
    show tomi si_wa at sprava with right_03
    a_t "\"Хм-м."
    extend " А я думаю, что есть какая-то доля истины в предположении о виновности семьи Сонодзаки..."
    extend " Хотел бы услышать, что думает по сему поводу Мион-тян!\""
    nvl clear
    hide mion
    hide tomi
    with dissolve_04
    show mion se tk_a2 at central with dissolve_04
    a_m "\"Как пожелаете."
    a_m "...Помните, как в конце я призналась, что участвовала во всех прошлых событиях?"
    extend " И вот ощущается тут какая-то неестественность, правильно?"
    extend " Подумайте-ка хорошенько."
    extend " Ежели впрямь семья Сонодзаки стоит за всеми прошлыми случаями, то разве не круты они?!"
    a_m "Ведь преступления все до единого идеальны, так ведь?"
    extend " Они всё-всё-всё провернули так, что либо дело оказывается несчастным случаем, либо виновник — не род Сонодзаки, а кто-то другой.\""
    nvl clear
    scene bg 165 with left_03
    show shion si wink_a1 at sleva with left_03
    a_h "\"Ну, ясное же дело."
    extend " Семья Сонодзаки всё-таки. Она способна тайком провести что угодно."
    extend " Что ей стоит какое-то там идеальное преступление?\""
    show mion se wink_b2 at sprava with dissolve_04
    a_m "\"Именно, именно. Именно про это самое ощущение я и говорю!"
    extend " За прошедшие четыре года она убивала да похищала людей, и никто ведь никаких следов семьи Сонодзаки не находил?"
    show mion se aku_a1 with dissolve_02
    a_m "Но вот на пятом году совсем иное дело."
    extend " Убивали одного за другим, особо не разбираясь."
    extend " И притом так легко примечается след Сонодзаки.\""
    nvl clear
    hide shion with left_03
    show rena se nande_a1 at sleva with left_03
    a_r "\"И верно же."
    extend " В прошлом всякий случай был загадочен, и никто не сказал бы наверняка, проклятие то или преступление..."
    extend " А вот в пятом году всё грубо так, неискусно.\""
    nvl clear
    scene bg 166 with left_03
    show satoko se bik_a1 at sprava with right_03
    a_s "\"Смысл ваших слов непонятен."
    extend " Рика, ты что-нибудь поняла?\""
    show rika se de_a1 at sleva with left_03
    a_f "\"......Иначе говоря, если бы виновата была действительно семья Сонодзаки, они бы и в пятом году проделали не менее блестящую работу.\""
    show satoko se aki_a1 with dissolve_02
    a_s "\"И... что же ты хочешь сказать?"
    extend " Мион-сан отнюдь не убивала меня да Рику, а сделал то демон, который вселился в Мион-сан?"
    show satoko se wa_a1 with dissolve_02
    a_s "Ага, ага-а!!"
    extend " Как я считала и раньше, Мион-сан, оказывается, вовсе не плохая личность!!\""
    nvl clear
    scene bg 163 with right_03
    show rena se def_b1 at sprava with right_03
    a_r "\"Вот-вот."
    extend " Мы — я да Сатоко-тян — говорили, что виновато нечто, в неё вселившееся."
    extend " Значит... мы всё-таки оказались правы?!\""
    show ooishi si def_a1 at sleva behind rena with left_03
    a_o "\"В прошлый раз я склонялся к мысли, что всё-таки дело в проклятии, но данная глава ещё больше меня убедила."
    extend " Сообщённое мною в самом конце"
    extend " — о том, что Такано-сан и Мион-сан видели живьём после их смерти, — подтверждает мои предположения.\""
    nvl clear
    hide ooishi with right_03
    show takano si_def at sleva with left_03
    a_y "\"Ого..."
    extend " Вижу, теперь у сторонников проклятия появились сильные доводы."
    extend " Есть ли что возразить на них стороне преступника-человека?\""
    show rena se wa_b1 with dissolve_02
    a_r "\"В прошлый раз сторону «человека» заняли Мии-тян да Рика-тян."
    extend " Да ещё Томитаке-сан, точно."
    extend " В таком случае прошу не скупиться на возражения!\""
    nvl clear
    scene bg 161 with left_03
    show tomi si_uh at sprava with right_03
    a_t "\"Хммм, эх."
    extend " Даже не знаю, как бы сказать подходяще...\""
    show shion si def_a1 at sleva behind tomi with left_03
    a_h "\"Одним из оснований для веры в «Проклятие» является загадочное время смертей, так?"
    extend " А если я раскрою, в чём тут штука, то предположение «Человек» подтвердится?\""
    hide tomi with left_03
    show mion se wink_a1 at sprava with right_03
    a_m "\"О, Шион, у тебя есть чем возразить?\""
    nvl clear
    a_h "\"Посмотрим."
    extend " Итак, сестра, я согласна с тобой насчёт «человека»... но вот в чём не согласна, так в том, что главные виновники — семья Сонодзаки."
    extend " Закончить ли мне на этом, или позволите продолжать?\""
    hide mion with left_03
    show satoko se wa_a1 at sprava with right_03
    a_s "\"О-хо-хо-хо!"
    extend " Прошу любезно!"
    extend " Коль говорите, что дело не в проклятии, так докажите!!\""
    nvl clear
    scene bg 165 with right_03
    show takano si_def at sprava with right_03
    a_y "\"Что же, Шион-тян,"
    extend " объясни нам ту самую, последнюю, хитрость."
    extend " Если Мион-тян упала в колодец и разбилась в день того происшествия, каким образом она появилась несколько дней спустя и убила тебя с Кейти-куном?\""
    nvl clear
    show shion si wa_a1 at sleva with left_03
    a_h "\"Очень просто. Дело в сёстрах Сонодзаки."
    extend " А подтверждается оно так."
    extend " Потому что сеструха уже померла, только я могла пырнуть Кей-тяна ножом. Я притворилась сестрой и пырнула Кей-тяна!"
    a_h "Потом же вернулась к себе в комнату, подралась с привидением, а затем спрыгнула с балкона, покончив жизнь самоубийством.\""
    hide takano with left_03
    show tomi si_def at sprava with right_03
    a_t "\"В таком случае Мион-тян достаётся вся грязь."
    extend " Она убивает старосту деревни, остальных, выставляя Шион-тян жертвой,"
    extend " и, пока она таится в колодце, Шион-тян может убивать кого и сколько угодно.\""
    nvl clear
    hide shion with right_03
    show ooishi si def_a1 at sleva behind tomi with left_03
    a_o "\"Ясно..."
    extend " Ежели дело так, тогда Мион-сан дважды оплошала."
    a_o "Во-первых, её (труп) обнаружили, а во-вторых — она погибла тогда, когда должна была скрываться."
    extend " Так оно получается.\""
    hide tomi with left_03
    show rena se nande_a1 at sprava with right_03
    a_r "\"...Ого-го......"
    extend " Точно... Похоже на то...\""
    nvl clear
    hide ooishi with right_03
    show mion se to_a1 at sleva with left_03
    a_m "\"Но... я всё-таки не согласна!"
    extend " Чересчур дело не похоже на прежние идеальные преступления."
    extend " Пускай удался бы замысел, «Мион» ведь всё равно преступница, да?"
    extend " Ей пришлось бы всю жизнь либо скрываться, либо изображать из себя Шион?"
    a_m "Незавидная же участь!"
    extend " Это никакое не идеальное преступление!\""
    hide rena with left_03
    show rika se de_a1 at sprava with right_03
    a_n "{nw}"
    a_f "\"......Говоря коротко, пропади она иль погибни, Мии перестанет быть в любом случае.\""
    nvl clear
    hide mion with right_03
    show shion si wink_b1 at sleva with left_03
    a_h "\"Соображаешь, Рика-тян."
    extend " В общем, то, что Сонодзаки Мион сойдёт со сцены, является частью замысла."
    extend " Поэтому-то Мион берёт на себя ответ за все-все происшествия."
    extend " Берёт на себя всю вину и уходит!\""
    nvl clear
    hide rika with left_03
    show mion se wink_b1 at sprava with right_03
    a_m "\"И таким образом прикрывает подлинного виновника."
    extend " Стало быть, случай нынешнего лета вовсе не иное дело — нет, он завершает все прошлые происшествия, делая их «идеальными преступлениями»."
    extend " Как-то так, наверно?..\""
    scene bg 161 with left_03
    show takano si_def at sprava with right_03
    a_y "\"Юная глава семьи Сонодзаки, более всех подозреваемая, признаётся во всём и пропадает......"
    extend " Ах, какая подходящая концовка для настоящего виновника, не происходящего из рода Сонодзаки.\""
    nvl clear
    show satoko se aku_b1 at sleva with left_03
    a_s "\".........И я всё так же ничегошеньки не пойму......"
    extend " Что вы хотите сказать — Мион-сан взяла на себя всю вину?"
    extend " Неужели вы всё-таки не считаете её преступницей??...\""
    nvl clear
    hide takano with left_03
    show rena se def_b1 at sprava with left_03
    a_r "\"Понимаешь,"
    extend " есть подлинный виновник серии загадочных смертей."
    extend " И, чтобы его защитить, Мии-тян солгала, что «виновата во всём, в том числе и в предыдущих происшествиях»... вот что все хотят объяснить.\""
    hide satoko with right_03
    show ooishi si wa_a1 at sleva behind rena with left_03
    a_o "\"Ох, ну надо же...... Это ж я должен был сказать... Ну, точно — выдающийся детектив!"
    extend " Да уж... весьма убедительно!\""
    nvl clear
    scene bg 163 with right_03
    show mion se def_b2 at sprava with right_03
    a_m "\"Она совершила преступление, чтобы прикрыть подлинного виновника."
    extend " Так я считаю."
    extend " И ещё выскажу мнение, что преступник — некто не из рода Сонодзаки.\""
    show takano si_wa at sleva behind mion with left_03
    a_y "\"Стало быть, некто четыре года подряд совершал идеальные преступления, а в пятом году Мион-тян, дабы защитить его лучше, «натворила преступлений с целью воспрепятствовать расследованию». Права ли я?\""
    show mion se wink_a1 with dissolve_02
    a_m "\"Вот именно."
    extend " По-моему, тот «начальник» из предыдущей Главы довольно-таки подозрителен!\""
    hide takano with right_03
    show rika se wa_a1 at sleva with left_03
    a_f "\"......Потрясена."
    extend " Действительно, весьма логично\""
    extend ", — хлоп-хлоп-хлоп."
    nvl clear
    scene bg 166 with left_03
    show shion si def_b1 at sprava with right_03
    a_h "\"Всё же я думаю, что род Сонодзаки да сёстры виновны."
    extend " Сёстры совершали преступления, чтобы «искупить прошлое», разрубив оковы Трёх великих родов."
    extend " Так считаю я.\""
    nvl clear
    show tomi si_def at sleva with left_03
    a_t "\"«Искупить прошлое», то есть..."
    extend " Мион, как последняя глава рода, взяла на себя ответ за все тайные преступления Трёх родов, чтобы раз и навсегда покончить с их тёмным прошлым, после чего сёстры ушли.\""
    a_h "\"Да, именно так."
    extend " Нам, сестричкам, пришлось принимать тяжёлое решение, поэтому-то Глава вышла такой печальной."
    show shion si wink_b1 with dissolve_02
    extend " А-ха, да уж, это как-то чересчур!\""
    nvl clear
    hide tomi with right_03
    show rika se wa_a1 at sleva with left_03
    a_f "\"......Потрясена."
    extend " Действительно, весьма логично\""
    extend ", — хлоп-хлоп-хлоп."
    hide shion with left_03
    show rena se wa_a1 at sprava with right_03
    a_r "\"Хм-м?"
    extend " Кажется, Рика-тян тоже хочет что-то сказать."
    extend " Рика-тян, мы тебя слушаем!\""
    nvl clear
    show rika se ni_a1 with dissolve_02
    a_f "\"......Вопрос ко всем же..."
    extend " За что Кейти получил удар ножом?\""
    hide rena with right_03
    show satoko se def_a1 at sprava with right_03
    a_s "\"Ну, понятное же дело, Рика..."
    extend " Он забрался в обрядовое хранилище, куда просто так не позволено заходить.\""
    hide rika with left_03
    show ooishi si def_a1 at sleva with left_03
    a_o "\"Судя по-вашему, значит, и в прошлой главе Томитаке-кун и Такано-сан скончались из-за того, что пробрались в обрядовое хранилище."
    extend " .....................А?\""
    nvl clear
    scene bg 161 with right_03
    show takano si_wa at sprava with right_03
    a_y "\"Хи-хи-хи-хи......"
    extend " Что-то у вас не сходится.\""
    show rena se bik_a1 at sleva behind takano with left_03
    a_r "\"Э?"
    extend " В каком смысле не сходится?..\""
    show satoko se bik_b1 at central behind takano with dissolve_04
    a_s "\"Ах!!..."
    extend " Рэна-сан, точно же!"
    extend " Помните?!\""
    nvl clear
    scene bg 163 with left_03
    show rika se de_a1 at central with dissolve_04
    a_f "\"......Вот именно же."
    extend " В прошлой главе Кейти хотели убить, хотя в обрядовое хранилище не забирался он.\""
    nvl clear
    hide rika with dissolve_02
    a_n "Поднялся взволнованный гам!.."
    nvl clear
    show tomi si_uh at sprava with right_03
    a_t "\"Так он же......{w=1.0} а, знаю!"
    extend " Хинамидзава ж не любит чужаков?"
    extend " Вот поэтому Кейти-куна и хотели убить!..\""
    show mion se to_a1 at sleva with left_03
    a_m "\"Да ну, чепуха..."
    extend " Тогда бы и родители Кей-тяна под удар попали."
    extend " Но с ними-то ничего не случилось, как ни крути."
    extend " Ни тогда, ни сейчас.\""
    nvl clear
    scene bg 166 with right_03
    show satoko se aku_a1 at sprava with right_03
    a_s "\"Ну что, дорогие поклонники «Человека»?!"
    extend " Пока не объясните, зачем кому-то убивать Кейти-сана, разве сможете вы доказать свои убеждения?!!!\""
    show ooishi si wa_a1 at sleva with left_03
    a_o "\"Н-а-ха-ха-ха."
    extend " Но ведь и сторона «Проклятия» должна бы сперва объяснить, почему на Маэбару-сана напали как тогда, так и теперь.\""
    nvl clear
    hide satoko with left_03
    show rena se def_b1 at sprava with right_03
    a_r "\"Вот, казалось, почти подтвердили одно..."
    extend " а загадок-то ещё, оказывается, много...\""
    hide ooishi with right_03
    show takano si_def at sleva with left_03
    a_y "\"Хи-хи......"
    extend " Кроме гибели Кейти-куна, любой смерти можно найти объяснение... и лишь с ним почему-то никогда толком не ясно."
    extend " И тогда, и сейчас."
    extend " Нападения на него никак не относятся к его проникновению в Сайгудэн.\""
    hide rena with left_03
    show satoko se bik_b1 at sprava with right_03
    a_s "\"......Значит, и в прошлый раз, и теперь он совершил что-то, за что некто возжелал его смерти?..\""
    nvl clear
    scene bg 165 with right_03
    show ooishi si def_a1 at sprava with right_03
    a_o "\"...Понял..."
    extend " Если сумеем найти общие черты в действиях того Маэбары-сана и нынешнего... тогда, может быть, найдём ключ к разгадке всего...\""
    show tomi si_def at sleva behind ooishi with left_03
    a_t "\"Я наскоро прочитал оба сценария... и, насколько помню, Кейти-кун всегда вёл себя как обычно."
    extend " Разве что в хранилище обрядовых принадлежностей пробрался, а так ничего сомнительного в его повседневной жизни нет!\""
    hide ooishi with left_03
    show rena se ko_a1 at sprava with right_03
    a_r "\"Хммм..."
    extend " Что же Кейти-кун в обоих сценариях такого натворил?.."
    extend " В чём же он так провинился, что его убивают!\""
    hide tomi with left_03
    show rika se wa_a1 at sleva with left_03
    a_f "\"......Раз не знаем, так давайте спросим у него самого же.\""
    nvl clear
    stop music fadeout 1.0
    scene black with dissolve_04
    play ambient lsys17
    $ renpy.pause(2.0)
    stop ambient fadeout 0.1
    play music msys03_treat
    scene bg 011 with dissolve_04
    a_k "\"Эххх......"
    extend " Опять вы без меня веселитесь, пока я тут в одиночку сценарий читаю..."
    extend " Эээх...\""
    nvl clear
    scene bg 165
    show rena se nande_b1 at sprava
    with up
    a_r "\"Так это..."
    extend " Кейти-кун, попробуй, пожалуйста, найти в себе ответ......\""
    show mion se aku_a1 at sleva behind rena with right_03
    a_m "\"Кей-тян, за какие такие проступки тебя убивают?\""
    hide rena with left_03
    show satoko se aku_a1 at sprava with right_03
    a_s "\"Пренепременно за то, что постоянно меня шпыняет!!\""
    hide mion with right_03
    show rika se wa_a1 at sleva with left_03
    a_f "\"За грудь меня трогал, вот в чём он виноват.\""
    hide satoko with left_03
    show tomi si_wa at sprava with left_03
    a_t "\"Вот-вот!"
    extend " На мой взгляд, счастье каждый день находиться в окружении прекрасных девушек само по себе можно считать преступлением!\""
    nvl clear
    hide rika with right_03
    show ooishi si wa_a1 at sleva behind tomi with left_03
    a_o "\"Н-а-ха-ха-ха-ха!!"
    extend " Точно, преступление особой тяжести!"
    extend " Ах, ну кто бы не позавидовал его положению главного героя?"
    extend " Пожалуйста, дайте позаменять его хоть раз в жизни.\""
    hide tomi with left_03
    show takano si_fu at sprava with right_03
    a_y "\"Хи-хи-хи!.."
    extend " Положим, да: если учесть то хорошее, что ему выпало, — пожалуй, получить в итоге ножом в живот не такая уж и большая цена.\""
    nvl clear
    hide ooishi
    hide takano
    with dissolve_04
    show satoko se aku_a1 at central with dissolve_04
    a_s "\"Так что, Кейти-сан."
    extend " Припоминаете ли вы совершённый грех?\""
    play sound wa_006
    a_k "\"ММммМММММ!!!!" with Shake((0, 0, 0, 0), 1.0, dist=50)
    extend " И сейчас, и тогда!!"
    extend " Да что я сделал, чтоб заслужить такую жуткую участь!!"
    extend " И вы хотите, чтоб я нашёл ответ в себе?!"
    play sound wa_006
    extend " Я сам хочу знать — ЗА ЧТО ВЫ ВСЕ НА МЕНЯ ОПОЛЧИ-И-И-И-ИЛИИИСЬ?!!!\""
    nvl clear
    scene bg 161 with left_03
    play music msys02
    show rika se wa_a1 at sprava with right_03
    a_f "\".........Бедненький, бедненький."
    extend " Я тебя при встрече поглажу.\""
    show shion si def_a1 at sleva with left_03
    a_h "\"А не перечитать ли мне «Главу о Похищенных Демонами» после этой?..\""
    hide rika with left_03
    show mion se wink_a1 at sprava with right_03
    a_m "\"А я перечитаю «Главу о Хлопковых Корабликах» со стороны Мион."
    extend " Вдруг найду что-нибудь этакое, отличающееся от взгляда Кей-тяна на события.\""
    hide shion with right_03
    show satoko se wa_b1 at sleva with left_03
    a_s "\"А по-моему, так «демоны» всему виной!!"
    extend " Все хитрые штучки с необъяснимыми случаями объясняются работой «демонов»!!!\""
    show rika se wa_a1 at central with dissolve_04
    a_f "\"......Прямо плазма какая-то.\""
    nvl clear
    scene bg 165 with right_03
    show rena se def_a1 at sprava with right_03
    a_r "\"А каковы ваши мысли, товарищи читатели?"
    extend " Пожалуйста, не стесняйтесь присылать свои мнения!\""
    show mion se wa_b2 at sleva with dissolve_04
    a_m "\"Куда, говорите? Да в Заметках указано, в разделе «Пара слов о переводчиках»!!"
    extend " Автору прислать их вы опоздали, а вот переводчик покамест ещё рад почитать взрослый и вежливый обмен мнениями (не участвуя в нём)!!!\""
    nvl clear
    hide mion with dissolve_04
    show rena se wa_b1 with dissolve_02
    a_r "\"А теперь предлагаем пройти следующую игру в серии «Когда плачут цикады» — «Главу о Смертоносном Проклятии»!!!\""
    nvl clear
    show cinema with x_15
    show title02 with Dissolve(3.0)
    $ renpy.pause(2.0)
    show black behind title02 with Dissolve(3.0)
    $ renpy.pause(1.0)
    scene black with right_30
    stop music fadeout 1.0
    $ renpy.pause(1.0, hard=True)
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
