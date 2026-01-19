import cv2


darkness_scale = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]         

vc = cv2.VideoCapture(0)

if vc.isOpened():
	rval, frame = vc.read()
else:
	rval = False

while result := vc.read():

	rval, frame = result
	print(frame.shape)
	width, height, _ = frame.shape	

	
	ascii_characters = ""                                                       
                                                                                 
	for y in range(height):                                                     
		for x in range(width):                                                   
			r, g, b = frame[x, y]                                                                                              
			darkness = (r+g+b)/(255*3)                                            
			                                                   
			darkness_index = int(darkness*9)                           
			ascii_characters += darkness_scale[darkness_index]
		ascii_characters += "\n"
	
	print(ascii_characters)
		

vc.release()
