from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("tuner007/t5_abs_qa")
model = AutoModelForSeq2SeqLM.from_pretrained("tuner007/t5_abs_qa")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)


def get_answer(question):
    # Lägg till den givna kontexten här.
    context = "The human brain is the central organ of the human nervous system, and with the spinal cord makes up the central nervous system. The brain consists of the cerebrum, the brainstem and the cerebellum. It controls most of the activities of the body, processing, integrating, and coordinating the information it receives from the sense organs, and making decisions as to the instructions sent to the rest of the body. The brain is contained in, and protected by, the skull bones of the head.The cerebrum, the largest part of the human brain, consists of two cerebral hemispheres. Each hemisphere has an inner core composed of white matter, and an outer surface – the cerebral cortex – composed of grey matter. The cortex has an outer layer, the neocortex, and an inner allocortex. The neocortex is made up of six neuronal layers, while the allocortex has three or four. Each hemisphere is conventionally divided into four lobes – the frontal, temporal, parietal, and occipital lobes. The frontal lobe is associated with executive functions including self-control, planning, reasoning, and abstract thought, while the occipital lobe is dedicated to vision. Within each lobe, cortical areas are associated with specific functions, such as the sensory, motor and association regions. Although the left and right hemispheres are broadly similar in shape and function, some functions are associated with one side, such as language in the left and visual-spatial ability in the right. The hemispheres are connected by commissural nerve tracts, the largest being the corpus callosum. The brain weights about 3 pounds."

    input_text = "context: %s <question for context: %s </s>" % (
        context, question)
    features = tokenizer([input_text], return_tensors='pt')
    out = model.generate(input_ids=features['input_ids'].to(
        device), attention_mask=features['attention_mask'].to(device))
    return tokenizer.decode(out[0])
