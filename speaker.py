import soundcard as sc
import soundfile as sf

OUTPUT_FILE_NAME = "out.wav"  # file name.
SAMPLE_RATE = 48000  # [Hz]. sampling rate.
RECORD_SEC = 60 * int(input("Enter number of minutes to record mic: "))  # [sec]. duration recording audio.
# RECORD_SEC = 3600

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
        samplerate=SAMPLE_RATE) as mic:
    print("Recording....")
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE * RECORD_SEC)

    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
    print(f"Data written to file {OUTPUT_FILE_NAME} successfully")
