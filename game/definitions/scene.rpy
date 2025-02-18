transform panoramic(duration=32.0, distance=2.0, xstart=0.0, ystart=0.5, endx=1.0, endy=0.5):
    zoom distance
    xalign xstart
    yalign ystart
    ease duration xalign endx yalign endy

transform inspect(duration=8.0, xstart=0.5, ystart=0.5, endx=0.5, endy=0.0):
    xalign xstart
    yalign ystart
    ease duration xalign endx yalign endy