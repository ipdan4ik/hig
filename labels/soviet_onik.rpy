$ save_name = "Заседание Актёрского Состава\nОникакуси"
scene black
scene bg 161
show rena se wa_a1 at central
a_r "\"Мы желаем выразить наше самое искреннее спасибо за приобретение игры от студии 07th Expansion,"
extend " «Когда плачут цикады — Глава о Похищенных Демонами»!"
extend " Как она вам?"
extend " Надеемся, она вам хоть немного понравилась.\""
nvl clear
hide rena
show satoko se bik_a1 at sprava
a_s "\"Немного? Да какое там немного!"
extend " Как бы уважаемые не рассердились на такую Плохую Концовку?!\""
show rika se ni_a1 at sleva
a_f "\"...Я вот сердитая же.\""
nvl clear
hide satoko
show rena se def_a1 at sprava
a_r "\"Ну, как бы то ни было, говорят, глава «Похищенных демонами» — что-то вроде пролога к целой повести.\""
hide rika
show satoko se aki_a1 at sleva
a_s "\"И... так почему «пролог» обязательно было делать с жуткой Плохою Концовкой?!\""
show mion se wink_a2 at central
a_m "\"Ню-ню, давай-ка глянем иначе, а?"
a_m "Это — sound novel, звуковой роман то бишь, в котором игроку предстоит раскусить покрывающую всё-превсё загадку, дабы избежать унылой Плохой Концовки.\""
nvl clear
hide satoko
hide rena
hide mion
show rika se wa_a1 at sleva
a_f "\"...И это лишь первый сказ. Я жду следующего же.\""
show mion se def_a1 at sprava
a_m "\"И что же там дальше будет?"
extend " Рэна, ты что-нибудь слыхала?\""
scene bg 165
show rena se wa_a1 at sleva
a_r "\"Угу. По слухам... повествование следующего сценария пойдёт с другой стороны.\""
show satoko se aki_a1 at sprava
a_s "\"......Превесьма-таки неопределённо звучит."
extend " Что в виду-то имеется?\""
nvl clear
scene bg 165
show rena se def_b1 at sprava
a_r "\"Вы же видели, как «Оникакуси» представила нам серию загадочных смертей, произошедших в Хинамидзаве за все эти несколько лет?"
a_r "И вот сорока на хвосте принесла, что следующий сценарий раскроет старинную историю деревни.\""
nvl clear
show mion se def_b1 at sleva behind rena
a_m "\"Ну я совсем потерялась во всех этих загадочных происшествиях... Что за хрень вообще — «Проклятие Оясиро-сама»?"
extend " И чё такое «Оясиро-сама»? Они даже не объяснили.\""
nvl clear
show rena se ko_a1
a_r "\"...Хммм, я слыхала маловато, но......"
extend " У меня плохое предчувствие.\""
show rika se wa_a1 at central behind rena
a_f "\"......Да здравствует очередная скорбная повесть с проклятием.\""
show mion se wa_a2
a_m "\"Тем хуже Кей-тяну!"
extend " И как же проклянут его на сей раз?!\""
nvl clear
hide mion
hide rena
hide rika
show satoko se wa_a1 at sleva
a_s "\"Какая разница, я хочу знать, как дальше пойдёт рассказ!\""
nvl clear
scene white
scene bg 163
show ooishi si def_a1 at sprava
a_o "\"Эх-хе-хе-хе, ну, прошу прощения за опоздание.\""
show tomi si_def at sleva behind ooishi
a_t "\"Эй, ребята!"
extend " Классно сыграли!\""
hide ooishi
show mion se wa_a2 at sprava
a_m "\"Вы тооож!!!"
extend " Э? А где наш Кей-тян?\""
a_t "\"Кейти-кун пошёл читать следующую главу."
extend " Главным героем быть нелегко!\""
nvl clear
hide mion
show rena se nande_a1 at sprava
a_r "\"...Эх,"
extend " жалко."
extend " Показался бы он хоть на немножко.\""
show rika se de_a1 at central behind rena
a_f "\"......Он, боюсь, и не может — ему картинку не рисовали же.\""
hide tomi
show ooishi si wa_a1 at sleva behind rika
a_o "\"Рика-сан, такое только взрослым знать положено. Мм-хм-хм-хм!\""
nvl clear
scene black
scene bg 161
show tomi si_def at sprava
a_t "\"В любом случае... Кейти-куну и Рэне-тян тяжело в рассказе пришлось!\""
show satoko se bik_a1 at sleva
a_s "\"Тяжело? Какое там тяжело! Концовка очень, очень, очень худая!!!\""
show rena se nande_a1 at central
a_r "\"Вы знаете... я вот всё думаю, кто же на самом деле напал на Кейти-куна.\""
show tomi si_wa
a_t "\"Живой человек, подделывающийся под проклятие... Ну, так я по крайней мере думаю.\""
nvl clear
hide rena
hide tomi
hide satoko
show rika se de_a1 at sprava
a_f "\"......Но вот последний сделанный Кейти звонок.\""
show mion se tk_a1 at sleva
a_m "\"Ага,"
extend " я сама думала — что-то с ним не так."
a_m "Кей-тян тогда уж должен был знать, что преступник — человек.\""
hide rika
show satoko se def_a1 at sprava
a_s "\"......Безусловно, звонок диковинный."
extend " Как будто привидение за ним гналось.\""
hide mion
show rena se ko_a1 at sleva
a_r "\"От звонка вот... мне начинает казаться, что виноват всё-таки не человек, а проклятие.\""
nvl clear
scene bg 165
show ooishi si wa_a1 at sprava
a_o "\"Ну, мы долго лбы над этим ломали, почему бы не расспросить всех?"
extend " Сонодзаки-сан, ваше слово, начнём с вас.\""
show mion se wink_b2 at sleva behind ooishi
a_m "\"Я твёрдо верю в предположение «Человек»!"
a_m "Готова спорить, некто придумывает «происшествия», захваченный теми страшными старыми сказками про Хинамидзаву!\""
hide ooishi
show rena se def_a1 at sprava
a_r "\"Дельная мысль."
extend " Достаточно подозрительно, что загадочные смерти происходят каждый год в день фестиваля.\""
show mion se aku_a1
a_m "\"Серия загадочных смертей тоже взята из какой-то старинной сказки, я уверена!\""
nvl clear
scene bg 161
show satoko se aku_a1 at sprava
a_s "\"Ну, лично я считаю — ПРОКЛЯТИЕ!!!"
a_s "Если заметить, как едет крышей Кейти-сан в прихожей, или глянуть на тот последний звонок его, поди попробуй объяснить сиё человеком.\""
show rena se ko_a1 at sleva
a_r "\"Раз уж ты помянула..."
extend " те случаи вообще тяжело представить деянием рук человеческих.\""
nvl clear
scene bg 163
show tomi si_uh at sleva
a_t "\"...Хмм, даже так...... я всё равно считаю, что подозревать следует человека."
a_t "Прихожая и телефонная будка могли быть бредом, порождённым параноидальным воображением Кейти-куна.\""
show satoko se bik_b1 at sprava
a_s "\"Я-я не понимаю такие большие слова!!!\""
hide tomi
show rika se de_a1 at sleva
a_f "\"......Точнее сказать, они оказались бредом, вызванным страхом Кейти.\""
a_s "\"Ладно, ладно, значит... кто же то нечто, витавшее позади Кейти?!\""
nvl clear
scene bg 165
show mion se aku_a1 at sleva
a_m "\"Одна большая и жирная уловка.\""
show rena se bik_a1 at sprava
a_r "\"Мии-тян, что ты подразумеваешь под «уловкой»?\""
a_m "\"Как сказал дядюшка Томитаке, те случаи — бред испугавшегося Кей-тяна."
a_m "Писатель столь красно их расписал, чтобы игрокам казалось — дело в проклятии."
extend " Вот здесь и уловка!\""
nvl clear
scene bg 161
show satoko se aki_a1 at sprava
a_s "\"Н-Ну, верно... е-е-если вы так говорите, то...... эммм......\""
show tomi si_wa at sleva
a_t "\"Ха ха ха, ну, можно и так взглянуть.\""
nvl clear
hide satoko
hide tomi
show rena se nande_a1 at central
a_r "\"Если то правда, тогда... может, и прав был Ооиси-сан в своём предположении о вовлечённости всей деревни?"
a_r "Впрочем, как сам Ооиси-сан думает?\""
nvl clear
hide rena
show ooishi si wa_a1 at sleva
a_o "\"Кто, я?"
extend " Н-а-ха-ха-ха-ха......"
extend " Хм..."
extend " Да сложно сказать.\""
show tomi si_def at sprava
a_t "\"Э?"
extend " Я-то думал, вы всеми руками за «Человека» проголосуете.\""
show ooishi si def_a1 behind tomi
a_o "\"......Мой герой непреложно верил, что преступления совершал человек, но если так оно всё и есть, тогда полно всякого вздора и бессмысленной чуши.\""
show rena se def_a1 at central behind tomi
a_r "\"Например?"
extend " О, поведайте же нам свои блестящие умозаключения, Детектив Ооиси-сан!..\""
nvl clear
a_o "\"Во-первых, если закон преступил человек, нужен повод на то."
extend " ...Надо учесть, кому от преступлений навар идёт.\""
nvl clear
hide tomi
show mion se def_b1 at sprava behind rena
a_m "\"То есть вы имеете в виду — если преступник есть человек, то кому-то от загадочных смертей хорошо?\""
show ooishi si wa_a1
a_o "\"Именно."
extend " Могу понять возможные причины смертей тех, кто связан с плотиной, но последние жертвы к ней не относятся никоим боком."
a_o "...Да и кому вообще выгодно убийство Кейти-куна?\""
nvl clear
scene bg 163
show tomi si_def at sprava
a_t "\"А, вот как."
extend " После ваших слов даже я с точностью говорить уже не могу...\""
show satoko se aku_a1 at sleva behind tomi
a_s "\"В конце-то концов, денег-то никто не брал, ничего такого."
extend " Человеку нет повода становиться преступником!\""
hide tomi
show rena se nande_a1 at sprava
a_r "\"Но разве выгода не может заключаться в другом?"
a_r "Как Мии-тян молвила, вдруг имеет место попытка воссоздать некую старую быль......\""
nvl clear
scene bg 161
show mion se wink_b2 at sprava
a_m "\"От ыменно."
extend " Не заради денег убийство."
extend " Почему и считаю — на самом деле то...... ритуальная бойня с намерением воссоздать кровавое деревенское прошлое!\""
nvl clear
show rika se de_a1 at sleva behind mion
a_f "\"......Тогда позвольте спросить, как может кто-то получить с неё выгоду?..\""
hide mion
show tomi si_def at sprava
a_t "\"Выгода скорее психологическая... нежели материальная."
extend " ......Как знать... может, дело в мести,"
extend " некий местный обычай."
extend " ...Оставшаяся не раскрытой в данном эпизоде судьба!\""
nvl clear
scene bg 165
show ooishi si def_a1 at sleva
a_o "\"Понимаю..."
extend " Ты, сталбыть, полагаешь... что некая угнетаемая семья таким образом рассчиталась за древние обиды?"
extend " Хмммм......... Не могу всё-таки согласиться.\""
show mion se to_a1 at sprava
a_m "\"Тогда что? Ооиси-сан, вы чё, правда за Проклятие?!\""
hide ooishi
show satoko se aku_a1 at sleva behind mion
a_s "\"О да, да!!!"
extend " Так и сказал Ооиси-сан, а он детектива играет!"
extend " А посему — проклятие! Безоговорочно!!!\""
nvl clear
scene bg 165
show ooishi si def_a1 at sprava
a_o "\"Маэбара-сан говорил в сценарии, что Рэна-сан и Сонодзаки-сан пострадали от одержимости Оясиро-сама..."
extend " Действительно, если пораскинуть мозгами, объяснение самое логичное..."
extend " опасаюсь, что так.\""
show rena se nande_a1 at sleva
a_r "\"Ну-у... по правде сказать, я согласна с Ооиси-саном."
extend " ...Иначе никак не объяснить, почему Рэна и Мии-тян, вначале такие добрые, переменились и стали такими странными.\""
hide ooishi
show mion se maji_a1 at sprava
a_m "\"...К слову{cps=*0.4}.........{/cps} из уст Мион вам покажется странным, но... я считаю, дело во мне.\""
nvl clear
hide rena
show rika se de_a1 at sleva behind mion
a_f "\"......Мии толкует сложно для понимания."
extend " Хотелось бы разъяснений.\""
show mion se def_b1 at sprava
a_m "\"Ох, извини."
extend " ...Я просто говорю, так сказать..."
extend " жестокая очень история, да уж.\""
hide rika
show rena se ko_a1 at sleva
a_r "\"Что? ......Погоди-ка, Мии-тян."
extend " ...Ты действительно считаешь......\""
hide mion
show tomi si_uh at sprava
a_t "\"Полагаю, таков единственный возможный вывод."
extend " ...Хотя не берусь утверждать.\""
nvl clear
scene bg 161
show ooishi si def_a1 at sprava
a_o "\"В общем, что пытается она сказать — Рэна-сан и Сонодзаки-сан действительно по характеру злые, а обманывали Маэбару-сана, потому что тот в деревне новенький."
extend " ...Прав?\""
show satoko se hn_a1 at sleva
a_s "\"Нет! Не хочу-у-у!!!!"
show satoko se na_a1
extend " Уаааааааааа!!!"
extend " Во всём виновато проклятие!"
extend " Рэна-сан, Мион-сан и все остальные на деле добрые и хорошие-е-е-е!!!!\""
nvl clear
hide ooishi
show rena se ko_b1 at sprava
a_r "\"Я, я согласна!"
extend " Рэна и Мион-тян — очень хорошие девочки."
extend " ...Я уверена, они собой не владели в те жуткие минуты.\""
nvl clear
scene bg 163
show mion se wink_a1 at sleva
a_m "\"Хы, стало быть, Рэна тож за Проклятие."
extend " Ну ладно, вопрос всем на стороне Проклятия:"
extend " разве не нужен повод и проклятиям?"
extend " Видите ли, я не представляю себе, как можно прокляcть без причины."
extend " Ну, как объясните?\""
show satoko se bik_a1 at sprava
a_s "\"Проклятие суть есть проклятие!!!"
extend " Человеку объяснить его не под силу!\""
hide mion
show tomi si_wa at sleva behind satoko
a_t "\"А-ха-ха, но, Сатоко-тян,"
extend " человекоподобные боги рождены разумом человека."
extend " Следовательно, мышление тех богов доступно человеческому пониманию."
extend " ...Взгляни, к примеру, на богов греческих."
extend " Они плачут, злятся, завидуют... Очень по-человечески.\""
nvl clear
show rena se nande_a1 at central behind satoko
a_r "\"Значит... вы хотите сказать... Оясиро-сама, подобно человеку, проклинает по своему разумению?\""
a_t "\"Чудн{u}о{/u} говоришь, но да, так оно и есть по сути.\""
nvl clear
scene bg 161
show ooishi si wa_a1 at sprava
a_o "\"......Ну, говорится ведь: «Не буди лихо, пока оно тихо»."
extend " Н-а-ха-ха, верно-то как.\""
nvl clear
hide ooishi
show rika se de_a1 at sleva
a_f "\"......Коротко говоря, будь преступником хоть Оясиро-сама, хоть человек, повод свой нужен всяко.\""
show satoko se def_a1 at sprava
a_s "\"Но, Рика,"
extend " что, если мы не сможем найти причины... что тогда?\""
show rika se wa_a1
a_f "\"......Коротко говоря, не имею ни малейшего понятия.\""
nvl clear
scene bg 163
show rena se wa_a1 at sleva
a_r "\"А-ха-ха-ха-ха-ха!"
extend " И правда,"
extend " мы видели один только пролог большой истории."
extend " Должно быть много ещё не сказанных вещей.\""
show tomi si_def at sprava
a_t "\"Верно же."
extend " Пока что гадать затруднительно.\""
hide rena
show mion se tk_a1 at sleva behind tomi
a_m "\"Ну, блин!"
extend " Я хочу всё знать, что белое, а что чёрное!\""
hide tomi
show satoko se aki_a1 at sprava
a_s "\"Так и Мион-сан к тому стремится.\""
show mion se wa_a1
a_m "\"Аха-ха-ха!"
extend " Знаю, давайте посмотрим, что сможем изобразить с нашим ограниченным знанием!!!"
extend " Разве не весело будет применить свои клубные навыки в деле?\""
show rena se wa_b1 at central behind satoko
a_r "\"О, правда ведь!"
extend " Почему б не весело!\""
nvl clear
scene black
scene bg 161
show ooishi si wa_a1 at sleva
a_o "\"Хорошо, давайте тогда разберёмся."
extend " Я, значит, за Проклятие."
extend " Томитаке-кун, ты за Человека, да?\""
show tomi si_wa at sprava
a_t "\"Ага,"
extend " ставлю на преступника-человека.\""
hide ooishi
show mion se wa_a1 at sleva
a_m "\"Я также за человека!"
extend " Впрочем, и догадка о проклятии меня не смущает."
extend " Однако в увиденном до сей поры проклятию мало зацепок.\""
nvl clear
scene bg 163
show ooishi si def_a1 at sprava
a_o "\"Итого двое на стороне Человека."
extend " Рэна-сан, вы за Проклятие, так?\""
show rena se def_a1 at sleva
a_r "\"Так."
extend " Мы с Сатоко-тян за Проклятие."
extend " Верно?\""
hide ooishi
show satoko se wa_a1 at sprava
a_s "\"Ещё как!"
extend " Я всеми конечностями за Проклятие!"
extend " А кто говорит, что Рэна-сан и Мион-сан всамделишные злодейки, на тех да падёт проклятие на самих!!!\""
hide rena
show mion se to_a2 at sleva
a_m "\"Эй-эй,{w=1.0} мне и самой не нравится мысль о том, что моя героиня злая."
extend " ...Но в Клубном Режиме изволь оставаться собранной!"
extend " Пойдёшь у чувств \nна поводу — сгоришь как лучинка, ясно?\""
nvl clear
scene bg 161
show ooishi si wa_a1 at sleva
a_o "\"Конечно, конечно."
extend " Выбирайте что душе угодно.\""
show tomi si_def at sprava
a_t "\"Хм? Рика-тян, ты ничего ещё не сказала."
extend " Ты-то как думаешь?\""
hide ooishi
show rika se de_a1 at sleva behind tomi
a_f "\"......Я не считаю Оясиро-сама плохим божеством.\""
a_t "\"Ого, любопытная точка зрения.\""
a_f "\"......Я бы не стала чтить злобное божество, проклинающее народ."
extend " Предпочитаю бога благословляющего, нежели проклинающего.\""
nvl clear
hide tomi
show rena se wa_a1 at sprava
a_r "\"Ах да, Рика-тян же играла храмовую жрицу!.."
extend " И неплохо-то как сказала.\""
show mion se def_b1 at central behind rena
a_m "\"Ну так чего, Рика-тян?"
extend " Если думаешь не на Оясиро-сама, тогда{w=1.0}... по-твоему, преступник всё ж таки человек?!\""
show rika se wa_a1
a_f "\"......Именно так я решила.\""
nvl clear
scene bg 163
show ooishi si wa_a1 at sprava
a_o "\"Ох, надо же."
extend " ...Преровно все поделились,"
extend " половина за Проклятие, половина за Человека!\""
show tomi si_def at sleva behind ooishi
a_t "\"Рэна-тян, из любопытства поинтересуюсь-ка..."
a_t "Каковы впечатления игроков из Японии, прошедших бета-версию?\""
hide ooishi
show rena se def_b1 at sprava
a_r "\"Ну, ммм..."
extend " Угу,"
extend " многие склоняются к Человеку!\""
hide tomi
show mion se wink_a1 at sleva
a_m "\"Ха, вишь, вишь, чё говорила?!"
extend " Наши прожжённые товарищи, стреляные воробьи, уж им-то наблюдательности не занимать!\""
nvl clear
scene bg 161
show rika se de_a1 at sleva
a_f "\"......Но ведь бета-версия покрывала только часть главы.\""
show rena se wa_a1 at sprava
a_r "\"Ты права."
extend " Возможно, испытатели поменяют решение, пройдя главу до конца.\""
nvl clear
scene bg 161
show mion se wink_a1 at sprava
a_m "\"Ну так что"
extend " с разделением голосов делать будем?"
extend " Надо же остановиться на чём-то, иначе не интересно!\""
show tomi si_wa at sleva behind mion
a_t "\"С нечётным числом судей так бы не вышло."
extend " Чего бы я не отдал за один только надбавочный голос!\""
hide mion
show rena se wa_b1 at sprava
a_r "\"А, знаю!"
extend " Почему бы не спросить Кейти-куна?"
extend " Давайте позвоним!\""
hide tomi
show rika se wa_a1 at sleva
a_f "\"......Мнение убитого проклятием чрезвычайно ценно же.\""
show satoko se aku_a1 at central
a_s "\"Ну так чего мы ждём, пошли к телефону!!!\""
nvl clear
scene black
scene bg 011
a_r "\"Алло, Кейти-кун?"
extend " Рэна звонит!"
extend " Ты сейчас работою занят?\""
a_k "\"Да уж... занят работой так занят."
extend " Я-то думал, после сей главы мне дадут передышку, но тут уже над следующей работа кипит!!!\""
nvl clear
scene bg 165
show mion se def_a1 at sprava
a_m "\"Чё там Кей-тян?"
extend " Он занят?\""
show rena se nande_a1 at sleva
a_r "\"Угу."
extend " Дуется.\""
a_k "\"Эй, я всё слышал!!!"
extend " Вам-то небось весело на своём заседании!"
extend " Я тоже хотел пойти!!!\""
hide mion
show rika se wa_a1 at sprava
a_f "\"......Кейти сможет нас посетить, когда ему нарисуют картинку.\""
hide rena
show satoko se aki_a1 at sleva
a_s "\"Рика, не выдавай военную тайну...\""
nvl clear
hide satoko
hide rika
show rena se def_b1 at sleva
a_r "\"Ах да, Кейти-кун, извини."
extend " ...Помнишь,"
extend " как ты,"
extend " э-э{cps=*0.2}......{/cps} умер?"
extend " Ну и мы вот судачим, кого же подозревать.\""
show mion se wink_a2 at sprava
a_m "\"Или, по-другому, мы поделились в том, что собой представляет убийца — человека или Проклятие Оясиро-сама.\""
a_r "\"Мне так жаль!"
extend " Нам и впрямь не стоит тебя беспокоить, пока ты читаешь сценарий, но всё-таки..."
extend " Кейти-кун, ты к чему склоняешься?\""
nvl clear
a_k "\"Да это ж, блин, очевидно!!!\""
a_r "\"К чему же?\""
nvl clear
scene bg 165
a_k "\"Не в том дело, к чему!!!"
extend " Сперва на меня напали подозрительные деревенские дядьки, потом проклял тот Оясиро-сама!!!"
extend " Человеки, \nпроклятия"
extend " — они все на меня ополчились!!!!\""
show rika se wa_a1 at central
a_f "\".........Бедненький, бедненький."
extend " Я тебя при встрече поглажу.\""
nvl clear
hide rika
show black
show tomi si_def at sprava behind black
hide black
a_t "\"В итоге наши мнения разделены всё так же поровну.\""
show ooishi si def_a1 at sleva behind tomi
a_o "\"Я там ещё поразмыслю."
extend " Мог чего-нибудь не заметить.\""
nvl clear
scene bg 166
show rena se def_a1 at sprava
a_r "\"А теперь предлагаем пройти следующую игру в серии «Когда плачут цикады» — «Главу о Хлопковых Корабликах»!!!\""
nvl clear
show cinema
show title02
show black behind title02
scene black
$ renpy.full_restart()
