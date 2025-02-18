transform tinting(tintcolor):
  matrixcolor TintMatrix(tintcolor)

transform idle:
  ease 1.5 matrixcolor TintMatrix("#838383")

transform talk:
  ease 1.5 matrixcolor None

transform idling:
  function transidle

transform bigger:
  zoom 2.0

transform sepia(val='#ffeec2'):
  matrixcolor SepiaMatrix(val)

transform zoomout(zoomval=.9):
  zoom zoomval
  xalign .5
  yalign 1.0

transform sit(time=.5):
  ease time yoffset 30
  pause time

transform stand(time=.2):
  ease time yoffset 0
  pause time

transform leftish:
  xalign .25

transform slidezoom(duration=1.0, start_x=0.1, end_x=0.0, start_y=1.0, end_y=1.0, zoom_val=2.0):
  yalign start_y
  xalign start_x
  zoom zoom_val
  ease duration xalign end_x yalign end_y

transform slidezoomsprite(duration=1.0, start_x=0.1, end_x=0.0, start_y=0.0, end_y=0.0, zoom_val=1.5, start_alpha=0.0):
  yalign start_y
  xalign start_x
  zoom zoom_val
  alpha start_alpha
  ease duration xalign end_x yalign end_y alpha 1.0

transform blur_bg(intensity=10.0):
  easein 0.5 blur intensity