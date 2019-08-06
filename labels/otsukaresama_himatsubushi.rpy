if not persistent.chapter_hima
$ persistent.chapter = persistent.chapter + 1
$ persistent.chapter_hima = True
$ show_button_game_menu = False
$ _game_menu_screen = None
$ mouse_visible = False
call omake_between
scene omake_himatubusi
call omake_between
scene omake_tips
call omake_between
scene omake_jump
if persistent.chapter == 1
call omake_between
scene omake_bgm
call omake_between
scene omake_gallery
scene black
$ mouse_visible = True
scene expression "efe/haikei_4.jpg"
show expression "efe/Title.png" at top
show expression "efe/prava_disclaimer.png" at central
$ renpy.full_restart()
