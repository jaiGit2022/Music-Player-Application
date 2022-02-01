from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox


class MusicPlayer:
    """Class to handle methods of music player like play,pause, and stop"""

    def __init__(self):
        """
        Initializer of MusicPlayer class
        """

        mixer.init()  # starting the mixer from pygame

    def play_music(self):
        """
        A function that play the given music file
        """
        try:  # check if music is paused or playing for first time
            PAUSED
        except:
            try:  # play music for first time
                mixer.music.load(FILENAME)  # loading music file, choose by user
                mixer.music.play()  # play music
                statusbar["text"] = "Music is played"  # set the status to played
            except:  # if file is not selected
                tkinter.messagebox.showerror("Error", "File not found")
        else:
            mixer.music.unpause()  # unpause the music if it is paused.
            statusbar["text"] = "Music is resumed"  # set the status to resumed

    def stop_music(self):
        """
        A function that is responsible for stopping th music
        """
        mixer.music.stop()  # stop the music
        statusbar["text"] = "Music is stopped"  # set status to stop

    def pause_music(self):
        """
        A function that is responsible for pausing the music
        """
        global PAUSED
        PAUSED = True  # setting paused to True
        mixer.music.pause()  # pause music
        statusbar["text"] = "Music is paused"  # set status to paused

    @staticmethod
    def set_volume(value):
        """
        A function that is responsible for setting up the volume
        :param value:
        """
        value = int(value) / 100  # volume is under range of 100
        mixer.music.set_volume(value)  # setting up the volume


def browse_file():
    """
    Open choose file window
    """
    global FILENAME
    FILENAME = filedialog.askopenfilename()  # open window to ask for music file


def help_me():
    """
    Open help me dialogue box
    """
    tkinter.messagebox.showinfo("Help", "How can I help you?\nContact me @jkishan421@gmail.com")  # help message


if __name__ == "__main__":
    """Start of the main program"""

    window = Tk()  # making object of tkinter for GUI

    window.geometry("1000x500")  # setting up window size
    window.title("Python Music Player")  # setting up the title of window

    music_player = MusicPlayer()  # making object of MusicPlayer class

    menubar = Menu(window)  # adding menu to the window
    submenu = Menu(menubar, tearoff=0)  # adding submenu to the sub menu
    window.config(menu=menubar)

    menubar.add_cascade(label="File", menu=submenu)  # menu option File
    submenu.add_command(label="Open", command=browse_file)  # adding open file as a submenu
    submenu.add_command(label="Exit", command=window.destroy)  # exit in submenu

    submenu = Menu(menubar, tearoff=0)  # another menu
    menubar.add_cascade(label="About", menu=submenu)  # menu of About
    submenu.add_command(label="Help", command=help_me)  # adding Help as a submenu in About

    # setting up the frame for the window
    frame = Frame(window)
    frame.pack(padx=10, pady=10)

    # Creating play button with icon
    playPhoto = PhotoImage(file="static/play.png")  # loading icon from static folder
    playButton = Button(frame, image=playPhoto, command=music_player.play_music)  # creating button with the play icon
    playButton.grid(row=0, column=0, padx=10)  # positioning the play button

    stopPhoto = PhotoImage(file="static/stop.png")  # loading icon from static folder
    stopButton = Button(frame, image=stopPhoto, command=music_player.stop_music)  # creating button with the stop icon
    stopButton.grid(row=0, column=1, padx=10)  # positioning the stop button

    pausePhoto = PhotoImage(file="static/pause.png")  # loading icon from static folder
    pauseButton = Button(frame, image=pausePhoto,
                         command=music_player.pause_music)  # creating button with the pause icon
    pauseButton.grid(row=0, column=2, padx=10)  # positioning the pause button

    # scale to setting up the volume
    scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=MusicPlayer.set_volume)
    scale.set(70)  # default volume is 70
    scale.grid(row=1, column=1, pady=15)  # positioning the volume slider

    # status label
    statusbar = Label(window, text="Keep enjoying music", relief=SUNKEN, anchor=W)
    statusbar.pack(side=BOTTOM, fill=X)

    # run GUI
    window.mainloop()
