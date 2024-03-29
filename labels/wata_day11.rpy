    $ save_name = "Глава о Хлопковых Корабликах.\nДень Одиннадцатый, новое утро"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene white with Dissolve(1.0)
    scene bg 082 with Dissolve(3.0)
    play music msys06
    n "......Знакомый потолок."
    n "Сознание не прояснилось до конца... но я лежу под своим одеялом, как в любое другое утро."
    nvl clear
    n "Взглянул на часы... Так поздно лёг нынче спать, а сейчас то же самое время, в которое просыпаюсь всегда."
    n "{nw}"
    n "Неужто я смог проснуться в тот же самый час... хоть и поспав так мало?"
    n "......Чем дивиться загадочной природе человечьего тела, я скорее охреневал..."
    nvl clear
    n "Если опять тут засну, то хоть из пушки стреляй, не разбудишь......"
    extend " а потому я с большим трудом заставил себя встать с кровати."
    nvl clear
    scene black with left
    scene bg 210 with left
    n "За завтраком мать расспрашивала про прошедшую ночь."
    n "......Видимо, нам также звонили — спросить, не знаем ли мы, где Рика-тян и Сатоко, — потому мама немного догадывалась, что стряслось."
    nvl clear
    n "\"...Так ты до поздней ночи разыскивал их вместе с друзьями?\""
    n "\"..................Где-то до трёх, наверно..."
    extend "......... ага.\""
    n "\"......Так вы их нашли?"
    extend " Рику-тян и Сатоко-тян этих?\""
    nvl clear
    n "{b}*Хруп*{/b}."
    n "............Я вгрызся в жареный ломоть хлеба."
    extend " Вкуса не ощутил..."
    nvl clear
    play sound wa_028
    $ renpy.pause(2.0)
    n "Тут динь-динькнул дверной звонок."
    n "Глядь на часы — я уже пять минут как должен был встретиться с Рэной......"
    extend " Рэна и заявилась."
    nvl clear
    scene white with left_03
    scene bg 020 with left_03
    show rena se nande_a1 at central with dissolve_04
    n "\"Утра......"
    extend " Ты хоть немного поспал? ...поспал?\""
    n "\"...Сколько поспал, сам не знаю..."
    extend " Сдаётся, те часы можно пересчитать по куриным лапкам.\""
    show rena se wa_a1 with dissolve_02
    n "\"А-ха-ха-ха-ха.\""
    n "Рэна сама выглядит невыспавшейся..."
    extend " Привычной жизнерадостности ей не хватало."
    nvl clear
    n "\"......Пошли, что ли... в школу?\""
    n "\"Угу..."
    extend " Пожалуй, так лучше.\""
    n "Она улыбнулась, хоть и немного скованно."
    n "{nw}"
    n "Тоже, верно, за пропавших волнуется."
    n "Но, говорит, в школу идти всё равно надо."
    nvl clear
    show rena se def_a1 with dissolve_02
    n "\"......Если сегодня не пойдёшь, точно будешь изнывать от тревоги, пока спать не ляжешь..."
    extend " А я этого не хочу..."
    extend " поэтому пойдём вместе.\""
    n "\".........Ладно."
    extend " Погоди немного,"
    extend " соберу сумку.\""
    n "Искренняя забота Рэны... немного подняла настроение."
    nvl clear
    scene white with right_03
    stop music fadeout 1.0
    play ambient lsys22
    scene bg 066 with right_03
    n "Мы добрались до точки встречи с Мион, каковой там не оказалось."
    n "...Я-то думал, она будет ждать нас, раз мы запаздываем..."
    nvl clear
    show rena se hau_a1 at sprava with right_03
    n "\"Нынче Мии-тян могла и не смочь подняться...\""
    n "\"А... и верно......"
    extend " Ей-то не только нынешней ночью туго пришлось..."
    extend " Она ж и позавчера целую ночь не спала, искала деревенского старшего...\""
    n "Мы подождали ещё..."
    extend " Подошло время идти. Переглянулись."
    nvl clear
    n "\"Ну чё?.."
    extend " Ждём ещё?\""
    stop ambient fadeout 1.0
    play sound wa_026
    n "{nw}"
    n "Тут от свежего утреннего воздуха в мозгу наконец прояснилось... На ум пришли слова, ночью сказанные Ооиси-саном."
    n "Глав Трёх великих родов убирают одного за другим,"
    extend " и следующей... может стать глава семьи Сонодзаки..."
    n "{nw}"
    n "Но Мион же.............. она-то, конечно......"
    nvl clear
    play ambient lsys22
    show rena se def_b1 with dissolve_02
    n "\".........Пойдём."
    extend " Пускай сегодня поспит.\""
    n "Рэна легонечко хлопнула меня по спине."
    nvl clear
    n "\"Но вот правда ли......{w=1.0} Мион там......\""
    show rena se wa_a1 with dissolve_02
    n "\"Хм?"
    extend " Что говоришь?\""
    n "\"А... да так, сам с собой......"
    extend " Пошли, чё уж.\""
    n "Мы отправились во школу вдвоём."
    nvl clear
    scene white with right_03
    stop ambient fadeout 1.0
    scene bg 039 with right_03
    play music msys06
    n "По пути видел многих одноклассников идущими в школу с родителями."
    n "Некоторых родители везли на машине..."
    nvl clear
    scene bg 093 with right_03
    n "Директор стоял у школьных ворот, как страж."
    extend " Впервые такое вижу."
    nvl clear
    n "\"Здравствуйте.\""
    n "\"И вам здоровьица.\""
    n "Директор кланялся родителям."
    extend " Несколько пуг{u}а{/u}ло, что рядом с ним к стене прислонён деревянный меч..."
    nvl clear
    n "\"Маэбара-кун, доброе утро."
    extend " Доброе утро, Рюгу-кун.\""
    show rena se bik_b1 at sprava with right_03
    n "\"З-Здравствуйте...\""
    n "\"Поскорее идите в класс, учительница сделает важное объявление."
    extend " ...Хорошо?\""
    n "Мы оба отмолчались."
    n "{nw}"
    n "......Казалось, будто..."
    extend " ночное безумие выбралось наконец под свет солнца......"
    nvl clear
    scene black with Dissolve(1.0)
    stop music fadeout 1.0
    play sound wa_001
    $ renpy.pause(2.0)
    play sound wa_020
    scene bg 109 with left_03
    show chie si_def at sprava with dissolve_04
    play ambient lsys12
    n "\"Доброго всем утра.\""
    n "Только учительница вошла в комнату, как летавший по классу шёпот разом улёгся, словно его и не было..."
    extend " Наступила полнейшая тишина."
    n "{nw}"
    n "С учительницей зашёл сам директор..."
    extend " Видно: утро далеко не обычное."
    nvl clear
    n "\"Сначала директор сделает важное объявление."
    extend " Говорите, пожалуйста.\""
    hide chie with right_03
    n "Откашлявшись, директор встал за кафедру."
    nvl clear
    n "\"......Возможно, кое-кто из вас уже знает.\""
    n "......В комнате стало тихо."
    n "......Все смотрели на незанятые места Рики-тян и Сатоко."
    nvl clear
    scene bg 108 with right_03
    n "Директор в двух словах объяснил, что Рика-тян и Сатоко пропали."
    n "Здесь не было тех, кто не знал бы этого..."
    extend " Но многие до сих пор не могли поверить..."
    n "{nw}"
    n "И для них слово директора стало решающим доказательством."
    nvl clear
    n "......По всему классу там и сям послышались всхлипыванья..."
    n "Потом они наполнили всё помещение..."
    n "Директор у нас человек невозмутимый, но и он сейчас не сумел их выдержать..."
    nvl clear
    show chie si_def at sprava with left_03
    n "\"Так, ребята, слушайте все!"
    extend " С нынешнего дня всегда приходите и уходите в сопровождении родителей."
    extend " Те, чьи родители не могут вас забирать, — ходите вместе с другими."
    extend " Мы напечатали памятку, пускай каждый покажет её родителям."
    extend " Всем всё ясно?!\""
    n "Довольно резко проговорила учительница."
    n "......Ей самой не удаётся скрыть напряжённости, охватившей её из-за такого невиданного происшествия..."
    nvl clear
    n "Лучше бы уж закрыли школу на время."
    n "Но, как сказала Рэна, некоторые родители не желают закрытия школы, потому как работают в семье оба, полагаясь в плане попечительства на школу."
    nvl clear
    n "\"Итак, начинаю урок."
    extend " Староста класса...... ох, её нет сегодня..."
    extend " Значит, слово дежурному!\""
    n "\"Вста-а-а-ать.\""
    n "{nw}"
    n "Пусть нынче всё слетело с катушек, хотя бы школа должна оставаться в привычном виде...... С этим я соглашусь пока что."
    nvl clear
    scene black with Dissolve(1.0)
    scene bg 028 with Dissolve(1.0)
    $ renpy.pause(4.0)
    play sound wa_001
    $ renpy.pause(2.0)
    scene black with Dissolve(1.0)
    stop ambient fadeout 1.0
    scene bg 110 with up
    play music msys06
    n "Обычно учительница обедает в учительской комнате, но сегодня она осталась с нами."
    n "Не удержался от смеха, завидя пресловутый обед из карри... но со мной не посмеялся никто......"
    nvl clear
    scene bg 109 with left_03
    n "Рэна подсела ко мне со стулом и своею коробкой."
    n "Сегодня... из круга друзей остались только мы двое."
    extend " От того, что не надо было сдвигать парты, защемило в груди."
    nvl clear
    show rena se hau_a1 at central with dissolve_04
    n "\"...Спать хочется, да.\""
    n "\"Ага..."
    extend " Но мне теперь без разницы..."
    extend " Я скорее... завидую железобетонности нервов тех, кто способен теперь уснуть.\""
    show rena se wa_b1 with dissolve_02
    n "\"А-ха-ха-ха, согласна.\""
    nvl clear
    n "Утром страшно хотелось спать... но в напряжении, охватившем сегодня школу, весь сон как рукой сняло."
    n "Коробке Рэны недоставало всегдашнего великолепия."
    n "{nw}"
    n "...Чему тут удивляться."
    n "Она сама не ложилась спать допоздна."
    n "Вряд ли у неё хватило бы времени, чтоб сготовить какой-никакой обед..."
    extend " Да и спозаранку-то вряд ли подняться смогла..."
    nvl clear
    n "\"...Бери мой, не стесняйся."
    extend " Уж сегодня-то мой обед получше будет, признай.\""
    show rena se hau_b1 with dissolve_02
    n "\"Л-ладно... с твоего позволения."
    extend " Ух ты-ы... какой хороший рыбный рулетик с посыпкой из сыра.\""
    n "\"Да и ты, Рэна, отнюдь не подкачала, если уж честно. Хоть и покупное, а всё равно прилично.\""
    nvl clear
    n "......Я понял, что мы оба изо всех сил пытаемся вести себя как обычно."
    n "......Оглядел класс... Так вели себя только мы, все другие же выглядели подавленными."
    nvl clear
    show rena se wa_a1 with dissolve_02
    n "\"......Хи-хи-хи!"
    extend " Знаешь, мы так едим друг у друга из коробочек... будто...{w=0.8}{nw}"
    extend " ммм...{w=0.7}{nw}"
    extend "......... Ну, понимаешь!{w=1.0}{nw}"
    extend " Хау-у-у...\""
    n "\"Ха-ха-ха...... ха ха......\""
    n "\".........А ха ха ха.........\""
    n "Смех наш быстро утих..."
    extend " мой первым..."
    nvl clear
    n "\"Прости."
    extend " Мне, в общем...... жаль.\""
    show rena se nande_a1 with dissolve_02
    n "\"Не-не......... нормально."
    extend " Что поделаешь.\""
    n "Наши палочки для еды... повисли в воздухе..."
    extend " Мы больше так не могли."
    nvl clear
    stop music fadeout 1.0
    play ambient lsys12
    n "\"......Рика-тян и Сатоко{w=1.0}...... где ж они-то теперь?\""
    n "Жестокие, наверно, слова."
    n "Я напрямую заговорил... о том, про что все думали, но пытались не упоминать..."
    extend " Заметил — Рэна задержала дыхание..."
    nvl clear
    show rena se ko_a1 with dissolve_02
    n "\"..................Вчера Рэна многое услышала, пока Кейти-кун отсутствовал... Расскажу тебе, что разузнала.\""
    n "\"..................Извини за вчерашнее."
    extend " ......Расскажи, пожалуйста.\""
    nvl clear
    play music msys07
    n "Пока меня не было, Рэна помогала явившемуся женскому кружку варить суп."
    n "{nw}"
    n "Она слушала, как жители деревни докладывают о том, что узнали."
    nvl clear
    n "\"......Но так ничего точно и не узнали?"
    extend " Разве только, что те куда-то вдвоём отправились на велосипедах, вернувшись домой с уроков...\""
    n "{nw}"
    n "Так сказала вчера Мион..."
    extend " Зацепок — никаких."
    nvl clear
    show rena se nande_a1 with dissolve_02
    n "\"Угу..."
    extend " Полицейский сказал, они поехали куда-то поиграть, сразу после того как вернулись домой."
    n "А поехать куда-то играть сразу после возвращения домой...{w=1.0} можно в город, так?"
    n "......Посему вывод — они, верно, пропали где-то в Окиномии."
    extend " Полицейские обещали, после рассвета начнут смотреть ещё и в Окиномии.\""
    nvl clear
    scene black with Dissolve(1.0)
    scene bg 124 with Dissolve(1.0)
    n "Город?.."
    n "Коли так...... понятно, почему мы не могли отыскать их в Хинамидзаве."
    n "{nw}"
    n "Только... что-то, чую, не так..."
    n "Почему вот, не знаю...... но чувство есть..."
    nvl clear
    scene bg 094 with Dissolve(1.0)
    show rika se de_a1 at central with dissolve_04
    n "Тем днём я признался перед Рикой-тян кое в чём очень важном."
    n "Рика-тян сказала, чтоб я на неё положился..."
    extend " а потом... хмм, что же она сказала..."
    nvl clear
    n "Ах да, она сказала вроде бы, что если не постарается, то с одной из собачек тоже может случиться что-то плохое."
    n "{nw}"
    n "Кошки, собаки...... не знаю, кого именно Рика-тян так называла... но сдаётся мне, что вопрос отлагательства не терпел."
    nvl clear
    scene black with dissolve_04
    n "ЧЁРТ!!!....."
    n "Я тогда... свалил на неё все собственные заботы... и убежал!"
    n "{nw}"
    n "Теперь думаю... не следовало убегать."
    extend " Надо было попросить рассказать поподробнее... о тех собаках и кошках."
    n "Чем больше вспоминаю... тем больше вижу своих ошибок!!"
    nvl clear
    n "......Ну да ладно... короче, не думаю, что Рика-тян в таком состоянии спокойно поехала бы куда-то играть."
    n "......Разумеется, ни доказательств, ни основания быть убеждённым у меня нет."
    extend " Простое наитие."
    nvl clear
    scene bg 108
    show rena se def_a1 at central
    with fastup
    n "\"Думаю............{w=1.0} они в город не поехали...\""
    nvl clear
    n "\"И ты так думаешь, Кейти-кун?"
    extend " Рэна согласна."
    extend " Рика-тян и Сатоко-тян определённо пропали в Хинамидзаве.\""
    n "Я в изумлении на неё воззрился."
    n "...Ибо в сказанных Рэной словах ощущалась большая уверенность."
    nvl clear
    hide rena with left_03
    n "Рэна, смолкнув, пошла в коридор, забрав коробку с обедом."
    nvl clear
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    $ save_name = "Глава о Хлопковых Корабликах.\nДень Одиннадцатый, чутьё Рэны"
    play sound wa_020
    scene white with right_03
    scene bg 019 with right_03
    show rena se wa_b1 at sprava with right_03
    n "\"...Пойду коробку помою.\""
    n "Будто хочет приостановить пока разговор."
    n "Но тут до меня дошло: разговор, вероятно, такого толка, что класс — место неподходящее."
    nvl clear
    hide rena with right_03
    n "Я торопливо сграбастал коробку и вышел следом за Рэной."
    nvl clear
    scene black with left_03
    n "Рэна пошла не в подсобку, где стояли раковина с водонагревателем, а к питьевому фонтанчику за школой, куда ученики редко заглядывали."
    nvl clear
    scene bg 095 with dissolve_04
    play ambient lsys12
    n "...Она вымыла свою коробку."
    n "...Ничего между тем не говоря."
    n "{nw}"
    n "Потом же, убедившись, что рядом никого нет, она открыла рот."
    nvl clear
    show rena se nande_b1 at central with dissolve_04
    n "\"...Я не могла поверить, что Рика-тян и Сатоко-тян поехали поиграть"
    extend " в город......... поэтому сама порасспрашивала народ.\""
    n "\"Порасспрашивала?"
    extend " Про что?\""
    n "\"Тётенек из женского кружка......"
    extend " Помнишь, вчера в супе плавало много кубиков тофу?"
    extend " Бабушка из лавки тофу семьи Томита тоже пришла...\""
    nvl clear
    n "Лавка тофу семьи Томита......"
    n "А-а, вспомнил..."
    n "Один из тех магазинчиков, что стоят рядком по дороге к больнице."
    n "У них там ещё в аквариуме постоянно плавали, будто купались, огромные куски тофу."
    nvl clear
    show rena se def_a1 with dissolve_02
    n "\"Бабуля вспомнила, что Сатоко-тян заходила к ней купить тофу по дороге домой из школы.\""
    n "\"......Тофу?"
    extend " По дороге из школы?"
    extend " Это чего, улика?\""
    show rena se ko_b1 with dissolve_02
    n "\"Слушай..."
    extend " Ты помнишь виденное в домике Рики-тян?\""
    n "Рэна отошла от фонтанчика и развела руки, показывая как бы комнату Рики-тян."
    nvl clear
    show rena se def_b1 with dissolve_02
    n "\"Когда мы там появились, на плите стояла кастрюлька с мисо-супом..."
    extend " Внутри было, пожалуй, с полпачки тофу."
    extend " Остальное нашла в холодильнике."
    show rena se wa_b1 with dissolve_02
    extend " Они готовили холодный тофу."
    extend " Тарелку в клейкую плёнку завернули.\""
    n "{nw}"
    n "Продолжая говорить, она ходила туда-сюда, словно находясь в комнате Рики-тян."
    nvl clear
    n "\"Так, Рэна... и что с того?\""
    n "\"Кейти-кун."
    extend " В мисо-суп тофу кладётся в последнюю очередь."
    n "Иными словами, Рика-тян ли готовила, Сатоко-тян ли, но готовящая стояла у плиты почти до самой поры подавать на стол ужин.\""
    nvl clear
    stop ambient fadeout 1.0
    play sound wa_023
    n "\"Почти до самой поры...{w=1.0} подавать ужин?!...\""
    play music silver_mirror
    n "{nw}"
    n "Ну да, вчера же их великов не нашли... вот по тому лишь и заключила полиция, что Рика-тян да Сатоко куда-то поехали поиграть?!..."
    nvl clear
    show rena se def_a1 with dissolve_02
    n "\"Я заглянула в угловую корзинку, она была жутко грязная..."
    extend " Пищу почти всегда готовит Рика-тян, однако временами Сатоко-тян тоже пробует."
    extend " А значит, в тот вечер готовила Сатоко-тян.\""
    nvl clear
    n "\"......Хочешь сказать......{w=1.0} Сатоко никуда играть не гоняла...{w=0.8} потому что готовила ужин?!...\"{nw}"
    play sound wa_022
    extend ""
    n "\"Угу."
    extend " Я и в рисоварку заглядывала."
    extend " Там риса хватало как раз на двоих.\""
    n "\"......То есть они приготовили еды на двоих, но так её и не съели..."
    extend " Правильно понял?\""
    n "Рэна кивнула."
    nvl clear
    show rena se ko_b1 with dissolve_02
    n "\"А потом ещё глянула в холодильнике."
    extend " Там увидела холодный тофу из оставшейся половины."
    extend " Мало того."
    extend " Там стояли тарелочки с кое-какой едой на второе, завёрнутые в клейкую плёнку.\""
    n "{nw}"
    n "......Мы, когда хотим оставить недоеденное на завтра, плотно заворачиваем еду в плёнку из полиэтилена."
    n "Мама частенько так делает, чтоб следующим утром подать остатки на завтрак или положить мне в обеденную коробку."
    nvl clear
    show rena se nande_a1 with dissolve_02
    n "\"Да."
    extend " Продукты оборачивают плёнкой, когда хотят оставить их на потом."
    extend " И они положили еду в холодильник...... Стало быть, они в тот вечер есть её не собирались.\""
    n "\".........Ну{w=0.8}...... и что в том?..\""
    nvl clear
    show rena se ko_a1 with dissolve_02
    n "\"Кейти-кун."
    extend " Подумай получше..."
    extend " Они же оставили еду обёрнутой в плёнку?"
    extend " Что это значит, как думаешь?\""
    n "\"......Э-э...{w=0.8} ну......{w=1.0} им не пришлось есть ужин..."
    extend " Поели где-нибудь в ресторане или заказали себе чего-нибудь.\""
    nvl clear
    n "\"Слишком уж внезапно."
    extend " Если бы они заранее решили так сделать, то не стали бы готовить ужин..."
    extend " А ужин они готовили — на двоих."
    n "Получается, Сатоко-тян думала, что ужин они есть будут, и готовила его, пока не произошло {i}что-то{/i}.\""
    nvl clear
    n "\"......З-Значит......{w=1.0} Они вовсе не собирались куда-то поехать...{nw}"
    play sound wa_023
    extend " Так, да?!...\""
    nvl clear
    if renpy.loadable("music/Matsuri/22 - Fukurukouji No Neko.ogg"):
        play music scared_cat
    else:
        play music msys07
    show rena se def_a1 with dissolve_02
    n "\"Верно."
    extend " Поэтому пропали они где-то между тем, как закончили готовить ужин, и тем, как собирались поесть..."
    extend " Вероятно, где-то в семь вечера.\""
    n "\".........Ну и куда они запропастились в такой поздний час, не отужинав даже?..\""
    nvl clear
    show rena se wa_b1 with dissolve_02
    n "\"Ну конечно, снова ты за своё."
    extend " ...Помнишь ли, Кейти-кун?"
    extend " Что там стоял складной столик, а на нём — склянка из-под соевого соуса и стаканчик для палочек?\""
    n "{nw}"
    n "Может, и было что-то такое..."
    extend " Не могу вспомнить..."
    nvl clear
    show rena se def_b1 with dissolve_02
    n "\"Склянка для соевого соуса"
    extend " оказалась пустой."
    extend " Ни капли на донышке."
    extend " А ведь без него холодный тофу невкусен."
    extend " Поэтому я поглядела под раковиной, где там большая бутыль соуса.\""
    n "\"Откуда ты про неё знаешь?..\""
    show rena se wa_a1 with dissolve_02
    n "\"А-ха-ха-ха, так я ходила помогать Рике-тян готовить.\""
    n "Кашлянув, Рэна вновь посерьёзнела."
    nvl clear
    show rena se def_b1 with dissolve_02
    n "\"Так вот, я поглядела под раковиной — но никакой бутыли там не увидела.\""
    n "\"......Ну и что ж означает... отсутствие большой бутыли?..\""
    show rena se nande_a1 with dissolve_02
    n "\"Всё, что я дальше скажу, — просто мои догадки..."
    extend "... поэтому не перебивай меня, пока не закончу.\""
    nvl clear
    scene black with Dissolve(1.0)
    scene sepia_bg 062 with Dissolve(1.0)
    n "Прошлым вечером..."
    n "Сатоко готовила, как обыкновенно, ужин."
    n "Рика-тян, скорее всего, смотрела тем временем телепередачу какую, ну, или что-нибудь в таком духе."
    nvl clear
    n "Сатоко положила в суп кубики тофу и тут вдруг заметила, что соевый соус кончился, а ведь ужин-то скоро."
    n "{nw}"
    n "Так как Рике-тян всё равно было нечего делать, она пошла к соседям одолжить соуса, захватив большую бутыль."
    nvl clear
    scene black with Dissolve(1.0)
    scene bg 095
    show rena se def_a1 at central
    with Dissolve(1.0)
    n "\"...Я не так уж хорошо знаю, как положено водиться соседям... но разве принято ходить друг к другу за соусом?\""
    show rena se wa_a1 with dissolve_02
    n "\"Угу."
    extend " В Хинамидзаве — обычное дело.\""
    nvl clear
    scene black with Dissolve(1.0)
    scene sepia_bg 240
    show sepia_rika se wa_a1 at sprava
    with Dissolve(1.0)
    n "И вот Рика-тян поехала на велосипеде одолжить соуса."
    hide sepia_rika with left_03
    n "{nw}"
    n "И — не вернулась."
    nvl clear
    scene black with right_03
    scene sepia_bg 062
    show sepia_satoko se def_a1 at sleva
    with right_03
    n "Так что Сатоко позвонила соседям, в чей дом поехала за соусом Рика-тян."
    play ambient lsys17
    $ renpy.pause(2.0)
    stop ambient fadeout 1.0
    n "{nw}"
    n "...{i}«Не гостит ли у вас наша Рика?»{/i}"
    extend " — как-то так сказала."
    nvl clear
    n "А отвечали ей примерно так:"
    n "{nw}"
    n "\"...{b}{i}«Мы ужинаем, Сатоко-тян, давай-ка и ты приходи.{/i}{/b}"
    extend " {b}{i}Рика-тян уже угощается».{/i}{/b}"
    extend " ...Как-нибудь так её к себе позвали.\""
    nvl clear
    show sepia_satoko se aki_a1 with dissolve_02
    n "Шипя и плюясь, Сатоко завернула в плёнку приготовленную ей пищу."
    n "В холодильник же она её поставила, чтобы оставить на следующий день, на завтрак и на обед."
    nvl clear
    scene black with left_03
    scene sepia_bg 240
    show sepia_satoko se def_a1 at sprava
    with left_03
    n "И сама поехала на велосипеде"
    extend " туда, куда отправилась Рика-тян."
    nvl clear
    scene black with down
    stop music fadeout 1.0
    play music silver_mirror
    scene bg 094
    show rena se nande_b1 at central
    with down
    n "\"Только... уже тут кое-что непонятное."
    extend " Обычно ведь не готовят столько, чтоб хватало поделиться с гостем, свалившимся как снег на голову.\""
    n "{nw}"
    n "Представить нельзя, чтоб опытная домохозяйка наготовила сверх меры столько, чтобы хватило ещё на два рта."
    nvl clear
    n "\"...А не могло так выйти, чтоб получилось больше надобного?..\""
    show rena se ko_a1 with dissolve_02
    n "\"Ни при каких обстоятельствах.\""
    n "Твёрдо произнесла Рэна."
    nvl clear
    n "\"Ведь... Рика-тян же знала, что Сатоко-тян успела приготовить еду, верно?!"
    extend " Как бы ей ни расхваливали чужой ужин, она б никогда не позволила, чтоб старания Сатоко-тян пропали впустую.\""
    nvl clear
    n "......То всего лишь косвенные улики вперемешку с догадками Рэны."
    n "...Но вот звучат они... превесьма-таки убедительно."
    n "Потому что в теперешнем безнадёжном положении они выглядели лучиком света в кромешной тьме."
    nvl clear
    play sound wa_026
    n "\"......Тогда, Рэна..."
    extend " куда, по-твоему... поехала за соевым соусом Рика-тян?!\""
    n "Вот в чём главный вопрос!!..."
    n "{nw}"
    n "Двор, куда Рика-тян могла обратиться за соусом{w=1.0}... и который в совершенно естественном духе пригласил бы к себе Сатоко......"
    extend " Что же это за двор?!"
    nvl clear
    show rena se ko_b1 with dissolve_02
    n "Рэна медленно покачала головой..."
    nvl clear
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play ambient lsys12
    show rena se def_a1 with dissolve_02
    n "\"......Вот и всё, до чего Рэна додумалась."
    extend " Сплошное воображение, ничего больше."
    extend " Так что полиции лучше не говори.\""
    n "\"Но смысл-то скрывать?.."
    extend " Пускай хоть правдой окажется всего половина, им она может сгодиться...\""
    nvl clear
    show rena se nande_a1 with dissolve_02
    n "\"Кейти-кун......"
    extend " Тогда мы, значит, подозреваем жителей Хинамидзавы."
    extend " Этого нельзя делать без веских оснований...\""
    n "..........................."
    n "{nw}"
    n "Вижу, сюда идёт пара девочек вымыть коробки."
    hide rena with left_03
    n "...Рэна, прекращая разговор, пошла в класс..."
    nvl clear
    n "Я же, оставшись один, окунулся в громкий стрёкот цикад..."
    nvl clear
    scene bg 203 with up
    n "...Надо прояснить кое-что."
    n "...Самому себе."
    n "...Из того малого, что узнала, Рэна столько сумела выжать."
    n "......И тогда мне никакого труда не составит развить её догадку, раз уж я знаю куда больше Рэны..."
    nvl clear
    n "Как сказывал и Ооиси-сан прошлой ночью, дело творится внутри самой Хинамидзавы."
    n "{nw}"
    n "......Рэна не хочет верить, но преступником почти наверняка должен быть кто-то из Хинамидзавы."
    nvl clear
    stop ambient fadeout 0.5
    play music msys07
    scene bg 261 with Dissolve(1.0)
    n "Всё началось, когда мы четверо пробрались в запретное хранилище обрядовых принадлежностей."
    n "{nw}"
    n "И кто-то увидел, как мы туда пробирались."
    n "{nw}"
    n "Для преступников нарушение неприкосновенности хранилища заслуживает наказания смертью."
    nvl clear
    scene black with Dissolve(1.0)
    show tomi si_def at sleva with dissolve_04
    show takano si_def at sprava with dissolve_04
    n "......И в ту же самую ночь Томитаке-сана и Такано-сан убили."
    nvl clear
    scene black with m1
    n "Остались двое."
    show shion si def_a1 at central with dissolve_04
    extend " ...Я да Шион."
    hide shion with Dissolve(1.0)
    n "{nw}"
    n "Но, ещё не добравшись до меня с Шион... злодеи обрушились на старосту, которому Шион всё рассказала."
    n "{nw}"
    n "А следующей под удар попала... Рика-тян, которой всё рассказал я..."
    extend " Но что же насчёт Сатоко?.."
    extend " Прихватили ль её лишь заодно?.."
    nvl clear
    n "Уже погано, что Рику-тян из-за моего признания убрали..."
    extend " но что Сатоко, никоим образом к делу не относящуюся... погано вдвойне..."
    n "{nw}"
    n "{b}......Я во всём... виноват!!...{/b}"
    nvl clear
    n "Кто же исчезнет следующим?"
    n "Теперь-то уж... я иль Шион?.."
    nvl clear
    n "Но... почему они сразу не расправились с нами?"
    nvl clear
    n "Раз они смогли убрать старосту с Рикой-тян, так почему до сих пор не убрали Шион и меня?"
    n "Если бы они напали на меня иль Шион... конечно, мне нисколько того не хочется... но я б понял."
    n "{nw}"
    n "......Чего я не пойму и не прощу, так это зачем им убирать тех, кому мы признались."
    nvl clear
    n "...К слову сказать..."
    extend " вчера Шион говорила, что чувствует, как будто за нею кто-то следит."
    n "{nw}"
    n ".........Тогда... следит ли кто-то за мной?.."
    n "Почему-то... до сей поры я ничего такого не ощущал."
    n "Хоть я тут главный виновник, ничего подобного я не ощутил ни единого разу."
    nvl clear
    n "Возможно, правда, лишь потому, что я куда менее осмотрителен, чем Шион."
    n "{nw}"
    n ".........Впрочем, я отвлёкся."
    extend " Продолжу..."
    nvl clear
    n "Так почему злоумышленники не напали на меня с Шион?"
    n "......Думаю, тут-то и разгадка."
    n "{nw}"
    n "...А, часом......{w=1.0} не от ложных ли я предпосылок отталкиваюсь?.."
    nvl clear
    n "{cps=*0.4}...{w=0.05} ...{w=0.1} ...{w=0.15} ...{w=0.2} ...{w=0.25} ...{w=0.3} ...{w=0.35} ...{w=0.4} ...{w=0.45} ...{w=0.5}{/cps}{nw}"
    extend "Ответ всё не приходил."
    n "{nw}"
    n "Ясно лишь одно:"
    extend " я — участник этих событий..."
    extend " и я должен смотреть за их развитием, пока всё не закончится."
    nvl clear
    stop music fadeout 1.0
    play sound wa_001
    $ renpy.pause(2.0)
    scene bg 095 with up
    n "Разлетелся звон колокольчика, возвещающий об окончании обеденной перемены......"
    nvl clear
    n "Пропадёт ли кто-нибудь и сегодня?"
    n "......Если кто-то должен исчезнуть..."
    extend " то выберите сегодня меня..."
    extend " и пускай всё закончится."
    nvl clear
    n "В мозгу ожили вчерашние захлёбывающиеся вопли Шион, доносившиеся из телефонной трубки."
    n "{nw}"
    n "{i}Они намерены перебить сперва наших близких... а нас прикончат, лишь когда нас придавит невыносимое горе...{/i}"
    nvl clear
    play ambient lsys12
    n "\"Маэбара-кун, обеденная перемена закончилась."
    extend " Иди-ка ты в класс.\""
    n "Послушен директору, я вернулся в класс, где тишина стояла совсем как на похоронах..."
    nvl clear
    jump wata_day11_zvonok
