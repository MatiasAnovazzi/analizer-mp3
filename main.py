import json
import os
from audio import MaxRms
from player import MusicPlayer

# Lista de canciones (rutas)
playlist = [
    "superman.mp3",
    "jurabas-tu.mp3",
    "my-eyes.mp3",
    "the-search.mp3",
    "silbando.mp3"
]

player = MusicPlayer()
temp = {}

# 📂 Cargar el JSON existente si ya está creado
if os.path.exists("saved.json"):
    with open("saved.json", "r") as saved:
        try:
            temp = json.load(saved)
        except json.JSONDecodeError:
            print("⚠️ El archivo saved.json está dañado, se reiniciará.")
            temp = {}
else:
    print("📄 No se encontró saved.json, se creará uno nuevo.")

# 🔍 Revisar cada canción en la playlist
for song in playlist:
    if song not in temp:
        print(f"🎧 Analizando nueva canción: {song}")
        resultado = MaxRms(song)
        temp[song] = [resultado]
    else:
        print(f"✅ Canción ya analizada: {song}")

# 💾 Guardar el archivo actualizado
with open("saved.json", "w") as saved:
    json.dump(temp, saved, indent=4)

# ▶️ Reproducir todas las canciones
for song in playlist:
    momento = temp[song][0]
    player.play_song(song, momento)
