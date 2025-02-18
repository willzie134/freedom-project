
# transitions
define wipedown = CropMove(.5, mode="wipedown")
define wiperight = CropMove(.5, mode="wiperight")
define wipeup = CropMove(.5, mode="wipeup")
define wipeleft = CropMove(.5, mode="wipeleft")
define sfastdis = Dissolve(.2)
define fastdis = Dissolve(.5)
define meddis = Dissolve(1)
define slowdis = Dissolve(2.0)
define fastfade = Fade(.4, .2, .4)
define medfade = Fade(.5, 1.0, .5)
define slowfade = Fade(1.0, 2.0, 1.0)

define _scene_show_hide_transition = Dissolve(0.1)
# define moveoutleftdis = ComposeTransition(dissolve(.5), Transform(xoffset=-200, delay=1.0, new_widget=None, old_widget=None))

screen scene_indicator():
    frame:
        background color("#000")
        pos (0, 0)
        anchor(0, 0)
        xpadding 20
        ypadding 10
        
        text _(current_scene)