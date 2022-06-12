# AI Conveersation / AI vestluspartner
Prototüüp eestikeelse kõnetuvastuse, GPT-2 mudeli ning TTS mudeliga, 
mis suudab suvalisel teemal vestelda.

- Töötab CPU peal lokaalses masinas.

ENG: Prototype using Estonian ASR, GPT-2 and TTS to have conversations.

### Used Models / Kasutatavad mudelid
ASR: https://huggingface.co/TalTechNLP/espnet2_estonian
<br/>
GPT-2: https://huggingface.co/tartuNLP/gpt-4-est-large
<br/>
TTS: https://github.com/TartuNLP/text-to-speech-worker
<br/>
TTS API: https://api.tartunlp.ai/text-to-speech/v2

### Installation / Installimine
- Create conda env. / Loo conda keskkond
```
conda create --name ai-speaker python=3.9
```
- Activate conda env / Käivita keskkond
```
conda activate ai-speaker
```
- Install pip / Installi pip käivitatud keskkonnas
```
conda install pip
```
- Install requirements.txt / Installi requirements.txt
```
pip install -r requirements.txt
```
### Running on command line / Käivitamine käsurealt
```
python main.py
```
