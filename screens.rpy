################################################################################
## Инициализация
################################################################################

init offset = -1


################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Если есть боковое изображение ("голова"), показывает её поверх текста.
    ## По стандарту не показывается на варианте для мобильных устройств — мало
    ## места.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height


style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height



    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


    adjust_spacing False

## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")


style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv",who=__("Выбрали:"),what=__(i.caption))]


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 169
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

screen quick_menu():

    ## Сука, ебанный костыль!!!! Аж самому противно, но по другому никак
    zorder 100

    if quick_menu:

        frame:
            background None
            style_prefix "quick"
            textbutton "{size=+10}{alpha=0.0}w" xalign 0.76 yalign 0.85 action HideInterface()
            textbutton "{size=+10}{alpha=0.0}w" xalign 0.80 yalign 0.85 action ShowMenu('save')
            textbutton "{size=+10}{alpha=0.0}w" xalign 0.834 yalign 0.85 action ShowMenu('load')
            textbutton "{size=+10}{alpha=0.0}w" xalign 0.87 yalign 0.85 action ShowMenu('preferences')
            textbutton "{size=+10}{alpha=0.0}ws" xalign 0.92 yalign 0.85 action QuickSave()
            textbutton "{size=+10}{alpha=0.0}ws" xalign 0.96 yalign 0.85 action QuickLoad()


## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():

    vbox:
        style_prefix "navigation"

        yalign 0.82
        xalign 0.48

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Начать") action Start()

        else:

            textbutton _("История") action ShowMenu("history")

            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")

        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Завершить повтор") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Главное меню") action MainMenu()

        textbutton _("Экстра") action ShowMenu("about")


        if renpy.variant("pc"):

            ## Кнопка выхода блокирована в iOS и не нужна на Android и в веб-
            ## версии.
            textbutton _("Выход") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu

    add gui.main_menu_background

    ## Эта пустая рамка затеняет главное меню.
    frame:
        style "main_menu_frame"

    ## Оператор use включает отображение другого экрана в данном. Актуальное
    ## содержание главного меню находится на экране навигации.
    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text


style main_menu_vbox:
    xalign 1.0
    xoffset -12
    xmaximum 500
    yalign 1.0
    yoffset -12

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None, или "viewport", или "vpgrid", когда этот
## экран предназначается для использования с более чем одним дочерним экраном,
## включённым в него.

