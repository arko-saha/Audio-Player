from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog

# New GUI

root = Tk()
#root.geometry('1080x300')
root.title("Audition")
root.iconbitmap(r'Logo.ico')

# Edit GUI

menubar = Menu(root)
root.config(menu=menubar)

# MenuBar Fuctions

def details():
    tkinter.messagebox.showinfo('Audition', 'This is a dummy MP3 Player.')

def browse():
    global filename
    filename = filedialog.askopenfilename()
    
# Menu Bar Preparation

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse)
subMenu.add_command(label="Exit", command=root.destroy)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="Details", command=details)

#Pygame Mixer Init
                                      
mixer.init()

#Action Events

def Play():
    try:
        Paused
    except NameError:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusBar['text']= "Playing"   
        except:
            tkinter.messagebox.showerror('Error 404!', 'File Not Found.')    
    else:
        mixer.music.unpause()
        statusBar['text']= "Playing"

def Stop():
    mixer.music.stop() 
    statusBar['text']= "Stopped" 

def Pause():
    global Paused
    Paused = TRUE
    mixer.music.pause() 
    statusBar['text']= "Paused" 

def Rewind():
    Play()
    statusBar['text']= "Rewinded"


def Volume(val):
    volumeBtn.configure(image=volume_photo)
    volume = int(val)/100
    mixer.music.set_volume(volume)

muted = FALSE

def Mute():
    global muted
    
    if muted:  # Unmute the music
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volume_photo)
        scale.set(70)
        muted = FALSE
        
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mute_photo)
        scale.set(0)
        muted = TRUE
 


# Put them into Frame 

frame = Frame(root)
frame.pack(padx=10, pady=5)

# Play Button

play_photo = PhotoImage(file='Play.png')
playBtn = Button(frame, image=play_photo, command=Play)
#playBtn.pack(side=LEFT, padx=5)
playBtn.grid(row=0, column=0, padx=10)

# Stop Button

stop_photo = PhotoImage(file='Stop.png')
stopBtn = Button(frame, image=stop_photo, command=Stop)
#stopBtn.pack(side=LEFT, padx=5)
stopBtn.grid(row=0, column=3, padx=10)

# Pause Button

pause_photo = PhotoImage(file='Pause.png')
pauseBtn = Button(frame, image=pause_photo, command=Pause)
#pauseBtn.pack(side=LEFT, padx=5)
pauseBtn.grid(row=0, column=1, padx=10)

# Rewind Button

rewind_photo = PhotoImage(file='Rewind.png')
rewindBtn = Button(frame, image=rewind_photo, command=Rewind)
#pauseBtn.pack(side=LEFT, padx=5)
rewindBtn.grid(row=0, column=2, padx=10)

# Toggle Button

mute_photo = PhotoImage(file='Mute.png')
volume_photo = PhotoImage(file='Volume.png')
volumeBtn = Button(frame, image=volume_photo, command=Mute)
#stopBtn.pack(side=LEFT, padx=5)
volumeBtn.grid(row=0, column=4, padx=10)


# Scale Volume Button

scale = Scale(frame, from_=0, to_=100, orient=HORIZONTAL, command=Volume)
scale.set(65)
mixer.music.set_volume(0.65)
scale.grid(row=0, column=5, padx=10)


# Calling Second Frame 

durationframe = Frame(root)
durationframe.pack(padx=10, pady=5)




# Status Bar preparation

statusBar = Label(root, text="Welcome!", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

# Main Loop

root.mainloop()