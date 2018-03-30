import wave
import struct
import numpy as np

rate = 44100

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

#output_sound('sine440.wav', 440, 2)



audio.write(data)
#data = (open('output.txt','r').read())

#print(data)
packedData = data
#packedData = map(lambda v:struct.pack('h',v), data)
#frames = b''.join(packedData)
output_wave('example.wav', packedData,2)
print("Audio File Saved.")