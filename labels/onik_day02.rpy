    $ save_name = "Глава о Похищенных Демонами.\nДень Второй, прогулка-знакомство"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene white with Dissolve(3.0)
    play ambient lsys22
    scene bg 038 with m1
    n "Слишком разнежившись утром, я теперь опаздываю на встречу."
    n "Сегодня Рэна и Мион собирались показать мне Хинамидзаву."
    nvl clear
    play music msys01
    scene bg 066
    show mion si def_a1 at sleva
    show rena si def_a1 at sprava
    with left
    n "Они уже как раз ждали. Ровно там, где и договорились."
    nvl clear
    show mion si tk_a1 with dissolve_02
    n "\"Кей-тян, опоздаааал!\""
    n "\"П-Простите! Вчера просто по телевизору такие интересности показывали!\""
    n "\"О-о, это ты так оправдываешься перед девочками за опоздание?\""
    show rena si nande_a1 with dissolve_02
    n "\"Мии-тян, так ты ведь сама только-только пришла...\""
    show mion si aku_a1 with dissolve_02
    n "\"Хе-хе-хе-хе......"
    extend " Да уж, вчерашний выпуск «Круглосуточного патруля» вышел тем ещё, правда?\""
    n "{nw}"
    n "Да и ты не без грешка!"
    nvl clear
    n "Рэна зачем-то притащила огромную сумку."
    n "На кой... она вообще нужна?"
    show mion si wink_a1 with dissolve_02
    $ renpy.pause(0.4)
    show mion si aku_a1 with dissolve_04
    n "Подмигиванье Мион сразу всё поставило на свои места."
    n "{nw}"
    n "А, так Рэна и взаправду приготовила нам обед!"
    nvl clear
    show mion si to_a1 with dissolve_02
    n "\"Кей-тян, мне кажется, или..."
    extend " она как-то с готовкой ПЕРЕСТАРАЛАСЬ?!\""
    n "\"Я её не заставлял, понятно?!...\""
    show rena si hau_b1 with dissolve_02
    n "\"Н-Ничего...{w=0.3} Мне не в тягость... только не волнуйтесь...{w=0.4} ладушки? {font=DejaVuSans.ttf}☆{/font}\""
    nvl clear
    show mion si maji_a1 with dissolve_02
    n "\"Она, между прочим, ещё со вчерашнего дня трудилась!"
    extend " Из-за тебя!\""
    n "\"Н-Ну ладно... Я мужчина, потому... Да... Я СПРАВЛЮСЬ...{w=0.5}{nw}"
    extend " Сделаю то, что должен... ради неё!\""
    n "\"А?.."
    extend " То, что должен?... Про что ты? ...про что ты?!\""
    nvl clear
    show black with right
    n "Мы с Мион медленно повернулись к Рэне и уставились на дорожную сумку ненормальных размеров."
    n "Нельзя было и представить, что там лишь обед в коробках."
    n "{nw}"
    n "Но это же Рэна!.."
    nvl clear
    hide black with left
    n "\"{cps=*0.5}...{/cps}{w=0.5}...Там не меньше двух кило... как считаешь?\""
    show mion si aku_a1 with dissolve_02
    n "\"Когда поднимала, у неё вырвалось «опаньки»."
    extend " ......Пять кило.\""
    show rena si wa_b1 with dissolve_02
    n "\"Ой, н-не надо!.."
    extend " Кейти-кун — растущий мальчик!"
    extend " Вот я и подумала, что ему... понадобится много... {font=DejaVuSans.ttf}☆{/font}"
    extend " А-ха-ха... пойдём уже!{w=0.8}{nw}"
    extend " ...Опаньки!\""
    n "Принимая во внимание то, как напряглась Рэна... вряд ли там лишь обеденные коробки."
    n "{nw}"
    n "{nw}"
    n "\"...Согласен с тобой, Мион. Пять килограмм, не меньше...\""
    nvl clear
    show mion si to_a2 with dissolve_04
    n "\"Я тебе подмогну, так что... попробуй только не доесть!"
    extend " Никогда не прощу, если ты огорчишь Рэну!\""
    n "Похоже, надо побыстрее нагулять побольше аппетита..."
    nvl clear
    scene white with right
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    scene bg 042 with right
    play music msys02
    n "Повеселившись, мы не спеша двинулись в путь."
    n "Приятная прогулка под мягкими лучами утреннего солнца..."
    n "Проживаючи в городе, я не мог и представить, насколько же это хорошо для здоровья."
    nvl clear
    n "Тихо так. Одно слово — село."
    n "Никаких угрюмых конторщиков, прущихся на работу по выходным."
    n "Одна только мирная тишина, и нечего больше желать."
    nvl clear
    scene bg 041
    show mion si def_a1 at sprava
    show rena si def_a1 at sleva
    with right
    n "Какой бы крохотной ни была деревня, обходя её, народ повстречаешь в любом случае."
    nvl clear
    n "\"А, всего вам доброго.\""
    n "\"Добрый день."
    extend " Ого, да это никак... это же... Маэбара-кун?\""
    n "Они кланяются каждому встречному."
    n "И каждому встречному известно, как меня зовут."
    nvl clear
    n "\"Отчего меня все знают?!\""
    n "Мы уже с тремя разминулись, и все знают меня по имени. Как-то подозрительно всё это."
    show mion si wink_a1 with dissolve_02
    n "\"Аха-ха, печально, думаю, однако ж"
    extend " в Хинамидзаве не так много народу, потому все-е-е друг с другом знакомы.\""
    nvl clear
    n "\"Хочешь сказать, что..."
    n "Когда они видят незнакомца, то сразу же думают: «Ага, вот это Маэбара-сан, который только сюда переехал»?\""
    n "\"Угу. Что-то вроде того.\""
    n "Хоть здешняя система «свой-чужой» и незамысловата... но весьма, весьма впечатляет."
    nvl clear
    scene black with left
    n "Надо бы отныне следить за своим поведением."
    n "{nw}"
    n "Ежели меня кто-то застукает за просмотром непристойных картинок в книжном, на следующий день вся деревня непременно заклеймит меня извращенцем!!..."
    n "{nw}"
    n "Вот они, леденящие кровь ужасы Хинамидзавы!.."
    nvl clear
    scene bg 043 with left
    n "Но то было только начало."
    show rena si def_a1 at sprava with m1_03
    n "\"Конечно же, мы знаем всех."
    extend " Сначала мы повстречали дядюшку Такедзо, работающего в магазине велосипедов Макино."
    extend " Он увлекается игрой на бамбуковой флейте и бонсаем.\""
    show mion si def_a1 at sleva with left_03
    n "\"Потом был Дайсукэ-кун, второй сын владельца местной бакалейной лавки."
    extend " Любит меткую стрельбу, мечтает когда-нибудь стать первоклассным снайпером.\""
    n "\"А после него повстречалась Миё-сан, медсестра из Клиники Ириэ."
    extend " Говорят, она любит наблюдать за птичками, а также их фотографировать.\""
    n "\"...Погодите-ка, так вы не только имена знаете..."
    extend " но даже их занятия?!\""
    show rena si wa_a1
    show mion si wink_a2
    with dissolve_02
    n "Переглянувшись, Мион с Рэной засмеялись над моей ошарашенностью."
    nvl clear
    n "\"Можно и так сказать."
    extend " Здесь мы знаем друг о друге многое, не то что городские.\""
    n "\"А ну-ка, проверим."
    extend " Кто я такой?\""
    nvl clear
    show rena si wa_b1 with dissolve_02
    n "\"А-ха-ха-ха."
    extend " Маэбара Кейти-кууун."
    extend " Постоянно вредничает, но на деле он добрый и застенчивый.\""
    show mion si to_a2 with dissolve_02
    n "\"Приехал сюда три недели тому назад."
    extend " Любимое занятие — дремать."
    extend " Совсем недавно перешёл с плавок на боксёрские трусы."
    extend " ...Я права?\""
    n "\"Хватит, достаточно!!!\""
    show rena si hau_a1 with dissolve_02
    n "\"...Б-боксёрские......\""
    n "\"Хватит уже!\""
    nvl clear
    n "Да тут и малейшей подробности не утаишь."
    n "О зловещая... Хинамидзава!"
    nvl clear
    show black with left
    scene bg 040 with left
    n "\"Знаете, что-то у меня такое ощущение, что не мне показывают деревню, а деревне показывают меня...\""
    show rena si def_a1 at sleva with left_03
    n "\"Почти что так.\""
    show mion si def_a1 at sprava with right_03
    n "\"Дак мы вон какое парадное шествие устроили."
    extend " Все и думают:"
    extend " ага, наконец-то Кей-тян принялся познавать Хинамидзаву!\""
    nvl clear
    n "\"В Хинамидзаве осталось мало народу."
    extend " Мы все рады новому другу.\""
    n "Я уже чуть было не рассмеялся, но вовремя взял себя в руки."
    n "{nw}"
    n "А я-то хоть раз сходил поприветствовать нового соседа в городе?.."
    n "Похоже, здесь такими вещами не шутят."
    nvl clear
    scene bg 040 with dissolve_02
    n "Мы встретились с ещё одной незнакомой тётушкой."
    n "И она точно так же завела с нами разговор."
    n "\"А-а, здравствуйте."
    extend " А вы неплохо ладите, как замечательно!\""
    n "\"Это Фудзисима-сан."
    extend " Добрый день!\""
    n "\"А-а, Маэбара-кун! Хорошо-то, когда с обоих боков прелестные девушки, ага?"
    extend " Ну, как поживаешь?"
    extend " Привыкаешь понемногу?\""
    n "Проглотив своё обычное приветствие для таких случаев, я лишь усердно кивал."
    n "Улыбнувшись, тётенька сказала, что рада видеть меня в добром здравии."
    nvl clear
    show mion si wink_a2 at sprava
    show rena si def_a1 at sleva
    with dissolve_02
    n "\"Молодца!\""
    n "Когда я обернулся, Рэна и Мион мне подмигнули."
    nvl clear
    show rena si wa_a1 with dissolve_02
    n "\"...Ну так~{font=DejaVuSans.ttf}☆{/font}..."
    extend " не пора ли обедать?{w=0.3} ...обедать?\""
    n "Рэна, ослепительно сверкая улыбкой, напомнила нам о практически забытых изначальных намерениях."
    n "Мы переглянулись."
    nvl clear
    n "\"...Я мужчина. Я сделаю всё, что в моих силах."
    extend " ...Но тут же столько еды!\""
    show mion si def_a1 with dissolve_02
    n "\"...Ничего, Кей-тян. Положись на Дядьку Мион.\""
    n "...Ух ты, а ведь Мион прежде не казалась такой надёжной."
    n "Недаром ты наша староста!"
    nvl clear
    n "\"Рэна, раз уж мы собираемся поесть, то, может, подберём площадку с видом получше?\""
    show rena si wa_b1 with dissolve_02
    n "\"...О-о-о... давай!"
    extend " Отличная придумка, я за!\""
    n "Рэна радостно кивнула в ответ на предложение Мион."
    nvl clear
    scene black with up
    stop music fadeout 1.0
    play ambient lsys12
    scene bg 085 with up_30
    scene black with up
    scene bg 074 with up_30
    n "Забравшись по каменным ступенькам, я узрел храм, точно такой, каким я его себе представлял."
    n "Выглядит потрёпанным временем, но в то же время чист и ухожен."
    nvl clear
    $ save_name = "Глава о Похищенных Демонами.\nДень Второй, пикник на горе"
    scene bg 075 with down
    show rena si def_a1 at sprava with m1_03
    n "\"Храм Фурудэ."
    extend " Здесь, пожалуй, лучший вид во всей округе!\""
    show mion si def_a1 at sleva with fastdown
    n "\"Смотри, чтоб запомнил местечко!"
    extend " На следующее воскресенье здесь намечается фестиваль.\""
    n "\"Да-а? Разве не рановато ещё для фестивалей?\""
    n "\"Ватанагаси — не летний фестиваль. В прежние времена им отмечалось окончание зимы.\""
    n "{nw}"
    n "Ну я и шляпа — всегда по-городскому наивно считал, что их проводят лишь летом."
    nvl clear
    scene black with left_03
    scene bg 216 with left
    show rena si def_a1 with m1
    n "\"А теперь... давайте расставим коробочки......{w=0.7}{nw}"
    extend " вот так......\""
    n "Вскоре на подстилке расположились коробки самых разных цветов."
    n "От запахов текут слюнки."
    extend " Рэна приготовила их своими руками."
    extend " Ясен пень, они восхитительны."
    n "{nw}"
    n "...Но неужели мы таки осилим всё?!"
    n "Эй, Мион! Ты и правда считаешь, что достаточно лишь отличного вида?!!"
    nvl clear
    stop ambient fadeout 1.0
    scene bg 217 with right_03
    play music the_satoko
    show rika si de_a1 at sleva
    show satoko si def_a1 at sprava
    with right_03
    n "\"День добрый...\""
    nvl clear
    n "К нам подошли Рика-тян и Сатоко."
    n "...Они-то чего здесь делают?!"
    n "Глядя в мою сторону, Мион ухмыльнулась."
    n "{nw}"
    n "А, п-понял: тайный замысел Мион заключался в том, чтобы взять числом едоков!.."
    nvl clear
    n "Спасибо, Мион!"
    n "Для меня будет честью принять дело из твоих рук!"
    nvl clear
    show satoko si aki_a1 with dissolve_02
    n "\"Мы услышали шум и пришли посмотреть, что...{w=0.3}\n...{w=0.3}эй, это ещё что тако-о-е?!!\""
    n "\"А то не видишь?"
    extend " У нас обед,"
    extend " шведский стол."
    extend " Все блюда приготовлены Рэной!\""
    show satoko si bik_a1 with dissolve_02
    n "\"Я и сама вижу!!!"
    extend " Вы почему это едите на чужих задворках?!!\""
    n "\"Эй, храм — достояние общественности. Не говори так, словно здесь твои владения.\""
    show rika si ni_a1 with dissolve_02
    n "\"Кейти прав..."
    extend " Храм для всех же.\""
    nvl clear
    n "\"Ах-х... как я и думал, Рика-тян такая славная девочка!!..."
    extend " Садись к нам!"
    extend " Присоединяйся!\""
    scene bg 216 with left_03
    n "Освободив место для Рики-тян, я немедленно повернулся к Сатоко спиной."
    nvl clear
    show satoko si bik_a1 at sleva with dissolve_04
    n "\"Погодите-ка!"
    extend " А я где сидеть должна?!\""
    n "\"Для ТЕБЯ здесь нету ни места, ни еды!\""
    show rena si nande_a1 at sprava with m1_03
    n "\"...В-всё в порядке... для Сатоко-тян точно хватит...\""
    n "\"Нет! Я съем всё!!!\""
    n "\"Не дам!!!"
    extend " Рика-а-а!\""
    show rika si de_a1 at central with left_03
    n "\"Вот палочки...\""
    n "Сатоко и я кинулись на коробки, готовые начать сражение."
    nvl clear
    play music msys02
    scene bg 217 with right_03
    show mion si wink_a1 at sprava with right_03
    n "\"Вот так да... А ты знаешь, как накалить обстановку, Кей-тян."
    extend " Видать, у тебя талант.\""
    show rena si def_a1 at sleva with left_03
    n "\"Тарелка тебе, тарелка для Мии-тян, тарелка для Рики-тян.\""
    n "Рэна сноровисто раздала всем бумажные тарелки с палочками для еды."
    nvl clear
    scene bg 217 with m1
    show rika si ko_a1 at sleva with left_03
    n "\"Если мы промешкаем, они всё прикончат же...\""
    n "\"Твоя правда. Ну что!"
    extend " Погнали?!\""
    show rena si def_a1 at sprava with m1_03
    n "\"Ешьте вволю!"
    extend " Хватит на всех! {font=DejaVuSans.ttf}☆{/font}\""
    n "Скручивая крышку термоса, Рэна дала нам своё разрешение."
    nvl clear
    scene black with dissolve_04
    scene bg 216 with Dissolve(1.0)
    n "Теперь-то я понял. Она заготовила еды на пятерых."
    n "Хоть еды меньше и не стало, смысла в её количествах теперь гораздо больше."
    nvl clear
    show satoko si aku_a1 with dissolve_04
    n "\"Сей говяжьей котлетки ты не получишь!!!\"{nw}"
    play sound wa_005
    with hpunch
    extend ""
    n "\"Гха!!!{w=0.4} Сатоко, пихать локтем нечестно!!!\""
    show satoko si bik_a1 with dissolve_02
    n "\"Хватать за воротник нечестно нисколь не менее!!!\""
    nvl clear
    hide satoko with dissolve_02
    n "Могло показаться, что в начале ожесточённого сражения Сатоко как будто удерживала преимущество за счёт быстроты и локтей, но моё смертоносное искусство владения палочками быстро переломило ход битвы!"
    if persistent.matsuri:
        scene cg sweet_victory with Shake((0, 0, 0, 0), 0.5, dist=15)
    else:
        show satoko si hn_a1 at central with dissolve_02
    n "\"Ааааа! Только не последняя тефтелькаааааааааааааа!!!\""
    n "\"И Ходзё Сатоко ПРО-И-ГРА-ЛА-ла-ла-ла!!! Агха!!!\""
    nvl clear
    scene bg 216 with left_03
    n "Греясь в лучах славной победы над Сатоко, я запихал тефтельку в рот и тут же подавился."
    n "Движимая желанием помочь Рика-тян погладила меня по голове, хотя еда вообще-то в горле застряла."
    n "Глядя на нас, Рэна совсем разволновалась, от восторга ажно раскрасневшись."
    n "Мион пожурила Рэну за преступные мысли."
    nvl clear
    n "Для нас — обычнейшая трапеза."
    n "И я никаких усилий не пожалею..."
    extend " если так оно будет и дальше."
    nvl clear
    scene black with left
    scene bg 217 with left
    n "Когда жаркая битва наконец стихла,"
    extend " мы завели неторопливый разговор."
    nvl clear
    play music msys01
    n "Налив чай из термосов, делаем короткую передышку."
    nvl clear
    n "\"Вот не понимаю, почему в японском языке так мало слов для похвалы хорошей готовке?!\""
    show mion si wink_a2 at sleva with m1_03
    n "\"Вероятно, раньше во время приёма пищи просто не принято было болтать?\""
    show rena si def_b1 at sprava with m1_03
    n "\"Я читала, что давным-давно люди за едой не разговаривали вообще."
    extend " Должно быть, поварам грустно приходилось...\""
    show satoko si wa_a1 at central with fastdown
    n "\"Уверена, раньше были слишком поглощены едой, чтобы хвалить её вкус!\""
    n "Не-а, это только ты у нас такая."
    nvl clear
    scene bg 216 with left_03
    show rena si def_a1 at sleva with m1_03
    n "\"Даже так, любого повара порадует простое «вкусно»."
    extend " ...Иначе и знать не знаешь, стоило ли так трудиться.\""
    show rena si hau_a1 with dissolve_02
    n "От такого признания её щёки вспыхнули багровым пламенем."
    n "{nw}"
    show rika si ni_a1 at sprava with dissolve_04
    n "\"......Вкусно же.\""
    n "Идеально выбрав мгновение, Рика-тян поразила Рэну своей «похвалой» в самую точку, прямо промеж глаз."
    n "Её бесхитростная невинность Рэну просто зачаровала."
    nvl clear
    n "\"......Х-ха...\""
    n "\"Ха?..\""
    n "Рэна издала бессвязный лепет, и..."
    play sound wa_029
    extend " *хлоп* — от её макушки поднялось колечко дыма."
    show rena si ka_b1 with dissolve_02
    n "\"Х-Ха-а-у-у-у!!!"
    extend " ...Ри... Ри-Ри... Рика-тян, Рэ-Рэна д-должна з-забра... нет!"
    extend " Я хочу сказать, спасибо!!!\""
    n "\"......И правда очень вкусно.\""
    n "С восторженным воплем покрывшаяся румянцем Рэна крепко прижала к себе Рику-тян и стала тереться о неё щекой."
    nvl clear
    show rena si hau_a1 with dissolve_02
    n "\"Т-ты меня похвалила... вот, держи!"
    extend " Это тебе!\""
    n "Она воткнула зубочистку в яблочного кролика и сунула его Рике-тян."
    stop music fadeout 1.0
    n "{nw}"
    n "После того как та взяла кролика, настрой пикника быстро покатился куда-то совсем не туда."
    nvl clear
    scene bg 217 with right_03
    play music msys03
    show satoko si aku_a1 at sleva with m1_03
    n "\"Что такое, Сатоко?"
    extend " Что ты так смотришь?\""
    n "\"Все уже придумали похвалу получше, чтобы словить побольше кроликов?\""
    show mion si fu_a1 at sprava with dissolve_04
    n "\"Ничего себе тон."
    extend " Как может кто-то с таким ничтожным словарным запасом придумать хороший отзыв?!\""
    n "\"Хо-хо-хо... ну ладно."
    extend " Глядите, как работает мастер.\""
    n "{nw}"
    n "Сатоко кинула нам с Мион ещё один дерзкий взгляд, а затем внезапно изменила голос."
    nvl clear
    scene black with Dissolve(1.0)
    n "\"Ой... знаесь!"
    extend " ......Сатоко тозе ситает..."
    play sound wa_029
    extend " сто кухня сестлёнки Рэны осень вкусная...\""
    n "Состроив щенячьи глаза и заговорив как четырёхлетняя, Сатоко притворялась застенчивой малюткой."
    nvl clear
    scene bg 216 with left
    n "Что?!{w=0.4} ...И это похвала?!"
    extend " Так теперь ты не хнычешь, а прикидываешься застенчивой?!"
    nvl clear
    n "Впрочем, на Рэну её застенчивость ещё как подействовала."
    show rena si ka_a1 at sleva with dissolve_04
    n "Запылав, она зачарованно завращала головой!!..."
    n "\n\n\n{nw}"
    n "Н-не дай себя обмануть, Рэнаааа!!!"
    nvl clear
    show rena si ka_b1 with dissolve_02
    n "\"Ха... Хаууу!!...\""
    n "Конечно же, было поздно. Рэна сгребла Сатоко в охапку и начала тереться о неё щекой."
    n "\"Такая миилаая, такая миииилая!!!....."
    extend " Сатоко-тян такая милень... кая... {font=DejaVuSans.ttf}☆{/font} Рэна должна... забрать тебя домой... хау!\""
    n "*Чик*, *хруп*, *шух*! И Сатоко тоже получила кролика."
    nvl clear
    n "Запихав его за щёки, она горделиво на нас посмотрела."
    n "Время, затраченное на потопление Рэны, — меньше пяти секунд."
    n "О-Опять её грязные штучки!{w=0.4}{nw}"
    extend " Это же явное шулерство!!..."
    nvl clear
    scene bg 217 with right_03
    show satoko si aku_a1 at sprava with m1_03
    n "\"Ежели вам что-то не нравится, почему бы и вам не придумать, как похвалить Рэну-сан, чтоб получить от неё вознаграждение?\""
    n "Аааах тыыыы!!!"
    extend " Нечестно дерёшься!!!"
    n "Ты её даже и не похвалила-то по-настоящему!!!"
    nvl clear
    show mion si tk_a1 at sleva with fastdown
    n "\"Так-так, Сатоко."
    extend " Считаешь, что уже победила."
    extend " Ну ладно, сейчас ты увидишь кое-что покруче ваших мелочных уловок!\""
    n "\"З-Звучит многообещающе, Мион!"
    extend " И каков же твой план?!\""
    show mion si wink_a2 with dissolve_02
    n "\"Всё сделаешь ты, Кей-тян.\"{w=0.5} — \"Чё?!\""
    show satoko si wa_a1 with dissolve_02
    n "\"Хо-хо-хо! И что же вы изволите нам показать?"
    extend " Неуклюжесть стариков и старух?!\""
    nvl clear
    hide satoko
    hide mion
    with Dissolve(1.0)
    n "Мион предложила неслыханно дерзкую тактику..."
    n "Но иначе Сатоко не победить!!!"
    nvl clear
    scene black with left_03
    scene bg 216 with left_03
    n "Отхлебнув чаю, я повёл речь — естественно,"
    extend " мягко, спокойно."
    nvl clear
    n "\"Очень вкусно вышло."
    extend " ...Но вся ли еда приготовлена дома?\""
    show rena si def_a1 at central with m1_03
    n "\"Ой, нет......"
    extend " По правде говоря... тут в основном лишь разогретое...\""
    n "\"А какое же блюдо сделано тобой?\""
    show rena si nande_a1 with dissolve_02
    n "\"...А?.. Э-э-э?.."
    extend " {cps=*0.4}...Ммм...{/cps} я сте-{w=1.0}стесняюсь... Надо ли мне ответить?.. Точно?\""
    n "Рэну сразила необходимость управляться одновременно с мужчиной и с домашней кухней."
    nvl clear
    n "\"..........Я знаю!{w=0.4}{nw}"
    extend " Вот оно, не так ли?\""
    show rena si bik_b1 with dissolve_02
    n "\"А?{w=0.4}{nw}"
    extend " ......Что?!...{w=0.4}{nw}"
    extend " ......Хау-у-у!.....\""
    n "Потрясённая моим заявлением Рэна стала краснее варёного рака."
    nvl clear
    n "\"О... откуда ты знаешь?!..."
    extend " ...знаешь? ...Хау... что Рэ-Рэна приготовила?.....\""
    n "Ясен пень, мне поведала это Мион."
    n "...Всё идёт как задумано!!!"
    n "{nw}"
    n "А теперь я, наигранно стесняясь, пропускаю один удар сердца."
    extend " ...И провожу...{w=0.5} добивание."
    nvl clear
    play ambient lsys12
    n "\"{cps=*0.5}Потому что... они пахнут Рэной.\"{/cps}"
    stop music fadeout 0.2
    play sound wa_010
    show inverse_bg 216
    show inverse_rena si bik_b1
    with dissolve_02
    n "Мёртвая тишина."
    nvl clear
    n "Рэна, всё ещё кумачово-красная, застыла и не движется..."
    n "Подавившись писком, Сатоко точно так же покраснела."
    extend " Конечно же, покраснел и я сам..."
    nvl clear
    n "\"...Эх, вот бы поесть... сделанных руками Рэны яблочных кроликов...{cps=*0.3}{w=0.6}...{w=0.6}...{w=0.6}{/cps} ...да...\""
    n "{nw}"
    n "Как бы сильно я ни враждовал с Сатоко, это уже слишком...{w=1.0} Я, кажется, только что пересёк черту, за которую не должен был заступать... и зашёл за неё на целых десять метров..."
    n ".........В следующий миг..."
    nvl clear
    stop ambient fadeout 0.5
    hide inverse_bg
    hide inverse_rena
    with dissolve_02
    play music msys03
    play sound wa_006
    n "{size=32}{b}БАХ!!!{/b}{/size}{w=1.0}" with Shake((0, 0, 0, 0), 1.0, dist=15)
    n "{nw}"
    n "Передо мной грохнулась полная коробка кроликов."
    nvl clear
    show rena si ka_a1 at central with m1_03
    n "\"Не-не-не-не отк-кажешься, Кейти-кун?!!"
    extend " И-и-и-и-их много, можешь брать... ск-колько х-хочешь!!!\""
    n "*Бва?!* В мой рот влетела добрая дюжина кроликов, заставив опрокинуться вверх тормашками."
    nvl clear
    n "\"Ва-ва-ва-в... вот,{w=0.3} о-{w=0.3}открой ротик, К-К-К-Кейти-кун, с-скажи «аааам»...{w=0.5}......\""
    n "Придерживая мою голову на своём колене, она всё запихивала кроликов мне в рот."
    n "Лепеча изменившимся голосом, она продолжала...{w=0.2}...{w=0.2}...{w=0.2} набивать мой рот...{w=0.2} кро...{w=0.2} ли...{w=0.2}... {w=0.2}ка...{w=0.2}...{w=0.2} ми...{w=0.2}...{w=0.2}"
    nvl clear
    scene bg 217 with right_03
    n "\"Фа, у ак фефе, Фафофо? Ы оиииы...... (Ха, ну как тебе, Сатоко? Мы победили...)\""
    show mion si tk_a2 at sleva with right_03
    n "\"Славное самопожертвование, Кей-тян!!!"
    extend " Ну как, Сатоко?"
    extend " Безоговорочная победа, ммм?!!\""
    show satoko si bik_a1 at sprava with right_03
    n "\"П... поверить не могу!!!"
    show satoko si hn_a1 with dissolve_02
    extend " Н-ну и пусть, мне всё равно!!!\""
    n "Сатоко ажно зубами скрипела от злости!"
    extend " Я её уделал!!!"
    n "Теряя сознание, я смаковал сладкий вкус победы."
    nvl clear
    scene bg 217 with m1
    show rena si ko_b1 at sprava with m1_03
    stop music fadeout 0.2
    n "И тут Рэна вдруг перестала верещать..."
    n "\"......Рика-тян, ты не хочешь есть своего кролика?"
    extend " Почему?.. Я слишком много морской воды добавила?..{w=0.3} ...добавила?\""
    play music the_rika
    n "Рика-тян вынула зубочистку из кролика и с потрясённым видом взяла его сложенными ковшиком ладошками."
    nvl clear
    show rika si ko_a1 at sleva with dissolve_04
    n "\"......Кролик... такой бедненький..."
    extend " Я хочу ему помочь...\""
    stop music fadeout 0.2
    play sound wa_030
    show black
    show ryuuketu with ImageDissolve("efe/ryuuketu_efe.png", 0.3, 50, reverse=True)
    $ renpy.pause(0.2)
    hide black
    hide ryuuketu
    show rena si ka_b1 with dissolve_02
    n "*Хлоп!*"
    nvl clear
    $ renpy.pause(1.0)
    n ".........Кровь со звуком выстрела брызнула из носа Рэны."
    nvl clear
    play music msys03_treat
    n "\"...Т...{w=0.2} Т-Т... ТАААК МИИИИИИЛООООООО!{w=0.2}...{w=0.2}...{w=0.2} Сегодня...... Рэна точно...{w=0.2} заберёт тебя домоооой..........\""
    n "{nw}"
    n "Её макушка пошла кругом."
    n "А затем, придя в себя, Рэна схватила все яблочные дольки, рассыпанные вокруг меня, и водворила их на тарелку."
    nvl clear
    show rena si wa_b1 with dissolve_02
    n "\"Теперь вам не придётся грустить!..{w=0.5} Я отдаю вас Рике-тян, да...{w=0.2} точно!\""
    n "Завладевшая блюдом с кроликами Рика-тян взяла руку ничего не понимающей Сатоко и воздела её кверху, как судия.{w=1.0}{nw}"
    extend " И произнесла:"
    n "{nw}"
    show rika si ni_a1 with dissolve_02
    n "\"Ну а теперь победили мы.\""
    nvl clear
    hide rena
    hide rika
    with dissolve_04
    show mion si to_a2 at central with dissolve_02
    n "{cps=*0.7}\"...Ч... ...Чего-о-о-о-о-о-о-о-о?!!{/cps}"
    extend " Это что же получается?!! Из проигравших стали победителями?!!!\""
    n "\"......Ха хэ-хо хухэ хё хахо...... (Да мне-то уже всё равно...)\""
    n "{nw}"
    n "......Итак... моя смерть... оказалась напрасной..."
    nvl clear
    show cinema with x_15
    show title02 with Dissolve(3.0)
    stop music fadeout 5.0
    $ renpy.pause(2.0)
    show black behind title02 with Dissolve(3.0)
    $ renpy.pause(1.0)
    scene black with right
    play ambient lsys11
    $ save_name = "Глава о Похищенных Демонами.\nДень Второй, посещение свалки"
    n "Весь день мы резвились вовсю..."
    n "И даже не поняли, почему так быстро садится солнце."
    nvl clear
    scene bg 039 zakat with Dissolve(3.0)
    show mion si wink_a1 at sleva with dissolve_04
    n "\"Бывайте, Рэна и Кей-тян! Увидимся завтра!\""
    n "\"Спасибо за сегодняшнее, Мион. Повеселились на славу.\""
    show rena si def_b1 at sprava with left_03
    n "\"Увидимся завтра!!!\""
    n "{nw}"
    n "Сатоко и Рика-тян уже ушли. Распрощавшись и с Мион, мы с Рэной отправились домой, наслаждаясь вечерним воздухом."
    nvl clear
    scene bg 041 zakat with right
    show rena si def_a1 with left_03
    n "\"...Спасибо, что пришёл, Кейти-кун."
    extend " Понравилось?..\""
    n "\"Ещё бы."
    extend " Очень понравилось."
    extend " Мне даже домой идти не хочется!\""
    n "\"О... ну тогда, может быть,"
    extend " немного пройдёмся?{w=0.2}{nw}"
    extend " ...пройдёмся?\""
    n "\"Пройдёмся?"
    extend " Идти далеко?\""
    n "\"Немножко... но мы быстро дойдём!\""
    n "Эй, разве полный игр и прогулок день тебя не утомил?"
    n "Хоть меня и застало врасплох её предложение, возражать не стал."
    nvl clear
    scene black with Dissolve(1.0)
    play repeated lsys19
    scene bg 141 zakat with Dissolve(1.0)
    $ renpy.pause(1.5)
    scene black with Dissolve(1.0)
    scene bg 029 zakat with Dissolve(1.0)
    $ renpy.pause(1.0)
    scene bg 032 zakat with Dissolve(1.0)
    $ renpy.pause(1.0)
    scene white with dissolve_04
    scene bg 001 zakat with dissolve_02
    $ renpy.pause(1.0)
    scene bg 006 zakat with Dissolve(1.0)
    $ renpy.pause(1.0)
    play music msys05
    n "Пройдя по узенькой тропке, подымавшейся на вершину пригорка, мы вдруг узрели впереди широкий пустырь."
    n "{nw}"
    n "Похоже на... безжизненные останки строительной площадки."
    nvl clear
    scene bg 004 zakat with Dissolve(1.0)
    $ renpy.pause(1.0)
    stop repeated fadeout 1.0
    $ renpy.pause(1.0)
    scene bg 023 zakat with dissolve_04
    n "На спускавшемся к реке склоне тут и там возвышались кучи хлама."
    n "Должно быть, все они свалены здесь незаконно. Бьюсь об заклад, в газетах о чём-то таком писали."
    nvl clear
    show rena si wa_a1 at sprava with m1
    n "\"Хи-хи-хи!"
    extend " Давненько я здесь не быва-а-ала~а! Интересно, что тут новенького... новенького!\""
    n "\"Давненько?.. Рэна, ты хочешь сказать, что мы шли к этой... куче мусора?!\""
    show rena si ka_a1 with dissolve_02
    n "\"Э-это не мусор!.."
    extend " Для Рэны это гора сокрооовищ...\""
    nvl clear
    n "Рэна ожидаемо вошла в свой «миииленький» режим."
    n "Так она и здесь может найти что-то «миииленькое»??"
    nvl clear
    n "\"Ура!.. Новая горка!....."
    extend " Что же там такое... такое!..\""
    n "Рэна проворно поскакала вниз по шаткому спуску."
    extend " ...Как и положено сельской девчушке."
    n "\"Эй, подожди, я сейчас{cps=*0.5}......{/cps} Оп-ля!..\""
    n "Поскольку я вырос в городе, мои навыки горнолаза не годятся совсем никуда..."
    nvl clear
    n "\"Ничего, Кейти-кун, просто жди там! Я скоро!\""
    n "Я-то хотел пойти за ней... но уж лучше послушаюсь-ка."
    n "\"Аккуратнее!.."
    extend " Не упади там!\""
    n "\"Не бойся, не бойся!"
    extend " Со мной ничего не случится!\""
    nvl clear
    hide rena with left
    n "Прыгая аки газель, Рэна исчезла за холмом из досок."
    n "{nw}"
    n "Хоть и не нравилось оставаться в одиночестве, я слишком устал после длинного дня, чтобы за ней идти."
    n "После исчезновения бойкой Рэны лишь спокойствие окружало меня..."
    nvl clear
    $ renpy.pause(2.0)
    n "От пения вечерних цикад воздух потихоньку становился прохладнее..."
    n "Утомление всё сильнее клонило меня в сон."
    nvl clear
    n "В следующую секунду сон мигом пропал от шороха чьих-то шагов по гравию. Подскочив, я испуганно обернулся."
    nvl clear
    scene black with left_03
    scene bg 025 zakat
    show tomi si_def at sleva
    with left_03
    n "Какой-то парень, выглядевший фотографом, уставился на меня сквозь объектив фотокамеры."
    n "Он загорел и неплохо сложен,"
    extend " правда, веет от него некою ненадёжностью, неуверенностью."
    n "...Ну, на плохого человека он не похож."
    nvl clear
    show tomi si_uh with dissolve_02
    n "\"О-ох!"
    extend " Ты меня напугал!..\""
    n "Вижу, фотограф не ожидал, что я вдруг подскочу и обернусь. Он чуть не вскрикнул."
    n "Ага, кто б говорил!"
    nvl clear
    n "\"Кто тут кого ещё напугал-то...\""
    show tomi si_wa with dissolve_02
    n "\"Прости, прости."
    extend " Не хотел тебя пугать. Ты из Хинамидзавы?\""
    n "{nw}"
    n "По вопросу понятно, что сам он не из деревни."
    nvl clear
    n "Между тем, не обращая внимания на мою недоверчивую физиономию, парень представился."
    show tomi si_def with dissolve_02
    n "\"Я — Томитаке,"
    extend " свободный фотограф."
    extend " Временами посещаю Хинамидзаву.\""
    n "Да я как-то его именем и не интересовался..."
    nvl clear
    n "\"Разве не принято спрашивать перед съёмкой разрешения?\""
    show tomi si_wa with dissolve_02
    n "\"Прости, прости."
    extend " Я обычно диких птиц фотографирую."
    extend " Раньше как-то не задумывался о том, чтоб спросить у них разрешения."
    extend " А-ха-ха-ха!\""
    n "Это что ещё значит? Он что, принимает меня за птицу?"
    nvl clear
    n "\"Нет-нет, видишь ли, в лучах заката ты выглядел так фотогенично..."
    extend " Прости, что сперва не попросил разрешения.\""
    n "{nw}"
    n "А взрослые умеют быть обходительными."
    n "Чуть-чуть польстил — и я уж не злюсь за испуг."
    nvl clear
    n "Мне, вообще-то, не особо хотелось ошиваться с каким-то говорливым дядькой, да и Рэны всё ещё нигде не видать."
    n "Но этот дядька... Томитаке-сан всё продолжал и продолжал болтать, даже не замечая моих резких ответов."
    nvl clear
    n "\"Кейти-кууун! Прости за задеееержку!"
    extend " Я почти закооончила!\""
    n "Высунувшись из-за дальней груды хлама, Рэна помахала рукой."
    n "\"Так ты здесь с подругой?"
    extend " ......Что ей там надо?\""
    n "Сам бы хотел знать."
    nvl clear
    n "\"Э, кто знает..."
    extend " Наверно, проверяет давным-давно ею расчленённый и закопанный труп?\""
    n "Томитаке-сан застыл на секунду."
    n "Вот же ж. Ну и хрень я ляпнул, совсем как Рэна или другие девочки."
    nvl clear
    stop music fadeout 1.0
    show tomi si_def with dissolve_02
    n "\"Да... Ужасный был случай. Одну руку так и не нашли, верно?\"{w=3.0}{w=2.0}{nw}"
    nvl clear
    show rena si def_a1 at sprava with m1
    n "\"Ха-ха-ха! Спасибо, что подождал, Кейти-кун!"
    extend " Долго ли я пропадала?{w=0.3} ......пропадала?\""
    n "\"Похоже, пора мне сматывать удочки."
    extend " Прости, что напугал, «Кейти-кун».\""
    hide tomi with right_30
    n "Многозначительно усмехнувшись, Томитаке-сан повернулся и ушёл, растворившись в сумерках."
    n "Я даже ответить не успел, и теперь мне оставалось лишь ругать себя за тугодумие."
    nvl clear
    show rena si nande_a1 with dissolve_02
    n "\"Кейти-кун, ты сердишься?"
    extend " ...Почему?..{w=0.2} \n......почему?\""
    n "Рэна здесь ни при чём, но надо бы её подколоть на всякий пожарный."
    nvl clear
    scene bg 042 zakat with right
    play music msys05
    n "\"Ну и как оно?"
    extend " Нашла чё-нить хорошее?\""
    show rena si wa_a1 at sprava with dissolve_02
    n "\"Да!"
    extend " Слушай, слушай!"
    extend " Угадай, что я нашла?"
    extend " Кента-кунааа!!!\""
    n "\"Кента-куна?!"
    extend " ......А, ты про того дядьку, какой стоит перед каждым KFC?..{w=0.6} Такую статую в полный рост, верно?\""
    n "\"...Верно! Про Кента-куна! {font=DejaVuSans.ttf}☆{/font}"
    extend " ......Хау-у...... мииилый...... Рэна хочет забрать его домооой... {font=DejaVuSans.ttf}☆{/font}\""
    n "Уж не знаю, что именно для неё «мииилое», но чем-то Кента-кун явно ей приглянулся."
    nvl clear
    n "\"Это ведь просто хлам, верно?"
    extend " Раз ты так хочешь, можешь забрать его домой.\""
    show rena si nande_a1 with dissolve_02
    n "\"Он завален каким-то мусором."
    extend " Его не так просто достать..."
    extend " Да и скоро уже стемнеет, а там нет фонарей...\""
    n "Рэна выглядела очень расстроенной тем, что не может забрать домой найденное с таким трудом сокровище."
    nvl clear
    n "\"Я тебе помогу."
    extend " Считай, благодарность за сегодняшний вкусный обед.\""
    show rena si hau_a1 with m1
    n "\"...Хау..... спа-спасибо.......\""
    n "{nw}"
    n "Возвращавшиеся ко гнёздам птицы возвещали о скором наступлении темноты."
    nvl clear
    n "\"Кейти-кун мне поможет~{font=DejaVuSans.ttf}☆{/font}!..{w=0.3} Я смогу забрать Кента-куна домой..... Хау...\""
    n "Бессознательно покачиваясь на ходу, Рэна мечтательно улыбалась."
    nvl clear
    n "Я не хотел портить ей настроение, а потому решил задать вопрос как бы невзначай."
    n "\"Эй, Рэна..."
    extend " А в прошлом там что-нибудь происходило?\""
    n "\"Говорят, здесь пытались построить дамбу."
    extend " Но я мало что знаю...... хау...\""
    n "\"Может быть, во время строительства что-то произошло?"
    extend " Несчастный случай, к примеру.\""
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    show rena si def_a1 with dissolve_02
    n "{nw}"
    n "\"Не знаю.\"{w=0.2}"
    nvl clear
    n "Слишком уж резок тон её голоса."
    n "То был скорее отказ, нежели ответ."
    n "Должно быть, выглядел я очень удивлённым,"
    extend " так как лицо Рэны тут же смягчилось."
    nvl clear
    play ambient lsys11
    show rena si wa_a1 with dissolve_02
    n "\"Вообще-то я сюда только в прошлом году переехала.\""
    n "\"Что?"
    extend " Так и ты перевелась?"
    extend " Я-то думал...\""
    n "\"Потому-то и не особенно в курсе того, что здесь раньше происходило."
    extend " ...Прости~{font=DejaVuSans.ttf}☆{/font}!\""
    n "Насколько я понял, она многого не знает и говорить об этом не хочет."
    nvl clear
    scene bg 038 zakat with left_03
    n "Да и чему тут удивляться."
    extend " Никакую девочку не порадуют подобные разговоры."
    n "{nw}"
    n "{i}«Да... Ужасный был случай. Одну руку так и не нашли, верно?»{/i}"
    n "{nw}"
    n "В мозгу по-прежнему отдавались слова Томитаке-сана. Если это правда, то..."
    n "{nw}"
    n "Лишь цикады, казалось мне, могли знать ответ."
    nvl clear
    $ renpy.pause(3.0)
    show cinema with x
    show title02 with Dissolve(3.0)
    $ renpy.pause(3.0)
    scene black with Dissolve(3.0)
    show tips_received:
        xalign 0.5 yalign 0.2
    show text "Особняк Маэбара\nСамосуд на стройплощадке дамбы":
        xalign 0.5 yalign 0.3
    with Dissolve(1.0)
    $ renpy.pause(4.0)
    hide tips_received
    hide text
    with Dissolve(1.0)
    $ day_result = "onik_day03"
    call screen day_completed(tips="onikakusi")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
