"""
Raises the red value of every pixel by 30% in an image to get a sunset effect.
"""
from ezgraphics import GraphicsImage, GraphicsWindow
filename = input("Enter a filename (pre.png or mountain.png is recommended): ")

# load the original image
image = GraphicsImage(filename)

# Process image
width = image.width()
height = image.height()
for row in range(height):
    for col in range(width):
        red = image.getRed(row, col)
        green = image.getGreen(row, col)
        blue = image.getBlue(row, col)

        # cheeky way to clamp a value. found this online.
        newRed = sorted([0, int(red*1.3), 255])[1]

        # set pixel to new color
        image.setPixel(row, col, newRed, green, blue)

# Display
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
# the below line doesn't work on my computer.
#image.save("sunset-" + filename)
win.wait()
