    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play ambient lsys12
    scene bg 206 with dissolve_04
    n "Шуршание машины приблизилось к лачуге. Тихо скрипнули тормоза, и двигатель смолк."
    nvl clear
    n "Вольготно разлёгшийся человек тут же вскочил, прижался ко стенке возле окна и осторожно выглянул..."
    nvl clear
    n ".........Машина своя."
    n "Но он по-прежнему держался настороже."
    n "{nw}"
    n "Кто-то подошёл ко входной двери."
    extend " «...Тук,{w=1.0} тук-тук-тук»,{w=1.0} — раздался условный стук."
    nvl clear
    n "\"......Эй, я тут."
    extend " Открой, это я.\""
    n "\"А, отлично."
    extend " Погодь, сейчас открою.\""
    nvl clear
    play sound wa_020
    n "Он отпер дверь. На пороге стоял мужчина со здоровенными пластиковыми пакетами в обеих руках."
    n "{nw}"
    n "На пакетах, из которых выглядывали пачки с молоком и булочки, — надпись: «Севенс Март»."
    nvl clear
    play sound wa_002
    $ renpy.pause(0.2)
    play sound wa_003
    n "Вдвоём они высыпали содержимое пакетов на лежащее на полу одеяло."
    nvl clear
    n "\"Я купил лапши в стаканах, давай заварим?"
    extend " Как там сопляк?\""
    n "\"Хм?"
    extend " Да дрыхнет всё."
    extend " Хорошо, никаких забот."
    extend " Правда, когда срать хочет, сопеть начинает, возится.\""
    n "\"Ты там посматривай, чтоб не обосрался."
    extend " Если вдруг учуют — пиздец.\""
    n "\"...Да знаю я...\""
    nvl clear
    n "\"И кляп не забывай проверять."
    extend " Беда, если выпадет, но и слишком туго нельзя затягивать."
    extend " Если задохнётся — всё к чёрту.\""
    n "\"Да понял я, понял..."
    extend " Эй, разве я не просил привезти газ для горелки?"
    extend " А то кончился.\""
    n "\"Не помню такого.\""
    n "\"...Бля-я-я... Ну скажи, что ты шутишь..."
    extend " Ну что за дерьмо!!\""
    nvl clear
    n "Первый яростно защёлкал поджигом, пытаясь заставить горелку работать."
    n "{nw}"
    n "...Тот, кто ездил в город, поглядев на него, вздохнул."
    nvl clear
    scene bg 194 with left_03
    n "И медленно подошёл к углу комнаты."
    nvl clear
    n "...В углу свернулся на одеяле похищенный мальчик."
    nvl clear
    n "\".........Эй, пацан......{w=1.0} Ты как?\""
    n "Разумеется, он даже и мысли не допускал, что мальчик его расслышит."
    nvl clear
    n "Всё-таки в ушах у того — затычки, да вдобавок они, как и глаза, в несколько слоёв заклеены клейкой лентой."
    n "{nw}"
    n "А во рту — кляп изо скрученного полотенца."
    n "{nw}"
    n "......Из-за него тот не мог закрыть рта, в котором не переставала обильно выделяться слюна."
    nvl clear
    n "И, конечно, на этом не ограничивалось."
    n "Нечто вроде кожаного ремня туго стягивало запястья."
    nvl clear
    n "\"Покамест всё вроде отлично."
    extend " За свою шкуру можешь не беспокоиться..."
    extend " Кабы твой дед колебался, пришлось бы отрезать те мочку... и хорошо, что до того не дошло."
    extend " Наши главные — сущие демоны..."
    extend " Хто их знает, шо там прикажут с тобой сотворить......"
    extend " Но, вишь, говорят же, шоб пальцем тронуть не смели, — знач, пока усё хорошо...\""
    nvl clear
    n "\"Министр там останавливает стройку по-тихому."
    extend " Проект Хинамидзавской дамбы откладывается на неопределённый срок."
    extend " Сопляка-то когда отпустят?.."
    extend " Поскорее бы затянуться, блин.\""
    n "\"Грят, в главной семье ждут решающего момента."
    extend " Хрен их знает, когда это, но, мыслю, скоро...\""
    n "\"Ты рад, сопляк?"
    extend " Скоро тебя отпустят, хе-хе-хе...\""
    nvl clear
    scene black with fastup
    n "Было неизвестно, слышит ли их мальчик."
    n "{nw}"
    n "Тот знал всего лишь один способ хоть как-то уберечь рассудок от жестокой действительности: без конца спать..."
    nvl clear
    n "\"Ну так шо с газом-то, а?!"
    extend " На чём лапшу готовить?!!"
    extend " Хрен ли ты не сказал, шо он кончился!!\""
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_hima
    return
