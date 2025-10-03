import librosa
import numpy as np
from scipy.signal import find_peaks
import sys
def MaxRms(ruta):
# 1. Cargar el archivo de audio
    audio_file = ruta
    y, sr = librosa.load(audio_file, sr=22050)  # y = señal, sr = sample rate

# 2. Calcular energía por frames
    frame_length = 2048
    hop_length = 512
    rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=hop_length)[0]

# 3. Convertir a tiempo
    times = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=hop_length)

# 4. Buscar todos los picos de energía
    peaks, _ = find_peaks(rms, height=np.max(rms) * 0.83)  
# "height=..." -> solo picos que superen el 90% del valor máximo

# 5. Si hay picos, tomar el primero
    if len(peaks) > 0:
        first_peak_index = peaks[0]
        highlight_time = times[first_peak_index]
        print(f"Primer pico fuerte detectado en {highlight_time:.2f} segundos.")
        return highlight_time
    else:
        highlight_time = 0
        print("No se encontraron picos significativos.")
        return highlight_time
