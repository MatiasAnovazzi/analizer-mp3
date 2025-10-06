# main.py
from player import MusicPlayer

# Lista de canciones (rutas)
playlist = [
    "my-eyes.mp3",
    "the-search.mp3",
    "cancion3.mp3"
]

player = MusicPlayer()

def play_next(index=0):
    if index < len(playlist):
        player.play_song(playlist[index], on_end=lambda: play_next(index + 1))
    else:
        print("✅ Playlist terminada.")

play_next(0)

# Mantener vivo el programa mientras se reproduce
import time
while True:
    time.sleep(0.1)
