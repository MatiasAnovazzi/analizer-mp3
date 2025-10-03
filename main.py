from audio import MaxRms
import vlc, time

momento = MaxRms("silbando.mp3") - 3
reproductor = vlc.MediaPlayer("silbando.mp3")
reproductor.play()


# Saltar al tiempo del pico de energía
reproductor.set_time(int(momento * 1000))  
print("Reproduciendo audio...")
for v in range(0, 101, 10):
    reproductor.audio_set_volume(v)
    time.sleep(0.2)
duracion = reproductor.get_length() / 1000  # Obtener duración en segundos 
print(f"Duración del audio: {duracion} segundos")
time.sleep(duracion)