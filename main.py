from PIL import Image
import argparse


parser = argparse.ArgumentParser(
        prog="ascii_renderer"
        )

parser.add_argument("-i", 
		    "--image", 
                    required=True, help="Image to render in ascii")

parser.add_argument("-s", 
                    "--size", 
                    required=True, help="Width and height of output", nargs=2)

args = parser.parse_args()

img = Image.open(args.image) \
		.resize((int(i) for i in args.size)) \
		.convert("RGBA")

width, height = img.size
pixels = img.load()

darkness_scale = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
ascii_characters = []

for y in range(height):
   for x in range(width):  
      r, g, b, a = pixels[x, y]
      
      darkness = (r+g+b)/(255*3)   
      brightness = a/255
      darkness_index = int(darkness*brightness*9)
      ascii_characters.append(darkness_scale[darkness_index])

current_index = 0
content = ""

for x in range(height):
   content += "".join(ascii_characters[current_index:current_index+width]) + "\n"
   current_index += width

with open("output.txt", "w") as f:
   f.write(content)