screen game_menu(title=None, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add black2

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    if preferences:
        pass
    elif about:
        pass 
    elif save:
        pass
    elif load:
        pass
    else:
        use navigation

    textbutton _("Вернуться"):
            xalign 0.95 yalign 0.92 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 19
    top_padding 75

style game_menu_navigation_frame:
    xsize 175
    yfill True

style game_menu_content_frame:
    left_margin 25
    right_margin 13
    top_margin 7

style game_menu_viewport:
    xsize 575

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 7

style game_menu_label:
    xpos 32
    ysize 75

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -18


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save():
    add "save_mm3"
    add "save_mm2"
    tag menu

    use file_slots(_("Сохранить"))


screen load():
    add "save_mm"
    add "save_mm2"

    tag menu

    use file_slots(_("Загрузить"))


define file_slots_current_file = 0
    
screen file_slots(title):
      
    if file_slots_current_file > 0:
        add FileScreenshot(file_slots_current_file) pos(440,175)
    
    if file_slots_current_file < 0:
        add FileScreenshot(abs(file_slots_current_file), page = "quick") pos(440,175)    

    fixed pos (50,100):
        vbox box_wrap True:
            xfill True
            # transpose True
            spacing -29
            $ rows = 10
            for i in range(1, rows + 1):
                button:
                    action FileAction(i)
                    hovered [SetVariable("file_slots_current_file", i)]
                    unhovered [SetVariable("file_slots_current_file", 0)]
                    
                    fixed fit_first True:
                        # add FileScreenshot(i)

                        xfill True
                        #$ file_name = FileSlotName(i, rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)
                        text "[file_time!t]\n[save_name!t]"

    fixed pos (50,389): ###qsave
        vbox box_wrap True:
            xfill True
            # transpose True
            spacing -30
            $ rows = 1
            for i in range(1, rows + 1):
                button:
                    action FileLoad (1, confirm = False, page = "quick", newest = True)
                    hovered [SetVariable("file_slots_current_file",-1)]
                    unhovered [SetVariable("file_slots_current_file", 0)]
                 
                    fixed fit_first True:

                        xfill True
                        #$ file_name = FileSlotName(i, rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."), page = "quick")
                        $ save_name = FileSaveName(i, page = "quick")
                        text "[file_time!t]\n[save_name!t]"
                        
    textbutton _("Вернуться"):
        xalign 0.95 yalign 0.92 
        text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
        action Return()



screen file_slots2(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        fixed:

            ## Это гарантирует, что ввод будет принимать enter перед остальными
            ## кнопками.
            order_reverse True

            ## Номер страницы, который может быть изменён посредством клика на
            ## кнопку.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Таблица слотов.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Кнопки для доступа к другим страницам.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}А") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Б") action FilePage("quick")

                ## range(1, 10) задаёт диапазон значений от 1 до 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 32
    ypadding 2

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
default a = "a.1"

screen preferences():
    add "images/pref.png"
    add "images/pref2.png"   
    tag menu
    fixed:

        label _("{size=25}{color=#ffffff}Язык:"):
            xalign 0.02 yalign 0.16 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        textbutton _("Русский"): 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            xalign 0.02 yalign 0.2
            action Language(None)
        textbutton _("English"): 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            xalign 0.02 yalign 0.24
            action Language("english")
        textbutton _("Српски"): 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            xalign 0.02 yalign 0.28
            action Language("serbian")

        label _("{size=25}{color=#ffffff}Шрифт"):
            xalign 0.23 yalign 0.16 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        textbutton _("По умолчанию"): 
            xalign 0.46 yalign 0.17
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action gui.SetPreference("font", "DejaVuSans.ttf")
        textbutton _("DuduCyrillic"):
            xalign 0.62 yalign 0.17
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action  gui.SetPreference("font", "font/duducyrillic.ttf") 
        textbutton _("Philosopher"): 
            xalign 0.75 yalign 0.17
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action  gui.SetPreference("font", "font/philosopher.ttf")
        
        label _("{size=24}{color=#ffffff}Пропуск"): 
            xalign 0.23 yalign 0.24
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        textbutton _("Только просмотренный текст"): 
            xalign 0.5 yalign 0.24 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action Preference("skip", "seen")
        textbutton _("Весь текст"): 
            xalign 0.75 yalign 0.24 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action Preference("skip", "all")
        
        label _("{size=22}{color=#ffffff}Авточтение"): 
            xalign 0.23 yalign 0.32
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        textbutton _("Включить"): 
            xalign 0.5 yalign 0.32 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action [Preference("auto-forward", "toggle"), Preference("auto-forward after click", "enable")]
        textbutton _("Выключить"): 
            xalign 0.75 yalign 0.32 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action [Preference("auto-forward", "disable"), Preference("auto-forward after click", "disable")]
        
        label _("{size=22}{color=#ffffff}Youtub\nрежим"): 
            xalign 0.23 yalign 0.4 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        textbutton _("Включить"): 
            xalign 0.5 yalign 0.4 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action [SetField(persistent, "youtuber_mode", True), YoutubeToggle(True)]
        textbutton _("Выключить"): 
            xalign 0.75 yalign 0.4 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action [SetField(persistent, "youtuber_mode", False), YoutubeToggle(False)]
        
            

        label _("{size=25}{color=#ffffff}Музыка"):
            xalign 0.23 yalign 0.66 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        bar value Preference("music volume"):
            xmaximum 330
            xalign 0.61 yalign 0.66

        label _("{size=25}{color=#ffffff}Голос"):
            xalign 0.23 yalign 0.72 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        bar value Preference("voice volume"):
            xmaximum 330
            xalign 0.61 yalign 0.72

        label _("{size=25}{color=#ffffff}Звук"):
            xalign 0.23 yalign 0.78 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        bar value Preference("sound volume"):
            xmaximum 330
            xalign 0.61 yalign 0.78

        label _("{size=25}{color=#ffffff}Фон"):
            xalign 0.23 yalign 0.84 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ]
        bar value Preference("amby volume"):
            xmaximum 330
            xalign 0.61 yalign 0.84
        
        textbutton _("Вернуться"):
            xalign 0.95 yalign 0.92 
            text_outlines [ (absolute(1), "#333333", absolute(1), absolute(1)) ] 
            action Return()
            
screen preferences2():
    
    tag menu
    

    use game_menu(_("Настройки"), scroll="viewport"):


        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Пропуск")
                    textbutton _("Всего текста") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")
                    textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))

                ## Дополнительные vbox'ы типа "radio_pref" или "check_pref"
                ## могут быть добавлены сюда для добавления новых настроек.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")

                    bar value Preference("text speed")

                    label _("Скорость авточтения")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 141

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 219

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 7

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 282


## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    
    use game_menu(_("{alpha=0.0}История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                if h.who:

                    if h.voice and h.voice.filename:                                      
                        textbutton "▶" action Play("voice", h.voice.filename) xpos 0 ypos 0

                    textbutton _("Прыжок") action RollbackToIdentifier(h.rollback_identifier) xpos 0 ypos 30

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Берёт цвет из who параметра персонажа, если он
                        ## установлен.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")


## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 10

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Пробел")
        text _("Прохождение диалогов без возможности делать выбор.")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Esc")
        text _("Вход в игровое меню.")

    hbox:
        label _("Ctrl")
        text _("Пропускает диалоги, пока зажат.")

    hbox:
        label _("Tab")
        text _("Включает режим пропуска.")

    hbox:
        label _("Page Up")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Page Down")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label "H"
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label "S"
        text _("Делает снимок экрана.")

    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")

    hbox:
        label "Shift+A"
        text _("Открывает меню специальных возможностей.")


screen mouse_help():

    hbox:
        label _("Левый клик")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label _("Правый клик")
        text _("Вход в игровое меню.")

    hbox:
        label _("Колёсико вверх\nКлик на сторону отката")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Колёсико вниз")
        text _("Откатывает предыдущее действие вперёд.")


screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")


    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Start, Guide")
        text _("Вход в игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")

    textbutton _("Калибровка") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 5

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 157
    right_padding 13

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 19

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 63

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 4

            text _("Пропускаю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 15.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 282

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 213

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 250

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 375
