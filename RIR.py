####Room Impulse Reponse

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal 
#from scipy.io import wavfile
from wave import open as open_wave
#import soundfile as sound

#audio, fs=wave.open('./BIG HALL E002 M2S.wav')
#data, samplerate = sound.read('./BIG HALL E002 M2S.wav',channels=1, subtype='FLOAT')

def read_wave(filename="sound.wav"):
    """Reads a wave file.
    filename: string
    returns: Wave
    """
    fp = open_wave(filename, "r")

    nchannels = fp.getnchannels()
    nframes = fp.getnframes()
    sampwidth = fp.getsampwidth()
    framerate = fp.getframerate()

    z_str = fp.readframes(nframes)

    fp.close()

    dtype_map = {1: np.int8, 2: np.int16, 3: "special", 4: np.int32}
    if sampwidth not in dtype_map:
        raise ValueError("sampwidth %d unknown" % sampwidth)

    if sampwidth == 3:
        xs = np.fromstring(z_str, dtype=np.int8).astype(np.int32)
        ys = (xs[2::3] * 256 + xs[1::3]) * 256 + xs[0::3]
    else:
        ys = np.fromstring(z_str, dtype=dtype_map[sampwidth])

    # if it's in stereo, just pull out the first channel
    if nchannels == 2:
        ys = ys[::2]

    # ts = np.arange(len(ys)) / framerate
    #wave = Wave(ys, framerate=framerate)
    #wave.normalize()
    return ys

data=read_wave("./BIG HALL E002 M2S.wav")





#fp=open_wave("./BIG HALL E002 M2S.wav", "r")
#nframes=fp.getnframes()
#data=fp.readframes(nframes)
#channels=fp.getnchannels()
#rate=fp.getframerate()

#print(nframes)
#print(channels)
#print(rate)


#Plotting
fig1 = plt.figure()
plt.plot(data)
plt.show()