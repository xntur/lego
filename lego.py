from PIL import Image

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

def convert(img, size, contrast=0):
    bw_img = img.convert('L')
    contrast_img = change_contrast(bw_img, contrast)
    return contrast_img.resize(size)

def get(image_path):
    img = Image.open(image_path)
    sizeDiff = abs(img.size[0] - img.size[1])
    minSize = min(img.size[0], img.size[1])
    if sizeDiff / minSize > .1:
        raise Exception("Image needs to be square-ish (+/- 10%).")
    if minSize < 32:
        raise Exception("Image too small.")
    return img

_size = 255 / 4
_black = int(_size / 2)
_dark = int(_size / 2 + _size)
_light = int(_size / 2 + 2 * _size)
_white = int(_size / 2 + 3 * _size)

print(_black)
print(_dark)
print(_light)
print(_white)

def nearestpixel(val):
    print(val)
    b = abs(val - _black)
    d = abs(val - _dark)
    l = abs(val - _light)
    w = abs(val - _white)
    minimum = min(b, min(d, min(l, w)))
    if minimum == b:
        return _black
    elif minimum == w:
        return _white
    elif minimum == d:
        return _dark
    else:
        return _light

    
def nearest(image):
    pixels = image.load()
    image.show()
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            print(pixels[i, j])
            pixels[i, j] = nearestpixel(pixels[i, j])
            print(pixels[i, j])
    image.show()
    
def legoify(path, contrast=100):
    img = convert(get(path), (32, 32), contrast).resize((100, 100))
    nearest(img)
