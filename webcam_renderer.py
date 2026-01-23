import cv2
import shutil
import numpy as np
import os 

darkness_scale = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]    
darkness_scale_len = len(darkness_scale)
vc = cv2.VideoCapture(0)

if vc.isOpened():
	rval, frame = vc.read()
else:
	rval = False

while result := vc.read():
	
	rval, frame = result
		
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
	height, width = gray_frame.shape
	
	terminal_size = shutil.get_terminal_size((120, 80))
	terminal_height = np.linspace(0, height-1, terminal_size.lines-1, \
																	dtype=int)
	terminal_width = np.linspace(0, width-1, terminal_size.columns, dtype=int)

	gray_vec = gray_frame[np.ix_(terminal_height, terminal_width)]                        
	                                                 		
	ascii_characters = np.array(darkness_scale)[np.round(
								np.round(gray_vec/255*(darkness_scale_len-1))
								).astype(int)]
	
	print("\033[H\033[J", end="") 
	print("\n".join("".join(row) for row in ascii_characters))
