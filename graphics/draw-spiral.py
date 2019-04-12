
"""
This program will draw a paramaterized spiral.
"""
from ezgraphics import GraphicsWindow
from time import sleep
from random import randint

# create a graphics window
win = GraphicsWindow(500, 500)
canvas = win.canvas()

# Use a light gray background
canvas.setBackground("gray")
def main():
    drawSpiral(20, 10, 250, 250)
    #sleep(2)
    for i in range(10000):
        canvas.setOutline(randint(0,255),randint(0,255),randint(0,255))
        drawSpiral(randint(5,30), randint(3,15), randint(0, 450), randint(0, 450))
    win.wait()

def drawSpiral(depth, size, x, y):
    """
    Drawns lines in a spiral pattern.
    (int) depth: depth*2 is the number of line segments that make up the spiral.
    (float) siz: length between lines.
    (float) x, y: position spiral center.
    """
    newX, newY = x, y
    for i in range(depth):
        #                                           \/ i%2 so that corner is mirrored every other step
        newX, newY = drawCorner(newX, newY, size*i, i%2)
        sleep(0.1)

def drawCorner(x, y, segmentLength, isMirrored):
    """
    Draws two lines in an L shape. 
    Corner points southeast when not mirrored, northwest when mirrored.
    Returns the position of the last line vertex
    """
    if isMirrored:
        canvas.drawLine(x, y, x-segmentLength, y)
        sleep(0.1)
        canvas.drawLine(x-segmentLength, y, x-segmentLength, y+segmentLength)
        return (x-segmentLength, y+segmentLength)
    else:
        canvas.drawLine(x, y, x+segmentLength, y)
        sleep(0.1)
        canvas.drawLine(x+segmentLength, y, x+segmentLength, y-segmentLength)
        return (x+segmentLength, y-segmentLength)
    


if __name__ == "__main__":
    main()