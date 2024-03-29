    $ save_name = "Глава о Смертоносном Проклятии.\nДень Четырнадцатый, безмолвие"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    scene bg 086 with Dissolve(15.0)
    scene black with Dissolve(3.0)
    play ambient lsys19
    n "............Башка раскалывается."
    n "......Небо...... слепит."
    n "......Холодно........."
    extend " Больно."
    nvl clear
    n "Различные ощущения по частям пробуждают мои чувства от сна."
    nvl clear
    scene bg 086 with Dissolve(1.0)
    n "Я понял... что лежу на берегу реки лицом вниз."
    nvl clear
    n "...Во многих местах тело страшно болит."
    n "Кое-где на суставах содрана кожа. То темнея, то светлея, вокруг ссадин та стремительно набухала кровью."
    n "......Резкая боль при каждом движении \nпоказывала — некоторые кости сломаны."
    nvl clear
    n "...Поглядевши вверх, оценил, как высоко висит мост, с которого я упал."
    nvl clear
    n "......Чудо, что смог снова открыть глаза, свалившись оттуда."
    nvl clear
    scene bg 004 with left_03
    n "Неподалёку валялось развалившееся автомобильное кресло — наверно, детвора притащила для своих игр."
    n "{nw}"
    n "......Сдаётся... именно благодаря тому, что так удачно подвернулось оно, я и выжил."
    extend " Чудо, что тут сказать..."
    nvl clear
    n "Впрочем, не знаю... к счастью оно для меня — или к несчастью."
    n "Пускай смерть миновала...... но ведь я по-прежнему в безумном мире."
    nvl clear
    scene bg 205 with dissolve_04
    n ".........Сколько я пролежал без сознания?"
    nvl clear
    n "...Солнце в зените — значит, всего час или два, не больше."
    n "...Но если судить по телесной слабости, то не похоже, чтоб прошла всего пара часов."
    n "......Судя по ощущениям, я пролежал здесь никак не меньше десяти лет."
    nvl clear
    scene bg 086 with Dissolve(1.0)
    n "\".........Ох............ Ой-ёй-ёй...............\""
    n "Чем больше я приходил в себя, тем сильнее ощущал боль."
    n "......Такую, что даже подумалось: ох, лучше бы не просыпался."
    n "{nw}"
    n "......Надо пойти к врачу..."
    extend " Точно... к Начальнику в клинику..."
    nvl clear
    n "Только про неё подумал...... как в памяти начало всплывать то, что лучше бы не вспоминать."
    nvl clear
    n "Сатоко на мосту больше не видно."
    n "Вернулась в Хинамидзаву, стало быть..."
    n "{nw}"
    n "Пришла на обследование одетой...... и рассказала, что я чудн{u}о{/u} себя вёл."
    n "Без сомнений, полиция ждёт меня с распростёртыми объятьями."
    nvl clear
    scene bg 004 with left_03
    n "Теперь уж точно либо посадят за убийство дядьки, либо упекут в сумасшедший дом."
    n ".........Впрочем... какая разница."
    n "{nw}"
    n "Только бы избавили меня от боли."
    n "А уж потом пусть хоть варят, хоть в печь сажают живьём."
    nvl clear
    n "Подволакивая ногу, я пошёл, шатаясь из стороны в сторону."
    nvl clear
    scene black with left_03
    scene bg 141 with left_03
    n "Спустившись по берегу, я пробрался звериной, что ли, тропой через лес......"
    extend " Шёл наобум, надеясь выйти на знакомую дорогу."
    nvl clear
    scene black with left_03
    stop ambient fadeout 1.0
    scene bg 046 with left_03
    n "...Наконец найдя её... я поковылял в клинику."
    n "{nw}"
    n ".........Не в дом — но в клинику, где меня приняли за сумасшедшего."
    nvl clear
    scene bg 041 with left_03
    n ".........Духота — как в бане."
    nvl clear
    n "......Ветерка ни малейшего; воздух застоялся — не движется."
    nvl clear
    n "И всё время тянуло чем-то вроде сгоревшей яичницы, заставляя морщиться."
    n "{nw}"
    n "......И тут до меня дошло."
    n "Цикады не пели."
    nvl clear
    if renpy.loadable("music/Matsuri/21 - Minna, Inakunatta.ogg"):
        play music minna_inakunatta
    else:
        play music snow4
    n "Впервые на моей памяти Хинамидзава погрузилась в безмолвие."
    n "{nw}"
    n "...Раньше-то деревня не смолкала ни на единый час: по утрам радостно чирикали птицы, днём отовсюду звучал назойливый стрёкот дневных цикад, а на закате хигураси оглашали своим хором окрестности."
    nvl clear
    n "Сейчас же насекомых не слышно."
    nvl clear
    n "Только шелест, раздававшийся, когда ветер шевелил кроны."
    n ".........Подобное безмолвие я видел впервые."
    nvl clear
    n "Да и одиноко шелестевшие кроны казались какими-то безжизненными."
    nvl clear
    n "Они желты, и листьев с них опало не по времени года много."
    n "...Даже сорняки на обочине, должные расти сейчас буйными зарослями, пожелтели, ссохлись."
    n "{nw}"
    n "......От привычной июньской Хинамидзавы остался лишь солнечный свет..."
    extend " Такое ощущение, будто вдруг взяла и раньше срока настала осень."
    nvl clear
    n "\".......................................\""
    n "Поглядев на палые листья и увядшие сорняки, обнаружил множество лежавших на земле лапками кверху жучков."
    extend " ......Они не двигались."
    nvl clear
    n "Мёртвые."
    n ".........Присмотрелся. Они валялись там, \nздесь — повсюду... будто какой ребёнок рассыпал своё собрание насекомых."
    nvl clear
    n "......Интересно... что это за зловоние?"
    n "Воняет, как будто яичница сгорела..."
    n "{nw}"
    n "...И жуки мёртвые валяются, и деревья, раньше срока сбрасывающие листву......"
    n ".........Тут что, распылили средство против сорняков или вредных насекомых?"
    n "......Говорят, школу раз или два в году окуривают чем-то, чтоб избавиться от вредителей..."
    nvl clear
    scene black with right_03
    scene bg 042 with right_03
    n "Несмотря на стоявший в разгаре день, никого не было видно."
    n "Хоть и светло по-дневному...... но кажется, будто иду тёмной ночью."
    nvl clear
    n "Ну и верно — кому охота гулять, коль на улице такой смрад."
    n ".........И в чём же всё-таки дело..."
    n "{nw}"
    n "...............Ни звука,{w=0.8} ни малейшего шума,{w=0.9} ничьего дыхания... Безмолвие окутало Хинамидзаву."
    nvl clear
    scene black with right_03
    scene bg 039 with right_03
    n "Повернуть здесь...... и вскоре покажется школа."
    n "{nw}"
    n "...Но никаких звуков не слышно......"
    extend " Ни радостных детских воплей, ни диких криков."
    n "............Одна только... тишина."
    nvl clear
    scene black with left_03
    n "Когда тишина, которую я упорно пытался не замечать, стала давить на уши... показалась школа."
    nvl clear
    scene bg 093 with right_03
    n "И тогда — наконец-таки — раздались другие звуки."
    n "......Шумели двигателями грузовики."
    nvl clear
    n "Во дворе школы стояли, включив моторы, несколько грузовиков на высоченных колёсах."
    n "И около десятка человек, одетых в дождевики, возились рядом, сгружая что-то из кузовов."
    n "...Мне в своей небрежной одёжке и то жарковато... Каково им-то, поди."
    nvl clear
    n "......А-а, точно."
    n "Школа занимает здание у лесничества..."
    extend " Ничего диковинного в том, что их машины что-то делают на школьном дворе."
    n "{nw}"
    n "...Так иль иначе...... Чем они там, у грузовиков, занимаются?"
    n ".........Бедолаги... Приходится работать в такой жаре, да ещё и вонь..."
    nvl clear
    scene bg 027 with left_03
    n "Они выгружали какие-то разноцветные штуки, которые затем выкладывали на земле в ряды."
    n "Выгружаемые предметы...... походили на большие, словно бы сшитые из разноцветных заплаток мешки."
    n "{nw}"
    n "И весили они, похоже, прилично — те перетаскивали каждый попарно."
    nvl clear
    n "Их складывали стройными рядами — будто на прилавке с тунцами на рыбном рынке."
    n "Тунцов тех на дворе лежало немало — где-то несколько сотен."
    nvl clear
    n "...Забыв про евшую меня боль...... я заворожённо смотрел на невиданные доселе работы лесного хозяйства..."
    nvl clear
    scene bg 028 with right_03
    n "Пока я, позабывши про всё на свете, стоял у ворот... работавшие на площадке меня заметили."
    n "......Тыкая в меня пальцами, они о чём-то бурно заспорили."
    n "{nw}"
    n ".........Подумав, что сейчас будут кричать, чтоб не мешал работе... я решил поскорее уйти."
    nvl clear
    scene bg 093 with right_03
    n "Тут сзади подъехало ещё два грузовика."
    n "Я отошёл в сторону, пропуская машины во двор."
    n "......Кузова закрывает брезент, но и так видно, что загружены они доверху."
    nvl clear
    n "......От жуткого смрада, донёсшегося, когда те проезжали мимо, захотелось чихнуть."
    n "......Теперь воняло не пригоревшей яичницей... а чем-то намного хуже — вроде протухших, полуразложившихся крабьих потрохов."
    n "{nw}"
    n "Да что за чёрт..."
    n "...Ну чё сегодня отовсюду чем-то воняет..."
    nvl clear
    n "Тут взгляд выхватил иероглифы, намалёванные на борту проезжавшего грузовика белой краской."
    nvl clear
    scene black with dissolve_04
    n "{b}«Сухопутные силы самообороны»{/b}."
    n "{nw}"
    n "............Чего?"
    n "Силы самообороны?.. В смысле — армия?"
    extend " А чё они делают во дворе нашей школы?.."
    nvl clear
    scene bg 093 with dissolve_04
    n "\"Эй ты!"
    extend " Как ты сюда попал?!\""
    n "Неожиданно чья-то сильная рука схватила плечо."
    nvl clear
    n "Обернувшись, я увидал, что рядом стоит крытый внедорожник сил самообороны."
    n "...Сидевшие в нём люди были одеты во что-то вроде зелёных комбинезонов-дождевиков; лица — точь-в-точь как в кино — скрывали противогазы, а за спинами висели здоровенные газовые баллоны."
    n "...Оттого, что комбинезоны закрывали тех с головы до пят, не оставляя ни единого участка кожи открытым, выглядели они престранно."
    nvl clear
    n "\"............Как попал, говорите?..... Оооох-х-х......\""
    n "При попытке ответить рана на голове отозвалась резкой болью."
    n "{nw}"
    n "...Увидев, как исказилось моё лицо, военные переглянулись."
    n "......Из-за масок лиц не видать... но, похоже, они ошеломлены."
    nvl clear
    n "\"Ты из Хинамидзавы?"
    extend " Как звать и где ты живёшь?\""
    n "\".........Пока живу здесь..."
    extend " Зовут... Маэбара. Кейти."
    extend " ...А, живу я по адресу: город Шишибонэ, деревня Хинамидзава, улица XXX, дом такой-то...\""
    n "Когда я без колебаний назвал имя и адрес, военный, сидевший во внедорожнике, начал вызывать кого-то по рации."
    nvl clear
    n "\"...Вызываю штаб, приём."
    extend " Вызываю штаб, приём."
    extend " Это 402-й. Найден выживший."
    extend " Повторяю, это 402-й, найден выживший."
    extend " У въезда на двор лесничества.\""
    n "\"Это штаб. Вас поняли."
    extend " Как можно скорее позаботьтесь о его безопасности."
    extend " Каково состояние выжившего?\""
    n "\"Состояние удовлетворительное."
    extend " По всему телу ссадины и синяки, но без угрозы для жизни."
    extend " Передвигается самостоятельно."
    extend " Сейчас обеспечим ему защиту и доставим в штаб.\""
    nvl clear
    n ".........Я готовился встретить полицию... но вот Силы самообороны......"
    n "...Это уж чересчур."
    nvl clear
    scene black with left_03
    n "Подгоняемый ими, я полез на заднее сиденье."
    n "А потом... мне велели надеть такой же большущий противогаз, что носили все."
    n "...Я беспрекословно его надел, и один из экипажа туго-натуго затянул ремни."
    nvl clear
    n "......Он тяжёл, в нём жарко, мало что видно, а ещё трудно дышать."
    n "...Через очки противогаза всё выглядело неестественным."
    n "{nw}"
    n "Сопящее дыхание моё: «Пх-х-х... Пх-х-х-х...» — казалось дыханьем чудовища."
    n "{nw}"
    n "......Я совсем перестал соображать, что происходит."
    nvl clear
    n "Осторожно задал вопрос тому, кто затягивал на мне противогаз."
    nvl clear
    n "\"......Это...... извиняюсь......"
    extend " А что-то случилось?.....\""
    n "\"Ты где был?"
    extend " Что делал?\""
    n "{nw}"
    n "...Тот вопросом отвечал на вопрос..."
    extend " Ну что такое, я ж первым спросил..."
    nvl clear
    n "\".........Я в горах был... Упал с подвесного моста......"
    extend " Лежал, думаю, на берегу реки без сознания......"
    extend " Какой нынче день, знать не знаю.\""
    n "\"Сегодня двадцать второе июня пятьдесят восьмого года Сёва."
    extend " Среда.\""
    nvl clear
    n "...Ну дела......"
    extend " Сатоко сбросила меня с моста двадцать первого, во вторник."
    n "{nw}"
    n "......Получается... целый день напролёт я дрых на том берегу."
    nvl clear
    n "\"......Так что ж случилось-то?"
    extend " Что здесь делают Силы самообороны?"
    extend " Учения какие?\""
    n "\".......................................\""
    n "......Мой вопрос что, так неуместен?"
    n "...Никто не проронил ни слова."
    nvl clear
    $ save_name = "Глава о Смертоносном Проклятии.\nДень Четырнадцатый, гибель деревни"
    scene bg 101 with dissolve_04
    stop music fadeout 1.0
    n "Тот, что связывался со штабом, включил радиоприёмник."
    n "...И настроил его на какую-то волну."
    nvl clear
    n "......Послышался голос знакомого диктора..."
    nvl clear
    n "\"...провели в резиденции Премьер-министра."
    extend " Генеральный секретарь Кабинета министров Окуно ответил на заданные журналистами вопросы по поводу недостаточно быстрого развёртывания Сил самообороны"
    extend " при реагировании на беспрецедентное стихийное бедствие.\""
    nvl clear
    n "\"...считаем... что достаточно быстро приняли меры в ответ на просьбу губернатора развернуть войска.\""
    nvl clear
    n "\"Такими словами отвечал он, подразумевая, что после получения просьбы Силы самообороны были развёрнуты без промедления"
    extend " и винить за задержку следует управление префектуры."
    n "Остаётся под вопросом, насколько быстро губернатор понял, что произошла беспрецедентная катастрофа, и запросил ввод войск."
    extend " Потерянное на так называемые бюрократические проволочки с решением вопроса о вводе войск время, скорее всего, лишь усилило ущерб."
    extend " Что ж, будем следить за ходом расследования.\""
    nvl clear
    n "\"С вами был Огата, прямой репортаж из резиденции Премьер-министра."
    extend " А теперь ещё раз взглянем на действия правительства по борьбе с катастрофой.\""
    nvl clear
    scene black with down
    play music gas_disaster
    n "В ночь с 21-го июня по 22-е."
    n "Крупномасштабная природная катастрофа произошла в деревне Хинамидзава города Шишибонэ."
    n "{nw}"
    n "Подробности до сих пор неизвестны, но примерная картина такова: где-то в окрестностях посёлка из-под земли вырвался чрезвычайно ядовитый вулканический газ."
    n "Будучи тяжелее воздуха, он пошёл у земли потоком."
    nvl clear
    n "Спустившись по руслу реки, поток газа попал прямо в Хинамидзаву. Всего за несколько часов он покрыл всю область."
    nvl clear
    n "{b}Время — вторая половина ночи,{/b}"
    extend " {b}от двух до четырёх часов{/b}."
    n "{nw}"
    n "Газ накрыл все дома и хозяйства посёлка."
    n "{nw}"
    n "Предположительно, большинство жителей спали, а потому погибли, ничего не успев понять."
    n "{nw}"
    n "Из-за того, что произошла катастрофа поздней ночью, и случилась задержка с её обнаружением."
    n "...И всё же судьба дала возможность своевременно заметить случившееся."
    nvl clear
    n "{b}Три часа ночи{/b}."
    n "{nw}"
    n "Окиномийская газетная лавка послала в хинамидзавское отделение машину с грузом утренних газет."
    n "{nw}"
    n "По прибытии рассыльный должен был отзвониться, но в тот день звонок так и не поступил."
    n "{nw}"
    n "Хозяин газетной лавки звонил снова и снова, но из отделения не отвечали."
    n "{nw}"
    n "Он отправил старшего сына посмотреть, что случилось, — но и сын пропал без вести..."
    nvl clear
    n "\"...До чего ж грустно."
    extend " Будь тогда сделан звонок в полицию или пожарную службу, бедствие могло бы не принять такого размаха."
    extend " По крайней мере удалось бы предотвратить полное уничтожение деревни.\""
    nvl clear
    n "{b}Шесть утра{/b}."
    n "{nw}"
    n "От населения прилегающих к Хинамидзаве местностей начали поступать звонки с жалобами на запах протухших яиц, головокружение/тошноту/головную боль."
    n "{nw}"
    n "Основываясь на том, что звонки одинакового содержания поступали из одного небольшого района,"
    extend " в штабе пожарной службы предположили, что там потерпел аварию грузовик, перевозивший химические вещества, и позвонили в местный полицейский участок."
    nvl clear
    n "{b}Шесть с половиной утра{/b}."
    n "{nw}"
    n "Потеряна связь с машиной, направившейся в Хинамидзаву. Последнее сообщение — о запахе тухлых яиц."
    n "{nw}"
    n "Предполагая, что в окрестностях деревни — смертельно опасный газ, полицейский участок уведомил администрацию и главное полицейское управление префектуры."
    nvl clear
    n "{b}Восемь утра{/b}."
    n "{nw}"
    n "Так как губернатор в это время посещал соседнюю префектуру в качестве проверяющего, начальник префектурной службы предотвращения и устранения последствий стихийных бедствий, действуя соответственно сложившемуся положению, взял управление на себя и развернул штаб по устранению последствий катастрофы."
    n "{nw}"
    n "Однако до губернатора долго не удавалось дозвониться, поэтому произошла значительная задержка."
    nvl clear
    n "\"Как недавно замечали некоторые гражданские общества, поездки чиновников-ревизоров проводятся исключительно для укрепления дружеских отношений с ними, и представляют они собой не что иное, как попойки."
    n "Как сообщают источники, уважаемый губернатор всю ночь был мертвецки пьян и утром спал как убитый."
    extend " Даже когда начальник службы стихийных бедствий смог до него дозвониться, тот был слишком нетрезв, чтобы что-то понять.\""
    n "{nw}"
    n "Пришлось убить целый час на сбор сведений, пока губернатор не понял случившегося и не протрезвел..."
    nvl clear
    n "\"Не говоря уж о губернаторе, начальника ведомства по борьбе со стихийными бедствиями, взявшего на себя управление в отсутствие губернатора, также следовало бы привлечь к ответственности за бездействие."
    extend " Кроме того, для префектуры не было подготовлено программы действий при катастрофах, что ещё больше задержало принятие необходимых мер, приведя к непоправимым последствиям.\""
    nvl clear
    n "{b}Девять часов двенадцать минут{/b}."
    n "{nw}"
    n "По совету главного полицейского управления губернатор запросил ввод Сил самообороны."
    n "{nw}"
    n "Когда группа войск химической защиты, оснащённая защитой от газа, прибыла на место, с начала катастрофы прошло более восьми часов..."
    nvl clear
    n "\"Так или иначе, очень не повезло, что произошла она глубокой ночью."
    extend " Случись та же катастрофа днём, и всё сложилось бы совсем иначе.\""
    nvl clear
    n "Население всех составлявших деревню хозяйств погибло."
    n "{nw}"
    n "Жертв насчитывается более тысячи."
    n "{nw}"
    n "Силы самообороны до сих пор уточняют данные, но, скорее всего, число жертв будет лишь возрастать..."
    nvl clear
    n "\"В гостях у студии Фудзивара-сэнсэй, профессор университета XX..."
    extend " Сэнсэй, что вы скажете насчёт подобной внезапной утечки газа?\""
    nvl clear
    n "\"В районах вулканических кратеров — не такое и редкое дело."
    n "В Японии много действующих вулканов,"
    extend " и около их кратеров опасность извержений ядовитых газов крайне велика, так что альпинистам категорически не следует к ним приближаться.\""
    nvl clear
    n "\"Значит, газ, пахнущий тухлыми яйцами, что поразил Хинамидзаву, часто встречается у кратеров?\""
    n "\"Судя по характерному запаху тухлых яиц, я полагаю, газ этот — сернистый водород вулканического происхождения, виновник множества несчастных случаев."
    extend " При высокой концентрации очень опасен.\""
    nvl clear
    n "\"Хинамидзава расположена вдали от любых вулканов,"
    extend " но не мог ли сернистый водород как-нибудь выйти на поверхность не через кратер?\""
    n "\"За неимением более точных сведений я не могу говорить с уверенностью......"
    extend " однако известно, что в зарубежных странах происходили утечки газа из подземных лавовых бассейнов под горячими источниками."
    extend " Они происходят крайне редко, но всё же означают, что утечка газа возможна и вдали от кратера.\""
    nvl clear
    n "\"Благодарим вас, сэнсэй..."
    extend " Насколько нам известно, Управление национальной обороны только что сделало заявление."
    extend " Морикава-сан?\""
    nvl clear
    n "\"Да, говорит Управление обороны."
    extend " Управление только что объявило результаты проведённого Химическим институтом Сухопутных сил самообороны анализа вулканического газа, ставшего причиной трагедии."
    extend " Он представляет собой смесь углекислого газа и сероводорода.\""
    nvl clear
    n "\"Морикава-сан, скажите, продолжает ли облако газа распространяться?\""
    n "\"На данный момент, по докладу Девятой дивизии Сухопутных сил самообороны, ответственной за проведение спасательной операции, концентрация газа в воздухе становится меньше."
    extend " Дальнейшего распространения можно не опасаться."
    n "Тем не менее окрестности деревни Хинамидзава всё так же опасны. По их словам, необходимо продолжать наблюдение за развитием событий.\""
    nvl clear
    n "\"С вами был Морикава, прямой репортаж из Управления национальной обороны."
    extend " Продолжим репортажем о жителях окрестностей Окиномии, вынужденных покинуть свои дома."
    extend " В данный момент один из наших сотрудников находится в начальной школе Симосинодзаки, ставшей лагерем для...... *чшшш*... щает... *чш-ш-ш*... *чш-ш*...\""
    nvl clear
    scene bg 101 with up
    n "\"............Что это всё...{w=0.8}......... значит?\""
    n "{nw}"
    n "Ни один из сидевших в трясшемся на неровной дороге джипе мне не ответил."
    nvl clear
    n "Беспрецедентная природная катастрофа......{w=1.0} стёрла Хинамидзаву с лица земли... за одну ночь?.."
    n "{nw}"
    n "А где эта Хинамидзава?"
    n "...Наверно, какая-то деревенька глубоко в горах?.."
    n "Так всегда по радио говорят..."
    n "{nw}"
    n "Одни только названия... непонятно где расположенных мест, о которых ты и слыхом не слыхивал........."
    nvl clear
    n "Уничтожена?.."
    n "Что значит — «уничтожена»?.."
    n "Почему говорится только про погибших и раненых?.."
    n "Выживших сколько?"
    n "И куда все... перебрались?.."
    nvl clear
    scene bg 188 with dissolve_04
    n "Впереди наконец показалась клиника Начальника."
    nvl clear
    n "Впервые вижу висящий на флагштоке клиники флаг."
    n "......Флаг был наш, государственный, с Восходящим солнцем, — и он просто-напросто висел, устало поникнув..."
    nvl clear
    n "Стоянку загромоздили палатки Сил самообороны и тяжёлая техника."
    nvl clear
    scene bg 190 with left_03
    n "Завидев подъехавший джип, из клиники выбежали с носилками люди в белых халатах и противогазах."
    nvl clear
    n "\"Всё, парень, ты выбрался."
    extend " Как ты?"
    extend " Ходить можешь?\""
    n "\".........Могу..."
    extend " Ох-х-х......\""
    n "Стоило лишь охнуть от боли, как меня заставили лечь на носилки."
    n "......Человек, похожий на врача, начал меня осматривать, разговаривая с кем-то по рации."
    nvl clear
    scene bg 187 with right_03
    n "\"Много внешних повреждений."
    extend " Вероятны переломы и повреждения внутренних органов."
    extend " На голове огромная рана."
    extend " Зрачки в порядке. Крови на глазном дне не видно, однако нельзя отрицать возможное повреждение головного мозга...\""
    n "Тут... из клиники вынесли носилки с людьми."
    n "{nw}"
    n "............Судя по их одежде, то жители Хинамидзавы...{w=0.9} Жертвы."
    nvl clear
    n "Носилки остановились у грузовика."
    n "...Двое человек, взяв одного из лежавших на носилках за ноги да плечи... закинули его \nв кузов — совсем как обычный багаж......"
    nvl clear
    scene black with dissolve_04
    n "\".........О......... Оооох...... О-о-о-о-о-о-о-а-а-ах.........\""
    nvl clear
    n "...В кузове грузовика...... лежала куча тел."
    n "...По тому, как обращались с ними...... стало ясно — они мертвы."
    nvl clear
    scene bg 027 gray with Dissolve(1.0)
    n "И тогда... при виде бесформенных разноцветных мешков, как попало сваленных в кузов{cps=*0.4}.........{/cps}{w=0.7} я вспомнил стройные ряды на школьном дворе, походившие на прилавок с рыбой..."
    nvl clear
    n "{b}Сотни......... мёртвых тел.{/b}"
    n "{nw}"
    n "{b}{cps=*0.6}...Труп...{w=0.8} Труп...{w=0.5} Ещё труп...{w=0.5} Ещё...{w=0.5} Ещё...{w=0.5} И ещё...{w=0.8} И ещё...{w=0.4} И ещё...{w=0.4} Трупы...{w=0.8} Трупы!!!{/cps}{/b}"
    nvl clear
    scene black with dissolve_04
    scene bg 187 with right_03
    n "\"Придурки!!"
    extend " Аккуратнее с жертвами!"
    extend " Он — один из жителей!\""
    n "Солдаты, таскавшие мешки, вытянулись по стойке смирно и приложили руки к вискам........."
    nvl clear
    scene bg 203 with Dissolve(1.0)
    n "{b}\n\n\n\n\n\n\n\n{space=20}{cps=*20.0}......Я пожелал безумной Хинамидзаве сгинуть.{/cps}{/b}"
    nvl clear
    n "{b}Моё...{w=0.8} последнее...{w=0.8} желание...{w=0.8} тоже......{w=0.9} сбылось......{/b}"
    nvl clear
    scene bg 203 _faded with Dissolve(3.0)
    n ".........Ну всё...... Ни черта я не понимаю......"
    n "...Да и хрен с ним..."
    extend " .........Если моё желание... моё проклятие...... исполнится на следующий день......"
    n "То пускай я завтра утром умру."
    n "......И пусть наконец...... закончится та безумная ночь......"
    nvl clear
    scene black with Dissolve(3.0)
    n "\"...?!..."
    extend " Эй, он потерял сознание!!"
    extend " По имени его зовите!"
    extend " Быстро!\""
    n "\"Маэбара-кун!"
    extend " Ты меня слышишь?!"
    extend " Если слышишь, то поморгай!!"
    extend " Маэбара-кун!"
    extend " Маэбара-кун!"
    extend " {b}Маэбара-кун!!{/b}\""
    nvl clear
    n "Вдруг... мне стало наплевать на весь мир..."
    extend " Безразлично стало и то, что кто-то пытается до меня докричаться."
    nvl clear
    n "{b}\"Не дышит!{/b}"
    extend " {b}Освободите дыхательные пути!{/b}"
    extend " {b}Искусственное дыхание!!{/b}"
    extend " {b}Делайте всё, что можете!!{/b}"
    extend " {b}Чёрт, чёрт!!...{/b}"
    extend " {b}Хватит с нас жертв!!{/b}"
    extend " {b}Никто не должен умирать напрасно!!{/b}"
    extend " {b}Пусть он живёт!{/b}"
    extend " {b}Пусть живё-ё-ё-ёт!!\"{/b}"
    n "...Прямо над ухом кто-то, рыдая, кричал."
    nvl clear
    n "Он сказал......... никто не должен умирать напрасно.{w=0.8} Сказал, искренне в это веря."
    n "{nw}"
    n "И его...... очень-очень простая и обыденная правда... запала мне в душу."
    n "......Быть может...... я неправ был, отнимая чужую жизнь, пускай даже и ради Сатоко..."
    nvl clear
    n "...И... если катастрофа — плата за то......"
    n "{nw}"
    n ".........Слишком ты крут, Оясиро-сама..."
    n "............Почему ты... не поразил одного меня?.."
    nvl clear
    n "......Ах да... Сатоко же говорила..."
    n "Настоящее проклятие Оясиро-сама... первым делом убьёт не самого провинившегося... а его близких..."
    n "{nw}"
    n "Проклятие...... Оясиро-сама."
    nvl clear
    n "...До чего удобная отговорка подвернулась в последний миг...... Всё-таки катастрофа — не моё проклятие, но проклятие Оясиро-сама..."
    n "..................Так оно и должно быть, ведь я лежу на носилках, и всё же..."
    nvl clear
    n "......В последний миг я сообразил кое-что."
    n "{b}\n\n\n{cps=*0.6}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}А{w=0.1}-{w=0.1}а{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} {w=0.1}А{w=0.1} {w=0.1}в{w=0.1}е{w=0.1}д{w=0.1}ь{w=0.1} {w=0.1}ш{w=0.1}а{w=0.1}г{w=0.1}о{w=0.1}в{w=0.1}-{w=0.1}т{w=0.1}о{w=0.1} {w=0.1}т{w=0.1}е{w=0.1}х{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} {w=0.1}я{w=0.1} {w=0.1}с{w=0.1}е{w=0.1}г{w=0.1}о{w=0.1}д{w=0.1}н{w=0.1}я{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} {w=0.1}н{w=0.1}е{w=0.1} {w=0.1}с{w=0.1}л{w=0.1}ы{w=0.1}ш{w=0.1}а{w=0.1}л{w=0.1} {w=0.1}н{w=0.1}и{w=0.1} {w=0.1}р{w=0.1}а{w=0.1}з{w=0.1}у{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}{/cps}{/b}"
    nvl clear
    n "Теперь я...... свободен..."
    play ambient lsys11
    n "В голове разносилось пение хигураси... хотя слышать его я не мог."
    n "{nw}"
    n "Их одинокий хор... был мне заупокойной песнью."
    nvl clear
    jump tata_day14_epilogue
