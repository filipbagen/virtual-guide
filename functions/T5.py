from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("tuner007/t5_abs_qa")
model = AutoModelWithLMHead.from_pretrained("tuner007/t5_abs_qa")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def get_answer(question):
    context = "You are a Data Scientist working for a company. You are tasked with creating a model that can predict the price of a house based on its features. You are given a dataset with 79 features describing the houses. You are also given the price of each house. You are asked to create a model that can predict the price of a house based on its features. You are given a dataset with 79 features describing the houses. You are also given the price of each house. You are asked to create a model that can predict the price of a house based on its features. You are given a dataset with 79 features describing the houses. You are also given the price of each house. You are asked to create a model that can predict the price of a house based on its features. You are given a dataset with 79 features describing the houses. You are also given the price of each house. You are asked to create a model that can predict the price of a house based on its features."
    
    input_text = "context: %s <question for context: %s </s>" % (context, question)
    features = tokenizer([input_text], return_tensors='pt')
    out = model.generate(input_ids=features['input_ids'].to(device), attention_mask=features['attention_mask'].to(device))
    return tokenizer.decode(out[0])

