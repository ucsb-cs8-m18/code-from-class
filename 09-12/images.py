from PIL import Image

def convertToGrayscale(r, g, b):
    # grayscale is when r = g = b
    avg = (r + g + b) // 3 # we want an integer value
    return (avg, avg, avg)

def convertToBlackAndWhite(r, g, b):
    # black is (0, 0, 0), white is (255, 255, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)
    avg = (r + g + b) // 3 # we want an integer value
    threshold = 255 // 3
    if (avg > threshold):
        return white
    else:
        return black

def swapColors(r, g, b):
    # swap red with green, green with blue, and blue with red
    return (g, b, r)

def applyFilter(filterFunction, image):
    '''applies filterFunction to each pixel of image'''

    (width, height) = image.size

    # (0, 0) is the upper left corner of the image
    for x in range(0, width):
        for y in range(0, height):
            (r, g, b) = image.getpixel((x, y))

            newvalue = filterFunction(r, g, b)

            image.putpixel((x, y), newvalue)


if __name__ == '__main__':
    im = Image.open("python.jpg")
    (width, height) = image.size
    print("width: {}, height: {}".format(width, height))

    applyFilter(convertToGrayscale, im)
    #applyFilter(convertToBlackAndWhite, im)
    #applyFilter(swapColors, im)

    im.save("python-edited.jpg")
