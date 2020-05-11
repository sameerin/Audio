import numpy as np

import scipy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import pyaudio


##########       Constants       #############################
# constants
CHUNK = 4096             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second
##########                       #############################


####################### Plot Config ##########################
# Setup the basic plot handles and configure plots

# print(plt.style.available)
# plt.style.use('fivethirtyeight')
# plt.xkcd()
fig, (ax1, ax2) = plt.subplots(2, 1, facecolor="green")
ax1.set_xlabel('time')
ax1.set_ylabel('audio amplitude')
ax1.set_xlim([0, CHUNK-1])
ax1.set_ylim([-16000, 16000])
ax1.set_title('AUDIO')
ax1.set_facecolor('#000000')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('spectrum amplitude')
#ax2.set_xlim([0, CHUNK/2-1])
ax2.set_ylim([-500, 500])
ax2.set_title('SPECTRUM')
ax2.set_facecolor('#000000')
x = np.arange(0,  CHUNK, 1)
##########################             #########################


# Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# line = ax.plot(x, data_np, lw=1)

lines = []
lines_spectrum = []
scale = RATE/(2*CHUNK)


def animate(i):

    data_np = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    global ax1, ax2, lines, lines_spectrum

    for line in lines_spectrum:
        line.remove()
    for line in lines:
        line.remove()
    spectrum = scipy.fft.fft(data_np)
    spectrum = (2/CHUNK)*np.abs(spectrum[0:CHUNK//2])

    lines = ax1.plot(x, data_np, lw=1, color='white')
    lines_spectrum = ax2.plot(scale*np.arange(0, CHUNK/2, 1), spectrum, lw=1, color='white')
    return ax1, ax2


if __name__ == "__main__":
    ani = FuncAnimation(fig, animate,  interval=20, frames=200,  blit=False)


plt.tight_layout()
# ani.save('audio.mp4', writer=writer)
plt.show()
stream.stop_stream()
stream.close()
p.terminate()


##################### program end #####################


########## wasteful code #################
