﻿define eka_voice = ["audio/voice/eka/eka_key1.ogg", "audio/voice/eka/eka_key2.ogg", "audio/voice/eka/eka_key3.ogg", "audio/voice/eka/eka_key4.ogg"]

default typing_time = 0
define e = Character("Eka", callback=play_typing_sound, cb_typing_sound="audio/voice/eka_short.ogg")

init python:
    renpy.music.register_channel("ambiance", "sfx", loop=True, tight=True)
    current_scene = ""

label start:
    stop music
    show screen scene_indicator
    call prologue
    return
