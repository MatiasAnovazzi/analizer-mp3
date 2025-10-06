# player.py
import vlc
import threading
import time
from audio import MaxRms  # tu función ya existente

class MusicPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.fade_out_duracion = 5  # segundos
        self.fade_in_pasos = 10
        self.fade_in_tiempo = 0.2
        self._on_end_callback = None

    def _fade_in(self):
        self.player.audio_set_volume(0)
        for v in range(0, 101, int(100 / self.fade_in_pasos)):
            self.player.audio_set_volume(v)
            time.sleep(self.fade_in_tiempo)

    def _fade_out(self):
        print("🔉 Iniciando fade out...")
        for v in range(100, -1, -int(100 / self.fade_in_pasos)):
            self.player.audio_set_volume(v)
            time.sleep(self.fade_out_duracion / self.fade_in_pasos)
        print("⏹ Fade out completo, deteniendo reproducción.")
        self.player.stop()
        if self._on_end_callback:
            self._on_end_callback()

    def play_song(self, path: str, on_end=None):
        """Reproduce una canción aplicando fade in/out y salto al punto emocionante."""
        self._on_end_callback = on_end
        momento = MaxRms(path) - 3
        print(f"🎧 Reproduciendo {path}, salto a {momento:.2f}s")

        media = self.instance.media_new(path)
        self.player.set_media(media)

        def on_playing(event):
            print("🎵 Reproducción iniciada")

            def delayed_seek():
                while self.player.get_time() <= 0:
                    pass
                self.player.set_time(int(momento * 1000))
                print(f"⏩ Saltando a {momento:.2f}s")
                self._fade_in()

                duracion = self.player.get_length() / 1000
                while self.player.get_time() < (duracion - self.fade_out_duracion) * 1000:
                    time.sleep(0.1)
                self._fade_out()

            threading.Thread(target=delayed_seek, daemon=True).start()

        eventos = self.player.event_manager()
        eventos.event_attach(vlc.EventType.MediaPlayerPlaying, on_playing)
        self.player.play()
