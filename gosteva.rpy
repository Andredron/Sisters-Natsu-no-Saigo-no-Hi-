label gost_kom:
    if stage == 1 and days == 1:

        scene telo02
        play amby1 "sound/kran.ogg" fadeout 1.5 fadein 1.5
        $ renpy.movie_cutscene('ep02.webm')
        $ quick_menu = True
        au "............"

        play sound "sound/kran_off.ogg"
        scene telo03
        pause 1.0
        stop amby1
        pause 0.5

        voice "voice/006.ogg"
        nez "Наконец-то пришел."

        play sound "sound/shag2.ogg"
        scene telo04
        pause 0.5
        stop sound
        pause 1.6
        stop sound
        show rot_05

        voice "voice/007.ogg"
        nez "Соня{w=1.0}{nw}"

        show mor03
        $ store._history = False
        nez "Соня{fast}"

        $ store._history = True
        scene t53
        show rot_06

        voice "voice/008.ogg"
        nez "Как голова? Не болит?\nВсё в порядке?{w=2.5}{nw}"

        $ store._history = False
        show mor03
        nez "Как голова? Не болит?\nВсё в порядке?{fast}"

        au"............"

        $ store._history = True
        scene t53
        show rot_07

        voice "voice/009.ogg"
        nez "Что такое? Ещё не проснулся?{w=2.0}{nw}"

        $ store._history = False
        show mor03
        nez "Что такое? Ещё не проснулся?{fast}"

        $ store._history = True


        menu:
            "Да":
                au"Да..."

                scene t53
                show rot_08
                voice "voice/010.ogg"
                nez "Ну-ну. Покушай, и сон как рукой снимет.{w=4.0}{nw}"

                $ store._history = False
                show mor03
                nez "Ну-ну. Покушай, и сон как рукой снимет.{fast}"
                $ store._history = True

            "Нет":
                au"Нет..."

                scene telo05
                pause 0.8
                show rot_09

                voice "voice/011.ogg"
                nez "Хи-хи. Пойдём за стол."

        scene black with Dissolve(1.5)
        pause 1.5
        scene bgm04 with Dissolve(1.5)
        pause 1.5


        voice "voice/012.ogg"
        nez "Ой..."
        au"?"

        voice "voice/013.ogg"
        nez "Куда я перец положила?"

        voice "voice/014.ogg"
        nez "Может, он остался в кладовке?"
        au"............"

        stop amby
        scene black with Dissolve(1.5)
        pause 1.5
        play amby "audio/les.ogg" fadeout 1.5 fadein 1.5

        scene bgm05 with Dissolve(1.5)
        pause 1.5


        voice "voice/015.ogg"
        nez "Хи-хи-хи."

        scene black with Dissolve(1.5)
        pause 1.5

        scene t60 with Dissolve(1.5)
        pause 1.5
        play music "music/bgm02.mp3" fadeout 1.5 fadein 1.5
        show rot_10


        voice "voice/016.ogg"
        nez "Ну и дурочка я.\nОн был на столе."

        scene t60
        
        au "Э-э-э..."

        scene t60
        show rot_11

        voice "voice/017.ogg"
        nez "Пока ты спал, я целый час не могла найти оливковое масло."

        stop amby
        pause 1.0
        play amby "audio/les.ogg" fadeout 1.5 fadein 1.5

        scene t60
        au "Ха-ха-ха-ха."


        scene t61 with dissolve
        show telo06
        pause 0.5
        show rot_12

        voice "voice/018.ogg"
        nez "Слава богу.{w=1.5}{nw}"

        show mor04
        $ store._history = False
        nez "Слава богу.{fast}"

        $ store._history = True

        au "?"

        scene t61
        show rot_13

        voice "voice/019.ogg"
        nez "Похоже, ты в полном порядке.{w=1.9}{nw}"

        show mor04
        $ store._history = False

        nez "Похоже, ты в полном порядке.{fast}"

        $ store._history = True

        au "Ага."

        scene black with Dissolve(1.5)
        pause 1.5

        scene bgm05 with Dissolve(1.5)
        pause 1.5

        voice "voice/020.ogg"
        nez "Ты наелся? Может тебе еще хлеба пожарить?"

        scene black with Dissolve(1.5)
        pause 1.5

        scene t61
        show mor04
        with Dissolve(1.5)

        au "............"

        scene telo07
        pause 1.8
        show rot_14

        voice "voice/021.ogg"
        nez "Наверное, для парня, этой порции, было мало.{w=2.6}{nw}"

        show mor05
        $ store._history = False

        nez "Наверное, для парня, этой порции, было мало.{fast}"

        $ store._history = True

        au "............"

        scene t73
        show t73_8
        pause 0.5
        show rot_15

        voice "voice/022.ogg"
        nez "Что-то не так?{w=1.8}{nw}"

        show mor06
        $ store._history = False

        nez "Что-то не так?{fast}"

        $ store._history = True

        au "Э?.. Всё в порядке."

        scene t73
        show telo08
        pause 2.0
        show rot_16

        voice "voice/023.ogg"
        nez "Кушай как следует. Тебе ещё много дел надо сделать.{w=3.8}{nw}"
        
        show mor04
        $ store._history = False

        nez "Кушай как следует. Тебе ещё много дел надо сделать.{fast}"

        $ store._history = True


        au "Дел?.."

        show telo09
        pause 0.5
        scene t60
        show rot_17

        voice "voice/024.ogg"
        nez "А, уже забыл?{w=4.8}{nw}"

        $ store._history = False

        nez "А, уже забыл?{fast}"

        $ store._history = True


        menu:
            "Да":

                scene t61 
                show telo10
                pause 3.3
                show rot_18

                voice "voice/028.ogg"
                nez "Ой-ей, уже забыл?"

            "Нет":

                pause 0.5
                scene t61
                show telo11
                pause 0.5
                show rot_19

                voice "voice/025.ogg"
                nez "Чем займёшься?{w=4.8}{nw}"

                show mor04
                $ store._history = False

                nez "Чем займёшься?{fast}"

                $ store._history = True

                au "............"
                
                voice "voice/026.ogg"
                nez "......"
                
                au "Чем займусь?.."

                scene t61 
                show telo10
                pause 3.3
                show rot_18

                voice "voice/027.ogg"
                nez "Ой-ей, уже забыл?"

        scene black with Dissolve(1.0)
        pause 1.0
        play sound "audio/pishet.ogg"
        pause 4.0
        stop sound
        scene bgm06 with Dissolve(1.0)
        pause 1.0

        voice "voice/029.ogg"
        nez "Держи. Всё понятно?"

        scene black with Dissolve(1.0)
        pause 1.0
        scene t61
        show t61_3
        with Dissolve(1.0)
        pause 1.0
        show mor07
        pause 0.5
        scene t61
        show rot_20

        voice "voice/030.ogg"
        nez "Вот твой список задач.{w=4.8}{nw}"

        $ store._history = False
        show mor04

        nez "Вот твой список задач.{fast}"
        $ store._history = True

        scene t61
        show rot_21

        voice "voice/031.ogg"
        nez "Прибраться в ванной комнате, прополоть сорняки и сколотить забор во дворе.{w=4.8}{nw}"

        show mor04
        $ store._history = False

        nez "Прибраться в ванной комнате, прополоть сорняки и сколотить забор во дворе.{fast}"

        $ store._history = True

        scene telo07
        pause 1.2
        show rot_22
        voice "voice/032.ogg"
        nez "Наверное, стоит начать с ванной комнаты.{w=4.8}{nw}"

        show mor05
        $ store._history = False
        $ stage = 2
        nez "Наверное, стоит начать с ванной комнаты.{fast}"

        $ store._history = True
        pause 1.0
        stop music fadeout 1.5 
        stop amby fadeout 1.5 
        scene black with Dissolve(2.0)
        pause 2.0
        play amby "audio/les.ogg" fadeout 1.5 fadein 1.5
        $ kuhnya = 1
        call screen itag1








    elif stage == 2 and days == 1:
        $ renpy.movie_cutscene('shag_k.webm')
        #$ renpy.notify "Девушка:Лето пришло! Лето пришло! Лето пришло!\nМужчина: Порадуй себя этим летом кисленьким коктейлем Сауэр!\nДевушка:Лето пришло!"
        play sound "audio/tv01.ogg" fadeout 1.5 fadein 1.5
        play amby1 "audio/tv_fon.ogg" fadeout 1.5 fadein 1.5
        scene bgm07 at lev_prav
        pause 10.0


        voice "voice/033.ogg"
        nez "М-м? Что такое?"
        stop amby1 fadeout 1.5

        scene black with Dissolve(1.5)
        pause 1.5
        stop sound
        scene t86 with Dissolve(1.5)
        pause 1.5
        show rot_23
    

        voice "voice/034.ogg"
        nez "Ты что... забыл, что нужно сделать?{w=4.8}{nw}"
        show mor08
        $ store._history = False

        nez "Ты что... забыл, что нужно сделать?{fast}"

        $ store._history = True

        menu:
            "Забыл":
                scene telo12
                pause 2.0
                show mor09
                pause 1.0
                scene t101
                show rot_24


                voice "voice/036.ogg"
                nez "Вот как? Тебе нужно прибраться в ванной комнате.{w=4.8}{nw}"

                show mor09
                $ store._history = False

                nez "Вот как? Тебе нужно прибраться в ванной комнате.{fast}"

                $ store._history = True
                pause 0.5
                scene t101
                show telo13
                pause 3.5
                show rot_25


                voice "voice/037.ogg"
                nez "Потрудись как следует.{w=4.8}{nw}"

                $ store._history = False

                nez "Потрудись как следует.{fast}"

                $ store._history = True
                scene black with Dissolve(1.5)
                pause 1.5

            "Не забыл":
                scene telo14
                pause 2.1
                show rot_26

                voice "voice/035.ogg"
                nez "Угу. Потрудись как следует.{w=4.8}{nw}"

                $ store._history = False

                nez "Угу. Потрудись как следует.{fast}"

                $ store._history = True

                scene black with Dissolve(2.0)
                pause 2.0
        $ gostin = 0
        call screen itag1







    elif stage == 3 and days == 1:
        $ renpy.movie_cutscene('shag_k.webm')
        play sound "audio/tv02.ogg" fadeout 1.5 fadein 1.5
        play amby1 "audio/tv_fon.ogg" fadeout 1.5 fadein 1.5
        scene bgm07_1 at lev_prav
        pause 13.0

        scene black with Dissolve(1.5)
        stop sound
        stop amby1 fadeout 1.5
        pause 1.5
        scene t116
        show mor10
        with Dissolve(2.0)
        pause 2.0

        au ".................."

        scene t117 at verh_niz
        pause 6.5
        
        au ".................."

        scene t118 at verh_niz2
        pause 5.0

        au ".................."

        scene t118 at verh_niz3
        pause 4.5
        scene t119
        show mor11

        au ".................."

        scene telo15
        pause 1.0
        show mor12
        pause 0.5

        voice "voice/038.ogg"
        nez "Хи-хи..."

        scene telo16
        pause 0.6
        play sound "sound/polosh.ogg"
        pause 1.9
        stop sound
        scene black with Dissolve(1.5)
        pause 1.5
        play sound "sound/shag2.ogg"
        pause 0.6
        stop sound
        show t154 with moveinright
        pause 3.0
        scene black with Dissolve(1.5)
        play sound "sound/dver_ot2.ogg"
        pause 1.5
        scene t155 with Dissolve(1.5)
        pause 1.5
        show rot_27


        voice "voice/039.ogg"
        nez "Ты отлично прибрался в ванной.{w=3.6}{nw}"

        $ store._history = False
        show mor13_1

        nez "Ты отлично прибрался в ванной.{fast}"

        $ store._history = True
        scene t155
        show telo17
        pause 1.5
        show rot_28

        voice "voice/040.ogg"
        nez "Дальше займись прополкой сорняков.{w=4.3}{nw}"

        $ store._history = False

        nez "Дальше займись прополкой сорняков.{fast}"

        stop music
        stop amby
        $ store._history = True
        scene black with Dissolve(2.5)
        pause 2.5
        $ kuhnya = 1
        $ gostin = 1
        $ ulicha = 1
        $ stage = 4
        play amby "audio/les.ogg" fadeout 1.5 fadein 1.5
        call screen itag1








    elif stage == 4 and days == 1:
        $ renpy.movie_cutscene('shag_k.webm')
        scene black with Dissolve(0.5)
        pause 0.5
        scene t86 with Dissolve(2.0)
        pause 2.0
        show rot_29

        voice "voice/041.ogg"
        nez "Ты что... забыл, что нужно сделать?{w=5.3}{nw}"

        $ store._history = False
        show mor13

        nez "Ты что... забыл, что нужно сделать?{fast}"
        $ store._history = True

        menu:
            "Забыл":
                scene t86
                pause 0.1
                scene telo12
                pause 2.0
                show rot_30

                voice "voice/042.ogg"
                nez "Ну же. Займись прополкой сорняков во дворе.{w=4.8}{nw}"
                
                $ store._history = False
                show mor14

                nez "Ну же. Займись прополкой сорняков во дворе.{fast}"

                $ store._history = True

                scene telo18
                pause 4.1
                show rot_31
                
                voice "voice/043.ogg"
                nez "Постарайся на славу.{w=1.5}{nw}"

                $ store._history = False

                nez "Постарайся на славу.{fast}"
                $ store._history = True
                stop music
                stop amby
                scene black with Dissolve(2.5)
                pause 2.5
                $ kuhnya = 1
                $ gostin = 0
                $ ulicha = 1
                $ stage = 4
                play amby "audio/les.ogg" fadeout 1.5 fadein 1.5
                call screen itag1

            "Не забыл":

                scene t86
                show rot_32

                voice "voice/044.ogg"
                nez "Молодец. Постарайся на славу.{w=2.8}{nw}"
                
                $ store._history = False
                show mor08

                nez "Молодец. Постарайся на славу.{fast}"

                $ store._history = True
                stop music
                stop amby
                scene black with Dissolve(2.5)
                pause 2.5
                $ kuhnya = 1
                $ gostin = 0
                $ ulicha = 1
                $ stage = 4
                play amby "audio/les.ogg" fadeout 1.5 fadein 1.5
                call screen itag1







    elif stage == 5 and days == 1:
        $ renpy.movie_cutscene('shag_k.webm')
        scene black with Dissolve(0.5)
        pause 0.5
        $ renpy.music.set_volume(1.0)
        play amby1 "audio/tv_fon.ogg" fadeout 1.5
        show bgm07_1 at lev_prav
        
        voice "voice/045.ogg"
        nov "Вчера днём, в 11 часов 13 минут, неопознанный молодой человек, ехавший на велосипеде по трассе Окутама Шу и попавший в аварию..."
        
        voice "voice/046.ogg"
        nov "...скончался в больнице."

        stop amby1 fadeout 1.5
        scene black with Dissolve(1.5)
        pause 1.5

        scene bgm10:
            xalign 1.0 yalign 1.0
            linear 5.5 xalign 0.1 yalign 1.0

        with Dissolve(2.5)

        voice "voice/047.ogg"
        nov "Полиция продолжает поиск водителя, скрывшегося с места происшествия.\nДалее, новости погоды..."
        
        scene bgm10:
            xalign 0.1 yalign 1.0
            linear 10.5 xalign 1.0 yalign 0.0

        pause 11.0
        au ".................."

        menu:
            "Приблизиться":
                pass

        scene bgm10:
            xalign 1.0 yalign 0.0

        pause 0.5

        show t156 with Dissolve(3.5)
        pause 1.5
        scene telo19
        play sound "sound/shag3.ogg"
        pause 1.0
        stop sound
        pause 5.3
        scene telo20

        voice "voice/048.ogg"
        nez "М-м...{w=1.2}{nw}"

        $ store._history = False
        show mor15

        nez "М-м...{fast}"
        $ store._history = True

        scene t176
        show rot_33

        nez "Мх...{w=1.1}{nw}"

        $ store._history = False
        show mor15

        voice "voice/049.ogg"
        nez "Мх...{fast}"

        $ store._history = True
        au "......"

        scene t177
        pause 0.1
        scene t178
        pause 0.1
        scene t179
        pause 0.1
        show mor16

        voice "voice/050.ogg"
        nez "Хи-хи..."

        scene telo21
        pause 1.2
        show mor17

        au "..........."

        scene telo22
        pause 1.1
        show rot_34

        voice "voice/051.ogg"
        nez "Травинка...{w=1.0}{nw}"

        $ store._history = False
        show mor18

        nez "Травинка...{fast}"

        $ store._history = True

        au"А..."

        scene telo23
        pause 0.5

        voice "voice/052.ogg"
        nez "Хи-хи-хи."

        scene black with Dissolve(1.5)
        stop music fadeout 1.5
        stop amby1 fadeout 1.5
        pause 1.5 
        play amby1 "audio/tv_fon.ogg" fadeout 1.5
        play music "audio/tv_oper.ogg" fadeout 1.5
        show bgm07_2 with Dissolve(1.5)
        pause 1.0

        voice "voice/053.ogg"
        svek "Акико-сан!"

        voice "voice/054.ogg"
        neves "В ч-чём дело, матушка?.."

        voice "voice/055.ogg"
        svek "Ты неправильно солишь цукэмоно, ну кто тебя так учил?!"

        voice "voice/056.ogg"
        neves "Простите, матушка..."

        voice "voice/057.ogg"
        svek "Ничего страшного, Акико-сан..."

        stop amby1 fadeout 1.5
        scene black with Dissolve(1.5)
        pause 1.5
        scene t208 with Dissolve(1.5)
        pause 1.5
        show rot_35

        voice "voice/058.ogg"
        nez "А...{w=3.0}{nw}"

        $ store._history = False
        show mor19

        nez "А...{fast}"
        $ store._history = True

        au "Э?"

        scene telo24
        pause 2.0
        show rot_36

        voice "voice/059.ogg"
        nez "Девушку в телевизоре...{w=1.5}{nw}"

        $ store._history = False
        show mor20

        nez "Девушку в телевизоре...{fast}"

        $ store._history = True

        au "......"

        scene t221
        show t221_4
        pause 0.3
        show t221_10
        pause 0.1
        show t221_8
        pause 0.1
        show rot_37

        voice "voice/060.ogg"
        nez "Зовут так же, как и меня. Акико.{w=4.2}{nw}"

        $ store._history = False
        show mor21

        nez "Зовут так же, как и меня. Акико.{fast}"

        $ store._history = True

        au "Акико?.."

        scene t221
        show rot_38

        voice "voice/061.ogg"
        akik "Все верно.{w=1.1}{nw}"

        $ store._history = False
        show mor21

        akik "Все верно.{fast}"
        $ store._history = True

        au "............"

        scene t221
        show telo25
        pause 1.9
        show rot_39

        voice "voice/062.ogg"
        akik "Спасибо за помощь с сорняками.{w=2.7}{nw}"

        $ store._history = False
        show mor22

        akik "Спасибо за помощь с сорняками.{fast}"

        $ store._history = True

        scene t232
        pause 0.1
        show t232_9
        pause 0.1
        show t232_10
        pause 0.1
        show t232_6
        pause 0.5
        show rot_40


        voice "voice/063.ogg"
        akik "Теперь забор. Ты уж потрудись."

        $ kuhnya = 1
        $ gostin = 1
        $ ulicha = 1
        $ stolov = 0
        $ stage = 6
        stop music fadeout 1.5
        stop amby fadeout 1.5
        scene black with Dissolve(2.5)
        pause 2.5
        play amby "audio/les.ogg" fadeout 1.5 fadein 1.5
        call screen itag1

    elif stage == 6 and days == 1:
        scene t232 with Dissolve(1.5)
        pause 1.5
        show rot_41

        voice "voice/064.ogg"
        akik "Ты что... забыл, что нужно сделать?{w=2.7}{nw}"

        $ store._history = False
        show mor22

        akik "Ты что... забыл, что нужно сделать?{fast}"

        $ store._history = True

        menu:
            "Не забыл":
                voice "voice/065.ogg"
                akik "Молодец. Постарайся."

            "Забыл":

                scene telo26
                pause 1.9
                scene t246
                show t246_1
                pause 0.1
                show t246_2
                pause 0.1
                scene t246
                pause 0.3
                show rot_42

                voice "voice/066.ogg"
                akik "Ну вот. Тебе нужно сколотить забор.{w=4.5}{nw}"

                $ store._history = False
                show mor23

                akik "Ну вот. Тебе нужно сколотить забор.{fast}"

                $ store._history = True

                scene telo27
                pause 1.1
                scene t257
                show t257_1
                pause 0.1
                scene t257

                voice "voice/067.ogg"
                akik "Постарайся."

        $ kuhnya = 1
        $ gostin = 0
        $ ulicha = 1
        $ stolov = 0
        $ stage = 6
        scene black with Dissolve(2.5)
        pause 2.5
        call screen itag1







        









