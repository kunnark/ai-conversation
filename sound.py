import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
import warnings
warnings.filterwarnings("ignore")
import logging
logging.getLogger().setLevel(logging.ERROR)

def save_sound():
    fs = 16000  # Sample rate
    seconds = 5  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('input.wav', fs, myrecording)  # Save as WAV file

def play():
    playsound('output.wav')