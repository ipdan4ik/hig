if not persistent.chapter_wata
$ persistent.chapter = persistent.chapter + 1
$ persistent.chapter_wata = True
$ show_button_game_menu = False
$ _game_menu_screen = None
$ mouse_visible = False
call omake_between
scene omake_watanagasi
call omake_between
scene omake_tips
if persistent.chapter == 1
call omake_between
scene omake_jump
call omake_between
scene omake_bgm
call omake_between
scene omake_gallery
if not persistent.chapter_tata
call omake_between
scene omake_unlock_tata
scene black
$ mouse_visible = True
scene expression "efe/haikei_2.jpg"
show expression "efe/Title.png" at top
show expression "efe/prava_disclaimer.png" at central
$ renpy.full_restart()
