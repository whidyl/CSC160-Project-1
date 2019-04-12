"""
Converts an image to grayscale
"""
from ezgraphics import GraphicsImage, GraphicsWindow
filename = input("Enter a filename (pre.png or mountain.png is recommended): ")

# load the original image
image = GraphicsImage(filename)

# process image
width = image.width()
height = image.height()
for row in range(height):
    for col in range(width):
        red = image.getRed(row, col)
        green = image.getGreen(row, col)
        blue = image.getBlue(row, col)

        # get grayscale value using weighted average
        shade = int(0.2126*red + 0.7152*green + 0.0722*blue)

        # set pixel to new color
        image.setPixel(row, col, shade, shade, shade)

# Display
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
# the below line gives me an error on my computer, although this is how the examples used it.
#image.save("sunset-" + filename)
win.wait()
