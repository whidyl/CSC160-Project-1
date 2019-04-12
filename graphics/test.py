"""
This file is for the purpose of testing the ezgraphics module.
"""
from ezgraphics import GraphicsWindow

# create a graphics window
win = GraphicsWindow(500, 500)
canvas = win.canvas()

# Use a light gray background
canvas.setBackground("light gray")

# draw
canvas.drawRect(100, 100, 50, 60)
win.wait()
