transform umuumu:
  yoffset 0
  block:
    ease .25 yoffset 15
    ease .25 yoffset 0
    repeat 2

transform nodding:
  yoffset 0
  ease .25 yoffset 25
  ease .25 yoffset 0

transform sighing: 
  yoffset 0
  ease .5 yoffset 30
  ease .5 yoffset 0

transform jumping:
  yoffset 0
  ease .2 yoffset -15
  ease .2 yoffset 0

transform trembling:
  ease .1 xoffset 2
  ease .1 xoffset -2
  repeat

transform fidgeting:
  block:
    ease .2 xoffset 5
    ease .2 xoffset -5
    repeat 2
  ease .1 xoffset 0

transform shaking:
  xoffset 0
  ease .25 xoffset 10
  ease .25 xoffset -10
  ease .25 xoffset 0

transform swaying:
  easein 1.0 xoffset 10
  easein 1.0 xoffset -10
  repeat

transform pushing(time=1.0):
  ease time zoom 1.2 yoffset 100

transform movedis(endpoint=-200, duration=1.0):
  delay duration
  ease duration xoffset endpoint alpha 0.0

transform trueleft:
  xalign .25
  yalign 1.0
  anchor (.5, 1.0)

transform trueright:
  xalign .75
  yalign 1.0
  anchor (.5, 1.0)

transform moveoutleft(value=-100, duration=1.0):
  easeout duration xoffset value alpha 0.0

transform moveoutright(value=100, duration=1.0):
  easeout duration xoffset value alpha 0.0

transform moveinleft(value=-100, duration=1.0):
  yalign 1.0
  xoffset value
  alpha 0.0
  easein duration xoffset 0 alpha 1.0

transform moveinright(value=100, duration=1.0):
  yalign 1.0
  xoffset value
  alpha 0.0
  easein duration xoffset 0 alpha 1.0

transform moveright(value=0.75, duration=1.0):
  ease duration xalign value

transform moveleft(value=0.25, duration=1.0):
  ease duration xalign value

transform movecenter(value=0.5, duration=1.0):
  ease duration xalign value