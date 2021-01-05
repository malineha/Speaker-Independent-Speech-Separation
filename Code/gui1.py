# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
from functools import partial
from tkinter import filedialog
from separate_sound import separate_sound
from gui2 import new_window
import tkinter,tkinter.filedialog
import tkinter.messagebox
import numpy
from PIL import ImageTk,Image

def open_masker():
    global fileName
    global f1
    #filez = filedialog.askopenfilename(filetypes=(("./sounds", ".wav .ogg"),   ("All Files", "*.*")))
    filez = tkinter.filedialog.askopenfilenames(parent=gui,title='Choose a file',filetypes=(("C:/SPEECH_SEPARATION--FinalYear/sounds/data/", ".wav .ogg"),   ("All Files", "*.*")))
    filez = gui.splitlist(filez)
    return filez
    
def newwindow():
	new_window()

	
# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="white") 

	# set the title of GUI window 
	gui.title("INPUT") 

	# set the configuration of GUI window 
	gui.geometry("500x500") 
	gui.configure(bg='skyblue')
	
	filename = PhotoImage(file = "C:/SPEECH_SEPARATION--FinalYear/gui.png")
	background_label = Label(gui, image=filename)
	background_label.place(x=50, y=50, relwidth=1, relheight=1)


	file = " "
	text = Label(gui, font=("bold", 15 ),text="Enter mixed .wav file")
	text.place(x=200,y=20)
	#f1=" "
	#b1 = Button(gui, text ='FILE 1',command = open_masker )
	#b1.place(x=200,y=50)
	s=open_masker()
	
	#b2 = Button(gui, text = 'FILE 2',command = open_masker)
	#b2.place(x=200,y=100)
	a = numpy.empty(0, dtype=object)
	b = numpy.empty(0, dtype=object)

	if len(s)==0:
		tkinter.messagebox.showinfo("Title", "NO FILE SELECTED")
	elif len(s)==1:
		tkinter.messagebox.showinfo("Title", "AS PER ASSUMPTION NEED MORE THAN ONE MIXED FILE")
		print("AS PER ASSUMPTION NEED MORE THAN ONE MIXED FILE")
	else:
		file=" "
		fileName=" "
		c = StringVar()
		
		for x in s:
			fileName=x
			b=numpy.append(b,fileName)
			#print(b)
			

	b3 = Button(gui,bg = "Royalblue1", font=("bold", 15), text = ' Get Separate Files',command = partial(separate_sound,b))
	b3.place(x=185,y=150)
	b4 = Button(gui,bg = "Royalblue1", font=("bold", 15) ,text = 'Separated Speech',command = newwindow)
	b4.place(x=200,y=420)

	gui.mainloop() 

