import pickle
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk
from tkinter import *
import pygame


def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str


def RemoveStopwords(text):
    nltk.download('stopwords')
    stop = stopwords.words('english')
    words = text.split()
    clean_str = ''
    for word in words:
        if word in stop:
            continue
        clean_str += word
    return clean_str


def Clean_Data(text):
    text = text.lower()
    text = punctuation_removal(text)
    text = RemoveStopwords(text)
    return text


def CreateResultWindow():
    result = Tk()
    result.geometry('300x100+200+100')
    result.title("Result!!!")
    tfidf_ngram = pickle.load(open('tf-idf.sav', 'rb'))
    text_to_check = inputText.get("1.0", END)
    text_to_check = Clean_Data(text_to_check)
    text_to_check = tfidf_ngram.transform([text_to_check])
    load_model = pickle.load(open('model.sav', 'rb'))
    prediction = load_model.predict(text_to_check)
    ans = "Fake" if prediction[0] == 1 else "Real"
    Label(result, text='Beep...Bop.....The text is predicted as a ' + ans + ' new').pack()
    Label(result, text='Thanks for using this!!!\n=))))', justify=CENTER).pack()
    inputText.delete('1.0', END)
    result.mainloop()


pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play(loops=0)
app = Tk()
app.title("Is This Fake?")
app.geometry('640x480+100+100')
instruction = "1. Paste the text you want to check\n2. Press the \"Check\" button\n3. Wait a few seconds"
label = Label(app, text=instruction, justify=LEFT).pack()
inputText = Text(app)
inputText.place(x=10, y=115, height=30, width=200)
inputText.pack()
Button(app, text='Check', command=CreateResultWindow).pack()
app.mainloop()


















