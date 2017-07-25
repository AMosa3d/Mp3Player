import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *

root = Tk()
root.minsize(350, 350)

listOfSongs = []
index = 0
labelstring = StringVar()

def playsong(event):
    pygame.mixer.music.play()


def stopsong(event):
    pygame.mixer.music.stop()


def nextsong(event):
    global index

    if index == len(listOfSongs) - 1:
        return
    index += 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelable()


def prevsong(event):
    global index

    if index == 0:
        return
    index -= 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelable()


def updatelable():
    global index
    labelstring.set(listOfSongs[index])


def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listOfSongs.append(files)

    pygame.mixer.init()
    labelstring.set(listOfSongs[index])
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()

directorychooser()



programlabel = Label(root, text='Media Player')
programlabel.pack()

listbox = Listbox(root)
listbox.pack()

songlable = Label(textvariable=labelstring, width=20)
songlable.pack()

i = 0
for song in listOfSongs:
    listbox.insert(i, song)
    i += 1


# Buttons Section
nextbutton = Button(root, text='Next Song')
previousbutton = Button(root, text='Previous Song')
playbutton = Button(root, text='Play')
stopbutton = Button(root, text='Stop')

playbutton.pack()
stopbutton.pack()
nextbutton.pack()
previousbutton.pack()

playbutton.bind("<Button-1>", playsong)
stopbutton.bind("<Button-1>", stopsong)
previousbutton.bind("<Button-1>", prevsong)
nextbutton.bind("<Button-1>", nextsong)

root.mainloop()
