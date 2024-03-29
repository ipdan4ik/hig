    $ save_name = "Глава о Потерянном Времени.\nДень Третий, находка"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with dissolve_04
    n ".........Едва смог заснуть."
    nvl clear
    n "Казалось, я целую вечность ворочался с боку на бок и дёргал ногами."
    n "Но каким-то образом я всё же заснул и не просыпался, пока солнце не поднялось в зенит."
    nvl clear
    play music lsys17
    n "......Усилием воли прогнал желание вернуться ко сну."
    n "И только тут заметил, что телефон звонит."
    nvl clear
    scene white with fade_010
    play ambient lsys22
    scene bg 056 with center_03
    n "На часах было почти полдесятого."
    n "Для утреннего звонка-будильника — слишком поздно."
    nvl clear
    stop music fadeout 0.01
    n "\"Акасака-сан?"
    extend " Доброе утро, звонит Ооиси."
    extend " Мм-хм-хм-хм!\""
    n "Как-то слишком было слышать голос Ооиси-си, не успев проснуться."
    n "В моём нежном ухе он гудел словно колокол."
    n "{nw}"
    n "...Впрочем, благодаря ему в голове окончательно прояснилось."
    nvl clear
    n "\"...А... А-а-а, здрасте."
    extend " Доброго утра.\""
    n "\"Хммм?"
    extend " Вы что, только проснулись?"
    extend " Хоть вы и в командировке, вам, знаете ли, надо просыпаться пораньше!"
    extend " Н-а-ха-ха-ха.\""
    n "\"Совершенно так."
    extend " Впредь постараюсь не залёживаться.\""
    nvl clear
    stop ambient fadeout 1.0
    n "\"У меня есть кое-что ещё, что может прогнать ваш сон."
    play sound wa_044
    extend " ......Из Хинамидзавского участка нам с прочими находками прислали одну очень любопытную вещицу.\""
    n "\"Находки?\""
    if renpy.loadable("music/SNOW4.mp3"):
        play music snow4
    else:
        play music msys07
    n "\"Давайте поговорим на месте, у нас в участке."
    extend " Сможете приехать к нам до обеда?\""
    n "\"Н-Нет, я приеду сейчас же!..\""
    nvl clear
    n "Господин Ооиси знает о моём задании."
    n "И говорит, будто у него есть нечто, что может согнать с меня сон."
    extend " А значит, вряд ли у него что-то, что мне ни к чему."
    nvl clear
    n "По правде говоря, после рассказанного вчера Сато-саном,"
    extend " я, зная, что меня раскрыли, больше не могу просто так бывать в Хинамидзаве."
    n "{nw}"
    n "...Иными словами, расследование заходит в тупик."
    n "И то, что у него есть некие сведения, которые могут навести меня на разгадку, — самая что ни на есть удача."
    nvl clear
    scene black with dissolve_04
    n "Я наскоро умылся, схватил куртку, выбежал на улицу и, поймав такси, отправился в участок Окиномия."
    nvl clear
    scene bg 192
    show ooishi si def_a1 at sleva
    with dissolve_04
    n "\"О, а вот и он."
    extend " Встречайте — Гений маджонга!\""
    n "\"Простите, опоздал."
    extend " ...Ну, что там у вас?\""
    nvl clear
    n "Не собираясь судачить о ночной игре, я сразу же попросил его перейти к делу."
    n "Похоже, он другого и не ожидал и, махнув рукой на маджонг, начал рассказывать."
    nvl clear
    n "\"Как я вам уже говорил, нынче утром с Хинамидзавского участка прислали посылку с найденными вещами.\""
    nvl clear
    n "На все находки, доставленные в малые полицейские участки, сначала составляют бумаги, а потом уже высылают на старший участок в Окиномии."
    n "{nw}"
    n "Господин Ооиси достал из ящика «это» — прозрачный пакет с наклеенным ярлычком — и положил на стол."
    nvl clear
    scene black with dissolve_04
    n "\".........Кошелёк?\""
    n "\"Видимо, так......"
    extend " В нём была только мелочь, никаких банкнот."
    extend " Я сначала думал,"
    extend " что кто-то его спёр, обчистил и выбросил.\""
    nvl clear
    n "Я не понимал, каким образом потерянный кошелёк относится к похищению внука министра, произошедшему в далёком Токио."
    n "{nw}"
    n "Если улика до того потрясающая, что ею заинтересовался господин Ооиси,"
    extend " — например, оказалось, что кошелёк принадлежит пропавшему внуку, — то это сногсшибательное открытие."
    nvl clear
    n ".........Но это же невозможно."
    n "...Разве такая удача бывает?"
    n "Может быть, на кошельке — инициалы?"
    n "Инициалы внука — Инугая Тосики — «Т. И»."
    n "{nw}"
    n "Тут я перестал разделять азарт господина Ооиси по поводу находки."
    nvl clear
    n "Надев прозрачные виниловые перчатки, он протянул мне другую пару."
    n "Кошелёк не казался мне важной уликой, и я не знал, есть ли смысл надевать перчатки, но, решив не отказываться, раз дают, я всё же их натянул."
    nvl clear
    n "Открыв пакетик, он вынул кошелёк и перевернул."
    nvl clear
    n "......Как я и догадывался, там были выбиты инициалы."
    n "Но нет — даже не инициалы: на нём латиницей было выбито: «{b}Toshiki I.{/b}»."
    nvl clear
    scene bg 192
    show ooishi si wa_a1 at sleva
    with dissolve_04
    n "«Ну?» — победоносно усмехнулся господин Ооиси."
    n "«......Чтобы утверждать, что кошелёк принадлежит внуку министра, этого ещё мало», — спокойно сказал я."
    nvl clear
    scene black with fastup
    n "......Ничего этот кошелёк не значит. Господин Ооиси поспешил с выводами."
    n "Ну не может быть, чтоб кошелёк пропавшего внука нашёлся у черта на рогах, да ещё так вовремя."
    n "......Вот-вот, и начнём с того, что Союз обороны Онигафути с делом вообще никак не связан."
    n "А значит, кошелёк — не внука........."
    nvl clear
    n "Я сам не знал, почему мне хотелось так думать."
    n "Там знали всё о, казалось бы, секретнейшем \nделе — от того, что именно произошло, до того, что я должен буду сюда приехать."
    n "......И чего ж я тогда твержу, что союз не может быть причастен?"
    n "Может быть, мне стоит включить всё своё внимание и присмотреться к кошельку?"
    nvl clear
    n "...С моего прибытия в Хинамидзаву прошло всего несколько дней."
    n "{nw}"
    n "Но с тех пор произошло столько всего... Возможно, моя прежняя чувствительность слегка притупилась."
    extend " Я потряс головой, прогоняя ненужные мысли."
    nvl clear
    scene bg 192 with dissolve_04
    n "Расстегнув молнию, детектив показал, что в кошельке."
    nvl clear
    n "В нём вперемешку с мелочью лежали какие-то смятые чеки."
    n "Из этого бардака Ооиси-си вынул погнувшуюся карточку из картона."
    nvl clear
    stop music fadeout 1.0
    n "......При её виде у меня оборвалось дыхание."
    n "То была карточка на посещение зубного врача."
    n "{nw}"
    play sound wa_027
    n "На ней — имя: «Инугай Тосики». Возраст."
    extend " ...Совпадает."
    n "{nw}"
    n "Адрес зубной клиники............ в Токио."
    nvl clear
    play music lsys15
    n ".........Нет нужды объяснять по несколько раз."
    n "{nw}"
    n "Каково расстояние от Хинамидзавы до Токио?"
    n "Хоть на Синкансэне, хоть скоростной автомобильной дорогой — много, много часов."
    n "{nw}"
    n "Так почему же в Хинамидзаве всплыл кошелёк с карточкой зубной клиники в Токио?"
    nvl clear
    play ambient lsys25
    n "Он принадлежит какому-то гостю из Токио?"
    n "Или кто-то из деревни, побывав как-то в Токио, посетил там зубного врача?"
    extend " Нет, нет — она, должно быть, случайно туда попала......"
    n "{nw}"
    n "Мозг лихорадочно пытался найти любую причину, по которой кошелёк не мог принадлежать Инугаю Тосики."
    n "Как будто кошелёк ни в коем случае не мог быть его..."
    nvl clear
    n "Но по мере того, как приходившие на ум причины отметались одна за другой,"
    extend " словно какая-то дымка, не дававшая рассмотреть кошелёк, рассеивалась, и он представал передо мной всё яснее и отчётливее."
    nvl clear
    show ooishi si def_a2 at sprava with dissolve_04
    n "\"......Ну?\""
    n "\"..............................\""
    n "Казалось, будто через позвоночник пустили ток."
    n "Сердце бешено колотилось, по всему телу медленно проступал пот."
    n "......Должно быть, господину Ооиси я, стоявший с открытым ртом, казался совершенным идиотом."
    nvl clear
    n "\"...Вы звонили в зубную клинику?\""
    show ooishi si wa_a1 with dissolve_02
    n "\"Так это же ваша работа?"
    extend " Мне такого не положено.\""
    n "\"...Когда это произошло?\""
    show ooishi si def_a1 with dissolve_02
    n "\"Его подобрал один из деревенских."
    extend " Вчера, думаю.\""
    nvl clear
    n "\"Нет, я хотел сказать, когда кошелёк потерялся?\""
    show ooishi si def_a2 with dissolve_02
    n "\"Крайний раз дождь был на прошлой неделе, ровно семь дней назад."
    extend " В кошельке всё сухо, значит, самое большее — шесть дней как.\""
    n "\"Кто ещё знает о кошельке?\""
    n "\"Полицейский с Хинамидзавского участка, которому принесли кошелёк,"
    extend " потом ещё несколько человек из бюро находок"
    extend " и, наконец, вы и я."
    extend " Языком я не молол:"
    extend " а ну как оно имеет отношение к засекреченному делу?\""
    nvl clear
    n "\"......Могу я воспользоваться телефоном?\""
    show ooishi si wa_a1 with dissolve_02
    n "\"Конечно, конечно."
    extend " Для внешней связи наберите сначала ноль.\""
    nvl clear
    scene black with dissolve_04
    scene bg 011 with dissolve_04
    n "Я набрал номер клиники, напечатанный на карточке."
    nvl clear
    n "В голове тяжело бухало в такт сердцебиению."
    n "{nw}"
    n "......Ах ты ж, значит, и так бывает?!"
    nvl clear
    play repeated lsys17
    n "Все адреса на карточке и бумажках, лежавших в кошельке, указывали на тот район, где жил похищенный внук."
    n "{nw}"
    n "Совпадало имя на карточке,"
    extend " да и приблизительное время утери совпадало со временем похищения."
    nvl clear
    n "Конечно, я мог сказать, что всё чушь и совпало случайно."
    n "И никакая кошелёк не улика."
    n "{nw}"
    n "......То, что я сейчас узнаю по телефону, значит куда больше всех этих косвенных доказательств......"
    nvl clear
    stop repeated fadeout 1.0
    n "\".........Здравствуйте, спасибо, что позвонили."
    extend " Зубная клиника XX.\""
    n "\"Добрый день. Звонят из полицейского участка XXX."
    extend " Нам принесли потерянный кошелёк, и мы хотим узнать, как связаться с владельцем."
    extend " Не могли бы вы нам помочь?"
    extend " В кошельке нашлась карточка посетителя вашей клиники."
    extend " ......Да."
    extend " Имя — Инугай Тосики-кун."
    extend " Сейчас я продиктую вам номер карты. Не могли бы вы назвать номер его домашнего телефона?"
    extend " ......Да, премного благодарю."
    extend " Поможете?\""
    nvl clear
    n "Пока ждал ответа, достал свободной рукой карманный блокнот."
    n "......Перелистнул на страничку с домашним адресом внука и его телефоном."
    nvl clear
    n "\"Спасибо большое."
    extend " ............Да, прошу любезно.\""
    n "{nw}"
    n "И я начал сравнивать цифры, доносившиеся из трубки, с цифрами, записанными у меня в блокноте."
    nvl clear
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    n "......Почувствовав спиной нечто странное, обернулся."
    n "{nw}"
    play ambient lsys18
    n "Я наткнулся на взгляд господина Ооиси."
    n "Тот недоумевающе на меня посмотрел."
    n "Почему я обернулся, ощутив спиной что-то не то?"
    n "{nw}"
    stop ambient fadeout 1.0
    play sound wa_024
    n "......А потому, что диктовавшая номер на другом конце провода"
    extend " {cps=*0.6}как будто глядела ко мне в блокнот, {cps=*0.6}читая записанные в нём цифры...{/cps}{/cps}"
    nvl clear
    scene black with dissolve_04
    play ambient lsys12
    n "По всей видимости, в центре были поражены моим звонком."
    n "{nw}"
    n "Сколько меня ни расспрашивали о достоверности улики, я лишь отвечал, что так всё и есть........."
    nvl clear
    n "Сперва трубку взял мой начальник,"
    extend " начавший придирчиво засыпать вопросами по поводу найденной мной (если можно так выразиться) невероятной улики."
    n "{nw}"
    n "Но на все вопросы я отвечал отрицательно, и он замолчал."
    extend " Наконец трубку передали главе отдела."
    nvl clear
    n "Я заметил, что к его появлению шум, доносившийся с того конца трубки, совсем стих."
    n "{nw}"
    n "Задав те же вопросы о кошельке, шеф тихо сказал."
    nvl clear
    stop ambient fadeout 0.5
    play music meditation
    scene bg 011 with fastdown
    n "\"Понятно."
    extend " Мы вышлем несколько человек в подкрепление."
    extend " Они должны приехать к вечеру."
    extend " Вас же прошу продолжать расследование."
    extend " Постарайтесь побольше узнать о той местности, где нашли кошелёк."
    extend " Кано-сан возьмёт нескольких человек и сразу же......\""
    n "{nw}"
    n "Раз он собирается прислать моего начальника, значит, шеф уверен, что виновен Союз обороны Онигафути."
    n "Всё же мне показалось, что он не готов поверить, пока его доверенный помощник собственнолично не засвидетельствует улику."
    nvl clear
    scene bg 192
    show ooishi si def_a1 at sleva
    with dissolve_04
    n "\"Ну и?\""
    n "\"Сказали, вышлют несколько человек в подкрепление."
    extend " Мне приказано продолжать расследование."
    extend " Так где, говорите, нашли кошелёк?\""
    nvl clear
    n "\"Кажется, в окрестностях Такацудо..."
    extend " Мы — в Окиномии."
    extend " Проехать вон по той дороге — и мы в Хинамидзаве."
    extend " А там ещё дальше вверх по течению — и вот вам и Такацудо.\""
    n "{nw}"
    n "Объяснил Ооиси-си, водя пальцем по висевшей на стене карте."
    n "Оказывается, кошелёк нашли в ещё большей глуши, чем Хинамидзава."
    nvl clear
    show ooishi si def_a2 with dissolve_02
    n "\"В том районе практически нет жилых строений."
    extend " Оттуда давно все ушли."
    extend " Там и сям пустые дома. Тоскливо до жути.\""
    n "\"Ооиси-сан..."
    extend " Можете меня туда отвезти?\""
    show ooishi si wa_a1 with dissolve_02
    n "\"Конечно, меня не затруднит."
    extend " Всё равно вам одному сейчас по Хинамидзаве не поразгуливать."
    extend " Правда, придётся надеть маску да кепку.\""
    nvl clear
    n "Порадовало, с какой готовностью он согласился со мной поехать."
    n "......Если верить словам Сато-сана, меня почти раскрыли."
    n "Точно не знаю, догадались ли, что птенец из общественной безопасности — турист, вчера посетивший деревню."
    n "Но было бы слишком наивно уповать на обратное."
    nvl clear
    scene black with dissolve_04
    n "Никоим образом нельзя отрицать, что Такацудо может служить укрытием злоумышленникам."
    n "{nw}"
    n "Там не живут люди, к тому же там нет нормальной дороги, поэтому даже местные без особой надобности туда не заглядывают."
    n "Словом, покинутый, забытый всеми тупик."
    n "Лучшего места, чтобы спрятать похищенного внука, не отыскать."
    nvl clear
    n "Помимо того, в Такацудо нельзя попасть, не проехав через Хинамидзаву."
    n "Всё это лишь подчёркивает его выгодность."
    nvl clear
    n "Я больше не мог не признавать."
    n "......Нет сомнения: преступление совершено Союзом обороны Онигафути либо кем-то, нанятым ими."
    n "{nw}"
    n "В таком случае..."
    extend " они могут знать, что кошелёк попал к полицейским."
    n "......Они ведь знают и то, какие шаги предпринимает Отдел общественной безопасности."
    extend " Уж об этом они знать должны."
    nvl clear
    n "А если так...... то, вполне возможно, меня уже ждут."
    n "{nw}"
    n "А я не настолько смел — точнее, не настолько безумен, — чтобы забредать в самое сердце вражеской территории в одиночку."
    nvl clear
    scene bg 192
    show ooishi si def_a1 at central
    with dissolve_04
    n "\"Без вас, Ооиси-сан, я бы не смог попасть в деревню."
    extend " Очень признателен, что вы согласились помочь."
    extend " Признаться, думал, что вы снова попросите денег.\""
    show ooishi si wa_a1 with dissolve_02
    n "\"Н-а-ха-ха-ха."
    extend " Ну, говоря начистоту, я бы предпочёл туда не ездить,"
    extend " и было б неплохо, заплати вы мне."
    extend " Но разве могу я не выполнить просьбу товарища по игре?"
    extend " Мм-хм-хм-хм!..\""
    nvl clear
    n "Ухмыльнувшись, он хлопнул меня по спине."
    n "Насколько я понял, им больше руководила верность данному слову, нежели верность службе."
    n "{nw}"
    n "А впрочем, какая разница."
    extend " Я был рад, что тот согласился помочь по своей воле."
    nvl clear
    n "\"Ну что, тогда — выезжаем?\""
    n "...Если враг знает, что кошелёк у полиции..."
    n "То заложника должны перепрятать."
    extend " Нельзя терять ни секунды."
    n "{nw}"
    n "Однако детектив почему-то начал расстёгивать куртку."
    nvl clear
    n "\"...Что вы делаете?\""
    show ooishi si aku_a1 with dissolve_02
    n "\"Так, предосторожность."
    extend " Раз уж мы собираемся таскать из огня каштаны, то надо бы соответствующе подготовиться."
    extend " Надевать будете?\""
    n "{nw}"
    n "Господин Ооиси вытащил из-под стола пару противоножевых жилетов......"
    nvl clear
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    play ambient lsys12
    $ renpy.pause(5.0)
    $ save_name = "Глава о Потерянном Времени.\nДень Третий, мальчик"
    n "Его имя — Инугай Тосики."
    nvl clear
    n "Внук министра строительства Инугая."
    n "Вот и всё, ни больше ни меньше."
    n "{nw}"
    n "В целом он учится хорошо, если не брать в расчёт несколько низкие оценки по творчеству и физкультуре."
    n "Хорошая учёба — заслуга репетитора, приходящего дважды в неделю."
    n "Не считая того, что он по-прежнему не умел выполнять подъём переворотом на турнике, школу он в целом любил."
    nvl clear
    n "Разумеется, он прекрасно понимал, что его дед — один из министров."
    n "Но, не менее прекрасно зная, что многим не нравятся такие отношения,"
    extend " он сильно не любил, когда его деда называли министром строительства."
    nvl clear
    n "А ещё он чуть лучше обычных людей понимал, что значит быть Министром строительства."
    n "{nw}"
    n "А значило это вот что: чем больше ты стараешься сделать людям лучше, тем больше у тебя врагов."
    n "Когда его раз назначили старостой класса, он убедился на собственном опыте."
    nvl clear
    n "У деда много врагов."
    n "И, так как их противостояние может задеть и его, ему придётся жить осторожнее любого другого."
    extend " Так учили его родители."
    nvl clear
    n "Поэтому...... он сразу сообразил, почему его похитили."
    n "В нём видели не Инугая Тосики, но внука министра строительства Инугая."
    n "С ним случилась беда не из-за того, что он допустил какую-то страшную промашку, но из-за положения деда..."
    extend " Нельзя сказать, чтоб намного, но на душе у него стало самую чуточку легче, когда он понял, что сам ни в чём не виноват."
    nvl clear
    n "Сперва он, конечно, как любой бы ребёнок на его месте, поддался страху. Он ёжился при мыслях о том, что с ним станут делать."
    n "Но так как он, связанный, не мог двигаться, он, естественно, начал думать."
    nvl clear
    n "Сперва он подумал: а зачем его похитили?"
    n "{nw}"
    n "Догадаться легко."
    n "У деда, министра, хотят что-то вытребовать, шантажируя заложником."
    extend " Тут и думать нечего."
    n "Легко понять, что, даже не зная, чем занимается министр строительства, можно получить многое, коли хорошенько его припугнуть."
    nvl clear
    n "Он уважал деда больше, чем средний внук."
    n "Он безоговорочно верил, что его дед — среди первейших лиц Японии."
    n "Вот поэтому он и не мог простить тех, кто угрожают его досточтимому дедушке, — и тем более не мог простить, что его самого используют в целях шантажа."
    nvl clear
    n "Его дед — страшно занятой человек, и ему редко удаётся выкроить время, чтоб повидаться с родными."
    n "Поэтому-то, когда время у него всё же находится, он появляется без предупреждения, неожиданно."
    n "И показывает, как любит внука, заодно прося прощения за то, что не смог появиться на Новый год и на летних каникулах."
    nvl clear
    n "К нему нередко относятся дурно из-за того, что его дед — политик, Министр."
    extend " Но никогда он в своей жизни не думал, что хочет, чтобы дед перестал заниматься политикой."
    nvl clear
    n "Он уважал своего деда и потому от всего сердца желал, чтобы тот оставался в политике как можно дольше."
    n "Но...... вот его похитили; деда шантажируют."
    n "Дед наверняка страдает, ведь он внука так любит......"
    nvl clear
    n "Он может пойти на что угодно, чтобы его спасти."
    n "......Может быть, он даже откажется от своих убеждений, чтобы вызволить его из беды."
    n "{nw}"
    n "Может быть, он, чтобы спасти внука, согласится на требования похитителей..."
    nvl clear
    n "Как только в голову пришла такая мысль..."
    extend " он ощутил жаркий, неописуемый гнев."
    n "Он не мог простить себе, что из-за его положения дедушка мучается, а ещё не мог простить трусов, так грязно шантажирующих деда."
    n "{nw}"
    n "Пока он предавался размышлениям, страх незаметно ушёл..."
    nvl clear
    n "И первым делом он подумал о том же, о чём подумал бы на его месте любой мальчик."
    n "Он храбро подумал, что вот он сейчас выпутается, побьёт гнусных негодяев и передаст их полиции для справедливого наказания."
    n "На ум пришли смелые герои из читанных им комиксов для мальчишек."
    nvl clear
    n "В воображении он влёгкую выбрался из пут и, порхая как бабочка, начал разделываться со злоумышленниками, укладывая одного за другим жалящими ударами."
    n "{nw}"
    n "Всё происходило лишь в его воображении, но для него, ничего не видевшего из-за повязки, оно казалось лучше и увлекательнее всякого мультсериала."
    n "По правде сказать, в неволе он столько провёл, развлекая себя с помощью воображения, что ему приходилось совсем не так плохо, как считали преступники."
    nvl clear
    n "Но в конце концов ему наскучило, и тогда он понял, что пустые мечты ни к чему не приведут."
    n "И он захотел чем-нибудь облегчить тяжесть дедова положения."
    n "Он больше, чем что бы то ни было, ненавидел себя за то, что своим положением причиняет страдания дедушке."
    nvl clear
    n ".........И тогда он сообразил."
    nvl clear
    n "Избивать гнусных злодеев необязательно... Помочь дедушке куда проще."
    n "{nw}"
    n "Надо всего-то сбежать из плена."
    n "Без него злодеи не смогут что-либо вытребовать у дедушки."
    nvl clear
    n "Они связали его, но обращаются нормально, даже не забывают кормить."
    n "......Иначе говоря, он — просто-напросто их козырь."
    extend " Его не собираются мучить или, тем более, убивать."
    n "{nw}"
    n "Пока он не рыпается, ему хуже не сделают."
    nvl clear
    n "Поняв это, мальчик ощутил прилив храбрости."
    n "И дальше он уже не раздумывал."
    n "{nw}"
    stop ambient fadeout 0.5
    play music silver_mirror
    n "Он, Инугай Тосики, решил сбежать."
    nvl clear
    n "В ушах в качестве затычек — нечто вроде кусочков посудной губки."
    n "...Но на самом деле звук они не задерживают, и разговоры похитителей он слышит прекрасно."
    nvl clear
    n "Он понял, что это даёт ему преимущество, и, когда похитители что-либо ему говорили, делал вид, что не слышит из-за затычек."
    n "{nw}"
    n "Те, видимо, думая, что мальчик всё равно не слышит, спокойно разговаривали обо всём, не понижая голоса."
    extend " И потому он смог узнать многое."
    nvl clear
    n "Во-первых...... они не в Токио."
    n "По-видимому, они находились где-то далеко в горной глуши."
    n "{nw}"
    n "Также, по тому, какие неудобства терпели преступники, он догадался, что до ближайшего города неблизко."
    nvl clear
    n "Им приходилось ездить за покупками да прочими необходимыми в жизни вещами на машине."
    n "Тут он приуныл."
    extend " Он понял, что простейший способ самозащиты, которому его научили в школе: бежать со всех ног и во всё горло звать на помощь — не сработает."
    nvl clear
    n "Полёт его воображения, рисовавшего дерзкий побег, разом оборвался."
    n "Нужно найти кого-то, кто его защитит."
    n "Раз такого поблизости нет, надежда на успех побега невелика."
    n "{nw}"
    n "В чужих местах, в сердце гор, вдали от людского жилья."
    n "Без машины за покупками не сходить."
    n "......В таком положении... побег становится крайне затруднителен."
    nvl clear
    n "......Приуныв, он вернулся к своей первой мечте."
    extend " Той, где он, став героем манги для мальчиков, расправляется с похитителями."
    nvl clear
    n "Но... даже предаваясь таким глупым мечтам,"
    extend " где-то в душе он отказывался признавать поражение и продолжал искать способа выбраться."
    extend " ......И наконец додумался вот до чего."
    n "{nw}"
    n "Если цель далеко... то всего-то и надо, что сделать её ближе."
    n "А цель эта — тот, кто его защитит."
    extend " Иными словами, кто-то кроме преступников."
    nvl clear
    n "Если он притворится, что вдруг серьёзно захворал, преступники либо повезут его в больницу, либо вызовут врача."
    n "Они, скорее всего, заколеблются."
    extend " Но заложник, как он уже знал, важнее всего."
    n "Умри он, и его больше не удастся использовать."
    nvl clear
    n "Ему повезло — он знал, как надо симулировать хворь."
    n "{nw}"
    n "Под конец прошлого года"
    extend " он по неосмотрительности попал под машину, и ему сделали операцию."
    n "На животе до сих пор отчётливо виден шрам."
    nvl clear
    n "Он постарался вспомнить, как больно ему тогда было."
    n "Пережитый опыт позволял сыграть с недосягаемо большей убедительностью."
    extend " Он верил, что у него всё получится."
    nvl clear
    stop music fadeout 1.0
    n "\"............У-у-у-у-у-ммммм......"
    extend " М-м-мммм-м-м......\""
    nvl clear
    play ambient lsys15
    n "Поначалу они подумали, что тот хочет по-большому."
    n "Распутав руки (и оставив замотанными глаза), они хотели отвести его в туалет."
    nvl clear
    n "Однако мальчик не попытался встать."
    n "Схватившись руками за живот, он скорчился на полу."
    nvl clear
    n "\"......Эй, в чём дело?"
    extend " Живот болит, что ли?\""
    n "Из-за затычек в ушах он не мог ответить."
    n "Он едва успел удержать кивок."
    nvl clear
    n "\"Шо такое?\""
    n "\"...Хм... Да вон, пацан чё-т за живот держится."
    extend " Болит, кажись?\""
    nvl clear
    n "Некоторое время похитители наблюдали за его «мучениями»."
    n "Один раздумывал, что делать, а другой, похоже, размышлял, а не притворство ли это."
    nvl clear
    n "\"Шо случилось, парень?"
    extend " Пузо болит?\""
    n "\"У него затычки, он не слышит.\""
    n "\"От дерьмо......"
    extend " У нас лякарств от живота нема."
    extend " Съездить в аптеку?\""
    n "\"Но от живота много всяких лекарств."
    extend " Я что, дурак покупать всякую дрянь, не зная симптомов?..\""
    n "\"За живот держится — наверно, запор."
    extend " Давай-ка купим ему слабительного."
    extend " Ошибёмся, дак хучь не околеет.\""
    nvl clear
    n "\"Ну-ну, не торопись."
    extend " Вдруг у него аппендицит?"
    extend " У меня дядька как-то раз взял и заболел."
    extend " У, жуть была!\""
    n "Один из преступников склонился над скрючившимся в три погибели мальчишкой."
    nvl clear
    n "\"......Бедолага..."
    extend " Ого, аж вспотел весь..."
    extend " Что, живот?"
    extend " Болит, да?"
    extend " Эй, слышь, ты не нажимай так, ежли болит...\""
    n "Поняв, что похитители заинтересовались его животом, он как бы случайно задрал майку, выставляя шрам напоказ."
    nvl clear
    n "Глаза закрывала клейкая лента, и мальчик не видел, какое впечатление шрам произвёл на похитителей."
    n "{nw}"
    n "Но, так как те надолго погрузились в молчание, он понял — да, именно то, которое нужно."
    nvl clear
    n "\".........Чёрт бы меня побрал."
    extend " Смотри-ка, а шрам-то не такой уж старый.\""
    n "\"......Глянь, у него жару не?"
    extend " Градусника не завалялось?\""
    n "\"Какой ещё, на хрен, градусник?"
    extend " Но ты погляди, какой потный..."
    extend " Хм-м... Лоб вроде горячий.\""
    n "\"....................................\""
    nvl clear
    n "\"......Я слыхал, от долгого перенапряга старые раны начинают ныть.\""
    n "\"Ну и шо терь делать?!!"
    extend " Шо, лекарства тут не помогут?!\""
    n "\"......Хрен знает, что ему там оперировали..."
    extend " но мне это... не нравится."
    extend " Как бы он тут ноги не протянул...\""
    nvl clear
    n "\".............Дело дрянь."
    extend " Ой какая дря-янь...\""
    n "\".........Лучше уж показать его доктору."
    extend " А не то возьмёт ещё да отдаст концы...\""
    n "{nw}"
    n "По их словам Инугай Тосики понял, что всё идёт в точности по его задумке. Торжествуя в душе, он продолжал корчиться от мнимой боли."
    nvl clear
    n "Преступники явно волновались. Даже ничего не видя, он знал: они забегали по комнате, не зная, что делать."
    nvl clear
    n "\"......Отвезём его в клинику?\""
    n "\"М-м-м......... не, не дило."
    extend " ............Нехай дохтор сам к нам приедет.\""
    n "\"Доктор Ириэ?"
    extend " ......Уверен?"
    extend " Думаешь, ничего не случится?\""
    n "\".........З заложником не должно нишо случиться."
    extend " Шо делать — вишь, медлить нельзя!\""
    nvl clear
    n "Один из них торопливо выбежал наружу, завёл автомобиль и уехал."
    n "Другой, нервничая, принялся носовым платком вытирать пот со лба пленника."
    nvl clear
    n "......Кажется, приедет врач."
    n "{nw}"
    n "Если врач не один из них, тогда он — цель."
    extend " У него надо попросить помощи."
    nvl clear
    n "Конечно, преступники не собираются того допускать."
    n "Что придумать?"
    n "......Тут уж как получится."
    n "{nw}"
    n "Пот, выступивший на его лбу, был отчасти от волнения..."
    nvl clear
    scene white with fade_010
    scene bg 194 with center_03
    n "И тут от глаз и ушей отлепили ленту."
    n "{nw}"
    n "Впервые за последние несколько дней он увидал яркий свет. Свет жёг, слепил."
    n "Затем изо рта вынули мешавший дышать кляп."
    nvl clear
    n "\"...Ты в порядке, пацан?"
    extend " Скоро приедет врач."
    extend " Потерпи немного.\""
    n "\"............У-у-у-у-у-ух......"
    extend " Гх-х-х-х-х-х......\""
    n "Приедет врач... Приедет врач..."
    n "Ну и как же попросить его помочь, как же сбежать от преступников?"
    extend " В голове кружился целый хор мыслей."
    nvl clear
    n "\"...Ну, ты и так знаешь,"
    extend " но не вздумай ляпнуть при докторе чего лишнего."
    extend " ......Нам, знаешь ли, не хотелось бы тебя обижать."
    extend " Понимаешь, ага?..\""
    n "Внутренне страдая, Инугай Тосики кивнул, показывая, какой он послушный..."
    nvl clear
    n "Его замысел и замысел его врага."
    n "{nw}"
    n "...Верят ли его притворству или не верят — его цель они знают и наверняка попытаются помешать."
    nvl clear
    n "От напряжения рискованной игры желудок сжался, и мальчику показалось, что живот заболел по-настоящему."
    extend " А может, и не показалось?"
    n "{nw}"
    n "Впрочем, спешить некуда..."
    n "Если он и не сумеет намекнуть доктору, то всё равно ничего не потеряет."
    n "{nw}"
    n "Хотя нет — потеряется предлог связаться с врачом."
    nvl clear
    n "Это ещё не потеря, если потом удастся придумать ещё что-нибудь."
    n "Но сейчас он не мог придумать способа проще и впечатляющей."
    n "{nw}"
    n "......Ах, чем больше я думаю, тем сильнее уверен: сейчас — пан или пропал!"
    nvl clear
    stop ambient fadeout 1.0
    n "Вскоре... послышалось шуршание возвращающейся машины."
    nvl clear
    n "Громко захлопали дверцы."
    extend " Всё ближе и ближе застучали шаги."
    nvl clear
    play sound wa_020
    show irie doc def_a1 at sprava with right_03
    play ambient lsys12
    n "Молодой мужчина в белом халате."
    n "Увидев мальчика, он подозрительно нахмурился."
    nvl clear
    show irie doc maji_a1 with dissolve_02
    n "\"...................Кто он?\""
    n "\"...............\""
    n "\"............Он ведь не из деревни?\""
    n "Похитители промолчали."
    extend " ......Тут молодой врач, видимо, понял, что дело непростое."
    nvl clear
    n "Один из похитителей угрожающе проговорил."
    nvl clear
    n "{b}\"Не ваше дело, доктор.\"{/b}"
    show irie doc maji_a2 with dissolve_02
    n "{b}\".....................\"{/b}"
    n "В тишине доктор и преступники некоторое время пристально глядели друг на друга."
    n "Наконец, не сумев больше спокойно выносить вида корчащегося от боли мальчика, врач, как и надеялись преступники, махнул рукой на выяснение обстоятельств."
    nvl clear
    show irie doc maji_a1 with dissolve_02
    n "\"...Меня беспокоит этот старый шрам..."
    extend " Что за операцию ему делали?\""
    n "\".........Понятия не имеем.\""
    n "\"...Хм-м-м-м........."
    extend " Вообще-то, надо бы отвезти его в клинику.\""
    n "\"Доктор, ну, право...\""
    nvl clear
    hide irie with right_03
    n "Врач сказал, что хочет отвезти мальчика в клинику, но похитители только молча мотали головами из стороны в сторону."
    n "......Слабая надежда рассыпалась в прах; впрочем, было только естественно, что похитители воспротивились."
    nvl clear
    n "Тут его глаза пересеклись со взглядом врача."
    n "Кажется, заметив что-то неестественное в корчах мальчика, врач усомнился, а так ли серьёзна болезнь на деле."
    nvl clear
    show irie doc def_a1 at central with right_03
    n "\".........Вы в порядке?"
    extend " Я врач."
    extend " Когда у вас появился шрам?\""
    n "\"......М-м-м-м....... Ух......"
    extend " В прошлом... году...{w=2.0} зимой......{w=2.0} в аварии......\""
    show irie doc maji_a2 with dissolve_02
    n "\"Авария..."
    extend " Вот как......"
    extend " Это нехорошо......\""
    n "Сейчас нельзя, чтоб врач догадался, что недуг — мнимый."
    n "Надо как-то найти с ним общий язык, дать понять, что он в плену и его нужно спасти."
    nvl clear
    show irie doc maji_a1 with dissolve_02
    n "\"Сейчас я попробую вас прощупать."
    extend " Скажете, где болит?\""
    nvl clear
    n "\"......АААааааай-й-й-й!!!.....\""
    n "\"...Хм....... Хм-м.....\""
    nvl clear
    n "При виде столь острой реакции врач, скрестив на груди руки, задумался..."
    n "{nw}"
    n "Надо как-то попасть в больницу."
    n "Первый и единственный раз в жизни Инугаю Тосики выпало играть больного..."
    nvl clear
    show cinema with x_15
    show title02 with Dissolve(3.0)
    $ renpy.pause(2.0)
    show black behind title02 with Dissolve(3.0)
    $ renpy.pause(1.0)
    scene black with right
    jump hima_day03_protest
