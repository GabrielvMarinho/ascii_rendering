import cv2
import os

darkness_scale = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]    

vc = cv2.VideoCapture(0)

if vc.isOpened():
	rval, frame = vc.read()
else:
	rval = False

while result := vc.read():

	rval, frame = result
	
	width, height, _ = frame.shape	

	
	ascii_characters = ""                                                       
                                                                                 
	
	for y in range(width):                                                     
		if y%5==0:
			for x in range(height):                                                   
				if x%2==0:
					r, g, b = frame[y, x]                                                                                              
					darkness = (r+g+b)/(255*3)					                                            			                                                   
					darkness_index = int(darkness*9)                           
					ascii_characters += darkness_scale[darkness_index]
			ascii_characters += "\n"
	
	os.system('clear')
	print(ascii_characters)

vc.release()
