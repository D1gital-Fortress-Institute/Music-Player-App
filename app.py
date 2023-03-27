from pygame import mixer
from tkinter import Tk, Label, Button, filedialog, messagebox



# Function to play song
def play_song():
    
    file_name = filedialog.askopenfilename(initialdir="C:/", title="Please select a music file")
    current_song = file_name
    song_title = file_name.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        print(current_volume)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green", text=f"Now Playing: {song_title}")
    except Exception:
        messagebox.showerror(title="Can't Play File Type", message="File type not playable")


# Function to reduce volume
def reduce_volume():
    global current_volume
    try:
        if current_volume <= 0:
            volume_label.config(fg="red", text=f"Volume : Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text=f"Volume : {current_volume}")
    except Exception:
        return

# Function to increase volume
def increase_volume():
    global current_volume
    try:
        if current_volume >= 1:
            volume_label.config(fg="green", text=f"Volume : Highest Reached")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text=f"Volume : {current_volume}")
    except Exception:
        return
    
# Function to pause music
def pause_music():
    try:
        mixer.music.pause()
    except Exception:
        return
    

# Function to resume music
def resume_music():
    try:
        mixer.music.unpause()
    except Exception:
        return



if __name__=='__main__':
    current_volume = float(0.5)


    #Main Window Screen
    window = Tk()
    window.geometry("400x400") #Screen Size
    window.resizable(0, 0) # ENabling the screen not resizable
    window.title("Music Player")


    #Labels
    top_header_label = Label(window, text="DFI MUSIC PLAYER", font=("Calibri", 15, "roman", "bold"), fg="red")
    select_music_label = Label(window, text="Please select a music track you would like to play", font=("Calibri", 12, "roman", "bold"), fg="blue")
    song_title_label = Label(window, font=("Calibri", 12))
    volume_info_label = Label(window, text="VOLUME", font=("Calibri", 12),fg="black")
    volume_label = Label(window, font=("Calibri", 12))


    #Buttons
    select_music_button = Button(window, text="Select song", font=("Calibri", 12), command=play_song, bg="green")
    pause_music_button = Button(window, text="pause", font=("calibri", 12), command=pause_music)
    resume_music_button = Button(window, text="resume", font=("calibri", 12), command=resume_music)
    decrease_music_button = Button(window, text="-", font=("calibri", 12), width=5, command=reduce_volume)
    increase_music_button = Button(window, text="+", font=("calibri", 12), width=5, command=increase_volume)
    
    


    # Arrange labels and button in grid
    top_header_label.grid(sticky="N", row=0, padx=120)
    select_music_label.grid(sticky="N", row=1)
    select_music_button.grid(sticky="N", row=2, pady=20)
    pause_music_button.grid(sticky="E", row=3, padx=40)
    resume_music_button.grid(sticky="W", row=3, padx=40)
    song_title_label.grid(sticky="N", row=3)
    volume_info_label.grid(sticky="N", row=4)
    volume_label.grid(sticky="N", row=5)
    increase_music_button.grid(sticky="E", row=5, padx=100)
    decrease_music_button.grid(sticky="W", row=5, padx=100)



    window.mainloop()