import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import nltk

# Download necessary NLTK resources
nltk.download('punkt')  # For tokenization
nltk.download('wordnet')  # For WordNet

# Initialize the recognizer
r = sr.Recognizer()

# Homophone mapping
homophones = {
    'break': 'brake',
    'brake': 'brake',
    'sea': 'see',
    'see': 'see',
    'which': 'witch',
    'witch': 'witch'
}

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def record_text():
    # Loop in case of errors
    while True:
        try:
            # Use the microphone as source for input
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listen for the user's input
                audio2 = r.listen(source2)

                # Using Google's speech recognition
                MyText = r.recognize_google(audio2)
                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Could not understand audio")
    
    return

def output_text(text):
    text_box.insert(tk.END, text + "\n")
    return

def custom_tokenizer(text):
    tokens = word_tokenize(text)
    for i, token in enumerate(tokens):
        lower_token = token.lower()
        if lower_token in homophones:
            # Check the context of the word
            if lower_token in ['break', 'brake']:
                if i > 0 and tokens[i-1].lower() in ['i', 'you', 'he', 'she', 'it', 'we', 'they']:
                    tokens[i] = 'brake'  # Use 'brake' if preceded by a pronoun
                elif i < len(tokens) - 1 and tokens[i+1].lower() in ['your', 'the']:
                    tokens[i] = 'brake'  # Use 'brake' if followed by 'your' or 'the'
                else:
                    tokens[i] = 'break'  # Default to 'break'
            elif lower_token in ['sea', 'see']:
                if i > 0 and tokens[i-1].lower() in ['i', 'love', 'enjoy']:
                    tokens[i] = 'see'  # Use 'see' if preceded by certain phrases
                else:
                    tokens[i] = 'sea'  # Default to 'sea'
            elif lower_token in ['which', 'witch']:
                if i > 0 and tokens[i-1].lower() in ['the', 'a']:
                    tokens[i] = 'witch'  # Use 'witch' if preceded by 'the' or 'a'
                else:
                    tokens[i] = 'which'  # Default to 'which'
    return tokens

def start_recording():
    text = record_text()
    tokens = custom_tokenizer(text)  # Use the custom tokenizer
    text = ' '.join(tokens)
    output_text(text)
    print("Wrote Text")

root = tk.Tk()
root.title("Speech to Text")

text_box = scrolledtext.ScrolledText(root, width=50, height=10)
text_box.pack(padx=10, pady=10)

button = tk.Button(root, text="Start Recording", command=start_recording)
button.pack(padx=10, pady=10)

root.mainloop()