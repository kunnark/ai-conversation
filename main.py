import backend as be
import sound as sound
import asr as asr
import tts
import warnings
import sys
from utils.spinner import Spinner
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    run = True
    tts.tts("Tere, mina olen tehisintellekt, hakkame rääkima.")
    sound.play()
    while run:
        print("> Räägi midagi ... ")
        with Spinner():
            input_sound = sound.save_sound()
        print("> Tuvastan, mida sa ütlesid ... ")

        with Spinner():
            text = asr.recognize_speech()
        print("> Sina ütlesid:", text)

        if "lõpetame vestluse" in text:
            text_to_speech = tts.tts("Kohtumiseni! Lõpetan vestluse.")
            sound.play()
            run = False
            sys.exit()

        print("> Mõtlen vastust ...")
        with Spinner():
            q, a = be.inference(text, "news")

        answer = be.show(a)
        print("> Minu vastus:", answer)
        text_to_speech = tts.tts(answer)
        sound.play()
        sys.stdout.flush()