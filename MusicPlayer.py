import tkinter as tk
from tkinter import filedialog
import pygame


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []
        self.current_track = 0
        self.paused = False

        pygame.mixer.init()

        self.create_gui()

    def create_gui(self):
        # Create labels and buttons
        self.label = tk.Label(self.root, text="Music Player")
        self.label.pack()

        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.add_button = tk.Button(self.root, text="Add Track", command=self.add_track)

        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()
        self.add_button.pack()

        self.volume_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume")
        self.volume_scale.set(50)
        self.volume_scale.pack()

        # Configure event bindings
        self.listbox.bind("<Double-Button-1>", self.play_selected_track)

    def play_music(self):
        if not self.playlist:
            return

        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            track = self.playlist[self.current_track]
            pygame.mixer.music.load(track)
            pygame.mixer.music.set_volume(self.volume_scale.get() / 100.0)
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()

    def add_track(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
        if file_path:
            self.playlist.append(file_path)
            track_name = file_path.split("/")[-1]
            self.listbox.insert(tk.END, track_name)

    def play_selected_track(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.current_track = int(selected_index[0])
            self.play_music()


if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
