

        # ---------Importing require libraries-----------------

import os
import webbrowser
from tkinter.filedialog import askdirectory

import menu as menu
import pygame
from mutagen.id3 import ID3
from tkinter import *
from PIL import ImageTk, Image



        # ---------Creating Window-----------------
        
        
window = Tk()

window.title("Music Player")
window.geometry('600x450')
window.configure(bg="antiquewhite")



        # ---------Creating Frame-----------------

frame1 = Frame(window, bg="seashell")
menu = Menu(frame1)
window.config(menu=menu)

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(window, textvariable=v, width=40, bg="gray")

index = 0



        # ---------To ask user to choose Directory-----------------
        
def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])

            listofsongs.append(files)

    pygame.mixer.init()
    if len(listofsongs) != 0:
        pygame.mixer.music.load(listofsongs[0])
        # pygame.mixer.music.play()
    else:
        print("Add the correct Directory which has mp3 files")
        exit()

directorychooser()



        # ---------Updating song for each click-----------------
        
def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    # return songname


def nextsong(event):
    global index
    index += 1
    if len(listofsongs) == index:
        index = 0
        pygame.mixer.music.load(listofsongs[index])
    else:
        pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def prevsong(event):
    global index
    if index != 0:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
    else:
        index = len(listofsongs) - 1
        pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def pausesong(event):
    global index
    pygame.mixer.music.pause()



def currentsong(event):
    global index
    pygame.mixer.music.play()
    updatelabel()


def end():
    exit()


def help():
    webbrowser.open("https://t.me/HarshaVardhan17_02")


def contact():
    webbrowser.open("https://t.me/HarshaVardhan17_02")


def stopsong(event):
    pygame.mixer.music.fadeout(1000)


                                    # ---------Creating Menus-----------------


        # ---------Creating Playlist menu----------

subMenu = Menu(menu)
menu.add_cascade(label="Media Files", menu=subMenu)  # Cascading Options on the ToolBar Such as: File Edit
subMenu.add_command(label="Open Files", command=directorychooser)
subMenu.add_separator()



        # -----------Creating Contact Menu----------

contactMenu = Menu(menu)
menu.add_cascade(label="Contact Me", menu=contactMenu)
contactMenu.add_command(label="Want Help Ping me", command=help)
contactMenu.add_command(label="Report Error Ping me", command=contact)

subMenu.add_separator()
subMenu.add_command(label="Exit Player", command=exit)

one1 = Label(window, text="           ").pack(fill=X)
one = Label(window, text="Welcome Guys To Harsha Vardhan's Music Player", bg="black", fg="white").pack(fill=X)

label = Label(window, text='Playlists')
label.pack()




        # --------------Creating Listbox and adding to window--------------


listbox = Listbox(window, width=50, bg="seashell")
listbox.pack(padx=5, pady=5)


realnames.reverse()
for items in realnames:
    listbox.insert(0, items)
realnames.reverse()


        #---------------Creating Buttons--------------


previousbutton = Button(window, text=' ⏮ Previous Song', fg="black", width=20, bg="purple")
previousbutton.pack(padx=5, pady=5)

playbutton = Button(window, text=' ▶ Play song', fg="black", width=20, bg="turquoise")
playbutton.pack(padx=5, pady=5)

pausebutton = Button(window, text=' ⏸ Pause song', fg="black", width=20, bg="lightskyblue")
pausebutton.pack(padx=5, pady=5)

nextbutton = Button(window, text=' ⏭ Next Song', fg="royalblue", width=20, bg="black")
nextbutton.pack(padx=5, pady=5)

stopbutton = Button(window, text=' ⏹ Stop Music', fg="red", width=20, bg="coral")
stopbutton.pack(padx=5, pady=5)

nextbutton.bind("<Button-1>", nextsong)
playbutton.bind("<Button-1>", currentsong)
pausebutton.bind("<Button-1>", pausesong)
previousbutton.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)


#-------------Adding Current song to the window-------------
songlabel.pack()

window.mainloop()
