import requests
import warnings
warnings.filterwarnings("ignore")
import logging
logging.getLogger().setLevel(logging.ERROR)

def tts(input_text):
    if len(input_text) > 2:
        URL = "https://api.tartunlp.ai/text-to-speech/v2"
        PARAMS = {'text': input_text, 'speaker':'Albert', 'speed':0.7}
        with requests.post(url=URL, json=PARAMS, stream=True) as r:
            with open("output.wav", 'wb') as f:
                f.write(r.content)
    else:
        return None