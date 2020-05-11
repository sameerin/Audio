import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyaudio
import struct
import time

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
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(1)

x = np.arange(0,  CHUNK, 1)
##########################             #########################


p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)


def animate(i):
    data_np = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    global ax
    ax.cla()
    ax.set_xlabel('time')
    ax.set_ylabel('audio amplitude')
    ax.set_xlim([0, CHUNK-1])
    ax.set_ylim([-9999, 9999])
    ax.set_title('AUDIO')
    ax.plot(x, data_np, lw=1)

    return ax


if __name__ == "__main__":
    ani = FuncAnimation(fig, animate,  interval=20, blit=False)


plt.tight_layout()
plt.show()
stream.stop_stream()
stream.close()
p.terminate()


##################### program end #####################


########## wasteful code #################
