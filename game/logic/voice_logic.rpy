
init python:
    import time
    typing_time = 0
    def play_typing_sound(event, interact=True, typing_sound=None, **kwargs):

        global typing_time
        typing_time += 1
        if not interact:
            return

        typing_speed = preferences.text_cps

        if typing_speed > 0:
            renpy.music.set_audio_filter("sound", renpy.audio.filter.Delay(min(1 / typing_speed, 0.01)))
        
        if event == "show_done":
        
            if typing_sound and typing_speed > 0:
                renpy.sound.play(typing_sound, loop=True)
        elif event == "slow_done":
            typing_time = 0
            renpy.sound.stop()