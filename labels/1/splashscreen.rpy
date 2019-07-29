    $ show_button_game_menu = False
    $ mouse_visible = False
    $ _game_menu_screen = None
    scene logo 07 th with dissolve
    $ renpy.pause(1.0)
    scene logo alchemist with dissolve
    $ renpy.pause(1.0)
    scene white with fade
    $ renpy.pause(1.0)
    show title with dissolve:
        xalign 0.5 yalign 0.5
        linear 1.5 xalign 0.5 yalign 0.0
    $ renpy.pause(2.0)
    $ mouse_visible = True
    $ _game_menu_screen = "game_menu"
    return
