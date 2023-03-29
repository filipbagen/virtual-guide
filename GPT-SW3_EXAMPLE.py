# %% [markdown]
# GPT-SW3
# https://nlu-lab.notion.site/Prompthandboken-7cd943cc230642f2b8243807731e81ae
#   
# Fick inbjudan genom att anmäla mig via denna länk: https://docs.google.com/forms/d/e/1FAIpQLSebZv__Me6YUO_kFetDZevwXgSsYSVnXWzG5H68MIwN4XmdtQ/viewform
# 
# Borde inte ta långt innan man får mejl, men hör av om det tar för lång tid.

# %%
from huggingface_hub import login  
login()

# %%
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Initialize Variables
model_name = "AI-Sweden-Models/gpt-sw3-1.3b"
device = "cuda:0" if torch.cuda.is_available() else "cpu" #in case i run this on my laptop or pc

# %%

# Initialize Tokenizer & Model
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()
model.to(device)

# %%
def generate_text(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    output = model.generate(
        inputs = input_ids,
        max_new_tokens = 200,
        do_sample=True,
        top_p=1, temperature=0.7
        )
    return tokenizer.decode(output[0])

prompt = "Följande är en konversation mellan en besökare på museet och en guide. Guiden arbetar på museet. Guiden är hjälpsam, informativ och mycket vänlig. \n" \
            "Museet innehåller tre utställningar, den första utställningen heter 'Hitta nemo igen' av Hermann Gustafsson \n\n\n"\
            "Besökare: Hej, jag är här för att se utställningen 'Hitta nemo igen', och jag har en fråga!\n" \
            "Guide: Hej, vad kul! Vad vill du veta om utställningen?\n" \
            "Besökare: Vet du vem som skapade utställningen?\n" 
print(generate_text(prompt))         


