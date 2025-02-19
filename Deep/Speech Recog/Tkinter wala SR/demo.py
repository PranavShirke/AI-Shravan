import speech_recognition as sr
import tkinter as tk
from threading import Thread

# Function to continuously listen and transcribe speech
def recognize_speech():
    global listening
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        while listening:
            try:
                status_label.config(text="Listening...", fg="blue")
                root.update()
                audio = recognizer.listen(source)  # Listen indefinitely
                text = recognizer.recognize_google(audio)  # Convert speech to text
                result_label.config(text=result_label.cget("text") + "\n" + text)  # Append text
            except sr.UnknownValueError:
                result_label.config(text=result_label.cget("text") + "\n" + "[Couldn't understand]")
            except sr.RequestError:
                result_label.config(text="Speech recognition service unavailable")
            root.update()

# Start listening in a separate thread
def start_listening():
    global listening
    if not listening:
        listening = True
        result_label.config(text="")  # Clear previous text
        status_label.config(text="Listening...", fg="blue")
        Thread(target=recognize_speech, daemon=True).start()

# Stop listening
def stop_listening():
    global listening
    listening = False
    status_label.config(text="Press Mic to Start", fg="black")

# GUI Setup
root = tk.Tk()
root.title("Live Speech Transcription")
root.geometry("500x400")

status_label = tk.Label(root, text="Press Mic to Start", font=("Arial", 14))
status_label.pack(pady=10)

mic_button = tk.Button(root, text="🎤 Start", font=("Arial", 16), command=start_listening)
mic_button.pack(pady=5)

stop_button = tk.Button(root, text="🛑 Stop", font=("Arial", 16), command=stop_listening)
stop_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=450, justify="left")
result_label.pack(pady=10)

listening = False  # Flag to control the listening loop

root.mainloop()