    if not persistent.chapter_tata:
        $ persistent.chapter = persistent.chapter + 1
        $ persistent.chapter_tata = True
        $ show_button_game_menu = False
        $ _game_menu_screen = None
        $ mouse_visible = False
        call omake_between
        scene omake_tatarigorosi with spiral5
        $ renpy.pause(10.0)
        call omake_between
        scene omake_tips with spiral5
        $ renpy.pause(10.0)
        call omake_between
        scene omake_jump with spiral5
        $ renpy.pause(10.0)
        if persistent.chapter == 1:
            call omake_between
            scene omake_bgm with spiral5
            $ renpy.pause(10.0)
            if persistent.matsuri:
                call omake_between
                scene omake_gallery with spiral5
                $ renpy.pause(10.0)
        if not persistent.chapter_hima:
            call omake_between
            scene omake_unlock_hima with spiral5
            $ renpy.pause(10.0)
        scene black with Dissolve(1.0)
        $ mouse_visible = True
        $ renpy.pause(1.0, hard=True)
        scene expression "efe/haikei_3.jpg" with Dissolve(1.0)
        show expression "efe/Title.png" at top
        show expression "efe/prava_disclaimer.png" at central
        with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
