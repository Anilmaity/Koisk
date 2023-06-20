import pyaudio

# Set up the audio stream
chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100

audio = pyaudio.PyAudio()
stream = audio.open(
    format=format,
    channels=channels,
    rate=rate,
    input=True,
    frames_per_buffer=chunk
)

# Start capturing audio
print("Recording started. Press Ctrl+C to stop.")

frames = []
try:
    while True:
        data = stream.read(chunk)
        frames.append(data)
except KeyboardInterrupt:
    pass

# Stop capturing audio
print("Recording stopped.")

stream.stop_stream()
stream.close()
audio.terminate()