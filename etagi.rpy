screen itag2:
    tag etagh
    if smena == 0:
        add "images/etag2d.png"
    else:
        add "images/etag2n.png"
    fixed:
        textbutton _("{outlinecolor=#ffffff}В дальнюю комнату") xalign 0.34 yalign 0.3 action [Hide("itag2"),Jump("d_kom")]
        textbutton _("{outlinecolor=#ffffff}В спальню") xalign 0.3 yalign 0.4 action [Hide("itag2"),Jump("sp_kom")]
        textbutton _("{outlinecolor=#ffffff}В первую комнату") xalign 0.25 yalign 0.5 action [Hide("itag2"),Jump("per_kom")]
        textbutton _("{outlinecolor=#ffffff}Во вторую комнату") xalign 0.20 yalign 0.6 action [Hide("itag2"),Jump("vtr_kom")]
        textbutton _("{outlinecolor=#ffffff}В ванную комнату") xalign 0.20 yalign 0.7 action [Hide("itag2"),Jump("van_kom")]
        textbutton _("{outlinecolor=#ffffff}На 1-й этаж") xalign 0.8 yalign 0.9 action [Hide("itag2"),Show("itag1")]

screen itag1:
    tag etagh
    if smena == 0:
        add "images/etag1d.png"#день
    else:
        add "images/etag1n.png"#ночь
    fixed:
        if kuhnya == 1:
            textbutton _("{outlinecolor=#ffffff}На кухню") xalign 0.4 yalign 0.5 action [Hide("itag1"),Jump("kuh_kom")]
        if gostin == 1:
            textbutton _("{outlinecolor=#ffffff}В гостинную") xalign 0.8 yalign 0.5 action [Hide("itag1"), Jump("gost_kom")]
        if stolov == 1:
            textbutton _("{outlinecolor=#ffffff}В столовую") xalign 0.95 yalign 0.6 action [Hide("itag1"), Jump("gost_kom")]
        textbutton _("{outlinecolor=#ffffff}На 2-й этаж") xalign 0.1 yalign 0.4 action [Hide("itag1"), Show("itag2")]
        if ulicha == 1:
            textbutton _("{outlinecolor=#ffffff}На улицу") xalign 0.5 yalign 0.95 action [Hide("itag1"),Jump("ulicha")]

        