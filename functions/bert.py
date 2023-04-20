from transformers import AutoModel, AutoTokenizer, BartForConditionalGeneration, pipeline
import torch

def BRT (prompt):
    answerer_model = "KBLab/bert-base-swedish-cased-squad-experimental" # Swedish BERT model
    mask_model = "KBLab/bart-base-swedish-cased" #Swedish BART model

    # Use pipeline to produce an answerer from BERT
    answerer = pipeline("question-answering", model=answerer_model, tokenizer=answerer_model)

    doc = "Philip is 22 years old."
    q = prompt

    answer_output = answerer({ 
        'question': q,
        'context': doc
    })
    answer = answer_output['answer'] 
    return answer


# model = BartForConditionalGeneration.from_pretrained(mask_model)
# tok = AutoTokenizer.from_pretrained(mask_model)
# model.eval()

# input_ids = tok.encode(
#     "Jag har ätit en utsökt <mask> på restaurang vid <mask> .", return_tensors="pt"
# )
# # Beam search
# output_ids = model.generate(
#     input_ids,
#     min_length=15,
#     max_length=25,
#     no_repeat_ngram_size=3,
#     num_beams=8,
#     early_stopping=True,
#     do_sample=True,
#     num_return_sequences=6
# )
# tok.decode(output_ids[0])

# print(output_ids[0])