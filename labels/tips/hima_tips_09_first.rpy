    n "......Я вижу, вы разочарованы."
    n "{nw}"
    n "Ну ещё бы."
    n "Очевидно, что с выбором вы оплошали."
    nvl clear
    n "Может, в другой коробке оказалась бы плитка шоколада."
    n "Нет, может, кое-что намного, намного лучше — например, билет на поездку вдвоём на Гавайи."
    nvl clear
    n "Но если бы вы и хотели посмотреть, что там, другая-то коробка исчезла."
    n "Теперь уже никак не узнать."
    n "{nw}"
    n "И вы начинаете думать так, чтобы себя утешить."
    n "Мало ли... вдруг в другой коробке вообще ничего не было, и выбрали вы как раз правильную."
    n "{nw}"
    n "И, удовольствовавшись грошовой наградой (да хоть бы и наоборот — всё равно), вы кидаете её в рот, жуёте, и вам становится чуточку веселее."
    nvl clear
    n "Ну так как вы считаете?"
    n "Дай вам другую попытку, открыли бы другую коробку?"
    n "......Одна беда — вам никогда больше не удастся поиграть в выбор из красной и синей коробок."
    n "И вы больше никогда не сможете выбрать другой вариант."
    nvl clear
    n "Разве не твердили вам папа с мамой: выбирай с умом, так как выбор даётся лишь однажды?"
    n "Хи-хи-хи-хи......"
    n "{nw}"
    n "Видите?"
    extend " Выбор — не бог весть какое дело..."
    extend " Что, немного разочарованы?"
    extend " Аха-ха-ха-ха-ха-ха......"
    nvl clear
    if not persistent.hima_asobi:
        if asobi_box == 1:
            $ persistent.hima_asobi = 1
        else:
            $ persistent.hima_asobi = 2
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_hima
    return
