    play music msys06
    scene bg 119 with Dissolve(1.0)
    n "{b}Планшет с извещением{/b}."
    n "{nw}"
    n "Раньше в японских деревнях вместо интернета и доски объявлений пользовались {i}кайран-бан{/i}, «извещениями». Они представляли собой планшет, переходящий от дома к дому, на который жители, кому что было сказать, крепили свои объявления — например, заходите ко мне отведать сакэ такого-то числа, такой-то продаёт машину и так далее."
    n "Нет, планшет не графический, если у кого-то возникли такие ассоциации. Данный планшет представляет собой маленькую папку либо дощечку с креплением для бумаги в виде двух незамкнутых колечек."
    nvl clear
    scene bg 101 with Dissolve(1.0)
    n "{b}Рэна ругает Ооиси-сана{/b}."
    n "{nw}"
    n "В начале двенадцатого дня Рэна разговаривает с Ооиси-саном в машине. Вначале разговаривает она (как умелая переговорщица) очень грубо и непочтительно, посему просьба при чтении иметь в виду, что её обращение «вы» звучит как плевок в лицо."
    n "«Ты» сюда не подходит — как по истинной окраске этого слова, так и уместности."
    nvl clear
    scene bg 200 with Dissolve(1.0)
    n "{b}Мацутакэ{/b}."
    n "{nw}"
    n "Грибы, похожие на знакомые всем опята."
    n "Произрастают под соснами, посему и называются {i}«мацутакэ»{/i} — сосновые грибы."
    nvl clear
    scene bg 199 with Dissolve(1.0)
    n "{b}Двускатная крыша{/b}."
    n "{nw}"
    n "Говоря точнее, {i}«гассё-дзукури»{/i} (буквально: {i}сложенные в молитве ладони{/i}) — в которой скаты крыши находятся под очень крутым наклоном (45-60 градусов) и сделаны из соломы. Получается высокий чердак в два-три человеческих роста (зависит от ширины дома и количества жилых этажей). Подобное строение чердака весьма подходит для разведения шелковичных червей, которое является основным занятием в деревне {b}Сиракава-го{/b}, послужившей прототипом Хинамидзавы."
    n "Постройки с крышами {i}гассё-дзукури{/i} занесены в список Всемирного наследия ЮНЕСКО (про что упоминает в разговоре хозяйка), так как нынче осталось их мало. Раньше же они встречались в Японии повсеместно."
    nvl clear
    n "{b}Горы Хаккода{/b}."
    n "{nw}"
    n "{b}«Хаккодасан»{/b}, вулканический горный хребет {b}Хаккода{/b}, отличается суровой зимой, хотя самая высокая гора (пик {b}Одакэ{/b}) подымается всего-то на 1585 метров. Печально известны тем, что погубили практически 95 процентов (199 из 210) личного состава пятого полка восьмой дивизии японской армии в 1902 году. Полк пытался пересечь славящиеся суровым климатом горы, готовясь к войне в Сибири, о чём и упоминает Кейти, говоря про марш-бросок в стужу."
    n "Окончилось дело 23 января — гибельным бураном."
    nvl clear
    n "{b}Бразильский карнавал{/b}."
    n "{nw}"
    n "Имеется в виду {b}Карнавал в Рио-де-Жанейро{/b}, на котором полураздетые девушки танцуют самбу."
    n "Думаю, сущность наказания, которое пришлось исполнять Рэне, более чем очевидна..."
    nvl clear
    n "{b}Рубанул крест-накрест{/b}."
    n "{nw}"
    n "Приём из игр серии {b}Pokemon{/b} так называемого {b}«второго поколения»{/b}, называющийся {b}Cross Chop{/b}. Как следует из названия, представляет собой удар крест-накрест."
    n "Стоит, правда, заметить, что {i}покемоны{/i} увидели свет {b}лишь в 1996 году{/b}..."
    nvl clear
    n "{b}Пастила из красных бобов{/b}."
    n "{nw}"
    n "{i}Ёкан{/i} — сладость из красных бобов {i}адзуки{/i}, агар-агара (заменителя желатина. Буддизм — такая же насильно привитая вера в Японии, как на Руси христианство, — запрещает убийство животных, а ведь именно из них делается желатин.) и сахара."
    n "Похожа на русскую пастилу, только густая желеобразная, а не рассыпчатая."
    nvl clear
    if renpy.seen_audio("music/Matsuri/18 - Oyashiro-Sama.ogg") and persistent.matsuri:
        play music onigafuchi
    n "{b}Речь Мион{/b}."
    n "{nw}"
    n "Выражение {b}«Чёрные Корабли»{/b} (Курофунэ) в своём основном смысле обозначает американские военные пароходы {b}Миссиссиппи, Плимут, Саратога и Саскуэханна{/b}, приплывшие в Японию 14 июля 1853 года под командованием коммодора (соответствует званию контр-адмирала в России. Раньше также существовало звание «капитан-командор», ещё больше соответствовавшее «коммодору».) Перри."
    n "Прибытие военных кораблей прервало торговую закрытость Японии от европейских стран (кроме Голландии, с которой японцы торговлю и раньше вели), став поворотной вехой в её истории."
    nvl clear
    n "{b}Отмена княжеств{/b} — {i}Хайхан-тикэн{/i}, указ японского правительства от 29 августа 1871 года, которым отменялись независимые княжеские землевладения ({i}хан{/i}) и вводились новые административные единицы, зависимые от государственной власти, — префектуры ({i}кэн{/i})."
    n "{b}Построить процветающую страну с мощным войском{/b}.\n\n{i}Фукоку-кёхэй{/i}, лозунг Японии времён правления Мэйдзи."
    extend " Буквально — «Процветание и сила!» (или «Богатая страна, сильное войско!», или «Обогатим страну и укрепим войско!»)."
    n "Ознаменовал переход Японии к национализму."
    nvl clear
    n "{b}Война с империей Цин{/b} — имеется в виду развязавшаяся в 1894—1895 годах война Японии с маньчжурской империей Цин, в состав которой входил Китай."
    n "{b}Буракумины{/b} (буквально: {size=20}«жители особых поселений»{/size}) — потомки сословия «нечистых», и поныне пребывающие в Японии."
    n "Кто смотрел хороший советский фильм {b}«Кин-Дза-Дза!»{/b}, тот может сравнить «нечистых» прошлого с пацаками — жили в особых поселениях (гетто), носили особую одежду, при встрече с любым не из их касты должны были снимать головной убор... нет, «ку» два раза говорить не должны."
    extend " В общем, самое дно."
    nvl clear
    n "«Нечистыми» в период Токугава считались те, кто делал «нечистую», «недостойную» работу — свежевал животных, убирал улицы, выступал в поисках заработка шутом."
    n "После прихода Мэйдзи ко власти, сословия в 1871 году отменили, однако вбитые раз убеждения не выветриваются так запросто, и {i}буракуминов{/i} продолжали гнушаться — и продолжают по сей день, хоть и в меньшем уже объёме. За нынешних {i}буракуминов{/i} стараются не выходить, на них стараются не жениться, их стараются не принимать на работу."
    n "{b}Штаб-квартира Макартура{/b} — ставка оккупационной администрации в Японии после Второй мировой войны, коей заведовал генерал Дуглас Макартур."
    n "Участвовала в проведении послевоенных реформ и создании новой конституции."
    nvl clear
    n "{b}Харбин, отряд 731 и его работа{/b}."
    n "{nw}"
    n "Об этом не стоит рассказывать в заметках. Просто посоветую прочитать книгу {b}Моримуры Сэйити{/b} под названием {b}«Кухня дьявола»{/b}."
    n "Слабонервным также советую иметь под боком какую-нибудь поганую посуду."
    nvl clear
    n "{b}Сукияки{/b}."
    n "{nw}"
    n "Японская похлёбка на основе говядины (или, для буддистов, которым вера не позволяет, кубиков тофу). Отличительная особенность — блюдо продолжает готовиться и во время приёма пищи. Участники собираются у стола и, когда вода закипит, кидают в неё чего надо по вкусу. Общий котёл, короче, и в готовке участвуют все."
    n "«На соевом соусе» в данном случае значит, что {i}сукияки{/i} варится на соевом соусе, не воде."
    nvl clear
    n "{b}Договор{/b}."
    n "{nw}"
    n "Официальное название: {b}«Договор о взаимном сотрудничестве и гарантиях безопасности между США и Японией»{/b}. Подписан 19 января 1960 года в г. Вашингтон (округ, разумеется, Колумбия)."
    n "Хотя он был куда менее унизителен для желтолицых, чем ранее подписанный {b}Сан-Францисский{/b}, всё же он, по сути, закреплял Японию в позиции послушной собачки Соединённых Штатов на весь свой срок действия.{w=2.0} Конечно же, рядовым японцам сиё не понравилось, и они выходили на улицы выражать своё недовольство и устраивать беспорядки."
    nvl clear
    n "{b}Кайсяку{/b}."
    n "{nw}"
    n "Помощник при обряде самоубийства ({i}сэппуку{/i} или {i}харакири{/i}), должный в определённый миг отрубить голову, чтобы совершающий самоубийство не выказал слабости от настигших его смертных мук."
    n "По вполне очевидным причинам должность, пускай и уважаемая, отнюдь не легка и — тем более — не приятна."
    nvl clear
    scene black with Dissolve(2.0)
    show rika se ni_a1 at central with dissolve_04
    n "{b}Плазма{/b}."
    n "{nw}"
    n "\"Когда я скажу на вечеринке слово «плазма», я буду иметь в виду привычку некоторых людей объяснять любые сверхъестественные явления с помощью плазмы.{w=1.0} «Прилёты НЛО», спираль в небе над Норв... забудьте же.{w=2.0} В общем, даже явления божеств, которых вызывают жрицы вроде меня, тоже могут объяснить плазмой. Вот такие дела.\""
    n "\"Благодарю за разъяснение, Рика-тяма. Иди, тебя друзья ждут.\""
    nvl clear
    show rika se wa_a1 with dissolve_02
    $ renpy.pause(2.0)
    scene white with Dissolve(7.0)
    $ renpy.pause(1.0)
    show cinema with x
    show title02 with Dissolve(3.0)
    $ renpy.pause(3.0)
    scene black with Dissolve(3.0)
    call screen translation_notes
    return
