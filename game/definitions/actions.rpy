transform reset_camera(duration=1.0):
    ease duration xoffset 0 yoffset 0 zoom 1.0

transform camera_zoom(duration=1.0, value=1.1, blurval=0.0):
    align (0.5, 0.5)
    ease duration zoom value blur blurval

transform camera_look_center(duration=1.0):
    ease duration xoffset 0 yoffset 0

transform camera_look_left(duration=1.0, value=75):
    ease duration xoffset value

transform camera_look_right(duration=1.0, value=-75):
    ease duration xoffset value

transform camera_look_up(duration=1.0, value=50):
    ease duration yoffset value

transform camera_look_down(duration=1.0, value=-50):
    ease duration yoffset value

transform look_left(duration=1.0):
    yalign 0.5
    ease duration xalign 0.0

transform look_right(duration=1.0):
    yalign 0.5
    ease duration xalign 1.0
