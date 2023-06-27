from llama_cpp import Llama
import subprocess

def water():
    # Preparing the prompt for the large language model
    prompt = "Prompt: I am a bamboo plant named Lucky. You are my owner, Neel, a silly guy who has a big beard and uses Arch Linux. I am dying because you haven't watered you in multiple days. As a result, I, Lucky the bamboo, am writing a very long, mean, and insulting monologue. This is the monologue:"
    MAX_TOKENS = 400

    # Output for the llm
    output = llm(prompt, max_tokens = MAX_TOKENS, stop=["Response:", "Neel:"])

    text = output["choices"][0]["text"]
    convert_to_voice(text, 'water.wav')
    print("\n" + text + "\n")
    return text

def convert_to_voice(text, filename):
    # Use piper to convert to voice

    PIPER = '/home/neel/piper/piper'
    MODEL = '/home/neel/models/danny/en-us-danny-low.onnx'

    # Subprocess to run bash commands in python
    # although there are ways to interface piper in python directly
    echo_proc = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
    piper_proc = subprocess.Popen([PIPER, "--model", MODEL, "--output_file", filename], stdin=echo_proc.stdout)
    piper_proc.wait()
    piper_proc.communicate()

# LLM Model is WizardLM 7b uncensored, so that it can make insults without any restrictions
LLM_MODEL = '/home/neel/models/wizardlm-7b-uncensored-ggml-q4_0.bin'
llm = Llama(model_path = LLM_MODEL)
