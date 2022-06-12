from espnet2.bin.asr_inference import Speech2Text
import soundfile
import warnings
warnings.filterwarnings("ignore")

model = Speech2Text.from_pretrained(
    "TalTechNLP/espnet2_estonian",
    lm_weight=0.6, ctc_weight=0.4, beam_size=60
)

def recognize_speech():
    speech, rate = soundfile.read("input.wav")
    assert rate == 16000
    text, *_ = model(speech)
    output = text[0]
    return output



