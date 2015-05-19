#!/usr/bin/python

from swampy.World import World
from rectangle import Rectangle, Point

def draw_rectangle(Canvas, Rectangle):
    bbox = [[Rectangle.corner.x, Rectangle.corner.y], 
            [Rectangle.corner.x + Rectangle.width, 
             Rectangle.corner.y + Rectangle.height]]
    Canvas.rectangle(bbox, outline="black", width=2, fill="green4")
    

world = World()

canvas = world.ca(width=500, height=500, background="white")
box = Rectangle()
box.corner = Point()
box.corner.x = 50
box.corner.y = 50
box.width = 100
box.height = 100

draw_rectangle(canvas, box)
world.mainloop()
