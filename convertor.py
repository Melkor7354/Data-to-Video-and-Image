import math
import numpy
from PIL import Image


def ascii_color_encode():
    ascii_colors = {}

    # Generating unique RGB values for ASCII characters
    for i in range(128):
        red = (i * 17) % 256  # Unique red component
        green = (i * 33) % 256  # Unique green component
        blue = (i * 49) % 256  # Unique blue component

        # Storing RGB values in a dictionary with ASCII value as key
        ascii_colors[i] = [red, green, blue]

    # Displaying the dictionary
    return ascii_colors


def text_to_picture(path, ascii_colours, save_as):
    file = open(path, 'r')
    data = file.read()
    ascii_values = []
    for i in data:
        if ord(i) < 128:  # Check if character falls within ASCII range
            ascii_values.append(ord(i))
        else:
            ascii_values.append(ord(' '))  # Replace non-ASCII characters with a space ' '
    square = int(math.ceil(math.sqrt(len(ascii_values))))
    print(square)  # Adjusted square size
    total_elements = square * square
    for i in range(total_elements - len(ascii_values)):
        ascii_values.append(ord(' '))  # Fill remaining spaces with ' '
    pixel_array = []
    for i in range(0, len(ascii_values)):
        pixel_array.append(ascii_colours[ascii_values[i]])

    array = numpy.array(pixel_array, dtype=numpy.uint8).reshape(square, square, 3)

    image = Image.fromarray(array)
    image.resize((1000, 1000))
    image.save(f'{save_as}.png')


def picture_to_text(picture_path, ascii_colours, output_name):
    image = Image.open(picture_path)
    pixels = image.load()
    width, height = image.size
    data = []
    for i in range(width):
        for j in range(height):
            data.append(pixels[j, i])
    text = ''
    for k in data:
        for j in ascii_colours:
            if ascii_colours[j] == list(k):
                text += chr(j)

    with open(f'{output_name}.txt', 'w') as file:
        file.write(text)


picture_to_text('Sample.png', ascii_color_encode(), 'Text')