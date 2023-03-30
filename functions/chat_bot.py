from huggingface_hub import login
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

login("")
# Initialize Variables
# model_name = "AI-Sweden-Models/gpt-sw3-1.3b"
model_name = "AI-Sweden-Models/gpt-sw3-126m"
# in case i run this on my laptop or pc
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# Initialize Tokenizer & Model
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)

# Set the period/full stop as the stop token
tokenizer.pad_token = "."


model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()
model.to(device)


def generate_text(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    output = model.generate(
        inputs=input_ids,
        max_new_tokens=20,
        do_sample=True,
        top_p=1, temperature=0.7
    )
    return tokenizer.decode(output[0])


# prompt = "Följande är en konversation mellan en besökare på museet och en guide. Guiden arbetar på museet. Guiden är hjälpsam, informativ och mycket vänlig. \n" \
#     "Museet innehåller tre utställningar, den första utställningen heter 'Hitta nemo igen' av Hermann Gustafsson \n\n\n"\
#     "Besökare: Hej, jag är här för att se utställningen 'Hitta nemo igen', och jag har en fråga!\n" \
#     "Guide: Hej, vad kul! Vad vill du veta om utställningen?\n" \
#     "Besökare: Vet du vem som skapade utställningen?\n"
# prompt = 'hej, hur mår du?'

# print(generate_text(prompt))
