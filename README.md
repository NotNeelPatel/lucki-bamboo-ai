# Lucki-Bamboo-AI

Using a water level sensor, a Raspberry Pi, an Intel NUC, and some AI resources, I present to you: Lucki Bamboo-AI.

Lucki the bamboo checks to see if he needs to be watered using the water level sensor, and if he does, the Raspberry Pi will send a GET request to the Intel NUC server, which will send a wav file to be played. In the meantime, the server will generate a new response and convert it to a wav file.

This project uses [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) for generating prompts and [piper](https://github.com/rhasspy/piper) for converting the text output to audio. 

## Example
https://github.com/NotNeelPatel/lucki-bamboo-ai/assets/91706742/d7282bab-22ac-402e-8f33-b5dff42d8c07

## Wiring
![Wiring](https://github.com/NotNeelPatel/lucki-bamboo-ai/assets/91706742/305e27aa-04bf-43d7-9a8f-37e40e07de84)
