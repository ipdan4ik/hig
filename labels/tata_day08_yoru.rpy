    $ save_name = "Глава о Смертоносном Проклятии.\nДень Восьмой, раздумья Кейти"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    play music msys06
    n "Вернувшись домой, я принял душ, дабы смыть пот."
    nvl clear
    n "Обычно, приняв душ, я забываю обо всём плохом, произошедшем за день."
    n "......Но не сегодня."
    nvl clear
    n "Выйдя из душевой, я обнаружил чистое бельё опрятно сложенным в корзинке для одежды."
    n "......Обычно не обращавший на это внимания, нынче я был рад маминой предусмотрительности."
    nvl clear
    n "...Но в то же время она заставила вспомнить о мучениях Сатоко."
    n "{nw}"
    n "Пока я радуюсь проявленной ко мне доброте, Сатоко, возможно, в эти же самые минуты осыпает, будто пощёчинами, злобною бранью дядька."
    nvl clear
    scene bg 080 with up
    n "Я поднялся к себе, на второй этаж."
    n "......И уселся за письменный стол, сложив на груди руки."
    n "{nw}"
    n "Повесткой дня была, конечно же... Сатоко."
    nvl clear
    n "...Нам, детям, казалось, что вмешательство государственного учреждения всё разрешит."
    n "{nw}"
    n "......Но, поговорив с Начальником...... я понял, что не так-то всё просто."
    nvl clear
    n "......Сатоко, упрямясь, упорно не хочет признавать издевательств... Пытается их терпеливо сносить."
    n "{nw}"
    n "...И это — затем, чтобы искупить вину перед Сатоши, столько её защищавшим и в итоге бросившим."
    nvl clear
    n "...Пока Сатоко так считает......{w=1.0} просто не будет."
    n "Но я говорил Начальнику."
    n "{nw}"
    n "Говорил, что буду действовать по своему разумению, коли почую, что жизнь Сатоко под угрозой."
    nvl clear
    n "Всё же и я в итоге собираюсь ждать, что будет..."
    n "...Но моё ожидание всё-таки отличается от ожидания друзей и Начальника."
    nvl clear
    n "...Когда сложится чрезвычайное положение... я доложу."
    extend " Звонком."
    n "......Если Сатоко узнает, кто доложил, то, верно, по характеру своему меня проклянёт."
    n "{nw}"
    n "...Но я верю, что в конце концов решение окажется неплохим."
    nvl clear
    stop music fadeout 1.0
    n "...............Но постой, Маэбара Кейти.{w=1.0}"
    n "...А кто сказал, что всё закончится на моём обращении?.."
    n "{nw}"
    play ambient lsys13
    n "......Предположим, я сообщу в органы вроде того же центра защиты детей...{w=1.0}...... а они, как и в прошлом году, подождать решат — что тогда?.."
    nvl clear
    n "...В прошлом году тоже вон решили повременить, и действительно, на время положение улучшилось, но... тётка, чувствуя себя униженной, стала нападать на племянницу исподтишка."
    extend " ......В конце концов её нападки стали только изощрённее."
    n "{nw}"
    n "А в нынешнем году — дядька."
    n ".........Днём я впервые повидал его рожу... и по ней видел — он станет действовать не коварством, но куда более прямо и жестоко."
    nvl clear
    n "Он не будет скрытничать, как поступила бы коварная тётка... нет, он куда более непосредственен..."
    extend " Ему бы пристало пускать в ход кулаки да пинки."
    n "Это легко понять по тем синякам, какие я сегодня видел на Сатоко."
    n "{nw}"
    n "......Чёрт... Простодушничаешь, Маэбара Кейти!!"
    n "Как бы ни сильна была моя готовность сообщить в центр... она ничего не значит, если Сатоко не спасётся!!"
    nvl clear
    n "Доложить в органы — всего лишь один способ, и на него полагаться опасно."
    n "Мы, помимо того, должны обеспечить безопасность Сатоко..."
    nvl clear
    scene bg 082 with fastup
    n "Почесав макушку, я, желая хоть чуток остыть, откинул затылок."
    n ".....................Вспомнилась сегодняшняя перепалка с друзьями."
    nvl clear
    stop ambient fadeout 1.0
    scene bg 118 with dissolve_04
    if renpy.loadable("music/Rainy days.mp3"):
        play music rainy_days
    else:
        play music gear
    n "Стыдно, ведь я-то и не замечал, пока Рэна мне не сказала."
    n "{nw}"
    n "...Верно."
    n "......Дом у меня большой."
    n "Гораздо больше, чем покрытые соломой домишки Хинамидзавы..."
    n "И действительно, незанятых комнат у нас хватает."
    n "{nw}"
    n "......Я никогда не считал себя богатым... но и бедным — ни разу."
    nvl clear
    n "...Просто не признавал правды, потому что не хочется считаться зазнайкой..."
    n "......Но моя семья всё-таки... должна быть богата."
    nvl clear
    n "У нас тут полно пустых комнат, которыми может воспользоваться Сатоко."
    n "Гостевая практически всегда пустует, кроме тех случаев, когда у нас остаются переночевать папины товарищи по работе."
    n "Несколько помещений отведены отцом под кладовки, но и они вполне сойдут для жилья, если там хорошенько прибраться."
    nvl clear
    scene black with dissolve_04
    scene bg 108 gray with dissolve_04
    n ".........Вот питание... может оказаться куда более трудной задачей, чем кажется мне, ребёнку."
    nvl clear
    n "С обедом как-нибудь разберёмся."
    n "Каждый из нас вполне может принести еды чуть больше, чем надо."
    n "Мы и так всегда делимся, так что за обед можно не беспокоиться."
    nvl clear
    scene bg 210 gray with dissolve_04
    n "...Но вот... завтрак и ужин... Тут уж без матери не обойтись."
    n "......Уговорить маму — задачка посложнее, чем выпросить комнату."
    extend " (Впрочем, не думаю, что и комнату легко будет выпросить...)"
    nvl clear
    n "Сколько же стоит месячное питание одного человека?.."
    n "Наверно, где-то пару десятков тысяч йен в месяц?.."
    extend " Если я возьму на себя расходы, будут родители возражать?"
    n "{nw}"
    n ".........У меня в копилке скопилось тысяч десять-двадцать."
    n "По правде сказать, с новогодними деньгами выходит и больше... только родители всё забрали да положили в банк срочным вкладом."
    extend " ......Если удастся их оттуда достать, то наберётся вполне приличная сумма."
    nvl clear
    n "Ну и, если на то пойдёт, попрошу Мион с Рэной и Рикой-тян разделить ношу."
    n "{nw}"
    n "Ясен пень, я не стану на них полагаться."
    n "Рэна уже ругалась,"
    extend " что я сваливаю хлопоты на других."
    n "{nw}"
    n "......Я попрошу помощи."
    n "Но в основном буду поддерживать Сатоко своими силами."
    n "Я справлюсь!.."
    nvl clear
    scene bg 170 gray with dissolve_04
    n "Ой, но... надо ж позаботиться не об одном питании."
    n "......В жизни много без чего ещё нельзя \nобойтись — например, без мытья, без стирки одежды."
    n "{nw}"
    n "......Маманя дюже строга насчёт разбазаривания чего бы то ни было, тут с ней спорить — себе дороже."
    n "...Возьмёт, скажет что-нибудь... вроде цены за стиральный порошок для Сатоко."
    nvl clear
    n "...Словом, одними тратами на еду не обойдёшься."
    n "Денег... надобно больше."
    n "{nw}"
    n "(Эй, Маэбара Кейти, когда это ты додумался до того, что деньгами можно решить всё?!"
    extend " Пускай у тебя будут деньги... для начала тебе нужно получить разрешение от родителей!"
    extend " Чтоб согласились долгое время содержать постороннюю девочку!..)"
    nvl clear
    n "И как ты собираешься их уговаривать?.."
    n "......Маэбара Кейти, если чуток успокоишься, ты же поймёшь, что хрена с два их уговоришь?"
    n "{nw}"
    n "Пускай даже они всерьёз меня выслушают, всё равно ведь скажут звонить в полицию."
    nvl clear
    n "Пускай даже я добьюсь некоторого сочувствия, всё равно ведь спросят:"
    n "{i}«А почему именно семье Маэбара должна достаться вся тяжесть?»{/i}"
    n "{nw}"
    n "...Да..."
    n "...Очень грустно и раздражающе... но моей решимости мало."
    n "...Одной моей решимостью...... ничего не добьёшься."
    nvl clear
    scene black with dissolve_04
    n "\"............Почему дети......... настолько беспомощны?.....\""
    n "......Мне обидно."
    n "......Думал, по решимости мне никто не ровня..."
    extend " Думал, даже Начальник мне уступает."
    extend " .........Но вот..."
    nvl clear
    stop music fadeout 1.0
    n "В этот миг послышался стук в дверь, и в комнату заглянула мама."
    nvl clear
    scene bg 082 _door with dissolve_04
    play ambient lsys13
    n "\"Ты спишь?"
    extend " Ужин готов, я тебя уже несколько раз позвала.\""
    n "\"......А... м-м, сейчас приду...\""
    nvl clear
    scene black with dissolve_04
    scene bg 210 _lamp with dissolve_04
    n "Вообще говоря, кто я таков, чтобы так рассуждать, живя за счёт родителей."
    n "...Пока я сижу тут, сложа ручки, мне готовят еду."
    n "Это самое обычное дело, родительская обязанность по отношению к их ребёнку."
    n "{nw}"
    n "...Но сейчас я понял, что такая обычная с виду штука на самом деле является правом."
    n "...Я понял, как сложно дать другому пользоваться этим правом..."
    nvl clear
    n "Даже простой, привычно однообразный ужин казался сегодня наполненным куда большим смыслом."
    n "На столе стоит ужин для троих — для меня, для отца и для матери."
    n "......Насколько же трудно добавить туда ещё одну порцию?"
    nvl clear
    n "Думай, Маэбара Кейти..."
    n "Раз на четырёх наготовить сложно... надо задуматься над тем, чтобы делить три порции на четырёх."
    nvl clear
    n "............О..."
    n "При подходе с другого ракурса...... в башке откуда ни возьмись появилась дерзкая мысль..."
    nvl clear
    n "Точно."
    n "......Незачем получать отказы от бати с маманей."
    extend " ...Достаточно и того, чтобы про её пребывание тут не знали."
    nvl clear
    n "Родители, правда, задали мне здоровую взбучку, когда заметили, но в мою комнату вполне возможно попасть с улицы, забравшись на крышу первого этажа и пробравшись по водостоку в окно."
    n "Сатоко половчее меня будет, ей много легче."
    n "{nw}"
    n "...Я и не задумывался, но главное-то условие — спрятать её от дядьки."
    nvl clear
    scene black with Dissolve(1.0)
    scene bg 119 with Dissolve(1.0)
    n "Выполнение плана по укрыванию Сатоко у меня в доме начнётся в тот день, когда государственные органы решат подождать, что будет."
    n "{nw}"
    n "Иными словами, дядька по-прежнему будет её опекуном."
    nvl clear
    scene bg 121 with dissolve_04
    n "Если при таких обстоятельствах он узнает, что та открыто живёт у нас, то, вне всяких сомнений, тут же прибежит и заберёт её обратно."
    n "{nw}"
    n "Он её законный опекун, а значит, родители должны будут беспрекословно выдать ему Сатоко."
    n "Поэтому... её проживание у меня надо сохранить в тайне!"
    n "{i}(Для поддержания секретности неплохо было бы заручиться согласием родителей... но говорят же: «Хочешь обмануть врага — сначала обмани друга»......){/i}"
    nvl clear
    scene bg 210 _lamp with left_03
    n "......Хорошо."
    n "...Нежели надеяться, что мне каким-то чудом удастся уговорить родителей...... давайте подумаем, как обеспечить ей скрытное проживание."
    n "Пока я здесь, она может находиться в моей комнате на втором этаже, не издавая ни звука."
    n "{nw}"
    n "......Вопрос в том, что делать днём."
    nvl clear
    n "Если уж прятать её от дяди, то в школу она ходить не должна."
    n "......Возможно, ей будет одиноко, но так всё же лучше."
    extend " (Учить Сатоко могу и я."
    extend " Вообще-то, я и так преподаю на уроках младшим ребятам, так что я к сему делу привычен!)"
    nvl clear
    scene bg 117 with dissolve_04
    n "......Днём я должен ходить в школу, посему дома меня не будет."
    n "{nw}"
    n "......Так как я уже парень взрослый, родители мою личную жизнь уважают и без спроса в мою комнату, пока меня нет, не заглядывают."
    extend " (...Я так считаю.)"
    extend " ......Пока она не будет высовывать носу из моей комнаты... как-нибудь обойдётся, наверно..."
    nvl clear
    n "А если бы и решили родители зайти ко мне, комната-то на втором этаже, а значит, об их приближении заранее оповестят звуки шагов по лестнице."
    n "{nw}"
    n "Пока родители поднимутся по ступенькам (...надо посчитать, сколько секунд занимает подъём), у неё будет какое-то время на то, чтобы спрятаться в чулане."
    nvl clear
    scene bg 210 _lamp with right_03
    n "Стой, Кейти, стой!"
    extend " У тебя выходит противоречие!!..."
    n "Коли Сатоко не пойдёт в школу, то как быть с обедом?!"
    n "{nw}"
    n "......Так, успокоиться!"
    extend " Можно ведь оставить ей свой."
    n "Я пойду в школу без коробки с обедом, а там друзья поделятся со мной нарочно приготовленными излишками."
    n "{nw}"
    n "......Хорошо... здесь порядок."
    extend " ......Ещё есть какие противоречия, недоглядки?"
    nvl clear
    stop ambient fadeout 0.5
    play music msys06
    n "...Точно, завтрак и ужин."
    n ".........Без завтрака как-нибудь обойдёмся."
    n "{nw}"
    n "...По воскресеньям люди частенько дрыхнут всё утро, едят лишь два раза в день, и ничего с ними не происходит."
    nvl clear
    n "Что до ужина...... я скажу родителям, будто у меня увеличился аппетит, чтоб каждый день получать побольше."
    n "......А часть буду относить наверх и отдавать Сатоко!.."
    nvl clear
    stop music fadeout 1.0
    n ".........Испытывая свою задумку..."
    n "{nw}"
    n "......Я поднялся из-за стола с блюдом жареной рыбы."
    nvl clear
    play ambient lsys13
    n "\"В чём дело, Кейти?"
    extend " Когда ешь, сиди спокойно.\""
    n "\"А, угу."
    extend " ...Хочется некоторого разнообразия, видите ли."
    extend " ...Можно я поем у себя в комнате?\""
    n "\"...Да ты всё изгваздаешь."
    extend " Ешь за столом.\""
    n "\"............Эх... ладно, извините...\""
    nvl clear
    n "...Эй, что за..."
    n "Они не дают мне забрать даже тарелку с жареной рыбой?!"
    n "{nw}"
    n "Взять еду так, чтобы они не заметили... в жисть не получится."
    nvl clear
    n "...Впрочем... подумать стоит."
    n "...Должен же быть какой-то способ незаметно увести со стола еду, вроде ловкого фокуса с обманом зрения..."
    n "{nw}"
    n "(Если сегодня и не получится ничего придумать, может осенить завтра!..)"
    nvl clear
    scene black with fastdown
    n "Есть понемногу расхотелось, и я, раньше обычного встав из-за стола, ушёл к себе."
    nvl clear
    scene bg 081 with right_03
    n "...Я решил продумать всё заново, но теперь с точки зрения Сатоко."
    n "......Предположим, вот мать начала сюда подыматься. Так, прячемся!.."
    nvl clear
    n "Я открыл дверь чулана."
    n "{b}......Штррррх.{/b}"
    extend " ...Тихо не открывается."
    nvl clear
    if renpy.loadable("music/Rainy days.mp3"):
        play music rainy_days
    else:
        play music gear
    n "Эге-ге... какого чёрта, обычно-то дверь открывается без всякого шума!"
    n "Чего та вдруг?!"
    extend " Дом, что ли, бракованный?!"
    extend " Уже разваливаться начинает?!"
    extend " Может, надо смазать пазы?!"
    extend " Воском их замазывать, да?!"
    nvl clear
    n "Пускай звук и тих, но меня волнует, чтобы поднявшаяся мать ни при каких обстоятельствах не могла понять по нему, что к чему."
    n "{nw}"
    n "......Но с этим я как-нибудь разберусь."
    n "Надо всего лишь переделать дверь так, чтобы она открывалась без шума."
    nvl clear
    n "Ну, как бы то ни было... пока будем считать, что я залез в чулан без единого звука."
    nvl clear
    stop ambient fadeout 1.0
    play sound wa_020
    scene black with right_03
    n ".........Мой футон, в общем-то, всё время лежит на полу."
    n "Поэтому матери нет повода открывать чулан."
    n "...И всё-таки он может у неё появиться."
    nvl clear
    n "Нужно добавить туда ещё и какую-то маскировку, чтобы мать ничего не заметила, даже открыв чулан."
    n "Но чем лучше будет маскировка... тем меньше времени будет у Сатоко, чтобы спрятаться, и тем больше вероятность, что её присутствие обнаружат по звукам."
    nvl clear
    n "............Неожиданно......... мне захотелось в туалет."
    nvl clear
    n "...Туалет?!....."
    nvl clear
    n "А ведь естественное желание сходить по-большому...... на самом-то деле ставит под угрозу всю затею..."
    nvl clear
    n "Туалет есть только на первом этаже."
    n "Воспользоваться им так, чтобы не заметила семья, невозможно в принципе."
    n "{nw}"
    n "......Наверно, придётся достать какой-нибудь \nпереносной нужник, чтобы она могла им пользоваться, не выходя из моей комнаты. \n(Что-то вроде горшка, говоря по-простецки."
    extend " \n...Хотя вряд ли Сатоко такое понравится...)"
    nvl clear
    n "...Но... у испражнений-то запашок ох какой......"
    n "Возможно, родителям и не придётся заходить ко мне в комнату, чтобы его учуять."
    nvl clear
    n "......Зато с мытьём порядок."
    n "Можно помыться, когда родителей дома не будет."
    n "Но вот с туалетом беда."
    n "Если прихватит живот, а родители будут в это время разгуливать по первому этажу... она ничего не сможет поделать!.."
    nvl clear
    n "...Я и не заметил, когда снова начал расцарапывать голову."
    n "Сидя в тёмном чулане, прижав колени к груди......"
    extend " я, зарывшись в них лицом, принялся нещадно раздирать башку."
    nvl clear
    n "...Чем больше думал, тем больше находил противоречий."
    n "...Чем больше думал, тем больше моя затея разваливалась..."
    n "...Чем больше ломал башку...... тем больше понимал, насколько бессилен."
    nvl clear
    n "От долгого сидения в тесноте в позвоночнике появилась и начала разгораться боль."
    n "А мне придётся навязать её и Сатоко, если уж решу её здесь укрыть."
    nvl clear
    n "...Ей придётся жить здесь, задыхаясь в темноте, в тесноте... хрен знает сколько."
    n "Но и это намного лучше, чем жить, подвергаясь дядькиным издевательствам... так мне хотелось думать."
    nvl clear
    n "......Наконец воздуха начало не хватать... и я, сдавшись, выполз из чулана."
    nvl clear
    play sound wa_020
    stop music fadeout 1.0
    scene bg 082 with left_03
    play ambient lsys13
    n "Посмотрев на часы... я увидел, что сейчас три с половиной часа утра."
    n "...Не верится, как быстро промчалось время."
    n "{nw}"
    n "И на меня тут же, словно подстраиваясь под время, напала убийственная сонливость."
    scene black with dissolve_02
    play sound wa_004
    n "Уступая неодолимой силе, я бухнулся на футон."
    nvl clear
    n "...Вот дерьмо. Нет, хрен там, я не позволю себе заснуть."
    n "......Впустую потрачу время — значит, ничем не буду отличаться от Начальника и Мион с Рэной, решивших понаблюдать за развитием событий."
    nvl clear
    n "Я... должен думать, думать, думать хотя бы минуту, секунду дольше всех остальных... о том, как спасти Сатоко..."
    nvl clear
    n "......Неужели никак нельзя?"
    n "Неужели никак нельзя?"
    n "{nw}"
    n "Слова, которые я бормотал самому себе, кружились, кружились перед глазами...... медленно утягивая в беспамятство........."
    nvl clear
    n "В последнее мгновение перед потерей сознания мне подумалось."
    nvl clear
    n "Конечно, в моей затее полно дырок и недочётов...... но в целом она отнюдь не плоха."
    n "{nw}"
    n "Завтра я предложу свой дерзкий план друзьям."
    n "Возможно, Мион сумеет чем-то помочь, а Рэна неожиданно дополнит его блестящими усовершенствованиями."
    nvl clear
    n ".........И, что главнее всего..."
    n "Я должен убедиться, что все готовы объединить силы для спасения Сатоко..."
    n ".....................Отвратительно, до чего же легко я уступаю сонливости."
    n "{nw}"
    n ".........Прости меня... Сатоко..."
    nvl clear
    scene bg 118 with Dissolve(1.0)
    $ renpy.pause(2.0, hard=True)
    scene black with Dissolve(1.0)
    $ renpy.pause(2.0, hard=True)
    jump tata_day09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
