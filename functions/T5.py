from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("tuner007/t5_abs_qa")
model = AutoModelWithLMHead.from_pretrained("tuner007/t5_abs_qa")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def get_answer(question):
    context="Anna is 23 years old. She is a student at UC Berkeley. She is studying computer science. She is from San Francisco."

    input_text = "context: %s <question for context: %s </s>" % (context, question)
    features = tokenizer([input_text], return_tensors='pt')
    out = model.generate(input_ids=features['input_ids'].to(device), attention_mask=features['attention_mask'].to(device))
    return tokenizer.decode(out[0])

