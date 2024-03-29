    scene black with Dissolve(1.0)
    play ambient lsys13
    n "{b}Клиника{/b}."
    n "{nw}"
    n "В Японии клиники хоть и не государственные, зато недорогие."
    nvl clear
    n "{b}Ишшо{/b}."
    n "{nw}"
    n "Двое в приёмной говорили на местном наречии."
    nvl clear
    n "{b}Привокзальная площадь{/b}."
    n "{nw}"
    n "На привокзальных площадях скучиваются магазины и рестораны, надеясь привлечь проезжающих. Сами станции служат своеобразными торговыми центрами."
    nvl clear
    n "{b}Некурящие{/b}."
    n "{nw}"
    n "Сомнительно, что в 1983 такое было. Япония присоединилась к запрету на курение только в 2000 году нашей эры."
    nvl clear
    n "{b}Тэнгу{/b}."
    n "{nw}"
    n "Известные создания в японских поверьях. Поначалу представлялись птицеподобными демонами-подстрекателями, позднее представление изменилось на более человекообразных, краснолицых духов-защитников с длинными носами."
    nvl clear
    n "{b}Горные отшельники{/b}."
    n "{nw}"
    n "{i}Сэннин{/i} — живущие в отдалении от людей бессмертные кудесники."
    nvl clear
    n "{b}Дизавтономия{/b}."
    n "{nw}"
    n "Вызванное непомерной нагрузкой на психику состояние, приводящее к головокружению и другим ухудшениям здоровья. Английские переводчицы подозревают, что так Ооиси-сан выпендрился: «От нагрузки она стала рассеянной любительницей ломать вещи — больше тебе знать не положено»."
    nvl clear
    n "{b}Архивы по месту жительства{/b}."
    n "{nw}"
    n "В Японии каждую семью нужно засвидетельствовать в местном органе управления (ЗАГСе).\nРегистрационные карты включают имя, место жительства, дату рождения, пол и начало срока проживания каждого жителя.\nКроме того, там указано, владеет ли гражданин или семья местом своего проживания, если нет — какое гражданин или семья имеют отношение ко владельцу."
    nvl clear
    n "{b}Охаги{/b}."
    n "{nw}"
    n "Японская традиционная сладость, состоит из рисового шарика, слепленного из {i}суси-риса{/i} и {i}клейкого риса{/i}, покрытого сладкой пастой из красных бобов.\nВ {i}охаги{/i} мало составляющих и печь его не надо, почему хорошо их делать в качестве летнего угощения."
    nvl clear
    n "{b}Бобовая паста{/b}."
    n "{nw}"
    n "{i}Цубусиан{/i}, делается из грубо помолотых бобов {i}адзуки{/i} вперемешку с сахаром."
    nvl clear
    n "{b}Зелёный чай{/b}."
    n "{nw}"
    n "Кейти показывает хороший тон в японском понимании: зелёный чай вместе с японской традиционной сладостью (в нашем случае — {i}охаги{/i}), как упоминалось в заметках к одиннадцатому дню."
    nvl clear
    n "{b}Одэн{/b}."
    n "{nw}"
    n "{i}Одэн{/i} — известное блюдо, в котором куча составных варятся в одном бульоне. Обычно включает яйца, жареный {i}тофу{/i} с добавками ({i}гаммо{/i}) и... хм... {i}хампэн{/i}. {i}Хампэн{/i} это такое измельчённое рыбье мясо ({i}сурими{/i}). По консистенции похоже на зефир или внутреннюю часть крабовых палочек, если читатель знаком с таким блюдом. Переводчик понятия не имеет, как это лучше описать.\n{w=3.0}Ларьки, продающие {i}одэн{/i}, — в таком Ооиси со своим начальником ужинали — обычно располагаются на свежем воздухе и продают спиртное. Посетители усаживаются на стулья и заказывают себе что угодно из бульона вместе с сакэ или пивом.\n{w=3.0}Наборы для приготовления одэна можно купить в магазинах."
    nvl clear
    show ooishi si wa_a1 at central with fastup
    n "{b}Сусукино{/b}."
    n "{nw}"
    n "Квартал красных фонарей в Саппоро, Хоккайдо."
    nvl clear
    n "{b}Вождение в пьяном виде{/b}."
    n "{nw}"
    n "Закон против пьяных водителей в Японии весьма суров. Уже 0,3 промилле достаточно для наказания (переводчицы с такого офигевают — нам всё равно, у нас даже квас пить лучше не надо). Высшее наказание для езды с таким уровнем алкоголя в крови — три года принудительных работ либо штраф размером 500 000 йен. Это сейчас, какие были в 1983 году — неизвестно, но тяжёлыми они были всегда. С доступностью автобусов, метро и такси нет причин зря лишний раз рисковать."
    nvl clear
    n "Кстати говоря, принятое название денежной валюты Японии — иена, а не йена."
    n "Просьба считать это авторским начертанием, с учётом того, что в японском языке на «и» и «и краткую» один знак."
    stop ambient fadeout 4.0
    show ooishi si def_a2 at sprava with move
    show rena si ka_a1 at sleva with left_03
    n "И на этом со двенадцатым днём всё!"
    nvl clear
    hide rena with moveoutleft
    hide ooishi with moveoutright
    call screen translation_notes
    return
