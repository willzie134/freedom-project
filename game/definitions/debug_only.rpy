init python:
    def debug_save(filename, extra_info=""):
        
        renpy.take_screenshot()
        renpy.save(filename, extra_info)