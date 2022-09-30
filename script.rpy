label start:
    scene adidas
    au "оригинал файлы"
    scene t244
    au "которые модиф движком"

    $ renpy.music.set_volume(0.1, channel ='amby')
    show screen my_keys
    $ quick_menu = False
    stop music
    $ stage = 0 #основные события
    $ smena = 0 #1 ночь, 0 день
    $ days = 1 
    $ kuhnya = 0
    $ gostin = 1
    $ ulicha = 0
    $ stolov = 0

    scene black with Dissolve(1.0)
    pause 0.5
    centered "ВНИМАНИЕ\n\nПросим обратить внимание, что распространение игры через сеть Интернет без разрешения правообладателя запрещено.\n\nКроме того, скачивание игры из сети Интернет запрещено и не является копированием для частного использования.\n\nБлагодарим вас за понимание.{fast}{w=5} {nw}" 
    with Dissolve(1.0)
    pause 1.5
    $ renpy.movie_cutscene('vid.webm')

    play amby "audio/les.ogg" fadeout 1.5 fadein 1.5
    play sound "sound/dver_ot.ogg"

    centered "1990 год{w=1} {nw}"
    
    pause 1.0

    centered "1 августа{w=1} {nw}"

    scene black with Dissolve(3.0)
    $ quick_menu = True

    scene p01
    $ renpy.movie_cutscene('ep01.webm')
    pause 0.1
    show rot_01

    voice "voice/001.ogg"
    nez "Доброе утро.{w=0.7}{nw}" 
    show mor01

    $ store._history = False

    nez "Доброе утро.{fast}"

    $ store._history = True



    scene telo01
    pause 3.2
    scene p02
    show rot_02
    voice "voice/002.ogg"
    nez "Проснулся?{w=0.5}{nw}"

    $ store._history = False
    show mor02
    nez "Проснулся?{fast}"

    scene p02
    $ store._history = True
    show rot_03
    voice "voice/003.ogg"
    nez "{w=0.5}Как себя чувствуешь?{w=1.0}{nw}"

    $ store._history = False
    show mor02
    nez "Как себя чувствуешь?{fast}"

    $ store._history = True
    au "......."

    scene p02
    show rot_04
    voice "voice/004.ogg"
    nez "Ой-ей, все ещё дремешь?{w=4.5}{nw}"
    show mor02
    $ store._history = False
    nez "Ой-ей, все ещё дремешь?{fast}"


    $ store._history = True
    scene black with Dissolve(1.5)
    pause 1.5
    scene bgm01 with Dissolve(1.5)
    pause 1.5

    voice "voice/005.ogg"
    nez "Как проснёшься, спускайся завтракать."
 
    scene black with Dissolve(1.5)
    pause 1.5
    play sound "sound/shag2.ogg"
    scene bgm02 with Dissolve(1.5)
    pause 2.5
    scene bgm03 with Dissolve(1.5)
    pause 2.5
 
    menu:
        "Выйти из комнаты":
            $ stage = 1

    
    scene black with Dissolve(1.5)
    play sound "sound/shag3.ogg"
    pause 1.5
    stop sound
    call screen itag2

