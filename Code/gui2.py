from tkinter import *

from tkinter import filedialog
from functools import partial
import pygame
import tkinter.messagebox

from PIL import ImageTk,Image

def listenfile(file):
	pygame.init()

	pygame.mixer.music.load("C:/SPEECH_SEPARATION--FinalYear/Separated/"+file)

	pygame.mixer.music.play()



def open_masker1():
    global fileName
    fileName = filedialog.askopenfilename(filetypes=(("C:/SPEECH_SEPARATION--FinalYear/Separated/", ".wav .ogg"),   ("All Files", "*.*")))
    if len(fileName) == 0:
    	tkinter.messagebox.showinfo("Title", "NO FILE SELECTED")
    file=fileName.split('/')
    
    masker_track = fileName
    if fileName =="": 
        fileName = None 
    else:
        fh = open(fileName, "r")
        fh.close()  
    return file[3]



def new_window():
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="white") 

	# set the title of GUI window 
	gui.title("OUTPUT") 
	
	# set the configuration of GUI window 
	gui.geometry("500x500") 
	gui.configure(bg='skyblue')
	
	#filename = PhotoImage(file = "/home/pradnya/Downloads/project/diagram/gui.png")
	#background_label = Label(gui, image=filename)
	#background_label.place(x=10, y=10, relwidth=1, relheight=1)

	text = Label(gui, bg = "Royalblue1", font=("bold", 15),text="Choose file")
	text.place(x=200,y=20)
	#b2 = Button(gui, text ='choose file',command = open_masker1)
	#b2.place(x=200,y=100)
	file=open_masker1()
	b3 = Button(gui, bg = "Royalblue1", font=("bold", 15), text ='play file',command = partial(listenfile,file))
	b3.place(x=185,y=150)
	



	