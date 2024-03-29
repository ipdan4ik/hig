    stop music fadeout 2.0
    scene black with Dissolve(3.0)
    play music nageki_bgm
    n "Это детективно-психологический роман в жанре кинетической визуальной новеллы."
    n "Что такое визуальная новелла?"
    n "Чужеродное слово «новелла» полностью соответствует в определении нашему слову «повесть». Или «роман», кому как удобнее."
    n "Слово же «визуальная» означает, что текст книги сопровождается графическим рядом."
    n "А кинетическая — что читатель неспособен повлиять на ход событий, в отличие от игровых романов навроде Fate/Stay Night, где герой всё время должен делать выбор, от которого зависит развязка."
    nvl clear
    n "В серии «Когда {color=#f00}плач{/color}ут цикады» большой упор сделан также на звуковое сопровождение. Пройдясь по сюжету, вы заметите сами."
    n "Замысел создателя таков: пускай читатель попробует сам разгадать все загадки Хинамидзавы."
    n "А в помощь ему, кроме встречающихся в основном тексте намёков, будут ниспосланы TIPS, они же ПОДСКАЗКИ."
    n "Однако, чтобы задача не оказалась чересчур легка, создатель не поскупился на отвлекающие и уводящие в сторону сведения."
    n "За что и любим{w=0.5} (ударение можно поставить и так, \nи этак)."
    nvl clear
    if persistent.chapter_onik:
        n "Очень сильно влияет на разгадываемость манера повествования."
        n "Оно проходит через призму эмоций рассказчика. И не всегда (гораздо чаще наоборот) его мнение объективно."
        n "Как могли заметить дотошные читатели, прочитав Первую Главу."
        nvl clear
    if persistent.chapter_wata:
        n "Кроме того, многое рассказчик может не знать и сам."
        n "И потому есть Главы Ответов, в которых даны ответы на большинство задаваемых соответствующей Главой вопросов."
        n "Например, на заданные в Оникакуси вопросы отвечает Цумихоробоси (6-я Глава);{w=1.0} на заданные в Ватанагаси — Мэакаси (5-я Глава);{w=1.0} \nТатаригороси — Минагороси (7-я Глава);{w=1.0} Химацубуси, соответственно, Мацурибаяси (8-я Глава)."
        nvl clear
        n "Помимо них, есть побочные Главы, но о них вы вполне можете узнать в Интернете."
        nvl clear
    if persistent.chapter_tata:
        n "Как вы заметили, также большое значение имеет музыкальное сопровождение, призванное передать чувства рассказчика."
        n "И автор умело использует его для придания психологической нагрузки."
        n "Третья Глава очень тяжёлая."
        nvl clear
    if persistent.chapter_hima:
        n "{cps=*0.5}{i}А ещё иногда так бывает, что для чуда недостаёт всего одного небольшого усилия.{/i}{/cps}"
        n "{cps=*0.5}{i}Чтобы кто-то вспомнил, где он ошибся в далёком прошлом, даже если в этом прошлом он никогда не был...{/i}{/cps}"
        extend " И в этот раз вернулся и всё сделал правильно."
        nvl clear
    if persistent.chapter >= 1:
        n "Если же у вас есть вопрос, почему герои произведения, погибшие или убитые в предыдущей Главе, вдруг возродились в этой, отвечу на него так."
        n "Главные герои раз за разом переживают один и тот же летний месяц 1983 года, месяц летнего солнцестояния — Июнь."
        n "А почему так? Потому что кое-кто не хочет, чтобы этот месяц закончился грустно."
        n "И, с помощью концепции «бесконечного множества параллельных реальностей», раз за разом переходит кое с кем вместе в следующий мир."
        nvl clear
        if persistent.chapter >= 3:
            n "Однако раз за разом кое-чьё скромное желание побеждает чужая, злая воля — потому что простого скромного желания недостаточно. Для того чтобы пойти наперекор судьбе, нужна сплочённая воля многих. И, чтобы понять это, для начала придётся совершить много ошибок и много раз погибнуть."
            n "Впрочем, здесь уже пошли спойлеры, поэтому, товарищи, читайте все Главы."
            nvl clear
    n "Если в тексте встречается слово, которому, по мнению переводчика, требуется разъяснение (может, слово сложное, а может, японской культуры, а может, он просто счёл, что неплохо бы пояснить), смысл слова раскрывается в Заметках Переводчика."
    n "Потому что, бывает, Заметки поясняют и слова, встречающиеся в ПОДСКАЗКАХ, следует прочесть сначала ПОДСКАЗКИ ко дню, а потом уже Заметки."
    n "Каждое подобное слово встречается в Заметках к одной Главе только раз."
    n "Если же оно встречается в другой Главе, то поясняется в той заново."
    n "Так устроены Заметки Переводчика."
    nvl clear
    n "Кавычки английского типа (\"например\") в самом повествовании применяются только и только для обозначения речи вслух."
    n "В качестве основных кавычек используются русские кавычки-«ёлочки». В качестве дополнительных — кавычки-„лапки“."
    n "Если в каком-нибудь слове вдруг встречается подчёркнутая гл{u}а{/u}сная — это ударение."
    n "Оно ставится в тех случаях, когда иначе слово можно прочитать в неверном значении."
    n "К примеру, б{u}о{/u}льшая часть и больш{u}а{/u}я часть.{w=0.75} Изредка ударения подчёркиваются для дополнительной помощи при осмыслении слова — там, где переводчик счёл более-менее нужным."
    nvl clear
    stop music fadeout 7.0
    n "И на этом я с вами закончу."
    n "Для лучшего понимания того, на чём построен сюжет, следует прочитать Главу Завершающую."
    n "О Подыгрывании Фестивалю."
    nvl clear
    call screen translation_notes
    return
