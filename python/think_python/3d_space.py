from visual import *

scene.range = (256, 256, 256)
scene.center = (128, 128, 128)

#color = (0.1, 0.1, 0.9)
#sphere(pos=scene.center, radius=128, color=color)

t = range(0, 256, 51)
for x in t:
    for y in t:
        for z in t:
            pos = x,y,z
            color = (x*0.004, y*0.004, z*0.004)
            sphere(pos=pos, radius=10, color=color)
