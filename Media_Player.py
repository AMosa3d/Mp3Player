import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *

root = Tk()
root.minsize(300, 300)

listOfSongs = []
index = 0


def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listOfSongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()


label = Label(root, text='Media Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

nextbutton = Button(root, text='Next Song')
nextbutton.pack()

previousbutton = Button(root, text='Previous Song')
previousbutton.pack()

playbutton = Button(root, text='Play')
playbutton.pack()

stopbutton = Button(root, text='Stop')
stopbutton.pack()

directorychooser()
root.mainloop()
