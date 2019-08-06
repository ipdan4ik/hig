if not persistent.chapter_tata
$ persistent.chapter = persistent.chapter + 1
$ persistent.chapter_tata = True
$ show_button_game_menu = False
$ _game_menu_screen = None
$ mouse_visible = False
call omake_between
scene omake_tatarigorosi
call omake_between
scene omake_tips
call omake_between
scene omake_jump
if persistent.chapter == 1
call omake_between
scene omake_bgm
call omake_between
scene omake_gallery
if not persistent.chapter_hima
call omake_between
scene omake_unlock_hima
scene black
$ mouse_visible = True
scene expression "efe/haikei_3.jpg"
show expression "efe/Title.png" at top
show expression "efe/prava_disclaimer.png" at central
$ renpy.full_restart()
