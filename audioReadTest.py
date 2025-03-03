import wave
import numpy as np


with wave.open(r"./dataSource.wav") as f:
    metadata = f.getparams()
    frames = f.readframes(metadata.nframes)

print(metadata)
# print(frames)

pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)

dt = 1/metadata[2]
t_verdier = np.linspace(0,len(normalized_amplitudes)*dt,len(normalized_amplitudes))


print(dt)
print(t_verdier)
print(normalized_amplitudes)
