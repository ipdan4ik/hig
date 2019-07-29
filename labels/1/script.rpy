    image logo 07 th = "efe/logo_07th.jpg"
    image logo alchemist = "efe/logo_alchemist.jpg"
    image title = "efe/Title.png"
    image title02 = "efe/Title_cinematic.png"
    image cinema = "efe/cinema.png"
    image white = "efe/white.jpg"
    image red = "efe/red.jpg"
    image black = "efe/black.jpg"

    $ spiral2 = ImageDissolve("efe/2.png", 1.0, 64, reverse=False)
    $ spiral3 = ImageDissolve("efe/3.png", 2.0, 32, reverse=False)
    $ spiral4 = ImageDissolve("efe/4.png", 1.0, 32, reverse=False)
    $ spiral5 = ImageDissolve("efe/5.png", 1.0, 32, reverse=False)
    $ dissolve_02 = Dissolve(0.2)
    $ dissolve_04 = Dissolve(0.4)
    $ fade_010 = Fade(0.006, 0.001, 0.003, color="#fff")
    $ fade_025 = Fade(0.01, 0.005, 0.01, color="#fff")
    $ fade_050 = Fade(0.03, 0.005, 0.015, color="#fff")
    $ b_down = ImageDissolve(im.Tile(im.Rotozoom(im.Flip("blindstile.png", horizontal=True), 90, 0.5)), 1.0, 8)
    $ b_left = ImageDissolve(im.Tile(im.Rotozoom(im.Flip("blindstile.png", horizontal=True), 0, 0.5)), 1.0, 8)
    $ b_right = ImageDissolve(im.Tile(im.Rotozoom("blindstile.png", 0, 0.5)), 1.0, 8)
    $ center = ImageDissolve("efe/center.png", 1.5, 32, reverse=True)
    $ center_03 = ImageDissolve("efe/center.png", 0.3, 32, reverse=True)
    $ fastdown = ImageDissolve("efe/down.png", 0.3, 32, reverse=True)
    $ down = ImageDissolve("efe/down.png", 1.5, 32, reverse=True)
    $ down_30 = ImageDissolve("efe/down.png", 3.0, 32, reverse=True)
    $ up = ImageDissolve("efe/up.png", 1.0, 32, reverse=True)
    $ up_30 = ImageDissolve("efe/up.png", 3.0, 32, reverse=True)
    $ fastup = ImageDissolve("efe/up.png", 0.3, 32, reverse=True)
    $ left_03 = ImageDissolve("efe/left.png", 0.3, 32, reverse=False)
    $ left = ImageDissolve("efe/left.png", 1.5, 32, reverse=False)
    $ left_30 = ImageDissolve("efe/left.png", 3.0, 32, reverse=False)
    $ right = ImageDissolve("efe/right.png", 1.5, 32, reverse=False)
    $ right_03 = ImageDissolve("efe/right.png", 0.3, 32, reverse=False)
    $ right_30 = ImageDissolve("efe/right.png", 3.0, 32, reverse=False)
    $ m1 = ImageDissolve("efe/m1.png", 1.0, 32, reverse=True)
    $ m1_03 = ImageDissolve("efe/m1.png", 0.3, 32, reverse=True)
    $ m1_30 = ImageDissolve("efe/m1.png", 3.0, 32, reverse=True)
    $ efe_aa = ImageDissolve("efe/aa.png", 0.3, 32, reverse=True)
    $ ryuuketu_efe = ImageDissolve("efe/ryuuketu_efe.png", 1.0, 32, reverse=True)
    $ toketu_efe = ImageDissolve("efe/toketu_efe.png", 1.0, 32, reverse=True)
    $ x = ImageDissolve("efe/x.png", 5.0, 32, reverse=False)
    $ x_15 = ImageDissolve("efe/x.png", 1.5, 32, reverse=False)

    $ dissolve_02 = Dissolve(0.2)
    $ dissolve_04 = Dissolve(0.4)
    $ fade_010 = Fade(0.006, 0.001, 0.003, color="#fff")
    $ fade_025 = Fade(0.01, 0.005, 0.01, color="#fff")
    $ fade_050 = Fade(0.03, 0.005, 0.015, color="#fff")
    $ center = ImageDissolve("efe/center.png", 1.5, 32, reverse=True)
    $ center_03 = ImageDissolve("efe/center.png", 0.3, 32, reverse=True)
    $ fastdown = ImageDissolve("efe/down.png", 0.3, 32, reverse=True)
    $ up = ImageDissolve("efe/up.png", 1.0, 32, reverse=True)
    $ fastup = ImageDissolve("efe/up.png", 0.3, 32, reverse=True)
    $ left_03 = ImageDissolve("efe/left.png", 0.3, 32, reverse=False)
    $ right_03 = ImageDissolve("efe/right.png", 0.3, 32, reverse=False)
    $ m1 = ImageDissolve("efe/m1.png", 1.0, 32, reverse=True)
    $ m1_03 = ImageDissolve("efe/m1.png", 0.3, 32, reverse=True)
    $ efe_aa = ImageDissolve("efe/aa.png", 0.3, 32, reverse=True)
    $ ryuuketu_efe = ImageDissolve("efe/ryuuketu_efe.png", 1.0, 32, reverse=True)
    $ toketu_efe = ImageDissolve("efe/toketu_efe.png", 1.0, 32, reverse=True)
    $ x_15 = ImageDissolve("efe/x.png", 1.5, 32, reverse=False)

    $ sleva = Position(xpos=0.25, xanchor='center')
    $ central = Position(xpos=0.5, xanchor='center')
    $ sprava = Position(xpos=0.75, xanchor='center')

    $ n = Character(None, kind=nvl, ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled")
    $ t = Character(None, kind=nvl, ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", callback=typewriter, what_font="CourierNew.ttf", what_slow_cps_multiplier=0.4)
    $ centered = Character(None, what_style="centered_text", window_style="centered_window", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled")
    $ config.nvl_page_ctc = anim.Filmstrip(image="efe/List.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1)
    $ config.nvl_page_ctc_position = "nestled"
    image tips_received = Text("Для прочтения доступны новые ПОДСКАЗКИ.", slow=False, style='default')

    $ n = Character(None, kind=nvl, ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled")
    $ t = Character(None, kind=nvl, ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", callback=typewriter, what_font="CourierNew.ttf", what_slow_cps_multiplier=0.4)
    $ a_n = Character(None, kind=adv, ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_c = Character("Тиэ", kind=adv, color="#5B93D4", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_f = Character("Рика", kind=adv, color="#788DF6", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_h = Character("Шион", kind=adv, color="#18A966", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_i = Character("Ириэ", kind=adv, color="#DBBC9E", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_k = Character("Кейти", kind=adv, color="#835959", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_m = Character("Мион", kind=adv, color="#18A966", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_o = Character("Ооиси", kind=adv, color="#948598", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_r = Character("Рэна", kind=adv, color="#FF8635", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_s = Character("Сатоко", kind=adv, color="#FFE165", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_t = Character("Томитаке", kind=adv, color="#F0F0F0", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)
    $ a_y = Character("Такано", kind=adv, color="#CAB068", ctc=anim.Filmstrip(image="efe/Caret.png", framesize=(24, 24), gridsize=(3, 1), delay=0.1), ctc_position="nestled", show_two_window=True, window_left_padding=35, window_right_padding=40, window_bottom_padding=10, what_ypos=-10)

    image haikei = "efe/haikei.jpg"
    image cg_haikei = "efe/cg_haikei.bmp"
    image end_1 = "efe/end_1.bmp"
    image end_2 = "efe/end_2.bmp"
    image end_3 = "efe/end_3.bmp"
    image end_matsuri = "efe/end_matsuri.jpg"
    image furiker_a = "efe/furiker_a.jpg"
    image furiker_b = "efe/furiker_b.jpg"
    image kenkei = "efe/kenkei.jpg"
    image kouan = "efe/kouan.jpg"

    image wata_kanji_01 = "efe/kanji_01.jpg"
    image wata_kanji_02 = "efe/kanji_02.jpg"
    image wata_kanji_03 = "efe/kanji_03.jpg"
    image wata_kanji_04 = "efe/kanji_04.jpg"
    image wata_kanji_05 = "efe/kanji_05.jpg"
    image wata_kanji_06 = "efe/kanji_06.jpg"
    image wata_kanji_07 = "efe/kanji_07.jpg"
    image wata_kanji_08 = "efe/kanji_08.jpg"
    image tatari_list = "efe/tatari_list.jpg"
    image tatari_ed_credits = "efe/tatarigoroshi_staff.jpg"
    image tatari_ep_h15 = "efe/tatari_ep_h15.jpg"
    image staff = "efe/staff.jpg"

    image omake_haikei = "efe/omake_haikei.bmp"
    image omake_onikakusi = "efe/omake_onikakusi.bmp"
    image omake_watanagasi = "efe/omake_watanagasi.bmp"
    image omake_tatarigorosi = "efe/omake_tatarigorosi.bmp"
    image omake_himatubusi = "efe/omake_himatubusi.bmp"
    image omake_unlock_wata = "efe/omake_unlock_wata.bmp"
    image omake_unlock_tata = "efe/omake_unlock_tata.bmp"
    image omake_unlock_hima = "efe/omake_unlock_hima.bmp"

    image omake_tips = "efe/omake_tips.bmp"
    image omake_bgm = "efe/omake_bgm.bmp"
    image omake_jump = "efe/omake_jump.bmp"
    image omake_gallery = "efe/omake_gallery.bmp"

    image chapter 1 = "efe/chapter_1.jpg"
    image chapter 2 = "efe/chapter_2.jpg"
    image chapter 3 = "efe/chapter_3.jpg"
    image chapter 4 = "efe/chapter_4.jpg"

    image chapter onik_1 = "efe/chapter_onik_1.jpg"
    image chapter onik_2 = "efe/chapter_onik_2.jpg"
    image chapter wata_1 = "efe/chapter_wata_1.jpg"
    image chapter wata_2 = "efe/chapter_wata_2.jpg"
    image chapter tata_1 = "efe/chapter_tata_1.jpg"
    image chapter tata_2 = "efe/chapter_tata_2.jpg"
    image chapter hima_1 = "efe/chapter_hima_1.jpg"
    image chapter hima_2 = "efe/chapter_hima_2.jpg"

    image gomenasai x1 = "efe/gomenasai_x1.jpg"
    image gomenasai x2 = "efe/gomenasai_x2.jpg"
    image gomenasai x39 = "efe/gomenasai_x39.jpg"
    image okinomiya = "efe/okinomiya.jpg"
    image ryuuketu = "efe/red_blood.jpg"
    image toketu1a = "efe/toketu1a.jpg"
    image toketu1b = "efe/toketu1b.jpg"
    image toketu1c = "efe/toketu1c.jpg"
    image s53 = "efe/s53.jpg"
    image s60 = "efe/s60.jpg"

    image si_onikakusi = "efe/si_onikakusi.jpg"
    image si_watanagasi = "efe/si_watanagasi.jpg"
    image si_tatarigorosi = "efe/si_tatarigorosi.jpg"
    image si_himatubusi = "efe/si_himatubusi.jpg"
    image aka1 = "efe/aka1.jpg"
    image aka2 = "efe/aka2.jpg"
    image tyuui_disclaimer = "efe/tyuui_disclaimer.jpg"
    image tyuui_s58 = "efe/tyuui_s58.jpg"
    image uso_da = "efe/uso_da.jpg"
    image the_end = "efe/the_end.jpg"


    image cg bukatsu = "cg/bukatsu.jpg"
    image cg shion_kei = "cg/busty_girl.jpg"
    image cg ct full = "cg/caught_full.jpg"
    image cg ct kei = "cg/caught_keiichi.jpg"
    image cg ct rena = "cg/caught_rena.jpg"
    image cg crazy face = "cg/creepy_face.jpg"
    image cg crazy strike = "cg/creepy_strike.jpg"

    image cg door girl = "cg/door_1.jpg"
    image cg door fingers = "cg/door_2.jpg"
    image cg door delusion = "cg/door_3.jpg"
    image cg moon rika_1 = "cg/furude_no_rika_1.jpg"
    image cg moon rika_2 = "cg/furude_no_rika_2.jpg"
    image cg moon rika_3 = "cg/furude_no_rika_3.jpg"
    image cg hatred_satoko = "cg/just_die_already.jpg"

    image cg pat empty = "cg/satoko_br_1.jpg"
    image cg pat patting = "cg/satoko_br_2.jpg"
    image cg rika_warning = "cg/tokyo_e_kaette.jpg"
    image cg nata normal = "cg/nata_onna.jpg"
    image cg nata terror = "cg/nata_terror.jpg"
    image cg mion_eye = "cg/mii_chan.jpg"
    image bg kumasan = "cg/kuma_san.jpg"

    image cg eating_satoko = "cg/satoko_nom.jpg"
    image cg sweet_victory = "cg/glorious_triumph.jpg"
    image cg ningyo_rena = "cg/ningyo_rena.jpg"
    image cg omochikaeri = "cg/omochikaeri.jpg"
    image cg akasaka 1 = "cg/player_1.jpg"
    image cg akasaka 2 = "cg/player_2.jpg"
    image cg akasaka 3 = "cg/player_3.jpg"

    image cg renapan x1 = "cg/renapan_x1.jpg"
    image cg renapan x7 = "cg/renapan_x7.jpg"
    image cg renapan_rika x1 = "cg/renapan_rika_x1.jpg"
    image cg renapan_rika x7 = "cg/renapan_rika_x7.jpg"
    image cg usoda stare = "cg/usoda_1.jpg"
    image cg usoda closeup = "cg/usoda_3.jpg"
    image cg usoda shout = "cg/usoda_2.jpg"

    image cg interview 1 = "cg/thousand_yard_stare.jpg"
    image cg interview 2 = "efe/black.jpg"
    image cg trap_master 1 = "cg/homerun_1.jpg"
    image cg trap_master 2 = "cg/homerun_2.jpg"
    image cg basutei_girl 1 = "scenes/bg_046.jpg"
    image cg basutei_girl 2 = "efe/black.jpg"
    image cg basutei_girl 3 = "cg/shoujo_3.jpg"


    image rena si def_a1 = "characters/Rena/re_si_def_a1.png"
    image rena si bik_a1 = "characters/Rena/re_si_bik_a1.png"
    image rena si hau_a1 = "characters/Rena/re_si_hau_a1.png"
    image rena si hi_a1 = "characters/Rena/re_si_hi_a1.png"
    image rena si hii_a1 = "characters/Rena/re_si_hii_a1.png"
    image rena si hiwa_a1 = "characters/Rena/re_si_hiwa_a1.png"
    image rena si ka_a1 = "characters/Rena/re_si_ka_a1.png"
    image rena si ko_a1 = "characters/Rena/re_si_ko_a1.png"
    image rena si ko_a2 = "characters/Rena/re_si_ko_a2.png"
    image rena si nande_a1 = "characters/Rena/re_si_nande_a1.png"
    image rena si okoru_a1 = "characters/Rena/re_si_ok_a1.png"
    image rena si wa_a1 = "characters/Rena/re_si_wa_a1.png"

    image rena si def_b1 = "characters/Rena/re_si_def_b1.png"
    image rena si bik_b1 = "characters/Rena/re_si_bik_b1.png"
    image rena si hau_b1 = "characters/Rena/re_si_hau_b1.png"
    image rena si hi_b1 = "characters/Rena/re_si_hi_b1.png"
    image rena si hii_b1 = "characters/Rena/re_si_hii_b1.png"
    image rena si hiwa_b1 = "characters/Rena/re_si_hiwa_b1.png"
    image rena si ka_b1 = "characters/Rena/re_si_ka_b1.png"
    image rena si ko_b1 = "characters/Rena/re_si_ko_b1.png"
    image rena si ko_b2 = "characters/Rena/re_si_ko_b2.png"
    image rena si nande_b1 = "characters/Rena/re_si_nande_b1.png"
    image rena si okoru_b1 = "characters/Rena/re_si_ok_b1.png"
    image rena si wa_b1 = "characters/Rena/re_si_wa_b1.png"


    image rena se def_a1 = "characters/Rena/re_se_def_a1.png"
    image rena se bik_a1 = "characters/Rena/re_se_bik_a1.png"
    image rena se hau_a1 = "characters/Rena/re_se_hau_a1.png"
    image rena se hi_a1 = "characters/Rena/re_se_hi_a1.png"
    image rena se hii_a1 = "characters/Rena/re_se_hii_a1.png"
    image rena se hiwa_a1 = "characters/Rena/re_se_hiwa_a1.png"
    image rena se ka_a1 = "characters/Rena/re_se_ka_a1.png"
    image rena se ko_a1 = "characters/Rena/re_se_ko_a1.png"
    image rena se ko_a2 = "characters/Rena/re_se_ko_a2.png"
    image rena se nande_a1 = "characters/Rena/re_se_nande_a1.png"
    image rena se okoru_a1 = "characters/Rena/re_se_ok_a1.png"
    image rena se wa_a1 = "characters/Rena/re_se_wa_a1.png"

    image rena se def_b1 = "characters/Rena/re_se_def_b1.png"
    image rena se bik_b1 = "characters/Rena/re_se_bik_b1.png"
    image rena se hau_b1 = "characters/Rena/re_se_hau_b1.png"
    image rena se hi_b1 = "characters/Rena/re_se_hi_b1.png"
    image rena se hii_b1 = "characters/Rena/re_se_hii_b1.png"
    image rena se hiwa_b1 = "characters/Rena/re_se_hiwa_b1.png"
    image rena se ka_b1 = "characters/Rena/re_se_ka_b1.png"
    image rena se ko_b1 = "characters/Rena/re_se_ko_b1.png"
    image rena se ko_b2 = "characters/Rena/re_se_ko_b2.png"
    image rena se nande_b1 = "characters/Rena/re_se_nande_b1.png"
    image rena se okoru_b1 = "characters/Rena/re_se_ok_b1.png"
    image rena se wa_b1 = "characters/Rena/re_se_wa_b1.png"

    image rena ts def_a1 = "characters/Rena/re_ts_def_a1.png"
    image rena ts bik_a1 = "characters/Rena/re_ts_bik_a1.png"
    image rena ts hau_a1 = "characters/Rena/re_ts_hau_a1.png"
    image rena ts hi_a1 = "characters/Rena/re_ts_hi_a1.png"
    image rena ts hii_a1 = "characters/Rena/re_ts_hii_a1.png"
    image rena ts hiwa_a1 = "characters/Rena/re_ts_hiwa_a1.png"
    image rena ts ka_a1 = "characters/Rena/re_ts_ka_a1.png"
    image rena ts ko_a1 = "characters/Rena/re_ts_ko_a1.png"
    image rena ts ko_a2 = "characters/Rena/re_ts_ko_a2.png"
    image rena ts nande_a1 = "characters/Rena/re_ts_nande_a1.png"
    image rena ts okoru_a1 = "characters/Rena/re_ts_ok_a1.png"
    image rena ts wa_a1 = "characters/Rena/re_ts_wa_a1.png"

    image rena ts def_b1 = "characters/Rena/re_ts_def_b1.png"
    image rena ts bik_b1 = "characters/Rena/re_ts_bik_b1.png"
    image rena ts hau_b1 = "characters/Rena/re_ts_hau_b1.png"
    image rena ts hi_b1 = "characters/Rena/re_ts_hi_b1.png"
    image rena ts hii_b1 = "characters/Rena/re_ts_hii_b1.png"
    image rena ts hiwa_b1 = "characters/Rena/re_ts_hiwa_b1.png"
    image rena ts ka_b1 = "characters/Rena/re_ts_ka_b1.png"
    image rena ts ko_b1 = "characters/Rena/re_ts_ko_b1.png"
    image rena ts ko_b2 = "characters/Rena/re_ts_ko_b2.png"
    image rena ts nande_b1 = "characters/Rena/re_ts_nande_b1.png"
    image rena ts okoru_b1 = "characters/Rena/re_ts_ok_b1.png"
    image rena ts wa_b1 = "characters/Rena/re_ts_wa_b1.png"
    image rena_eye = "characters/Rena/rena_eye.png"


    image mion ts aku_a1 = "characters/Mion/me_ts_aku_a1.png"
    image mion ts def_a1 = "characters/Mion/me_ts_def_a1.png"
    image mion ts fu_a1 = "characters/Mion/me_ts_fu_a1.png"
    image mion ts hau_a1 = "characters/Mion/me_ts_hau_a1.png"
    image mion ts hi_a1 = "characters/Mion/me_ts_hi_a1.png"
    image mion ts ika_a1 = "characters/Mion/me_ts_ika_a1.png"
    image mion ts maji_a1 = "characters/Mion/me_ts_maji_a1.png"
    image mion ts bik_a1 = "characters/Mion/me_ts_bik_a1.png"
    image mion ts sin_a1 = "characters/Mion/me_ts_sin_a1.png"
    image mion ts tk_a1 = "characters/Mion/me_ts_tk_a1.png"
    image mion ts to_a1 = "characters/Mion/me_ts_to_a1.png"
    image mion ts wa_a1 = "characters/Mion/me_ts_wa_a1.png"
    image mion ts wink_a1 = "characters/Mion/me_ts_wink_a1.png"
    image mion ts yo_a1 = "characters/Mion/me_ts_yo_a1.png"

    image mion ts aku_a2 = "characters/Mion/me_ts_aku_a2.png"
    image mion ts def_a2 = "characters/Mion/me_ts_def_a2.png"
    image mion ts fu_a2 = "characters/Mion/me_ts_fu_a2.png"
    image mion ts hau_a2 = "characters/Mion/me_ts_hau_a2.png"
    image mion ts hi_a2 = "characters/Mion/me_ts_hi_a2.png"
    image mion ts ika_a2 = "characters/Mion/me_ts_ika_a2.png"
    image mion ts maji_a2 = "characters/Mion/me_ts_maji_a2.png"
    image mion ts bik_a2 = "characters/Mion/me_ts_bik_a2.png"
    image mion ts sin_a2 = "characters/Mion/me_ts_sin_a2.png"
    image mion ts tk_a2 = "characters/Mion/me_ts_tk_a2.png"
    image mion ts to_a2 = "characters/Mion/me_ts_to_a2.png"
    image mion ts wa_a2 = "characters/Mion/me_ts_wa_a2.png"
    image mion ts wink_a2 = "characters/Mion/me_ts_wink_a2.png"
    image mion ts yo_a2 = "characters/Mion/me_ts_yo_a2.png"

    image mion si aku_a1 = "characters/Mion/me_si_aku_a1.png"
    image mion si def_a1 = "characters/Mion/me_si_def_a1.png"
    image mion si fu_a1 = "characters/Mion/me_si_fu_a1.png"
    image mion si hau_a1 = "characters/Mion/me_si_hau_a1.png"
    image mion si hi_a1 = "characters/Mion/me_si_hi_a1.png"
    image mion si ika_a1 = "characters/Mion/me_si_ika_a1.png"
    image mion si maji_a1 = "characters/Mion/me_si_maji_a1.png"
    image mion si bik_a1 = "characters/Mion/me_si_bik_a1.png"
    image mion si sin_a1 = "characters/Mion/me_si_sin_a1.png"
    image mion si tk_a1 = "characters/Mion/me_si_tk_a1.png"
    image mion si to_a1 = "characters/Mion/me_si_to_a1.png"
    image mion si wa_a1 = "characters/Mion/me_si_wa_a1.png"
    image mion si wink_a1 = "characters/Mion/me_si_wink_a1.png"
    image mion si yo_a1 = "characters/Mion/me_si_yo_a1.png"

    image mion si aku_a2 = "characters/Mion/me_si_aku_a2.png"
    image mion si def_a2 = "characters/Mion/me_si_def_a2.png"
    image mion si fu_a2 = "characters/Mion/me_si_fu_a2.png"
    image mion si hau_a2 = "characters/Mion/me_si_hau_a2.png"
    image mion si hi_a2 = "characters/Mion/me_si_hi_a2.png"
    image mion si ika_a2 = "characters/Mion/me_si_ika_a2.png"
    image mion si maji_a2 = "characters/Mion/me_si_maji_a2.png"
    image mion si bik_a2 = "characters/Mion/me_si_bik_a2.png"
    image mion si sin_a2 = "characters/Mion/me_si_sin_a2.png"
    image mion si tk_a2 = "characters/Mion/me_si_tk_a2.png"
    image mion si to_a2 = "characters/Mion/me_si_to_a2.png"
    image mion si wa_a2 = "characters/Mion/me_si_wa_a2.png"
    image mion si wink_a2 = "characters/Mion/me_si_wink_a2.png"
    image mion si yo_a2 = "characters/Mion/me_si_yo_a2.png"

    image mion se aku_a1 = "characters/Mion/me_se_aku_a1.png"
    image mion se def_a1 = "characters/Mion/me_se_def_a1.png"
    image mion se fu_a1 = "characters/Mion/me_se_fu_a1.png"
    image mion se hau_a1 = "characters/Mion/me_se_hau_a1.png"
    image mion se hi_a1 = "characters/Mion/me_se_hi_a1.png"
    image mion se ika_a1 = "characters/Mion/me_se_ika_a1.png"
    image mion se maji_a1 = "characters/Mion/me_se_maji_a1.png"
    image mion se bik_a1 = "characters/Mion/me_se_bik_a1.png"
    image mion se sin_a1 = "characters/Mion/me_se_sin_a1.png"
    image mion se tk_a1 = "characters/Mion/me_se_tk_a1.png"
    image mion se to_a1 = "characters/Mion/me_se_to_a1.png"
    image mion se wa_a1 = "characters/Mion/me_se_wa_a1.png"
    image mion se wink_a1 = "characters/Mion/me_se_wink_a1.png"
    image mion se yo_a1 = "characters/Mion/me_se_yo_a1.png"

    image mion se aku_b1 = "characters/Mion/me_se_aku_b1.png"
    image mion se def_b1 = "characters/Mion/me_se_def_b1.png"
    image mion se fu_b1 = "characters/Mion/me_se_fu_b1.png"
    image mion se hau_b1 = "characters/Mion/me_se_hau_b1.png"
    image mion se hi_b1 = "characters/Mion/me_se_hi_b1.png"
    image mion se ika_b1 = "characters/Mion/me_se_ika_b1.png"
    image mion se maji_b1 = "characters/Mion/me_se_maji_b1.png"
    image mion se bik_b1 = "characters/Mion/me_se_bik_b1.png"
    image mion se sin_b1 = "characters/Mion/me_se_sin_b1.png"
    image mion se tk_b1 = "characters/Mion/me_se_tk_b1.png"
    image mion se to_b1 = "characters/Mion/me_se_to_b1.png"
    image mion se wa_b1 = "characters/Mion/me_se_wa_b1.png"
    image mion se wink_b1 = "characters/Mion/me_se_wink_b1.png"
    image mion se yo_b1 = "characters/Mion/me_se_yo_b1.png"

    image mion se aku_a2 = "characters/Mion/me_se_aku_a2.png"
    image mion se def_a2 = "characters/Mion/me_se_def_a2.png"
    image mion se fu_a2 = "characters/Mion/me_se_fu_a2.png"
    image mion se hau_a2 = "characters/Mion/me_se_hau_a2.png"
    image mion se hi_a2 = "characters/Mion/me_se_hi_a2.png"
    image mion se ika_a2 = "characters/Mion/me_se_ika_a2.png"
    image mion se maji_a2 = "characters/Mion/me_se_maji_a2.png"
    image mion se bik_a2 = "characters/Mion/me_se_bik_a2.png"
    image mion se sin_a2 = "characters/Mion/me_se_sin_a2.png"
    image mion se tk_a2 = "characters/Mion/me_se_tk_a2.png"
    image mion se to_a2 = "characters/Mion/me_se_to_a2.png"
    image mion se wa_a2 = "characters/Mion/me_se_wa_a2.png"
    image mion se wink_a2 = "characters/Mion/me_se_wink_a2.png"
    image mion se yo_a2 = "characters/Mion/me_se_yo_a2.png"

    image mion se aku_b2 = "characters/Mion/me_se_aku_b2.png"
    image mion se def_b2 = "characters/Mion/me_se_def_b2.png"
    image mion se fu_b2 = "characters/Mion/me_se_fu_b2.png"
    image mion se hau_b2 = "characters/Mion/me_se_hau_b2.png"
    image mion se hi_b2 = "characters/Mion/me_se_hi_b2.png"
    image mion se ika_b2 = "characters/Mion/me_se_ika_b2.png"
    image mion se maji_b2 = "characters/Mion/me_se_maji_b2.png"
    image mion se bik_b2 = "characters/Mion/me_se_bik_b2.png"
    image mion se sin_b2 = "characters/Mion/me_se_sin_b2.png"
    image mion se tk_b2 = "characters/Mion/me_se_tk_b2.png"
    image mion se to_b2 = "characters/Mion/me_se_to_b2.png"
    image mion se wa_b2 = "characters/Mion/me_se_wa_b2.png"
    image mion se wink_b2 = "characters/Mion/me_se_wink_b2.png"
    image mion se yo_b2 = "characters/Mion/me_se_yo_b2.png"

    image mion ki aku_a1 = "characters/Mion/me_si_aku_a1.png"
    image mion ki def_a1 = "characters/Mion/me_si_def_a1.png"
    image mion ki fu_a1 = "characters/Mion/me_si_fu_a1.png"
    image mion ki hau_a1 = "characters/Mion/me_si_hau_a1.png"
    image mion ki hi_a1 = "characters/Mion/me_si_hi_a1.png"
    image mion ki ika_a1 = "characters/Mion/me_si_ika_a1.png"
    image mion ki maji_a1 = "characters/Mion/me_si_maji_a1.png"
    image mion ki bik_a1 = "characters/Mion/me_si_bik_a1.png"
    image mion ki sin_a1 = "characters/Mion/me_si_sin_a1.png"
    image mion ki tk_a1 = "characters/Mion/me_si_tk_a1.png"
    image mion ki to_a1 = "characters/Mion/me_si_to_a1.png"
    image mion ki wa_a1 = "characters/Mion/me_si_wa_a1.png"
    image mion ki wink_a1 = "characters/Mion/me_si_wink_a1.png"
    image mion ki yo_a1 = "characters/Mion/me_si_yo_a1.png"

    image mion ki aku_a2 = "characters/Mion/me_si_aku_a2.png"
    image mion ki def_a2 = "characters/Mion/me_si_def_a2.png"
    image mion ki fu_a2 = "characters/Mion/me_si_fu_a2.png"
    image mion ki hau_a2 = "characters/Mion/me_si_hau_a2.png"
    image mion ki hi_a2 = "characters/Mion/me_si_hi_a2.png"
    image mion ki ika_a2 = "characters/Mion/me_si_ika_a2.png"
    image mion ki maji_a2 = "characters/Mion/me_si_maji_a2.png"
    image mion ki bik_a2 = "characters/Mion/me_si_bik_a2.png"
    image mion ki sin_a2 = "characters/Mion/me_si_sin_a2.png"
    image mion ki tk_a2 = "characters/Mion/me_si_tk_a2.png"
    image mion ki to_a2 = "characters/Mion/me_si_to_a2.png"
    image mion ki wa_a2 = "characters/Mion/me_si_wa_a2.png"
    image mion ki wink_a2 = "characters/Mion/me_si_wink_a2.png"
    image mion ki yo_a2 = "characters/Mion/me_si_yo_a2.png"

    image mion mi aku_a1 = "characters/Mion/me_mi_aku_a1.png"
    image mion mi def_a1 = "characters/Mion/me_mi_def_a1.png"
    image mion mi fu_a1 = "characters/Mion/me_mi_fu_a1.png"
    image mion mi tk_a1 = "characters/Mion/me_mi_tk_a1.png"
    image mion mi to_a1 = "characters/Mion/me_mi_to_a1.png"
    image mion mi wa_a1 = "characters/Mion/me_mi_wa_a1.png"
    image mion mi wink_a1 = "characters/Mion/me_mi_wink_a1.png"

    image mion mi aku_a2 = "characters/Mion/me_mi_aku_a2.png"
    image mion mi def_a2 = "characters/Mion/me_mi_def_a2.png"
    image mion mi fu_a2 = "characters/Mion/me_mi_fu_a2.png"
    image mion mi tk_a2 = "characters/Mion/me_mi_tk_a2.png"
    image mion mi to_a2 = "characters/Mion/me_mi_to_a2.png"
    image mion mi wa_a2 = "characters/Mion/me_mi_wa_a2.png"
    image mion mi wink_a2 = "characters/Mion/me_mi_wink_a2.png"

    image mion_eye = "characters/Mion/mion_eye.png"
    image mion_hey = "characters/Mion/mion_eye_higurasi.png"


    image satoko se aki_a1 = "characters/Satoko/sa_se_aki_a1.png"
    image satoko se aku_a1 = "characters/Satoko/sa_se_aku_a1.png"
    image satoko se sakebu_a1 = "characters/Satoko/sa_se_br_a1.png"
    image satoko se def_a1 = "characters/Satoko/sa_se_def_a1.png"
    image satoko se hau_a1 = "characters/Satoko/sa_se_ha_a1.png"
    image satoko se hau_a2 = "characters/Satoko/sa_se_ha_a2.png"
    image satoko se hn_a1 = "characters/Satoko/sa_se_hn_a1.png"
    image satoko se hn_a2 = "characters/Satoko/sa_se_hn_a2.png"
    image satoko se mu_a1 = "characters/Satoko/sa_se_mu_a1.png"
    image satoko se mu_a2 = "characters/Satoko/sa_se_mu_a2.png"
    image satoko se na_a1 = "characters/Satoko/sa_se_na_a1.png"
    image satoko se bik_a1 = "characters/Satoko/sa_se_bik_a1.png"
    image satoko se wa_a1 = "characters/Satoko/sa_se_wa_a1.png"
    image satoko se yare_a1 = "characters/Satoko/sa_se_yare_a1.png"
    image satoko se yare_a2 = "characters/Satoko/sa_se_yare_a2.png"

    image satoko se aki_b1 = "characters/Satoko/sa_se_aki_b1.png"
    image satoko se aku_b1 = "characters/Satoko/sa_se_aku_b1.png"
    image satoko se sakebu_b1 = "characters/Satoko/sa_se_br_b1.png"
    image satoko se def_b1 = "characters/Satoko/sa_se_def_b1.png"
    image satoko se hau_b1 = "characters/Satoko/sa_se_ha_b1.png"
    image satoko se hau_b2 = "characters/Satoko/sa_se_ha_b2.png"
    image satoko se hn_b1 = "characters/Satoko/sa_se_hn_b1.png"
    image satoko se hn_b2 = "characters/Satoko/sa_se_hn_b2.png"
    image satoko se hn_b3 = "characters/Satoko/sa_se_hn_b3.png"
    image satoko se mu_b1 = "characters/Satoko/sa_se_mu_b1.png"
    image satoko se mu_b2 = "characters/Satoko/sa_se_mu_b2.png"
    image satoko se na_b1 = "characters/Satoko/sa_se_na_b1.png"
    image satoko se na_b2 = "characters/Satoko/sa_se_na_b2.png"
    image satoko se bik_b1 = "characters/Satoko/sa_se_bik_b1.png"
    image satoko se bik_b2 = "characters/Satoko/sa_se_bik_b2.png"
    image satoko se wa_b1 = "characters/Satoko/sa_se_wa_b1.png"
    image satoko se yare_b1 = "characters/Satoko/sa_se_yare_b1.png"
    image satoko se yare_b2 = "characters/Satoko/sa_se_yare_b2.png"

    image satoko ku aki_a1 = "characters/Satoko/sa_ku_aki_a1.png"
    image satoko ku aku_a1 = "characters/Satoko/sa_ku_aku_a1.png"
    image satoko ku def_a1 = "characters/Satoko/sa_ku_def_a1.png"
    image satoko ku hau_a1 = "characters/Satoko/sa_ku_ha_a1.png"
    image satoko ku hn_a1 = "characters/Satoko/sa_ku_hn_a1.png"
    image satoko ku na_a1 = "characters/Satoko/sa_ku_na_a1.png"
    image satoko ku bik_a1 = "characters/Satoko/sa_ku_bik_a1.png"
    image satoko ku wa_a1 = "characters/Satoko/sa_ku_wa_a1.png"

    image satoko ts aki_a1 = "characters/Satoko/sa_ts_aki_a1.png"
    image satoko ts aku_a1 = "characters/Satoko/sa_ts_aku_a1.png"
    image satoko ts def_a1 = "characters/Satoko/sa_ts_def_a1.png"
    image satoko ts hau_a1 = "characters/Satoko/sa_ts_ha_a1.png"
    image satoko ts hn_a1 = "characters/Satoko/sa_ts_hn_a1.png"
    image satoko ts na_a1 = "characters/Satoko/sa_ts_na_a1.png"
    image satoko ts bik_a1 = "characters/Satoko/sa_ts_bik_a1.png"
    image satoko ts wa_a1 = "characters/Satoko/sa_ts_wa_a1.png"
    image satoko ts yare_a1 = "characters/Satoko/sa_ts_yare_a1.png"

    image satoko ta aki_a1 = "characters/Satoko/sa_to_aki_a1.png"
    image satoko ta sakebu_a1 = "characters/Satoko/sa_to_br_a1.png"
    image satoko ta hau_a1 = "characters/Satoko/sa_to_ha_a1.png"
    image satoko ta hau_a1 = "characters/Satoko/sa_to_ha_a2.png"
    image satoko ta hn_a1 = "characters/Satoko/sa_to_hn_a1.png"
    image satoko ta hn_a1 = "characters/Satoko/sa_to_hn_a2.png"
    image satoko ta mu_a1 = "characters/Satoko/sa_to_mu_a1.png"
    image satoko ta mu_a2 = "characters/Satoko/sa_to_mu_a2.png"
    image satoko ta bik_a1 = "characters/Satoko/sa_to_bik_a1.png"
    image satoko ta wa_a1 = "characters/Satoko/sa_to_wa_a1.png"
    image satoko ta yare_a1 = "characters/Satoko/sa_to_yare_a1.png"
    image satoko ta yare_a2 = "characters/Satoko/sa_to_yare_a2.png"

    image satoko si aki_a1 = "characters/Satoko/sa_si_aki_a1.png"
    image satoko si aku_a1 = "characters/Satoko/sa_si_aku_a1.png"
    image satoko si sakebu_a1 = "characters/Satoko/sa_si_br_a1.png"
    image satoko si def_a1 = "characters/Satoko/sa_si_def_a1.png"
    image satoko si hau_a1 = "characters/Satoko/sa_si_ha_a1.png"
    image satoko si hau_a2 = "characters/Satoko/sa_si_ha_a2.png"
    image satoko si hn_a1 = "characters/Satoko/sa_si_hn_a1.png"
    image satoko si hn_a2 = "characters/Satoko/sa_si_hn_a2.png"
    image satoko si mu_a1 = "characters/Satoko/sa_si_mu_a1.png"
    image satoko si mu_a2 = "characters/Satoko/sa_si_mu_a2.png"
    image satoko si na_a1 = "characters/Satoko/sa_si_na_a1.png"
    image satoko si bik_a1 = "characters/Satoko/sa_si_bik_a1.png"
    image satoko si wa_a1 = "characters/Satoko/sa_si_wa_a1.png"
    image satoko si yare_a1 = "characters/Satoko/sa_si_yare_a1.png"
    image satoko si yare_a2 = "characters/Satoko/sa_si_yare_a2.png"

    image satoko si aki_b1 = "characters/Satoko/sa_si_aki_b1.png"
    image satoko si aku_b1 = "characters/Satoko/sa_si_aku_b1.png"
    image satoko si sakebu_b1 = "characters/Satoko/sa_si_br_b1.png"
    image satoko si def_b1 = "characters/Satoko/sa_si_def_b1.png"
    image satoko si hau_b1 = "characters/Satoko/sa_si_ha_b1.png"
    image satoko si hau_b2 = "characters/Satoko/sa_si_ha_b2.png"
    image satoko si hn_b1 = "characters/Satoko/sa_si_hn_b1.png"
    image satoko si hn_b2 = "characters/Satoko/sa_si_hn_b2.png"
    image satoko si mu_b1 = "characters/Satoko/sa_si_mu_b1.png"
    image satoko si mu_b2 = "characters/Satoko/sa_si_mu_b2.png"
    image satoko si na_b1 = "characters/Satoko/sa_si_na_b1.png"
    image satoko si bik_b1 = "characters/Satoko/sa_si_bik_b1.png"
    image satoko si wa_b1 = "characters/Satoko/sa_si_wa_b1.png"
    image satoko si yare_b1 = "characters/Satoko/sa_si_yare_b1.png"
    image satoko si yare_b2 = "characters/Satoko/sa_si_yare_b2.png"

    image satoko_eye = "characters/Satoko/satoko_eye.png"


    image shion ma aku_a1 = "characters/Shion/si_ma_aku_a1.png"
    image shion ma def_a1 = "characters/Shion/si_ma_def_a1.png"
    image shion ma fu_a1 = "characters/Shion/si_ma_fu_a1.png"
    image shion ma hau_a1 = "characters/Shion/si_ma_hau_a1.png"
    image shion ma ika_a1 = "characters/Shion/si_ma_ika_a1.png"
    image shion ma maji_a1 = "characters/Shion/si_ma_maji_a1.png"
    image shion ma bik_a1 = "characters/Shion/si_ma_bik_a1.png"
    image shion ma tk_a1 = "characters/Shion/si_ma_tk_a1.png"
    image shion ma to_a1 = "characters/Shion/si_ma_to_a1.png"
    image shion ma wa_a1 = "characters/Shion/si_ma_wa_a1.png"
    image shion ma wink_a1 = "characters/Shion/si_ma_wink_a1.png"
    image shion ma yo_a1 = "characters/Shion/si_ma_yo_a1.png"

    image shion si aku_a1 = "characters/Shion/si_si_aku_a1.png"
    image shion si def_a1 = "characters/Shion/si_si_def_a1.png"
    image shion si fu_a1 = "characters/Shion/si_si_fu_a1.png"
    image shion si hau_a1 = "characters/Shion/si_si_hau_a1.png"
    image shion si ika_a1 = "characters/Shion/si_si_ika_a1.png"
    image shion si maji_a1 = "characters/Shion/si_si_maji_a1.png"
    image shion si bik_a1 = "characters/Shion/si_si_bik_a1.png"
    image shion si tk_a1 = "characters/Shion/si_si_tk_a1.png"
    image shion si to_a1 = "characters/Shion/si_si_to_a1.png"
    image shion si wa_a1 = "characters/Shion/si_si_wa_a1.png"
    image shion si wink_a1 = "characters/Shion/si_si_wink_a1.png"
    image shion si yo_a1 = "characters/Shion/si_si_yo_a1.png"

    image shion si aku_b1 = "characters/Shion/si_si_aku_b1.png"
    image shion si def_b1 = "characters/Shion/si_si_def_b1.png"
    image shion si fu_b1 = "characters/Shion/si_si_fu_b1.png"
    image shion si hau_b1 = "characters/Shion/si_si_hau_b1.png"
    image shion si ika_b1 = "characters/Shion/si_si_ika_b1.png"
    image shion si maji_b1 = "characters/Shion/si_si_maji_b1.png"
    image shion si bik_b1 = "characters/Shion/si_si_bik_b1.png"
    image shion si tk_b1 = "characters/Shion/si_si_tk_b1.png"
    image shion si to_b1 = "characters/Shion/si_si_to_b1.png"
    image shion si wa_b1 = "characters/Shion/si_si_wa_b1.png"
    image shion si wink_b1 = "characters/Shion/si_si_wink_b1.png"
    image shion si yo_b1 = "characters/Shion/si_si_yo_b1.png"


    image rika se de_a1 = "characters/Rika/ri_se_de_a1.png"
    image rika se fu_a1 = "characters/Rika/ri_se_fu_a1.png"
    image rika se ko_a1 = "characters/Rika/ri_se_ko_a1.png"
    image rika se ko_a2 = "characters/Rika/ri_se_ko_a2.png"
    image rika se ni_a1 = "characters/Rika/ri_se_ni_a1.png"
    image rika se nk_a1 = "characters/Rika/ri_se_nk_a1.png"
    image rika se wa_a1 = "characters/Rika/ri_se_nipa_a1.png"

    image rika si de_a1 = "characters/Rika/ri_si_de_a1.png"
    image rika si fu_a1 = "characters/Rika/ri_si_fu_a1.png"
    image rika si ko_a1 = "characters/Rika/ri_si_ko_a1.png"
    image rika si ko_a2 = "characters/Rika/ri_si_ko_a2.png"
    image rika si ni_a1 = "characters/Rika/ri_si_ni_a1.png"
    image rika si nk_a1 = "characters/Rika/ri_si_nk_a1.png"
    image rika si wa_a1 = "characters/Rika/ri_si_nipa_a1.png"

    image rika ts de_a1 = "characters/Rika/ri_ts_de_a1.png"
    image rika ts ko_a1 = "characters/Rika/ri_ts_ko_a1.png"
    image rika ts ni_a1 = "characters/Rika/ri_ts_ni_a1.png"
    image rika ts wa_a1 = "characters/Rika/ri_ts_nipa_a1.png"

    image rika neko de_a1 = "characters/Rika/ri_neko_de_a1.png"
    image rika neko ko_a1 = "characters/Rika/ri_neko_ko_a1.png"
    image rika neko ni_a1 = "characters/Rika/ri_neko_ni_a1.png"
    image rika neko wa_a1 = "characters/Rika/ri_neko_nipa_a1.png"

    image rika miko de_a1 = "characters/Rika/ri_miko_de_a1.png"
    image rika miko ko_a1 = "characters/Rika/ri_miko_ko_a1.png"
    image rika miko ni_a1 = "characters/Rika/ri_miko_ni_a1.png"
    image rika miko wa_a1 = "characters/Rika/ri_miko_nipa_a1.png"

    image rika hima de_a1 = "characters/Rika/ri_si_de_a1.png"
    image rika hima fu_a1 = "characters/Rika/ri_si_fu_a1.png"
    image rika hima ko_a1 = "characters/Rika/ri_si_ko_a1.png"
    image rika hima ko_a2 = "characters/Rika/ri_si_ko_a2.png"
    image rika hima ni_a1 = "characters/Rika/ri_si_ni_a1.png"
    image rika hima nk_a1 = "characters/Rika/ri_si_nk_a1.png"
    image rika hima wa_a1 = "characters/Rika/ri_si_nipa_a1.png"

    image rika_eyes = "characters/Rika/rika_eyes.png"


    image ooishi si aku_a1 = "characters/Ooishi/oi_si_aku_a1.png"
    image ooishi si def_a1 = "characters/Ooishi/oi_si_def_a1.png"
    image ooishi si def_a2 = "characters/Ooishi/oi_si_def_a2.png"
    image ooishi si maji_a1 = "characters/Ooishi/oi_si_maji_a1.png"
    image ooishi si wa_a1 = "characters/Ooishi/oi_si_wa_a1.png"
    image ooishi yukata aku_a1 = "characters/Ooishi/oi_yk_aku_a1.png"
    image ooishi yukata def_a1 = "characters/Ooishi/oi_yk_def_a1.png"
    image ooishi yukata def_a2 = "characters/Ooishi/oi_yk_def_a2.png"
    image ooishi yukata maji_a1 = "characters/Ooishi/oi_yk_maji_a1.png"
    image ooishi yukata wa_a1 = "characters/Ooishi/oi_yk_wa_a1.png"
    image ooishi_stare = "characters/Ooishi/oisi_stare.png"

    image irie doc def_a1 = "characters/Irie/ir_doc_de_a1.png"
    image irie doc def_a2 = "characters/Irie/ir_doc_de_a2.png"
    image irie doc maji_a1 = "characters/Irie/ir_doc_maji_a1.png"
    image irie doc maji_a2 = "characters/Irie/ir_doc_maji_a2.png"
    image irie doc warai = "characters/Irie/ir_doc_warai.png"

    image irie yk def_a1 = "characters/Irie/ir_kyu_de_a1.png"
    image irie yk def_a2 = "characters/Irie/ir_kyu_de_a2.png"
    image irie yk maji_a1 = "characters/Irie/ir_kyu_maji_a1.png"
    image irie yk maji_a2 = "characters/Irie/ir_kyu_maji_a2.png"
    image irie yk warai = "characters/Irie/ir_kyu_warai.png"

    image irie si def_a1 = "characters/Irie/ir_si_de_a1.png"
    image irie si def_a2 = "characters/Irie/ir_si_de_a2.png"
    image irie si maji_a1 = "characters/Irie/ir_si_maji_a1.png"
    image irie si maji_a2 = "characters/Irie/ir_si_maji_a2.png"
    image irie si warai = "characters/Irie/ir_si_warai.png"

    image irie_lens = "characters/Irie/irie_lens.png"


    image chie si_def = "characters/sonota/sensei_1.png"
    image chie si_maji = "characters/sonota/sensei_2.png"
    image chie si_ko = "characters/sonota/sensei_3.png"


    image takano si_def = "characters/sonota/taka_def.png"
    image takano si_fu = "characters/sonota/taka_fu.png"
    image takano si_wa = "characters/sonota/taka_wa.png"


    image tomi si_def = "characters/sonota/tomi_def.png"
    image tomi si_uh = "characters/sonota/tomi_uh.png"
    image tomi si_wa = "characters/sonota/tomi_wa.png"


    image kuma si_def = "characters/sonota/kuma_def.png"
    image kuma si_uh = "characters/sonota/kuma_uh.png"
    image kuma si_wa = "characters/sonota/kuma_wa.png"





    define wa_001 = "sound/Chaimu.ogg"
    define wa_002 = "sound/Down.ogg"
    define wa_003 = "sound/Down2.ogg"
    define wa_004 = "sound/Down3.ogg"
    define wa_005 = "sound/Dageki.ogg"
    define wa_006 = "sound/Daidageki.ogg"
    define wa_007 = "sound/Finish.ogg"
    define wa_008 = "sound/wa_008.ogg"
    define wa_009 = "sound/GARASU.ogg"
    define wa_010 = "sound/Kyupirn.ogg"

    define wa_011 = "sound/Kira.ogg"
    define wa_012 = "sound/Hikaru.ogg"
    define wa_013 = "sound/Kamera.ogg"
    define wa_014 = "sound/Koruku.ogg"
    define wa_015 = "sound/Nageru.ogg"
    define wa_016 = "sound/Pou.ogg"
    define wa_017 = "sound/Tataku.ogg"
    define wa_018 = "sound/Tatakiwaru.ogg"
    define wa_019 = "sound/Waru.ogg"
    define wa_020 = "sound/Door.ogg"

    define wa_021 = "sound/Kami.ogg"
    define wa_022 = "sound/IWAKANNNOHATUGA.ogg"
    define wa_023 = "sound/HIMERARETAKYOUSOU.ogg"
    define wa_024 = "sound/JAKINIMITITAHAIKYO.ogg"
    define wa_025 = "sound/JIKUUNOSAKEME.ogg"
    define wa_026 = "sound/KIRINOMEIKYUU.ogg"
    define wa_027 = "sound/SINZOUAPPAKU.ogg"
    define wa_028 = "sound/Interfon.ogg"
    define wa_029 = "sound/Boyoon.ogg"
    define wa_030 = "sound/Thisikuki.ogg"

    define wa_031 = "sound/Kaze.ogg"
    define wa_032 = "sound/Kaminari1.ogg"
    define wa_033 = "sound/Kaminari2.ogg"
    define wa_034 = "sound/Taitoru.ogg"
    define wa_035 = "sound/Sizuku.ogg"
    define wa_036 = "sound/A6.ogg"
    define wa_037 = "sound/SE194.ogg"
    define wa_038 = "sound/SE137.ogg"
    define wa_039 = "sound/SE149.ogg"
    define wa_040 = "sound/SE068.ogg"

    define wa_041 = "sound/SE051.ogg"
    define wa_042 = "sound/Anahori.ogg"
    define wa_043 = "sound/A5_13391.ogg"
    define wa_044 = "sound/Suzu_1.ogg"
    define wa_045 = "sound/BELL.ogg"
    define wa_046 = "sound/MC071.ogg"
    define wa_047 = "sound/FINAL.ogg"

    define lovely_laugh = "sound/lovely_laugh.ogg"
    define usoda = "sound/usoda_loud.ogg"
    define gomenasai_sd = "sound/gomenasai.ogg"
    define loud_laughter = "sound/lovely_laugh_loud.ogg"
    define loud_crying = "sound/lovely_laugh_cry.ogg"
    define sobbing = "sound/sobbing.ogg"
    define kukekekeke = "sound/kuKEKEKEKEKEKEKE.ogg"
    define oni_laugh = "sound/devilish_laugh.ogg"
    define bakana_yatsu = "sound/bakana_yatsu.ogg"

    define oni001 = "sound/oni001.ogg"
    define oni002 = "sound/oni002.ogg"
    define oni003 = "sound/oni003.ogg"
    define oni004 = "sound/oni004.ogg"
    define oni005 = "sound/oni005.ogg"
    define oni006 = "sound/oni006.ogg"
    define oni007 = "sound/oni007.ogg"

    define wata001 = "sound/wata001.ogg"
    define wata002 = "sound/wata002.ogg"
    define wata003 = "sound/wata003.ogg"
    define wata004 = "sound/wata004.ogg"
    define wata005 = "sound/wata005.ogg"
    define wata006 = "sound/wata006.ogg"
    define wata007 = "sound/wata007.ogg"

    define tata001 = "sound/tata001.ogg"
    define tata002 = "sound/tata002.ogg"
    define tata003 = "sound/tata003.ogg"
    define tata004 = "sound/tata004.ogg"
    define tata005 = "sound/tata005.ogg"
    define tata006 = "sound/tata006.ogg"
    define tata007 = "sound/tata007.ogg"

    define hima001 = "sound/hima001.ogg"
    define hima002 = "sound/hima002.ogg"
    define hima003 = "sound/hima003.ogg"
    define hima004 = "sound/hima004.ogg"
    define hima005 = "sound/hima005.ogg"
    define hima006 = "sound/hima006.ogg"
    define hima007 = "sound/hima007.ogg"

    define lsys11 = "sound/ambient/Higurasi.ogg"
    define lsys12 = "sound/ambient/Semi.ogg"
    define lsys13 = "sound/ambient/Yoru.ogg"
    define lsys15 = "sound/ambient/Semi_R.ogg"
    define lsys17 = "sound/ambient/Denwa.ogg"
    define lsys18 = "sound/ambient/Suzu.ogg"
    define lsys19 = "sound/ambient/Kawa.ogg"
    define lsys20 = "sound/ambient/Mati.ogg"
    define lsys21 = "sound/ambient/Densya.ogg"
    define lsys22 = "sound/ambient/Suzume.ogg"

    define lsys23 = "sound/ambient/Ame.ogg"
    define lsys24 = "sound/ambient/Taip.ogg"
    define lsys25 = "sound/ambient/Kaze.ogg"
    define lsys26 = "sound/ambient/Futousurunabe.ogg"
    define lsys27 = "sound/ambient/Honou.ogg"
    define lsys28 = "sound/ambient/LOOP131.ogg"





    image bg 000 = "scenes/bg_000.jpg"
    image bg 001 = "scenes/bg_001.jpg"
    image bg 002 = "scenes/bg_002.jpg"
    image bg 003 = "scenes/bg_003.jpg"
    image bg 004 = "scenes/bg_004.jpg"
    image bg 005 = "scenes/bg_005.jpg"
    image bg 006 = "scenes/bg_006.jpg"
    image bg 007 = "scenes/bg_007.jpg"
    image bg 008 = "scenes/bg_008.jpg"
    image bg 009 = "scenes/bg_009.jpg"

    image bg 010 = "scenes/bg_010.jpg"
    image bg 011 = "scenes/bg_011.jpg"
    image bg 012 = "scenes/bg_012.jpg"
    image bg 013 = "scenes/bg_013.jpg"
    image bg 014 = "scenes/bg_014.jpg"
    image bg 015 = "scenes/bg_015.jpg"
    image bg 016 = "scenes/bg_016.jpg"
    image bg 017 = "scenes/bg_017.jpg"
    image bg 018 = "scenes/bg_018.jpg"
    image bg 019 = "scenes/bg_019.jpg"

    image bg 020 = "scenes/bg_020.jpg"
    image bg 021 = "scenes/bg_021.jpg"
    image bg 022 = "scenes/bg_022.jpg"
    image bg 023 = "scenes/bg_023.jpg"
    image bg 024 = "scenes/bg_024.jpg"
    image bg 025 = "scenes/bg_025.jpg"
    image bg 026 = "scenes/bg_026.jpg"
    image bg 027 = "scenes/bg_027.jpg"
    image bg 028 = "scenes/bg_028.jpg"
    image bg 029 = "scenes/bg_029.jpg"

    image bg 030 = "scenes/bg_030.jpg"
    image bg 031 = "scenes/bg_031.jpg"
    image bg 032 = "scenes/bg_032.jpg"
    image bg 033 = "scenes/bg_033.jpg"
    image bg 034 = "scenes/bg_034.jpg"
    image bg 035 = "scenes/bg_035.jpg"
    image bg 036 = "scenes/bg_036.jpg"
    image bg 037 = "scenes/bg_037.jpg"
    image bg 038 = "scenes/bg_038.jpg"
    image bg 039 = "scenes/bg_039.jpg"

    image bg 040 = "scenes/bg_040.jpg"
    image bg 041 = "scenes/bg_041.jpg"
    image bg 042 = "scenes/bg_042.jpg"
    image bg 043 = "scenes/bg_043.jpg"
    image bg 044 = "scenes/bg_044.jpg"
    image bg 045 = "scenes/bg_045.jpg"
    image bg 046 = "scenes/bg_046.jpg"
    image bg 047 = "scenes/bg_047.jpg"
    image bg 048 = "scenes/bg_048.jpg"
    image bg 049 = "scenes/bg_049.jpg"

    image bg 050 = "scenes/bg_050.jpg"
    image bg 051 = "scenes/bg_051.jpg"
    image bg 052 = "scenes/bg_052.jpg"
    image bg 053 = "scenes/bg_053.jpg"
    image bg 054 = "scenes/bg_054.jpg"
    image bg 055 = "scenes/bg_055.jpg"
    image bg 056 = "scenes/bg_056.jpg"
    image bg 057 = "scenes/bg_057.jpg"
    image bg 058 = "scenes/bg_058.jpg"
    image bg 059 = "scenes/bg_059.jpg"

    image bg 060 = "scenes/bg_060.jpg"
    image bg 061 = "scenes/bg_061.jpg"
    image bg 062 = "scenes/bg_062.jpg"
    image bg 063 = "scenes/bg_063.jpg"
    image bg 064 = "scenes/bg_064.jpg"
    image bg 065 = "scenes/bg_065.jpg"
    image bg 066 = "scenes/bg_066.jpg"
    image bg 067 = "scenes/bg_067.jpg"
    image bg 068 = "scenes/bg_068.jpg"
    image bg 069 = "scenes/bg_069.jpg"

    image bg 070 = "scenes/bg_070.jpg"
    image bg 071 = "scenes/bg_071.jpg"
    image bg 072 = "scenes/bg_072.jpg"
    image bg 073 = "scenes/bg_073.jpg"
    image bg 074 = "scenes/bg_074.jpg"
    image bg 075 = "scenes/bg_075.jpg"
    image bg 076 = "scenes/bg_076.jpg"
    image bg 077 = "scenes/bg_077.jpg"
    image bg 078 = "scenes/bg_078.jpg"
    image bg 079 = "scenes/bg_079.jpg"

    image bg 080 = "scenes/bg_080.jpg"
    image bg 081 = "scenes/bg_081.jpg"
    image bg 082 = "scenes/bg_082.jpg"
    image bg 083 = "scenes/bg_083.jpg"
    image bg 084 = "scenes/bg_084.jpg"
    image bg 085 = "scenes/bg_085.jpg"
    image bg 086 = "scenes/bg_086.jpg"
    image bg 087 = "scenes/bg_087.jpg"
    image bg 088 = "scenes/bg_088.jpg"
    image bg 089 = "scenes/bg_089.jpg"

    image bg 090 = "scenes/bg_090.jpg"
    image bg 091 = "scenes/bg_091.jpg"
    image bg 092 = "scenes/bg_092.jpg"
    image bg 093 = "scenes/bg_093.jpg"
    image bg 094 = "scenes/bg_094.jpg"
    image bg 095 = "scenes/bg_095.jpg"
    image bg 096 = "scenes/bg_096.jpg"
    image bg 097 = "scenes/bg_097.jpg"
    image bg 098 = "scenes/bg_098.jpg"
    image bg 099 = "scenes/bg_099.jpg"

    image bg 100 = "scenes/bg_100.jpg"
    image bg 101 = "scenes/bg_101.jpg"
    image bg 102 = "scenes/bg_102.jpg"
    image bg 103 = "scenes/bg_103.jpg"
    image bg 104 = "scenes/bg_104.jpg"
    image bg 105 = "scenes/bg_105.jpg"
    image bg 106 = "scenes/bg_106.jpg"
    image bg 107 = "scenes/bg_107.jpg"
    image bg 108 = "scenes/bg_108.jpg"
    image bg 109 = "scenes/bg_109.jpg"

    image bg 110 = "scenes/bg_110.jpg"
    image bg 111 = "scenes/bg_111.jpg"
    image bg 112 = "scenes/bg_112.jpg"
    image bg 113 = "scenes/bg_113.jpg"
    image bg 114 = "scenes/bg_114.jpg"
    image bg 115 = "scenes/bg_115.jpg"
    image bg 116 = "scenes/bg_116.jpg"
    image bg 117 = "scenes/bg_117.jpg"
    image bg 118 = "scenes/bg_118.jpg"
    image bg 119 = "scenes/bg_119.jpg"

    image bg 120 = "scenes/bg_120.jpg"
    image bg 121 = "scenes/bg_121.jpg"
    image bg 122 = "scenes/bg_122.jpg"
    image bg 123 = "scenes/bg_123.jpg"
    image bg 124 = "scenes/bg_124.jpg"
    image bg 125 = "scenes/bg_125.jpg"
    image bg 126 = "scenes/bg_126.jpg"
    image bg 127 = "scenes/bg_127.jpg"
    image bg 128 = "scenes/bg_128.jpg"
    image bg 129 = "scenes/bg_129.jpg"

    image bg 130 = "scenes/bg_130.jpg"
    image bg 131 = "scenes/bg_131.jpg"
    image bg 132 = "scenes/bg_132.jpg"
    image bg 133 = "scenes/bg_133.jpg"
    image bg 134 = "scenes/bg_134.jpg"
    image bg 135 = "scenes/bg_135.jpg"
    image bg 136 = "scenes/bg_136.jpg"
    image bg 137 = "scenes/bg_137.jpg"
    image bg 138 = "scenes/bg_138.jpg"
    image bg 139 = "scenes/bg_139.jpg"

    image bg 140 = "scenes/bg_140.jpg"
    image bg 141 = "scenes/bg_141.jpg"
    image bg 142 = "scenes/bg_142.jpg"
    image bg 143 = "scenes/bg_143.jpg"
    image bg 144 = "scenes/bg_144.jpg"
    image bg 145 = "scenes/bg_145.jpg"
    image bg 146 = "scenes/bg_146.jpg"
    image bg 147 = "scenes/bg_147.jpg"
    image bg 148 = "scenes/bg_148.jpg"
    image bg 149 = "scenes/bg_149.jpg"

    image bg 150 = "scenes/bg_150.jpg"
    image bg 151 = "scenes/bg_151.jpg"
    image bg 152 = "scenes/bg_152.jpg"
    image bg 153 = "scenes/bg_153.jpg"
    image bg 154 = "scenes/bg_154.jpg"
    image bg 155 = "scenes/bg_155.jpg"
    image bg 156 = "scenes/bg_156.jpg"
    image bg 157 = "scenes/bg_157.jpg"
    image bg 158 = "scenes/bg_158.jpg"
    image bg 159 = "scenes/bg_159.jpg"

    image bg 160 = "scenes/bg_160.jpg"
    image bg 161 = "scenes/bg_161.jpg"
    image bg 162 = "scenes/bg_162.jpg"
    image bg 163 = "scenes/bg_163.jpg"
    image bg 164 = "scenes/bg_164.jpg"
    image bg 165 = "scenes/bg_165.jpg"
    image bg 166 = "scenes/bg_166.jpg"
    image bg 167 = "scenes/bg_167.jpg"
    image bg 168 = "scenes/bg_168.jpg"
    image bg 169 = "scenes/bg_169.jpg"

    image bg 170 = "scenes/bg_170.jpg"
    image bg 171 = "scenes/bg_171.jpg"
    image bg 172 = "scenes/bg_172.jpg"
    image bg 173 = "scenes/bg_173.jpg"
    image bg 174 = "scenes/bg_174.jpg"
    image bg 175 = "scenes/bg_175.jpg"
    image bg 176 = "scenes/bg_176.jpg"
    image bg 177 = "scenes/bg_177.jpg"
    image bg 178 = "scenes/bg_178.jpg"
    image bg 179 = "scenes/bg_179.jpg"

    image bg 180 = "scenes/bg_180.jpg"
    image bg 181 = "scenes/bg_181.jpg"
    image bg 182 = "scenes/bg_182.jpg"
    image bg 183 = "scenes/bg_183.jpg"
    image bg 184 = "scenes/bg_184.jpg"
    image bg 185 = "scenes/bg_185.jpg"
    image bg 186 = "scenes/bg_186.jpg"
    image bg 187 = "scenes/bg_187.jpg"
    image bg 188 = "scenes/bg_188.jpg"
    image bg 189 = "scenes/bg_189.jpg"

    image bg 190 = "scenes/bg_190.jpg"
    image bg 191 = "scenes/bg_191.jpg"
    image bg 192 = "scenes/bg_192.jpg"
    image bg 193 = "scenes/bg_193.jpg"
    image bg 194 = "scenes/bg_194.jpg"
    image bg 195 = "scenes/bg_195.jpg"
    image bg 196 = "scenes/bg_196.jpg"
    image bg 197 = "scenes/bg_197.jpg"
    image bg 198 = "scenes/bg_198.jpg"
    image bg 199 = "scenes/bg_199.jpg"

    image bg 200 = "scenes/bg_200.jpg"
    image bg 201 = "scenes/bg_201.jpg"
    image bg 202 = "scenes/bg_202.jpg"
    image bg 203 = "scenes/bg_203.jpg"
    image bg 204 = "scenes/bg_204.jpg"
    image bg 205 = "scenes/bg_205.jpg"
    image bg 206 = "scenes/bg_206.jpg"
    image bg 207 = "scenes/bg_207.jpg"
    image bg 208 = "scenes/bg_208.jpg"
    image bg 209 = "scenes/bg_209.jpg"

    image bg 210 = "scenes/bg_210.jpg"
    image bg 211 = "scenes/bg_211.jpg"
    image bg 212 = "scenes/bg_212.jpg"
    image bg 213 = "scenes/bg_213.jpg"
    image bg 214 = "scenes/bg_214.jpg"
    image bg 215 = "scenes/bg_215.jpg"
    image bg 216 = "scenes/bg_216.jpg"
    image bg 217 = "scenes/bg_217.jpg"
    image bg 218 = "scenes/bg_218.jpg"
    image bg 219 = "scenes/bg_219.jpg"

    image bg 220 = "scenes/bg_220.jpg"
    image bg 221 = "scenes/bg_221.jpg"
    image bg 222 = "scenes/bg_222.jpg"
    image bg 223 = "scenes/bg_223.jpg"
    image bg 224 = "scenes/bg_224.jpg"
    image bg 225 = "scenes/bg_225.jpg"
    image bg 226 = "scenes/bg_226.jpg"
    image bg 227 = "scenes/bg_227.jpg"
    image bg 228 = "scenes/bg_228.jpg"
    image bg 229 = "scenes/bg_229.jpg"

    image bg 230 = "scenes/bg_230.jpg"
    image bg 231 = "scenes/bg_231.jpg"
    image bg 232 = "scenes/bg_232.jpg"
    image bg 233 = "scenes/bg_233.jpg"
    image bg 234 = "scenes/bg_234.jpg"
    image bg 235 = "scenes/bg_235.jpg"
    image bg 236 = "scenes/bg_236.jpg"
    image bg 237 = "scenes/bg_237.jpg"
    image bg 238 = "scenes/bg_238.jpg"
    image bg 239 = "scenes/bg_239.jpg"

    image bg 240 = "scenes/bg_240.jpg"
    image bg 241 = "scenes/bg_241.jpg"
    image bg 242 = "scenes/bg_242.jpg"
    image bg 243 = "scenes/bg_243.jpg"
    image bg 244 = "scenes/bg_244.jpg"
    image bg 245 = "scenes/bg_245.jpg"
    image bg 246 = "scenes/bg_246.jpg"
    image bg 247 = "scenes/bg_247.jpg"
    image bg 248 = "scenes/bg_248.jpg"
    image bg 249 = "scenes/bg_249.jpg"

    image bg 250 = "scenes/bg_250.jpg"
    image bg 251 = "scenes/bg_251.jpg"
    image bg 252 = "scenes/bg_252.jpg"
    image bg 253 = "scenes/bg_253.jpg"
    image bg 254 = "scenes/bg_254.jpg"
    image bg 255 = "scenes/bg_255.jpg"
    image bg 256 = "scenes/bg_256.jpg"
    image bg 257 = "scenes/bg_257.jpg"
    image bg 258 = "scenes/bg_258.jpg"
    image bg 259 = "scenes/bg_259.jpg"

    image bg 260 = "scenes/bg_260.jpg"
    image bg 261 = "scenes/bg_261.jpg"
    image bg 262 = "scenes/bg_262.jpg"
    image bg 263 = "scenes/bg_263.jpg"


    image bg 001 zakat = "scenes/bg_001_zakat.jpg"
    image bg 004 zakat = "scenes/bg_004_zakat.jpg"
    image bg 006 zakat = "scenes/bg_006_zakat.jpg"
    image bg 019 zakat = "scenes/bg_019_zakat.jpg"
    image bg 020 zakat = "scenes/bg_020_zakat.jpg"
    image bg 022 zakat = "scenes/bg_022_zakat.jpg"
    image bg 023 zakat = "scenes/bg_023_zakat.jpg"
    image bg 025 zakat = "scenes/bg_025_zakat.jpg"
    image bg 028 zakat = "scenes/bg_028_zakat.jpg"
    image bg 029 zakat = "scenes/bg_029_zakat.jpg"
    image bg 032 zakat = "scenes/bg_032_zakat.jpg"
    image bg 035 zakat = "scenes/bg_035_zakat.jpg"
    image bg 036 zakat = "scenes/bg_036_zakat.jpg"
    image bg 038 zakat = "scenes/bg_038_zakat.jpg"
    image bg 039 zakat = "scenes/bg_039_zakat.jpg"
    image bg 040 zakat = "scenes/bg_040_zakat.jpg"
    image bg 041 zakat = "scenes/bg_041_zakat.jpg"
    image bg 042 zakat = "scenes/bg_042_zakat.jpg"
    image bg 043 zakat = "scenes/bg_043_zakat.jpg"
    image bg 044 zakat = "scenes/bg_044_zakat.jpg"
    image bg 046 zakat = "scenes/bg_046_zakat.jpg"
    image bg 049 zakat = "scenes/bg_049_zakat.jpg"
    image bg 050 zakat = "scenes/bg_050_zakat.jpg"
    image bg 051 zakat = "scenes/bg_051_zakat.jpg"
    image bg 059 zakat = "scenes/bg_059_zakat.jpg"
    image bg 061 zakat = "scenes/bg_061_zakat.jpg"
    image bg 066 zakat = "scenes/bg_066_zakat.jpg"
    image bg 067 zakat = "scenes/bg_067_zakat.jpg"
    image bg 074 zakat = "scenes/bg_074_zakat.jpg"
    image bg 075 zakat = "scenes/bg_075_zakat.jpg"
    image bg 076 zakat = "scenes/bg_076_zakat.jpg"
    image bg 077 zakat = "scenes/bg_077_zakat.jpg"
    image bg 078 zakat = "scenes/bg_078_zakat.jpg"
    image bg 081 zakat = "scenes/bg_081_zakat.jpg"
    image bg 093 zakat = "scenes/bg_093_zakat.jpg"
    image bg 095 zakat = "scenes/bg_095_zakat.jpg"
    image bg 100 zakat = "scenes/bg_100_zakat.jpg"
    image bg 101 zakat = "scenes/bg_101_zakat.jpg"
    image bg 102 zakat = "scenes/bg_102_zakat.jpg"
    image bg 108 zakat = "scenes/bg_108_zakat.jpg"
    image bg 109 zakat = "scenes/bg_109_zakat.jpg"
    image bg 110 zakat = "scenes/bg_110_zakat.jpg"
    image bg 117 zakat = "scenes/bg_117_zakat.jpg"
    image bg 119 zakat = "scenes/bg_119_zakat.jpg"
    image bg 120 zakat = "scenes/bg_120_zakat.jpg"
    image bg 141 zakat = "scenes/bg_141_zakat.jpg"
    image bg 142 zakat = "scenes/bg_142_zakat.jpg"
    image bg 143 zakat = "scenes/bg_143_zakat.jpg"
    image bg 144 zakat = "scenes/bg_144_zakat.jpg"
    image bg 151 zakat = "scenes/bg_151_zakat.jpg"
    image bg 186 zakat = "scenes/bg_186_zakat.jpg"
    image bg 188 zakat = "scenes/bg_188_zakat.jpg"
    image bg 198 zakat = "scenes/bg_198_zakat.jpg"
    image bg 200 zakat = "scenes/bg_200_zakat.jpg"


    image bg 022 _day = "scenes/bg_022_day.jpg"
    image bg 080 _door = "scenes/bg_080_door.jpg"
    image bg 081 _door = "scenes/bg_081_door.jpg"
    image bg 082 _door = "scenes/bg_082_door.jpg"
    image bg 089 _mo = "scenes/bg_089_mo.jpg"
    image bg 082 night = "scenes/bg_082_night.jpg"
    image bg 085 night = "scenes/bg_085_night.jpg"
    image bg 115 _ohagi = "scenes/bg_115_ohagi.jpg"
    image bg 177 _tata = "scenes/bg_177_tata.jpg"
    image bg 062 _nolamp = "scenes/bg_062_nolamp.jpg"
    image bg 178 _cave_2 = "scenes/bg_178_cave1.jpg"
    image bg 178 _cave_4 = "scenes/bg_178_cave2.jpg"
    image bg 178 _cave_6 = "scenes/bg_178_cave3.jpg"
    image bg 178 _saiguden = "scenes/bg_178_saiguden.jpg"
    image bg 184 night = "scenes/bg_184_night.jpg"
    image bg 210 _lamp = "scenes/bg_210_lamp.jpg"
    image bg 247 watanagashi1 = "scenes/bg_247_watanagashi1.jpg"
    image bg 247 watanagashi2 = "scenes/bg_247_watanagashi2.jpg"


    image uso_da 2 = im.MatrixColor(im.AlphaMask("efe/uso_da.jpg", "efe/uso_da.jpg"), im.matrix.invert())
    image bg 022 red = im.MatrixColor("scenes/bg_022.jpg", im.matrix.tint(1.0, 0.125, 0.125))
    image rena se wa_a1 red = im.MatrixColor("characters/Rena/re_se_wa_b1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.125, 0.125))
    image rena se hiwa_b1 red = im.MatrixColor("characters/Rena/re_se_hiwa_b1.png", im.matrix.tint(1.0, 0.125, 0.125))
    image bg 143 red = im.MatrixColor("scenes/bg_143.jpg", im.matrix.tint(1.0, 0.125, 0.125))
    image bg 003 red = im.MatrixColor("scenes/bg_003.jpg", im.matrix.tint(1.0, 0.125, 0.125))
    image bg 081 _door red = im.MatrixColor("scenes/bg_081_door.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5625, 0.5625))
    image rena si hi_a1 rain = im.MatrixColor("characters/Rena/re_si_hi_a1.png", im.matrix.tint(0.4375, 0.4375, 0.71))
    image rena se hiwa_a1 red = im.MatrixColor("characters/Rena/re_se_hiwa_a1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5625, 0.5625))
    image mion si tk_a1 red = im.MatrixColor("characters/Mion/me_si_tk_a1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5625, 0.5625))
    image mion si wa_a2 red = im.MatrixColor("characters/Mion/me_si_wa_a1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5625, 0.5625))
    image mion si hi_a2 red = im.MatrixColor("characters/Mion/me_si_hi_a1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.125, 0.125))
    image bg 081 red = im.MatrixColor("scenes/bg_081_door.jpg", im.matrix.desaturate() * im.matrix.tint(1.0, 0.125, 0.125))
    image bg 081 _door fading = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_081_door.jpg", (141.5, 0), "characters/Mion/me_si_def_a1.png"), im.matrix.invert())
    image bg 080 _door red = im.MatrixColor("scenes/bg_080_door.jpg", im.matrix.tint(1.0, 0.3125, 0.3125))
    image sinka_bg 154 = im.MatrixColor("scenes/bg_154.jpg", im.matrix.desaturate() * im.matrix.tint(0.6, 0.6, 1.0))
    image sinka_mion si wa_a2 = im.MatrixColor("characters/Mion/me_si_wa_a1.png", im.matrix.desaturate() * im.matrix.tint(0.6, 0.6, 1.0))
    image mion ki sin_a1 red = im.MatrixColor("characters/Mion/me_si_sin_a1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.0, 0.0))
    image bg 142 _dark = im.MatrixColor("scenes/bg_142.jpg", im.matrix.tint(0.467, 0.467, 0.467))
    image bg 211 _vecher = im.MatrixColor("scenes/bg_211.jpg", im.matrix.tint(1.0, 0.58, 0.1) * im.matrix.brightness(-0.1))
    image ryuuketu_efe03 = im.MatrixColor("efe/ryuuketu_efe.png", im.matrix.tint(1.0, 0.0, 0.0))
    image bg 258 _dark = im.MatrixColor("scenes/bg_258.jpg", im.matrix.tint(0.4375, 0.4375, 0.467))
    image hima_mori_01 = im.MatrixColor("scenes/bg_144_rain.jpg", im.matrix.tint(0.6875, 0.6875, 0.6875))
    image hima_mori_02 = im.MatrixColor("scenes/bg_144_rain.jpg", im.matrix.tint(0.4375, 0.4374, 0.4375))


    image bg 222 desat = im.MatrixColor("scenes/bg_222.jpg", im.matrix.desaturate() * im.matrix.tint(0.6, 0.6, 0.6))
    image rena si wa_b1 desat = im.MatrixColor("characters/Rena/re_si_wa_b1.png", im.matrix.desaturate() * im.matrix.tint(0.35, 0.35, 0.35))
    image bg 003 gray = im.MatrixColor("scenes/bg_003.jpg", im.matrix.desaturate() * im.matrix.tint(0.375, 0.375, 0.375))
    image bg 081 _door gray = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_081_door.jpg", (-21.5, 0), "characters/Rena/re_se_hiwa_a1.png", (301.5, 0), "characters/Mion/me_si_hi_a1.png"), im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image bg 175 gray = im.MatrixColor("scenes/bg_175.jpg", im.matrix.desaturate() * im.matrix.tint(0.4375, 0.4375, 0.4375))
    image bg 196 gray = im.MatrixColor("scenes/bg_196.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.71, 0.71))
    image bg 075 gray = im.MatrixColor("scenes/bg_075.jpg", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image bg 093 gray = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_093.jpg", (139.5, 0), "characters/Satoko/sa_se_mu_a1.png"), im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image bg 108 gray = im.MatrixColor("scenes/bg_108.jpg", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image bg 210 gray = im.MatrixColor("scenes/bg_210.jpg", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image bg 170 gray = im.MatrixColor("scenes/bg_170.jpg", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image tata_satoko_01 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_109.jpg", (-12.5, 0), "characters/Satoko/sa_se_na_b1.png", (298.5, 0), "characters/Rena/re_se_ko_b1.png"), im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image tata_satoko_02 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_109.jpg", (-12.5, 0), "characters/Satoko/sa_se_na_b1.png", (298.5, 0), "characters/Rena/re_se_ko_b1.png"), im.matrix.desaturate() * im.matrix.tint(0.25, 0.25, 0.25))
    image bg 059 gray = im.MatrixColor("scenes/bg_059.jpg", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image satoko se mu_a1 gray = im.MatrixColor("characters/Satoko/sa_se_mu_a1.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image bg 159 gray = im.MatrixColor("scenes/bg_159.jpg", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))
    image bg 170 _tuman = im.MatrixColor("scenes/bg_170.jpg", im.matrix.desaturate() * im.matrix.tint(0.6875, 0.6875, 0.6875))
    image bg 027 gray = im.MatrixColor("scenes/bg_027.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.71, 0.71))
    image bg 203 _faded = im.MatrixColor("scenes/bg_203.jpg", im.matrix.desaturate() * im.matrix.tint(0.8125, 0.8125, 0.8125))
    image irie doc def_a1 desat = im.MatrixColor("characters/Irie/ir_doc_de_a1.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 0.5))


    image tomi si_def desat = im.MatrixColor("characters/sonota/tomi_def.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image bg 081 desat = im.MatrixColor("scenes/bg_081.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image bg 080 desat = im.MatrixColor("scenes/bg_080.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image bg 159 desat = im.MatrixColor("scenes/bg_159.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 108 = im.MatrixColor("scenes/bg_108.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion se to_a1 = im.MatrixColor("characters/Mion/me_se_to_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 129 = im.MatrixColor("scenes/bg_129.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_shion si wa_b1 = im.MatrixColor("characters/Shion/si_si_wa_b1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 153 = im.MatrixColor("scenes/bg_153.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion si to_a1 = im.MatrixColor("characters/Mion/me_si_to_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_satoko si wa_a1 = im.MatrixColor("characters/Satoko/sa_si_wa_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion si wa_a1 = im.MatrixColor("characters/Mion/me_si_wa_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion si wink_a1 = im.MatrixColor("characters/Mion/me_si_wink_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena si ka_b1 = im.MatrixColor("characters/Rena/re_si_ka_b1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_cg ningyo_rena = im.MatrixColor("cg/ningyo_rena.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena si wa_a1 = im.MatrixColor("characters/Rena/re_si_wa_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion si tk_a1 = im.MatrixColor("characters/Mion/me_si_tk_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 168 night = im.MatrixColor("scenes/bg_168_night.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 161 night = im.MatrixColor("scenes/bg_161_night.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_shion ma def_a1 = im.MatrixColor("characters/Shion/si_ma_def_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_shion ma hau_a1 = im.MatrixColor("characters/Shion/si_ma_hau_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 043 = im.MatrixColor("scenes/bg_043.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion se bik_a2 = im.MatrixColor("characters/Mion/me_se_bik_a2.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena se nande_a1 = im.MatrixColor("characters/Rena/re_se_nande_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 117 zakat = im.MatrixColor("scenes/bg_117_zakat.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 020 zakat = im.MatrixColor("scenes/bg_020_zakat.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_shion si wink_a1 = im.MatrixColor("characters/Shion/si_si_wink_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena se def_a1 = im.MatrixColor("characters/Rena/re_se_def_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena se hau_b1 = im.MatrixColor("characters/Rena/re_se_hau_b1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena se ko_a1 = im.MatrixColor("characters/Rena/re_se_ko_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 142 = im.MatrixColor("scenes/bg_142.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion se def_a1 = im.MatrixColor("characters/Mion/me_se_def_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rika se de_a1 = im.MatrixColor("characters/Rika/ri_se_de_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rika se wa_a1 = im.MatrixColor("characters/Rika/ri_se_nipa_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 062 = im.MatrixColor("scenes/bg_062.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 240 = im.MatrixColor("scenes/bg_240.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_satoko se def_a1 = im.MatrixColor("characters/Satoko/sa_se_def_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_satoko se aki_a1 = im.MatrixColor("characters/Satoko/sa_se_aki_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 082 = im.MatrixColor("scenes/bg_082.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_takano si_def = im.MatrixColor("characters/sonota/taka_def.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 210 = im.MatrixColor("scenes/bg_210.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_satoko se wa_b1 = im.MatrixColor("characters/Satoko/sa_se_wa_b1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 122 = im.MatrixColor("scenes/bg_122.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 059 = im.MatrixColor("scenes/bg_059.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 083 = im.MatrixColor("scenes/bg_083.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 084 = im.MatrixColor("scenes/bg_084.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 003 = im.MatrixColor("scenes/bg_003.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 015 = im.MatrixColor("scenes/bg_015.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 010 = im.MatrixColor("scenes/bg_010.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg kumasan = im.MatrixColor("cg/kuma_san.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 245 = im.MatrixColor("scenes/bg_245.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 109 = im.MatrixColor("scenes/bg_109.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 110 = im.MatrixColor("scenes/bg_110.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_satoko se bik_b1 = im.MatrixColor("characters/Satoko/sa_se_bik_b1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_satoko se na_a1 = im.MatrixColor("characters/Satoko/sa_se_na_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion se wa_a1 = im.MatrixColor("characters/Mion/me_se_wa_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena se wa_a1 = im.MatrixColor("characters/Rena/re_se_wa_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_mion se aku_a1 = im.MatrixColor("characters/Mion/me_se_aku_a1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_satoko se hn_b1 = im.MatrixColor("characters/Satoko/sa_se_hn_b1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_rena se ka_b1 = im.MatrixColor("characters/Rena/re_se_ka_b1.png", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 037 = im.MatrixColor("scenes/bg_037.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 034 = im.MatrixColor("scenes/bg_034.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 069 = im.MatrixColor("scenes/bg_069.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 070 = im.MatrixColor("scenes/bg_070.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 068 = im.MatrixColor("scenes/bg_068.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))
    image sepia_bg 212 = im.MatrixColor("scenes/bg_212.jpg", im.matrix.desaturate() * im.matrix.tint(0.71, 0.64, 0.64))


    image inverse_bg 216 = im.MatrixColor("scenes/bg_216.jpg", im.matrix.invert())
    image inverse_bg 024 = im.MatrixColor("scenes/bg_024.jpg", im.matrix.invert())
    image inverse_cg nata = im.MatrixColor("cg/nata_terror.jpg", im.matrix.invert())
    image inverse_rena si bik_b1 = im.MatrixColor("characters/Rena/re_si_bik_b1.png", im.matrix.invert())
    image inverse_cg door delusion = im.MatrixColor("cg/door_3.jpg", im.matrix.invert())
    image inverse_bg 049 = im.MatrixColor("scenes/bg_049.jpg", im.matrix.invert())
    image inverse_bg 020 = im.MatrixColor("scenes/bg_020.jpg", im.matrix.invert())
    image inverse_cg usoda shout = im.MatrixColor("cg/usoda_2.jpg", im.matrix.invert())
    image inverse_bg 051 = im.MatrixColor("scenes/bg_051.jpg", im.matrix.invert())
    image inverse_rena se hii_a1 = im.MatrixColor("characters/Rena/re_se_hii_a1.png", im.matrix.invert())
    image inverse_bg 004 = im.MatrixColor("scenes/bg_004.jpg", im.matrix.invert())
    image inverse_bg 080 _door = im.MatrixColor("scenes/bg_080_door.jpg", im.matrix.invert())
    image inverse_bg 117 zakat = im.MatrixColor("scenes/bg_117_zakat.jpg", im.matrix.invert())
    image inverse_bg 154 = im.MatrixColor("scenes/bg_154.jpg", im.matrix.invert())
    image inverse_mion si wa_a2 = im.MatrixColor("characters/Mion/me_si_wa_a2.png", im.matrix.invert())
    image inverse_bg 155 = im.MatrixColor("scenes/bg_155.jpg", im.matrix.invert())
    image inverse_satoko si wa_a1 = im.MatrixColor("characters/Satoko/sa_si_wa_a1.png", im.matrix.invert())
    image inverse_bg 028 = im.MatrixColor("scenes/bg_028.jpg", im.matrix.invert())
    image inverse_rika se wa_a1 = im.MatrixColor("characters/Rika/ri_se_nipa_a1.png", im.matrix.invert())
    image inverse_chie si_maji = im.MatrixColor("characters/sonota/sensei_2.png", im.matrix.invert())
    image inverse_bg 163 = im.MatrixColor("scenes/bg_163.jpg", im.matrix.invert())
    image inverse_bg 095 = im.MatrixColor("scenes/bg_095.jpg", im.matrix.invert())
    image inverse_rika se de_a1 = im.MatrixColor("characters/Rika/ri_se_de_a1.png", im.matrix.invert())
    image inverse_bg 080 = im.MatrixColor("scenes/bg_080.jpg", im.matrix.invert())
    image inverse_ooishi si maji_a1 = im.MatrixColor("characters/Ooishi/oi_si_maji_a1.png", im.matrix.invert())
    image inverse_bg 100 = im.MatrixColor("scenes/bg_100.jpg", im.matrix.invert())
    image inverse_bg 018 = im.MatrixColor("scenes/bg_018.jpg", im.matrix.invert())
    image inverse_bg 115 = im.MatrixColor("scenes/bg_115.jpg", im.matrix.invert())
    image inverse_bg 108 = im.MatrixColor("scenes/bg_108.jpg", im.matrix.invert())
    image inverse_mion se yo_a1 = im.MatrixColor("characters/Mion/me_se_yo_a1.png", im.matrix.invert())
    image inverse_bg 141 zakat = im.MatrixColor("scenes/bg_141_zakat.jpg", im.matrix.invert())
    image inverse_bg 143 zakat = im.MatrixColor("scenes/bg_143_zakat.jpg", im.matrix.invert())
    image inverse_satoko se na_a1 = im.MatrixColor("characters/Satoko/sa_se_na_a1.png", im.matrix.invert())
    image inverse_bg 187 = im.MatrixColor("scenes/bg_187.jpg", im.matrix.invert())
    image inverse_cg hatred_satoko = im.MatrixColor("cg/just_die_already.jpg", im.matrix.invert())


    image oni_rena 01 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_142.jpg", (138.5, 0), "characters/Rena/re_se_wa_b1.png"), im.matrix.desaturate() * im.matrix.tint(1.0, 0.8125, 0.8125))
    image oni_rena 02 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_142.jpg", (138.5, 0), "characters/Rena/re_se_wa_b1.png"), im.matrix.desaturate() * im.matrix.tint(1.0, 0.5625, 0.5625))
    image oni_rena 03 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_142.jpg", (138.5, 0), "characters/Rena/re_se_hiwa_b1.png"), im.matrix.desaturate() * im.matrix.tint(1.0, 0.5625, 0.5625))
    image oni_rena 04 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_142.jpg", (138.5, 0), "characters/Rena/re_se_hi_b1.png"), im.matrix.desaturate() * im.matrix.tint(1.0, 0.5625, 0.5625))
    image oni_rena 05 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_142.jpg", (138.5, 0), "characters/Rena/re_se_hi_b1.png"), im.matrix.desaturate() * im.matrix.tint(1.0, 0.375, 0.375))
    image oni_rena 06 = im.MatrixColor(im.Composite((640, 480), (0, 0), "scenes/bg_142.jpg", (138.5, 0), "characters/Rena/re_se_hi_b1.png"), im.matrix.desaturate() * im.matrix.tint(1.0, 0.125, 0.125))
    image oni_rena 07 = im.Composite((640, 480), (0, 0), "efe/black.jpg", (138.5, 0), im.MatrixColor("characters/Rena/re_se_hi_b1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.125, 0.125)))
    image oni_rena 08 = im.Composite((640, 480), (0, 0), "efe/black.jpg", (138.5, 0), im.MatrixColor("characters/Rena/re_se_hiwa_b1.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.125, 0.125)))


    image wata_owner_01 = im.MatrixColor("scenes/bg_118.jpg", im.matrix.tint(0.71, 0.71, 0.71))
    image wata_owner_02 = im.MatrixColor("scenes/bg_118.jpg", im.matrix.tint(0.467, 0.467, 0.467))
    image wata_owner_03 = im.MatrixColor("scenes/bg_118.jpg", im.matrix.tint(0.25, 0.25, 0.25))
    image wata_owner_04 = im.MatrixColor("scenes/bg_118.jpg", im.matrix.tint(0.125, 0.125, 0.125))


    image tata_kuruma 01 = im.MatrixColor("scenes/bg_103_rain.jpg", im.matrix.tint(0.875, 0.875, 0.875))
    image tata_kuruma 02 = im.MatrixColor("scenes/bg_103_rain.jpg", im.matrix.tint(0.8125, 0.8125, 0.8125))
    image tata_kuruma 03 = im.MatrixColor("scenes/bg_103_rain.jpg", im.matrix.tint(0.6875, 0.6875, 0.6875))
    image tata_kuruma 04 = im.MatrixColor("scenes/bg_103_rain.jpg", im.matrix.tint(0.5, 0.5, 0.5))
    image tata_kuruma 05 = im.MatrixColor("scenes/bg_103_rain.jpg", im.matrix.tint(0.375, 0.375, 0.375))
    image tata_kuruma 06 = im.MatrixColor("scenes/bg_103_rain.jpg", im.matrix.tint(0.25, 0.25, 0.25))
    image tata_kuruma 07 = im.MatrixColor("scenes/bg_103_rain.jpg", im.matrix.tint(0.125, 0.125, 0.125))


    image tata_jisitu 01 = im.MatrixColor("scenes/bg_082.jpg", im.matrix.tint(0.0625, 0.0625, 0.0625))
    image tata_jisitu 02 = im.MatrixColor("scenes/bg_082.jpg", im.matrix.tint(0.1875, 0.1875, 0.1875))
    image tata_jisitu 03 = im.MatrixColor("scenes/bg_082.jpg", im.matrix.tint(0.375, 0.375, 0.375))
    image tata_jisitu 04 = im.MatrixColor("scenes/bg_082.jpg", im.matrix.tint(0.6875, 0.6875, 0.6875))


    image hima_rain 01 = im.MatrixColor("scenes/bg_143_rain.jpg", im.matrix.tint(1.0, 0.6875, 0.6875))
    image hima_rain 02 = im.MatrixColor("scenes/bg_143_rain.jpg", im.matrix.tint(0.8125, 0.3125, 0.3125))
    image hima_rain 03 = im.MatrixColor("scenes/bg_143_rain.jpg", im.matrix.tint(0.5625, 0.0625, 0.0625))


    image bg 038 rain = "scenes/bg_038_rain.jpg"
    image bg 050 rain = "scenes/bg_050_rain.jpg"
    image bg 101 rain = "scenes/bg_101_rain.jpg"
    image bg 103 rain = "scenes/bg_103_rain.jpg"
    image bg 104 rain = "scenes/bg_104_rain.jpg"
    image bg 117 rain = "scenes/bg_117_rain.jpg"
    image bg 118 rain = "scenes/bg_118_rain.jpg"
    image bg 119 rain = "scenes/bg_119_rain.jpg"
    image bg 121 rain = "scenes/bg_121_rain.jpg"
    image bg 141 rain = "scenes/bg_141_rain.jpg"
    image bg 142 rain = "scenes/bg_142_rain.jpg"
    image bg 143 rain = "scenes/bg_143_rain.jpg"
    image bg 144 rain = "scenes/bg_144_rain.jpg"
    image bg 250 rain = "scenes/bg_250_rain.jpg"
    image bg 251 rain = "scenes/bg_251_rain.jpg"
    image bg 252 rain = "scenes/bg_252_rain.jpg"
    image bg 253 rain = "scenes/bg_253_rain.jpg"
    image bg 254 rain = "scenes/bg_254_rain.jpg"


    image bg 161 night = "scenes/bg_161_night.jpg"
    image bg 163 night = "scenes/bg_163_night.jpg"
    image bg 164 night = "scenes/bg_164_night.jpg"
    image bg 165 night = "scenes/bg_165_night.jpg"
    image bg 166 night = "scenes/bg_166_night.jpg"
    image bg 168 night = "scenes/bg_168_night.jpg"

    $ day_result = ""
    $ tips = "mainmenu"
    $ asobi_box = 0

label splashscreen:

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


label tips_context:

    $ unlock_prompt = True
    $ save_name = "У, фулюганы!\nНеча тут сохранятися!"

    scene cg_haikei with dissolve
    $ renpy.pause(0.2)
    if tips == "mainmenu_onik":
        call screen tips_onik
    elif tips == "mainmenu_wata":
        call screen tips_wata
    elif tips == "mainmenu_tata":
        call screen tips_tata
    elif tips == "mainmenu_hima":
        call screen tips_hima
    return


label omake_between:

    scene omake_haikei with spiral4
    play sound wa_041

    return


label toketu:

    show toketu1a with Dissolve(0.3)
    play sound wa_035
    $ renpy.pause(0.8, hard=True)
    scene toketu1b with Dissolve(0.3)
    play sound wa_035
    $ renpy.pause(0.8, hard=True)
    scene toketu1c with Dissolve(0.3)
    play sound wa_035
    $ renpy.pause(2.0, hard=True)

    return




label unlock_onik:

    $ _game_menu_screen = None
    $ unlock_prompt = True
    scene black
    show rena se def_a1 with fastdown
    a_r "День добрый."
    a_r "Стало быть, вы утверждаете, что знаете полное содержание первой арки?{nw}{w=1.0}"
    play sound lovely_laugh
    show rena se wa_a1 with fastdown
    $ renpy.pause(1.0)
    show rena se def_a1 with up
    a_r "Что же, посмотрим, сможете ли вы это подтвердить, ответив на три простых вопроса."
    a_r "Ответ на каждый вопрос — одно короткое существительное, начинающееся с заглавной буквы."
    a_r "Точку ставить не надо."
    a_r "Ну, значит..."
    show rena se wa_b1 with fastup
    play sound wa_011
    a_r "Поехали!{nw}{w=0.2}"
    $ question_1 = renpy.input("Предмет, использованный при наказании фотографа.", length=7)
    if question_1 == pass_onik_1:
        show rena se wa_a1 with fastdown
        a_r "Отлично!"
        a_r "Переходим ко следующему вопросу."
        show rena se bik_b1 with fastup
        $ question_2 = renpy.input("Уменьшительно-ласкательное название предмета, подаренного главным героем одной из девушек.", length=7)
        if question_2 == pass_onik_2:
            show rena se hau_a1 with fastdown
            a_r "Отлично... хау..."
            a_r "А теперь заключительный вопрос..."
            show rena se ko_a2 with fastdown
            $ question_3 = renpy.input("Предмет, которым была убита вышеупомянутая девушка.", length=7)
            if question_3 == pass_onik_3:
                play sound wa_012
                show rena se wa_a1 with fastup
                a_r "Отлично!"
                a_r "Вы доказали, что знаете содержание Первой Главы."
                hide rena with Dissolve(1.0)
                $ renpy.pause(1.0, hard=True)
                jump otsukaresama_onikakushi
            else:

                jump you_lied
        else:
            jump you_lied
    else:
        jump you_lied



label unlock_wata:

    $ _game_menu_screen = None
    $ unlock_prompt = True
    $ wata_q = 5
    scene black
    show mion si def_a1 with down
    a_m "Здоров. Чё, пришёл попытать счастья?{w=0.5} Тады не станем нежности разводить, начали.{w=0.7} Даю пять вопросов, ответить правильно надо хотя бы на три."
    a_m "Ответ на каждый вопрос должен писаться с заглавной буквы, в именительном падеже и единственном числе.{w=1.5} Разумеется, ответ согласуется с вопросом."
    $ question_1 = renpy.input("Фамилия одного из парней, с которыми Кей-тян играл на большом соревновании в магазине игрушек, а потом не раз ещё с ними пересекался (их называют в основном по фамилиям).", length=10)
    if question_1 in pass_wata_1:
        play sound wa_011
        show mion si wink_a2 with m1_03
        a_m "Молодца! Давай дальше!"
    else:
        $ wata_q += -1
    $ question_2 = renpy.input("Любимая приправа учительницы Сатоко.", length=10)
    if question_2 == pass_wata_2:
        play sound wa_012
        show mion si wa_a1 with left_03
        a_m "Аха-ха-ха! Так держать!"
    else:
        $ wata_q += -1
    $ question_3 = renpy.input("Фамилия убийцы друзей главного героя?", length=10)
    hide mion with dissolve_04
    $ renpy.pause(2.0, hard=True)
    show mion ki sin_a1 with Dissolve(1.0)
    if question_3 != pass_wata_3:
        $ wata_q += -1
    a_m "Молодец. Ещё два вопроса."
    $ question_4 = renpy.input("Японское название здания, играющего ключевую роль в данной Главе.", length=10)
    if question_4 == pass_wata_4:
        play sound wa_012
    else:
        $ wata_q += -1
    show mion ki wink_a1 with dissolve_04
    a_m "И заключительный вопрос! Отвечай честно!"
    play sound wa_047
    a_m "И-и-и-и..."
    show mion ki wa_a1:
        xalign 0.5 yalign 1.0
        linear 0.5 xalign 0.15
    show mion se bik_b1 at sprava as real_mion with moveinright
    $ question_5 = renpy.input("Каков цвет нижнего белья сеструхи?", length=10, exclude='бух')
    if question_5 != pass_wata_5:
        $ wata_q += -1
    if wata_q >= 3 and question_5 not in failpass_wata_5:
        play sound wa_012
        show mion se hau_a1 as real_mion with Dissolve(1.0)
        show mion ki wa_a1 with dissolve_02
        a_m "Ну что ж! Поздравляю, ты прошёл экзамен!"
        show mion ki wink_a2 with dissolve_02
        a_m "Кстати говоря, трусы на сеструхе чёрные. Как у меня!"
        show mion se bik_b1 as real_mion with dissolve_04
        a_m "ШИОННННН!!! АХ ТЫ ЗАСРААААНКАААААА!!!!!!!"
        play sound wa_007
        scene black with Shake((0, 0, 0, 0), 0.5, dist=30)
        $ renpy.pause(0.4, hard=True)
        play sound wa_005
        $ renpy.pause(0.4, hard=True)
        play sound wa_005
        $ renpy.pause(0.4, hard=True)
        play sound wa_003
        $ renpy.pause(0.7, hard=True)
        play sound wa_008
        $ renpy.pause(0.4, hard=True)
        play sound wa_036
        with Shake((0, 0, 0, 0), 4.0, dist=70)
        $ renpy.pause(2.5, hard=True)
        show mion se bik_b1:
            zoom 1.5 xalign 0.25 yalign 0.1
        with dissolve_04
        a_m "Н-ну, как бы то ни было..."
        play sound wa_008
        $ renpy.pause(0.3, hard=True)
        play sound wa_006
        scene black with Shake((0, 0, 0, 0), 0.5, dist=30)
        $ renpy.pause(0.5, hard=True)
        play sound wa_018
        $ renpy.pause(0.2, hard=True)
        play sound wa_005
        $ renpy.pause(0.8, hard=True)
        play sound wa_005
        $ renpy.pause(0.3, hard=True)
        play sound wa_030
        $ renpy.pause(0.4, hard=True)
        play sound wa_007
        $ renpy.pause(0.5, hard=True)
        play sound wa_005
        $ renpy.pause(0.3, hard=True)
        play sound wa_012
        $ renpy.pause(0.9, hard=True)
        play sound wa_006
        with Shake((0, 0, 0, 0), 1.5, dist=30)
        $ renpy.pause(0.2, hard=True)
        play sound wa_010
        $ renpy.pause(0.5, hard=True)
        play sound wa_005
        $ renpy.pause(0.4, hard=True)
        play sound wa_012
        $ renpy.pause(0.6, hard=True)
        play sound wa_030
        $ renpy.pause(0.6, hard=True)
        play sound wa_018
        with Shake((0, 0, 0, 0), 0.5, dist=20)
        $ renpy.pause(2.8, hard=True)
        play sound wa_007
        with Shake((0, 0, 0, 0), 1.0, dist=10)
        $ renpy.pause(4.0, hard=True)
        show mion ki sin_a1 at central with left_03
        a_m "Аха-ха! Ладно, ладно, получай свою награду."
        show mion ki fu_a2:
            alpha 1.0
            0.3
            linear 0.7 alpha 0.0
        with dissolve_04
        $ renpy.pause(1.0, hard=True)
        jump otsukaresama_watanagashi

    elif question_5 in failpass_wata_5:
        jump evil_sisters
    else:
        jump sad_sister


label unlock_tata:

    $ _game_menu_screen = None
    $ unlock_prompt = True
    stop music fadeout 2.0
    scene black
    show satoko ts bik_a1
    a_s "А куда это вы полезть изволили без моего разрешения?!"

    if persistent.matsuri:
        play sound lsys28

        $ ui.timer(17.0, ui.jumps("eaten_by_satoko"))
        show satoko ts aku_a1:
            crop (0, 0, 224, 384)
            size (224, 384)
            linear 12.0 crop (0, 0, 224, 192) xzoom 2.0
            linear 5.0 zoom 2.0 yanchor 0.75
        a_s "А ну, назад, назад!"
    else:
        show satoko ts aku_a1 with dissolve_02
    stop sound fadeout 0.01

    $ renpy.pause(3.0, hard=True)
    scene black with dissolve_04
    show satoko ku aki_a1 with fastup
    a_s "Какая невоспитанность! Могли бы и подождать, пока я переоденусь!"
    play music msys05
    show satoko ku wa_a1 with dissolve_02
    a_s "Ладно, вы же пришли сюда открыть Главу, так?"
    show satoko ku def_a1 with dissolve_02
    a_s "Вам понадобится ответить на семь вопросов. На каждый надобно отвечать существительным в именительном падеже. Точку ставить не нужно."
    show satoko ku aku_a1 with dissolve_02
    a_s "Вопросов нет?{w=0.2} Вопросов нет, приступаем.{w=0.1}{nw}"
    show satoko ku wa_a1 with dissolve_02
    $ question_1 = renpy.input("Кто готовил ужин в доме семьи Маэбара в первый день?", length=9)
    if question_1 == pass_tata_1:
        play sound wa_011
        a_s "Весьма хорошо! Вижу, отсутствием памяти вы не страдаете!"
        show satoko ku aku_a1 with dissolve_02
        a_s "Переходим к следующему!{w=0.2}{nw}"
        play sound wa_007
        $ question_2 = renpy.input("Краткое название предмета, потрясая которым, Кейти-сан прибыл на спортивную площадку начальной школы посёлка Окиномия, думая, что там идёт драка.", length=9)
        if question_2 == pass_tata_2:
            play sound wa_007
            show satoko ku def_a1 with dissolve_02
            a_s "Неплохо, неплохо! Давайте дальше!"
            $ question_3 = renpy.input("Как зовут тренера Бойцов Хинамидзавы?", length=9)
            if question_3 in pass_tata_3:
                play sound wa_029
                show satoko ku aki_a1 with dissolve_02
                a_s "Согласна с вами, личность он престраннейшая."
                show satoko ku hau_a1 with dissolve_02
                a_s "Тем не менее и к нему можно привыкнуть."
                $ question_4 = renpy.input("Во что играли на упомянутой площадке школы Окиномия... до того как туда прибыл Кейти-сан?", length=9)
                if question_4 == pass_tata_4:
                    play sound wa_011
                    show satoko ku wa_a1 with dissolve_02
                    a_s "Не правда ли, здорово я его?"
                    show satoko ku aki_a1 with dissolve_04
                    a_s "Впрочем, подождите минутку, будьте столь добры."
                    a_s "У меня, видите ли, не так много выражений лица с ошейником, поэтому для заключительных вопросов мне понадобится его снять."
                    hide satoko with dissolve_04
                    show irie si warai at sleva with dissolve_04
                    a_i "А пока моя будущая {cps=*0.6}служаночка~{font=DejaVuSans.ttf}☆{/font}...{/cps} переодевается, мы продолжим наш увлекательный допрос!"
                    show irie si maji_a2 with dissolve_02
                    $ question_5 = renpy.input("Фамилия подозрительной личности, повстречавшейся Маэбаре-сану после закапывания трупа.", length=9)
                    if question_5 == pass_tata_5:
                        show irie si def_a1 with dissolve_02
                        a_i "Да, ответ правильный. Переходим к следующему."
                        $ question_6 = renpy.input("Предмет, которым главный герой намеревался повторно убить одного человека, менее чем достойного уважения, но который сослужил ему медвежью услугу.", length=9)
                        if question_6 == pass_tata_6:
                            play sound wa_005
                            show irie si maji_a1 with dissolve_02
                            a_i "Убийство — не выход. Но иногда бывает так, что совесть не позволяет мне осудить убийцу."
                            show satoko se mu_a2 at sprava with dissolve_04
                            a_s "............"
                            show irie si maji_a2 with dissolve_02
                            a_i "Заключительный вопрос."
                            $ question_7 = renpy.input("Название (вид) стратегического сооружения, где произошла развязка данной Главы.", length=9)
                            if question_7 == pass_tata_7:
                                play sound wa_041
                                a_s "Верно..."
                                show satoko se hn_b3 with fastup
                                a_s "И вы знаете, что со мной потом стало?"
                                show satoko se na_b1 with dissolve_02
                                a_s "{cps=*2.0}Всё вышло так, как и говорила Мион-саааан! Уаааааа!{/cps}{w=0.1}{nw}"
                                hide satoko with moveoutleft
                                a_i "............"
                                a_i "Н-да."
                                scene black with dissolve_04
                                $ renpy.pause(1.0)
                                jump otsukaresama_tatarigoroshi
                            else:

                                jump wrong_answer
                        else:
                            jump wrong_answer
                    else:
                        jump wrong_answer
                else:
                    jump wrong_answer
            else:
                jump wrong_answer
        else:
            jump wrong_answer
    else:
        jump wrong_answer


label unlock_hima:

    $ _game_menu_screen = None
    $ unlock_prompt = True
    scene black
    show ooishi yukata def_a1
    a_o "Ваши документики?{w=1.0}{nw}"
    show ooishi yukata wa_a1 with dissolve_02
    a_o "Шучу, шучу. Мм-хм-хм-хм!"
    show ooishi yukata def_a1 with dissolve_02
    a_o "Полагаю, вы пришли сюда открыть четвёртую главу. Что ж, для этого вам придётся ответить на семь вопросов по её содержанию."
    a_o "Все ответы начинаются с заглавной буквы (все остальные буквы — строчные) и согласуются с вопросом. Точку ставить не нужно."
    show ooishi yukata def_a2 with dissolve_02
    a_o "Вы готовы? Тогда поехали."
    show ooishi yukata def_a1 with dissolve_02
    $ question_1 = renpy.input("Какова фамилия министра, связанного с делом о похищении, вокруг которого вертится сия Глава?", length=8)
    if question_1 in pass_hima_1:
        play sound wa_012
        show ooishi yukata wa_a1 with dissolve_02
        a_o "Отлично! Продолжим же?"
        $ question_2 = renpy.input("Имя жены следователя, занимавшегося данным делом и подружившегося в его ходе с Ооиси?", length=8)
        if question_2 == pass_hima_2:
            play sound wa_044
            show ooishi yukata def_a1 with dissolve_02
            a_o "Верно."
            $ question_3 = renpy.input("Игра, в которую играл главный герой вечером второго дня с Ооиси?", length=8)
            if question_3 in pass_hima_3:
                show ooishi yukata aku_a1 with dissolve_02
                play sound wa_010
                $ renpy.pause(0.3)
                play sound wa_011
                show ooishi yukata def_a2 with dissolve_04
                a_o "Эх, славная была партейка! Вот бы сыграть ещё хоть разок!"
                $ question_4 = renpy.input("Ключевая улика, позволившая завершить дело и спасти похищенного?", length=8)
                if question_4 in pass_hima_4:
                    play sound wa_011
                    a_o "Совершенно верно."
                    show ooishi yukata def_a1 at sleva with move
                    show rika hima de_a1 at sprava with dissolve_04
                    a_f "Ми-и."
                    show ooishi yukata wa_a1 with dissolve_04
                    a_o "О, Рика-сан? Добрый день, добрый день, мм-хм-хм!"
                    a_f "Добрый день же, Ооиси. Дальше вопросы буду задавать я."
                    show ooishi yukata def_a2 with dissolve_02
                    a_o "Что ж, прошу любезно."
                    show ooishi yukata def_a1 with dissolve_02
                    $ question_5 = renpy.input("Оружие, которым угрожали Акасаке, чтобы тот отдал спасённого.", length=8)
                    if question_5 == pass_hima_5:
                        play sound wa_012
                        show rika hima wa_a1 with dissolve_02
                        a_f "Нипа-а~{font=DejaVuSans.ttf}☆{/font}. Верно!"
                        show rika hima ko_a1
                        show ooishi yukata aku_a1
                        with fastdown
                        $ question_6 = renpy.input("Кто перерезал провода?", length=8)
                        if question_6 in pass_hima_6:
                            play sound wa_012
                            show rika hima wa_a1 with dissolve_02
                            a_f "Ми-и!{w=0.8}{nw}"
                            show ooishi yukata wa_a1 with left_03
                            a_o "Мм-хм-хм-хм-хм..."
                            show rika hima ni_a1 with dissolve_02
                            $ question_7 = renpy.input("Ми-и?", length=7, exclude="~!.")
                            if (question_7.find(pass_hima_7[0]) != -1) or (question_7.find(pass_hima_7[1]) != -1) or (question_7.find(pass_hima_7[2]) != -1):
                                play sound wa_029
                                $ renpy.pause(0.2)
                                play sound wa_029
                                show rika hima wa_a1 with dissolve_02
                                a_f "Нипа-а-а! ~{font=DejaVuSans.ttf}☆{/font}"
                                show ooishi yukata def_a1 with dissolve_02
                                a_o "Поздравляю! Вы открыли четвёртую Главу!"
                                scene black with Dissolve(1.0)
                                $ renpy.pause(1.0)
                                jump otsukaresama_himatsubushi
                            else:

                                jump bad_answer
                        else:
                            jump bad_answer
                    else:
                        jump bad_answer
                else:
                    jump bad_answer
            else:
                jump bad_answer
        else:
            jump bad_answer
    else:
        jump bad_answer



label you_lied:

    stop music
    play sound wa_022
    show rena se hi_a1 with fastdown
    a_r "Так ты не знаешь содержания Главы, значит{cps=*0.3}.........{/cps}{w=0.5}{nw}"
    $ renpy.pause(5.0)
    show rena se hii_a1 with fastdown
    play sound usoda
    a_r "{size=72}ВРУША!!!!!{/size}{w=0.2}{nw}"
    hide rena

    queue sound wa_015
    queue sound wa_005
    $ renpy.pause(1.0)
    scene ryuuketu with ryuuketu_efe
    queue sound wa_030

    $ renpy.pause(1.0)
    scene black with m1
    $ renpy.pause(2.0)
    $ renpy.full_restart()

label not_interested:

    scene black with fade
    show mion si yo_a1 with dissolve_04
    a_m "Да ну тебя... Не знаешь ты текста Главы. Иди читай честно."
    hide mion with dissolve_04
    $ renpy.pause(0.2)

    $ renpy.full_restart()

label sad_sister:

    show mion se hau_a1 as real_mion
    show mion ki aku_a2
    with dissolve_02
    a_m "Хммм. И с чего ты взял?"
    a_m "Впрочем, кого это интересует. На большинство вопросов ответ неверный. Иди отсюда подобру-поздорову."

    $ renpy.full_restart()

label evil_sisters:

    stop music
    play sound wa_024
    show mion ki hi_a1
    show mion se hi_a2 as real_mion
    with Dissolve(3.0)
    $ renpy.pause(2.0, hard=True)
    play sound wa_015
    $ renpy.pause(0.5)
    play sound wa_030
    scene ryuuketu with efe_aa
    $ renpy.pause(1.0)
    scene black with down_30
    $ renpy.pause(2.0)
    "Эх, дуралей...{w=2.0}{nw}"

    $ persistent.chapter = False
    $ persistent.chapter_onik = False
    $ persistent.chapter_wata = False
    $ persistent.chapter_tata = False
    $ persistent.chapter_hima = False

    "Никогда не говори, что знаешь цвет нижнего белья цундере, при ней. Никогда.{w=3.0}{nw}"
    $ renpy.full_restart()

label eaten_by_satoko:

    scene ryuuketu with ryuuketu_efe
    queue sound wa_030

    $ renpy.pause(1.0)
    scene black with m1
    $ renpy.pause(2.0)
    "Тебя съела Сатоко.{w=1.0}{nw}"

    $ persistent.chapter = False
    $ persistent.chapter_onik = False
    $ persistent.chapter_wata = False
    $ persistent.chapter_tata = False
    $ persistent.chapter_hima = False

    "Воистину, печальный конец.{w=1.0}{nw}"
    $ renpy.full_restart()

label wrong_answer:

    play sound wa_040
    scene black with Dissolve(3.0)
    "Ответ неверен."
    $ renpy.full_restart()

label bad_answer:

    show ooishi si def_a1 with dissolve_02
    a_o "Боюсь, ответ неверен."
    show rika hima ko_a1 at sprava with dissolve_02
    a_f "Ми-и-и..."
    scene black with Dissolve(1.0)
    $ renpy.full_restart()







label dead_end:
    play sound wa_015
    $ renpy.pause(0.8)
    play sound wa_005
    return

label dead_end_2:
    play sound wa_015
    $ renpy.pause(0.8)
    play sound wa_017
    return


label onikakushi_prologue:

    $ save_name = "Пролог"


    $ mouse_visible = False
    scene black
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    $ renpy.pause(2.0)
    play music nageki_musicbox
    scene si_onikakusi with dissolve_02
    $ renpy.pause(20.0, hard=False)

    if persistent.matsuri:

        scene black with Dissolve(4.0)
        show text "{font=times.ttf}Вначале было лишь лёгкое беспокойство.{/font}" at truecenter with Dissolve(1.0)
        play sound oni001
        $ renpy.pause(2.0)
        hide text with Dissolve(1.0)

        show text "{font=times.ttf}Он и не думал причинять кому-либо зла.{/font}" at truecenter with Dissolve(1.0)
        play sound oni002
        $ renpy.pause(3.0)
        hide text with Dissolve(1.0)

        show text "{font=times.ttf}Но из беспокойства родилось одиночество,{/font}":
            xalign 0.5 yalign 0.45
        with Dissolve(1.0)
        play sound oni003
        $ renpy.pause(2.0)
        show text "{font=times.ttf}перешедшее затем в подозрение.{/font}" as text2:
            xalign 0.5 yalign 0.55
        with Dissolve(1.0)
        $ renpy.pause(2.0)
        hide text
        hide text2
        with Dissolve(1.0)
        show text "{font=times.ttf}Вскоре тёмные, кровожадные мысли поработили сердце.{/font}" at truecenter with Dissolve(1.0)
        $ renpy.pause(4.0)
        hide text with Dissolve(1.0)

        show text "{font=times.ttf}К прежней жизни уже не вернуться.{/font}":
            xalign 0.5 yalign 0.45
        with Dissolve(1.0)
        play sound oni004
        $ renpy.pause(1.0)
        show text "{font=times.ttf}Парень ступает всё дальше.{/font}" as text2:
            xalign 0.5 yalign 0.55
        with Dissolve(1.0)
        $ renpy.pause(2.0)
        hide text
        hide text2
        with Dissolve(1.0)

        show text "{font=times.ttf}Даже не замечая разверстого впереди колодца в ад.{/font}" at truecenter with Dissolve(1.0)
        play sound oni005
        $ renpy.pause(4.0)

    scene chapter 1 with Fade(3.0, 0.5, 1.0)
    play sound oni006
    $ renpy.pause(2.0)
    scene chapter onik_1 with Dissolve(2.0)
    $ renpy.pause(0.5)
    scene chapter onik_2 with Dissolve(2.0)
    play sound oni007
    $ renpy.pause(2.0)
    scene black with Dissolve(3.0)

    if persistent.matsuri:
        show text "{font=times.ttf}Трагедия, порождённая желанием верить.{/font}" at truecenter with Dissolve(1.0)
        play sound "sound/oni008.ogg"
        $ renpy.pause(2.0)
        hide text with Dissolve(1.0)

        show text "{font=times.ttf}Льющиеся слёзы — слёзы раскаяния, обиды ли?{/font}" at truecenter with Dissolve(1.0)
        play sound "sound/oni009.ogg"
        $ renpy.pause(5.0)
        hide text with Dissolve(2.0)
        $ renpy.pause(2.0)

    play sound wa_015
    $ renpy.pause(1.0)
    play sound wa_005
    scene tyuui_disclaimer with Dissolve(0.2)
    $ renpy.pause(0.5)
    scene black with Dissolve(4.0)
    play sound wa_015
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    play sound wa_005
    scene tyuui_s58 with Dissolve(0.2)
    scene black with Dissolve(4.0)
    play sound wa_015
    $ renpy.pause(1.0)
    play sound wa_005
    $ renpy.pause(0.35)
    scene black
    play sound wa_030
    $ renpy.pause(3.0)
    $ mouse_visible = True


    play ambient lsys11
    n "\n\n\n\nЕсли уж страданий не избежать...{nw}{w=2.0}"
    n "{nw}"
    n "То пусть лучше страдает тело.{nw}{w=4.0}"
    nvl clear

    n "\n\nЯ верил.{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Нет...{w=0.5} верю.{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Даже сейчас верю.{nw}{w=2.0}"
    nvl clear

    call dead_end
    n "\n\nНо уже начинаю осознавать.{nw}{w=2.0}"
    n "Я верю лишь потому, что не хочу признавать правду.{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Я пытаюсь себя убедить...{nw}{w=2.0}"
    n "Но как же дурацки звучит этот плачущий голос...{nw}{w=2.0}"
    call dead_end
    n "{nw}"
    n "Пропитывая лицо, из моих глаз вытекают слёзы...{nw}{w=2.0}"
    nvl clear

    n "\n\n\n\nМои однообразные движения прекратились, и в комнате стихло.{nw}{w=4.0}"
    nvl clear

    scene bg 204 with center
    n "\n\n\nВсё, что я слышу, — отвратительно громкий плач вечерних цикад...{nw}{w=2.0}"
    n "{nw}"
    n "Кажется...{nw}{w=1.5}"
    n "Я всё ещё слышу её...{nw}{w=2.0}"
    n "{nw}"
    n "...Да нет, не может быть такого.{nw}{w=2.0}"
    n "Она уж ничего не произносит.{nw}{w=4.0}"
    nvl clear

    n "\n\n\n\nРыдал один я.{nw}{w=2.0}"
    n "{nw}"
    n "Она же не проронила и слезинки.{nw}{w=4.0}"
    nvl clear

    n "\nКогда она повторяла одно и то же, её лицо не выражало ничего, никаких эмоций.{nw}{w=2.0}"
    n "Раз у неё нет слёз для меня...{nw}{w=1.0}"
    extend " тогда и с моей стороны их не будет.{nw}{w=2.0}"
    n "{nw}"
    n "Не стоит по ним плакать.{nw}{w=4.0}"
    nvl clear

    n "{nw}"
    n "\nНо... почему сердцу так больно, а в глазах стоят слёзы?....{nw}{w=2.0}"
    n "{nw}"
    n "Потому что... я хочу верить, что до сих пор\nне со всем порвал.{nw}{w=4.0}"
    nvl clear

    n "\n\n\nМожет быть, хватит?{nw}{w=2.0}"
    n "{nw}"
    n "Внутри моего сердца прозвучал мягкий голос...{nw}{w=4.0}"
    nvl clear

    n "\n\n\nТы достаточно настрадался.{nw}{w=2.0}"
    n "{nw}"
    n "Снова и снова мне хотелось избавиться от своего саднящего сердца.{nw}{w=2.0}"
    n "{nw}"
    n "И всё-таки... я упрямо не хотел от него отказываться.{nw}{w=4.0}"
    nvl clear

    n "\nБез этих страданий было бы много легче...{nw}{w=2.0}"
    n "{nw}"
    n "Даже зная это, разве не выбрал я верить?{nw}{w=2.0}"
    n "Только я знаю, насколько такое трудно, и только меня можно за это вознаградить.{nw}{w=4.0}"
    nvl clear

    n "\n\nЭй, «я».{nw}{w=2.0}"
    n "Ты сделал всё, что смог.{nw}{w=2.0}"
    n "Я знаю...{nw}{w=2.0}"
    n "{nw}"
    n "Так, может...{nw}{w=2.0}"
    n "Не хватит ли себя истязать?..{nw}{w=4.0}"
    nvl clear

    n "\n\n\n\nК тому же...... я не выбрасываю свою боль.{nw}{w=2.0}"
    n "Я оставлю её тут, с нею.{nw}{w=2.0}"
    n "{nw}"
    n "Как возлагают цветы...{nw}{w=4.0}"
    nvl clear

    n "\n\nИтак...{nw}{w=2.0}"
    n "Успокойся...{nw}{w=2.0}"
    n "{nw}"
    n "Правая рука налилась свинцом...{nw}{w=2.0}"
    n "Но подними её ещё раз.{nw}{w=2.0}"
    n "{nw}"
    n "С каждым взмахом я забываю.{nw}{w=4.0}"
    nvl clear

    call dead_end
    n "\n\nКак радовался твоей доброте.{nw}{w=2.0}"
    n "{nw}"
    call dead_end
    n "Как наслаждался твоей милой улыбкой.{nw}{w=2.0}"
    n "{nw}"
    call dead_end
    n "Я любил гладить тебя по голове.{nw}{w=2.0}"
    n "{nw}"
    call dead_end
    n "Любил эту твою застенчивость.{nw}{w=2.0}"
    call dead_end
    $ renpy.pause(0.3)
    queue sound wa_030
    nvl clear

    n "{nw}"
    n "Это последний взмах.{nw}{w=2.0}"
    n "{nw}"
    n "После него я всё забуду.{nw}{w=2.0}"
    n "{nw}"
    n "Это для тебя...{nw}{w=2.0}"
    n "{nw}"
    n "Мой первый и последний......{nw}{w=1.0}"
    extend " букет цветов.{nw}{w=4.0}"
    nvl clear

    $ renpy.pause(2.0)
    scene black with Dissolve(3.0)
    n "\n\n\nНе знаю точно...{nw}{w=1.0}"
    extend " Но, кажется...{nw}{w=2.0}"
    n "{nw}"
    n "{nw}"
    play sound wa_015
    n "{cps=*0.4}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{w=0.05}.{/cps}{nw}{w=1.0}"
    extend "я любил тебя.{nw}{w=3.0}"
    nvl clear

    play sound wa_005
    scene aka1
    show title at truecenter
    with Dissolve(0.01)
    $ renpy.pause(3.0)
    show black behind title with Dissolve(3.0)
    $ renpy.pause(2.0)
    scene black with Dissolve(2.0)

    jump onik_day0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
