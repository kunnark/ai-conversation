from transformers import AutoTokenizer, AutoModelForCausalLM
import re
import warnings
warnings.filterwarnings("ignore")
import logging
logging.getLogger().setLevel(logging.ERROR)

device = "cpu" # cuda:0
m = AutoModelForCausalLM.from_pretrained("tartuNLP/gpt-4-est-large").to(device)
t = AutoTokenizer.from_pretrained("tartuNLP/gpt-4-est-large")

def trimoutput(outtxt):
    """remove text after the next >tag< starts and also do stupid sentence splitting"""
    searchRes = re.search(r'(>[^<]+<|\.)', outtxt[1:])

    if searchRes:
        return outtxt[:searchRes.span()[0] + 2].rstrip(">")
    else:
        return outtxt

def inference(question, source="news"):
  outputs = []

  if source is not None:
      prefs = source
  else:
      prefs = "general web news wiki doaj"

  for pref in prefs.split():
      enc_prompt = t.encode(f">{pref}< {question} Vastus:", return_tensors="pt").to(device)
      out = m.generate(input_ids = enc_prompt, max_length = 100, num_return_sequences=1, pad_token_id=t.eos_token_id)
      outputs.append(trimoutput(t.decode(out[0])))
  return question, outputs

def correct_output(output):
    output = output.strip()
    questions = "mis kes kus miks millal mida kuidas kellega millega millest kellest kui".split()
    splitted = output.split()
    if len(splitted) > 0 and splitted[0] in questions:
        output += "?"
    else:
        output += "."
    return output

def show(output):
  out = output[0].split("Vastus:")[1]
  out = correct_output(out)
  return out
