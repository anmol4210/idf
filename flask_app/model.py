import pickle
import re

def get_model(filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model

def pre_process(text):
    text = text.replace("[silence]","")
    text = text.replace("[noise]","")
    text = re.sub('[^a-zA-Z ]','',text)
    return text
    