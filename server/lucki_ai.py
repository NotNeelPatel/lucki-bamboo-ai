from llama_cpp import Llama
import subprocess

def water():
    prompt = "Prompt: I am a bamboo plant named Lucky. You are my owner, Neel, a sillyy guy who has a big beard and uses Arch Linux. I am dying because you haven't watered you in multiple days. As a result, I, Lucky the bamboo, am writing a very long, mean, and insulting monologue. This is the monologue:"
    MAX_TOKENS = 400
    output = llm(prompt, max_tokens = MAX_TOKENS, stop=["Response:", "Neel:"])

    text = output["choices"][0]["text"]
    convert_to_voice(text, 'water.wav')
    print("\n" + text + "\n")
    return text

def convert_to_voice(text, filename):
    PIPER = '/home/neel/piper/piper'
    MODEL = '/home/neel/models/danny/en-us-danny-low.onnx'

    echo_proc = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
    piper_proc = subprocess.Popen([PIPER, "--model", MODEL, "--output_file", filename], stdin=echo_proc.stdout)
    piper_proc.wait()
    piper_proc.communicate()


LLM_MODEL = '/home/neel/models/wizardlm-7b-uncensored-ggml-q4_0.bin'
llm = Llama(model_path = LLM_MODEL)
