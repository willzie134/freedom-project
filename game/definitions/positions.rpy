transform left:
    zoom 1.0
    xalign 0.1
    yalign 1.0

transform right:
    zoom 1.0
    xalign .9
    yalign 1.0

transform center:
    zoom 1.0
    xalign .5
    yalign 1.0

transform close:
    yanchor .85
    zoom 1.2

transform closer:
    yalign 0.0
    yoffset -10
    zoom 1.5

transform bg_default:
    yanchor 0.5
    zoom 1.0
    blur 0.0

transform bg_close(yval=0.9, zoomval=1.2, blurval=2.0):
    yanchor yval
    zoom zoomval
    blur blurval

transform bg_zoom(x=.5, y=.5, zoomval=1.0, blurval=1.0):
    xalign x
    yalign y
    zoom zoomval
    blur blurval