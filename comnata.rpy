label d_kom:
    $ renpy.movie_cutscene('d_com.webm')
    call screen itag2

label sp_kom:
    $ renpy.movie_cutscene('sp_com.webm')
    call screen itag2

label per_kom:
    $ renpy.movie_cutscene('per_com.webm')
    call screen itag2

label vtr_kom:
    $ renpy.movie_cutscene('vtor_com.webm')
    call screen itag2

label van_kom:
    if stage == 2:
        $ renpy.movie_cutscene('ep10.webm')
        scene black
        pause 0.1
        scene bgm08 with Dissolve(1.5)
        pause 1.9
        menu:
            "Прибраться в ванной":
                $ stage = 3
                $ gostin = 1
                $ renpy.movie_cutscene('ep11.webm')
                scene black 
                call screen itag2
    else:
        $ renpy.movie_cutscene('van_com.webm')
        call screen itag2

label kuh_kom:
    $ renpy.movie_cutscene('kuh_com.webm')
    call screen itag1


label ulicha:
    play amby "audio/les2.ogg" fadeout 1.5 fadein 1.5
    $ renpy.movie_cutscene('ep13.webm')
    scene black
    pause 0.1
    scene bgm09 with Dissolve(2.5)
    pause 3.0

    menu:
        "Заняться прополкой":
            scene black with Dissolve(2.5)
            pause 2.5
            $ renpy.movie_cutscene('ep14.webm')
            stop music fadeout 1.5
            stop amby fadeout 1.5
            $ kuhnya = 1
            $ gostin = 1
            $ ulicha = 1
            $ stolov = 1
            $ stage = 5
            play amby "audio/les.ogg" fadeout 1.5 fadein 1.5
            call screen itag1
