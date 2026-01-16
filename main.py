from PIL import Image

file_name = "image.png"

img = Image.open(file_name).resize((1000, 300)).convert("RGBA")

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

with open("file.txt", "w") as f:
   f.write(content)