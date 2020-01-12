# Last name(s), first name(s)
# Fraas Marcel

from PIL import Image, ImageDraw

# a)
def mb(c, max_iter):
    z = complex(0,0)
    n = 0
    alpha = complex(1,0)
    while (z.__abs__() <= 2) & (n < max_iter):
        n += 1
        z = 3/2*((z**2)/2-c-alpha)
        #print(f'Iteration: {n}')
    return n


# b)
# define variables here
max_iter = 80
a_start = -2
a_end = 1
b_start = -1
b_end = 1
height = 600
width = 800

im = Image.new('HSV', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(width):
    for y in range(height):
        # Conversion: pixel coordinate -> complex number
        a = a_start + (x / width)*(a_end - a_start)
        b = b_start + (y / height)*(b_end - b_start)
        c = complex(a,b)


        # Call mb here
        m = mb(c,max_iter)


        # Colored plot:
        hue = int(255 * m / max_iter)
        sat = 255
        if m < max_iter:
            value = 255
        else:
            value = 0
        draw.point([x, y], (hue, sat, value))
        #print(f'point: ({x},{y})')

im.convert('RGB').save('output.png', 'PNG') # file in which the image is stored