import warnings
import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="huggingface_hub")


# Cache model and tokenizer
@st.cache_resource
def load_model_and_tokenizer():
    load_tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
                                                
    load_model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
                                                                    
    return load_tokenizer, load_model


tokenizer, model = load_model_and_tokenizer()

@st.fragment()
def predict_emotion(msg):
    inputs = tokenizer(msg, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1)
        predicted_class = torch.argmax(probs, dim=1).item()
    return model.config.id2label[predicted_class]




# --------------Personalty Tracking ----------------
