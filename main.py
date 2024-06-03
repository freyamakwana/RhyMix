import tkinter                     # Standard GUI library for Python
import customtkinter               # An extended version of Tkinter with more customization options.
import pygame                      # Library used for creating games and multimedia applications
from PIL import Image, ImageTk     # PIL (Python Imaging Library) and ImageTk: For handling images in the GUI
from threading import Thread       # For threading, allowing certain tasks to run in parallel

customtkinter.set_appearance_mode("System")    # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Tkinter
root = customtkinter.CTk()         # Creates the main window using customtkinter
root.title('RhyMix')               # Sets the title of the window to "RhyMix".
root.geometry('400x480')           # Sets the size of the window to 400x480 pixels.
pygame.mixer.init()                # Initializes the Pygame mixer for playing audio.

list_of_songs = ['songs/Heather.wav.wav', 'songs/Thats what i like.wav.wav']
list_of_covers = ['img/dreamy-agjzsk3591hh0nun.jpg', 'img/dreamy_world-wallpaper-1920x1080.jpg']
n = 0                             # Index to keep track of the current song.

SONG_END = pygame.USEREVENT + 1             # Defines a new event type for when a song ends.
pygame.mixer.music.set_endevent(SONG_END)   # Tells Pygame to post the SONG_END event when a song finishes playing.

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2 = image1.resize((400, 350))
    load = ImageTk.PhotoImage(image2)         # Converts the image for use with Tkinter.

    label1 = tkinter.Label(root, image=load)  # Converts the image for use with Tkinter.
    label1.image = load
    label1.place(relx=.19, rely=.06)          # Positions the label within the window.

    stripped_string = song_name.split('/')[-1][:-4]  # Get the song name from the path
    song_name_label = tkinter.Label(text=stripped_string, bg='#222222', fg='white')    # Creates a label to display the song name
    song_name_label.place(relx=.4, rely=.6)       # Positions the song name label within the window

def update_progressbar():
    if pygame.mixer.music.get_busy():
        pos = pygame.mixer.music.get_pos() / 1000                          # Get position in seconds
        song_len = pygame.mixer.Sound(list_of_songs[n-1]).get_length()     # Gets the length of the current song.
        progressbar.set(pos / song_len)                                    # Sets the progress bar value based on the song's current position.
        root.after(1000, update_progressbar)                           # Schedule the next update

def play_music():
    global n                                   # Declares n as a global variable.
    if n >= len(list_of_songs):                # Checks if the current song index is out of range.
        n = 0                                  # Resets the song index if it exceeds the list length.
    song_name = list_of_songs[n]               # Gets the current song name.
    pygame.mixer.music.load(song_name)         # Loads the current song.
    pygame.mixer.music.play(loops=0)           # Plays the song.
    pygame.mixer.music.set_volume(.5)          # Sets the volume to 50%.
    get_album_cover(song_name, n)              # Displays the album cover and song name.
    n += 1                                     # Increments the song index for the next song.
    update_progressbar()                       # Starts updating the progress bar.

def skip_forward():
    play_music()                           # play song

def skip_back():
    global n                               # Declares n as a global variable.
    n -= 2                                 # Decrements the song index by 2 to go to the previous song.
    if n < 0:                              # Checks if the song index is out of range (negative).
        n = len(list_of_songs) - 1         # Sets the song index to the last song if it is negative.
    play_music()                           # Calls the play_music function to play the previous song.

def volume(value):
    pygame.mixer.music.set_volume(value)   # Sets the volume to the given value.

def check_music_end():
    for event in pygame.event.get():       # Loops through Pygame events.
        if event.type == SONG_END:         # Checks if the event type is SONG_END.
            play_music()                   # Calls the play_music function to play the next song.
    root.after(100, check_music_end)   # 100 millisecond

# All Buttons
play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

root.after(100, check_music_end)  # Start checking for song end event
root.mainloop()
