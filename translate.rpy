init -3 python: 
    if persistent.lang is None: 
        persistent.lang = "russian"
    lang = persistent.lang

init python:
    if lang == "english":
        style.default.font = "DejaVuSans.ttf" #english font here 
    elif lang == "russian": 
        style.default.font = "DejaVuSans.ttf" #russian font here
    elif lang == "serbian": 
        style.default.font = "DejaVuSans.ttf" #russian font here