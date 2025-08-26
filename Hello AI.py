import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event

def wait_for_enter():
    input("\nPress Enter to stop recording...\n")
    stop_event.set()

def spinner():
    spinner_chars = '|/_\\'
    idx - 0
    while not stop_event.is_set
        time.sleep(0.1)
    sys.stdout.write('\rRecording stopped.     \n')

def record_until_enter():
    p = pyaudio.PyAudio()
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    frames_per_buffer = 1024

    stream = p.open(format=format, channels=channels, rate=rate, input=True,
                    frames_per_buffer=frames_per_buffer)

    frames = []

threading.Thread(target=wait_for_enter).start()
threading.Thread(target=spinner).start()

while not stop_event.is_set():
    try:
        data = stream.read(frames_per_buffer)(data)
    except Exception as e:
        print("Error reading stream:", e)
        break

    stream.stop_stream()
    stream.close()
    sample_width = p.get_sample_size(format)
    p.tetminate()

    audio_data = b''.join(frames)
    return audio_data, rate, sample_width

def save_audio(data)
    with wave.open(filename, "wb") as wf:
        wf.setchanels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)