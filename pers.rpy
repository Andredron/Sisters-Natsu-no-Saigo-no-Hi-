
init python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

image movie = Movie(size=(config.screen_width, config.screen_height))

init python:
    renpy.music.register_channel("amby", mixer='amby', loop=True, stop_on_mute=True, tight=False, buffer_queue=True)
    renpy.music.register_channel("amby1", mixer='music', loop=True, stop_on_mute=True, tight=False, buffer_queue=True)
# автоматическое объявление
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ["images"]

init python:
    mtime = 1.5 # время в пути
    moveinright = MoveTransition(mtime, enter=_moveright)

init:
    transform lev_prav:
            xalign 1.0
            linear 8.5 xalign 0.0

    transform verh_niz:
            yalign 0.0
            linear 2.5 yalign 0.5
            linear 3.5 yalign 1.0
    transform verh_niz2:
            yalign 1.0
            linear 4.5 yalign 0.5
    transform verh_niz3:
            yalign 0.5
            linear 3.5 yalign 0.0

screen my_keys:
    key "mousedown_5" action ShowMenu("history")
    key 'K_ESCAPE' action ShowMenu('preferences')
    key 'mouseup_3' action ShowMenu('save')

# копия стандартного сэйбокса, но с режимом субтитров
screen say2(who, what):
    style_prefix "say"

    use my_keys

    if not persistent.youtube_mode:
        window:
            id "window"

            # копия обычного сэйбокса
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            text what id "what"
            if not renpy.variant("small"):
                add SideImage() xalign 0.0 yalign 1.0
    else:
        frame:
            style "empty"               # The empty style resets the frame to no background, margins, or padding.
            background "#000"           # Set the background to black.
            padding (5, 5)              # Add a bit of padding.
            align (.5, 1.)
            yoffset -25

            text what:
                id "what"               # Ren'Py needs this for a say screen to work.
                pos (0, 0)              # This screen needs the text to be positioned at (0, 0)
                layout "subtitle"       # Subtitle layout tries to make all lines even.
                text_align 0.5          # Center the text within the text block.
                size 25                 # Set the text size.

init python:
    if persistent.youtube_mode is None:
        persistent.youtube_mode = False

    # переключить (None) или установить (True/False) режим сабов
    def youtube_toggle(on=None):
        # если переключить:
        if on is None:
            on = not persistent.youtube_mode
        # задаём новое значение
        persistent.youtube_mode = on
    YoutubeToggle = renpy.curry(youtube_toggle)


default persistent.youtuber_mode = False
define config.default_music_volume = 0.2
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.5


init:
    if not persistent.set_afm_time:
        $ persistent.set_afm_time = True
        $ preferences.afm_enable = True
        $ _preferences.afm_time = 10

define au = Character(None, who_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], what_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], screen="say2", window_background="gui/bac.png")
define nez = Character(_('???'), who_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], what_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], screen="say2", color="#e49cab", what_color="#e49cab", window_background="gui/bac.png")
define nov = Character(_('Диктор'), who_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], what_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], screen="say2", color="#f7f4f4", what_color="#f7f4f4", window_background="gui/bac.png")
define svek = Character(_('Свекровь'), who_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], what_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], screen="say2", color="#e49cab", what_color="#e49cab", window_background="gui/bac.png")
define neves = Character(_('Невестка'), who_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], what_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], screen="say2", color="#e49cab", what_color="#e49cab", window_background="gui/bac.png")
define akik = Character(_('Акико'), who_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], what_outlines = [ (absolute(1), "#333333", absolute(1), absolute(1)) ], screen="say2", color="#e49cab", what_color="#e49cab", window_background="gui/bac.png")
