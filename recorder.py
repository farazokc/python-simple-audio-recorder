import pyaudio
# import pprint
import wave

FRAMES_PER_BUFFER = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

pa = pyaudio.PyAudio()

stream = pa.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)
frames = []

print('start recording')

# Recording appended to list
try:
    # DO THINGS
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

# Close file
stream.stop_stream()
stream.close()
pa.terminate()

# File settings
obj = wave.open('recording.wav', 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(pyaudio.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b''.join(frames))
obj.close()
