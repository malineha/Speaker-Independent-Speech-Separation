import numpy as np
from separate_sound2 import separate_sound2
from separate_sound3 import separate_sound3
import tkinter.messagebox

def separate_sound(b):
	# Specify the name
	name = np.empty(0, dtype=object)
	file=" "
	c=" "

	for x in b:
		#print(x)
		file=x.split("/")
		c=file[6]
		#print(c)
		f1=c.split('-')
		#print(f1[1])
		f3=f1[1].split('.')
		#print(f3[0])
		name=np.append(name,f3[0])
		#print(name.size)
		file=" "
		c=" "
	if name.size==2:
		separate_sound2(b,name)
	elif name.size==3:
		separate_sound3(b,name)
	elif name.size>3:
		tkinter.messagebox.showinfo("Title", " NOT MORE THAN 3 ")
	