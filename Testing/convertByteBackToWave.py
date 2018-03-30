import wave
import struct
import numpy as np

rate = 44100

def sine_samples(freq, dur):
    # Get (sample rate * duration) samples on X axis (between freq
    # occilations of 2pi)
    X = (2*np.pi*freq/rate) * np.arange(rate*dur)

    # Get sine values for these X axis samples (as integers)
    S = (32767*np.sin(X)).astype(int)

    # Pack integers as signed "short" integers (-32767 to 32767)
    as_packed_bytes = (map(lambda v:struct.pack('h',v), S))
    return as_packed_bytes

def output_wave(path, frames):
    # Python 3.X allows the use of the with statement
    # with wave.open(path,'w') as output:
    #     # Set parameters for output WAV file
    #     output.setparams((2,2,rate,0,'NONE','not compressed'))
    #     output.writeframes(frames)

    output = wave.open(path,'w')
    output.setparams((2,2,rate,0,'NONE','not compressed'))
    output.writeframes(frames)
    output.close()

def output_sound(path, freq, dur):
    # join the packed bytes into a single bytes frame
    frames = b''.join(sine_samples(freq,dur))

    # output frames to file
    output_wave(path, frames)

#output_sound('sine440.wav', 440, 2)

data = open('sine440.wav','rb').read()
audio = open("audio.txt",'wb')

audio.write(data)
#data = (open('output.txt','r').read())

#print(data)
packedData = data
#packedData = map(lambda v:struct.pack('h',v), data)
#frames = b''.join(packedData)
output_wave('example.wav', packedData)
print("Audio File Saved.")