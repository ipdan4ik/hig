    stop ambient fadeout 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    scene bg 110 with Dissolve(1.0)
    play ambient lsys12
    n "Ещё только июнь,{w=1.0}{nw}"
    extend " а уже так жарко."
    n "На улице кричат цикады, а по ночам летают комары."
    extend " ...Да уж, лето действительно пришло."
    n "{nw}"
    n "...Хорошо хоть, по утрам прохладно."
    nvl clear
    show satoko se bik_b1 at sprava with right_03
    n "\"Ох и духота же!\""
    n "Сатоко вяло обмахивалась юбкой."
    n "{nw}"
    n "...Знаешь, это не очень-то женственно."
    n "...Ты хоть и наглая, но всё же девочка."
    nvl clear
    show satoko se def_a1 with dissolve_02
    n "\"Вам-то хорошо небось, Кейти-сан, в одной-то рубашке..."
    extend " Мне даже завидно.\""
    n "\"С моей точки зрения, Сатоко, тебе в юбке куда свежее будет."
    extend " Девчонке вроде тебя ни за что не понять, как же в такую жару запаривается промежность!\""
    nvl clear
    show rena se hau_b1 at sleva with dissolve_02
    n "\"...За... запаривается...... хау......\""
    n "{nw}"
    n "Опять у этой девчушки мозги настроились на неприличный лад..."
    nvl clear
    n "\"А у твоей формы неплохой цвет, Рэна."
    extend " Даже взгляд на неё освежает.\""
    show rena se wa_a1 with dissolve_02
    n "\"А-ха-ха-ха-ха."
    extend " Спасибо!"
    extend " В ней и правда свежо.\""
    show satoko se aki_a1 with dissolve_02
    n "\"Хотела бы я летнюю форму как у Рэны-сан.\""
    nvl clear
    show rena se def_a1 with dissolve_02
    n "\"Но, Сатоко-тян, у тебя такое милое платьице!"
    extend " Ах, Рэна хочет его надеееть...\""
    show satoko se def_b1 with dissolve_02
    n "\"В нём очень жарко, между прочим."
    extend " Ваша форма безусловно прохладнее.\""
    show rena se hau_a1 with dissolve_02
    n "\"Но миииленький нарядик носить веселее. ......Хау!\""
    n "...Похоже, системы ценностей Рэны и Сатоко здорово разнятся..."
    nvl clear
    n "\"Так здесь нет определённых правил выбора формы, я правильно понимаю?\""
    show rena se def_b1 with dissolve_02
    n "\"Угу,"
    extend " их нет."
    extend " Пока всё в рамках приличий, носить можно даже повседневную одежду.\""
    n "Её здесь носят многие."
    extend " Есть ученики в форме, но у них она одного (и довольно скучного) покроя."
    nvl clear
    scene bg 109 with left_03
    n "\"...С этими-то что?"
    extend " На них на всех одно и то же.\""
    show satoko se aku_a1 at sleva with left_03
    n "\"То форма городской школы."
    extend " Хоть она и не требуется, всё равно носят.\""
    n "\"А у нас у всех форма разная."
    extend " ...Что, вся на заказ пошита?\""
    n "\"Да. Её достаёт Мион-сан.\""
    nvl clear
    show rena se def_a1 at sprava with right_03
    n "\"Один из родственников Мии-тян владеет магазином подержанной одежды, где можно найти форму любой школы страны по низкой цене.\""
    n "\"Так она попросила его подобрать вам разную форму?\""
    n "{nw}"
    n "...Ох уж эта Мион. Верно, здорово повеселилась, делая из друзей кукол для примерки одежды."
    n "{nw}"
    n "......Но что за странный магазин-то такой."
    n "Я могу понять продажу обычных б/у вещей, но зачем одежда со всей страны?"
    nvl clear
    n "...Что-то я в нём не пойму."
    n "Зачем нужна форма какой-то школы, о которой даже никто не слышал?"
    nvl clear
    show rena se nande_a1 with dissolve_02
    n "\"...Угу. Рэна тоже так считает."
    extend " У них ещё можно купить спортивную форму и старые школьные купальники."
    extend " ...Как-то противно выглядит носить поношенные купальники.\""
    n "\"Не очень-то похоже на процветающее предприятие."
    extend " ...Небось, Мион лишь помогает им немного заработать.\""
    show satoko se aki_a1 with dissolve_02
    n "\"...А Мион-сан всегда так уверенно говорит,"
    extend " что уж скоро дело начнёт процветать!\""
    nvl clear
    n "......Магазин подержанной школьной формы начнёт процветать?"
    n "{nw}"
    n "...Не понимаю."
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_onik
    return