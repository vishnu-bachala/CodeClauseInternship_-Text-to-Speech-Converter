import pyttsx3
import tkinter as tk
from tkinter import ttk

def init_tts_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    return engine, voices, rate

def set_voice(engine, voice_id):
    engine.setProperty('voice', voice_id)

def set_rate(engine, rate):
    engine.setProperty('rate', rate)

def speak_text(engine, text):
    engine.say(text)
    engine.runAndWait()

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")

        # Initialize TTS engine
        self.engine, self.voices, self.rate = init_tts_engine()

        # Text input
        self.text_label = ttk.Label(root, text="Enter text:")
        self.text_label.grid(column=0, row=0, padx=10, pady=10)
        self.text_entry = ttk.Entry(root, width=50)
        self.text_entry.grid(column=1, row=0, padx=10, pady=10)

        # Voice selection
        self.voice_label = ttk.Label(root, text="Select voice:")
        self.voice_label.grid(column=0, row=1, padx=10, pady=10)
        self.voice_var = tk.StringVar()
        self.voice_combobox = ttk.Combobox(root, textvariable=self.voice_var, state='readonly')
        self.voice_combobox['values'] = [voice.name for voice in self.voices]
        self.voice_combobox.grid(column=1, row=1, padx=10, pady=10)
        self.voice_combobox.current(0)

        # Speech rate
        self.rate_label = ttk.Label(root, text="Set rate:")
        self.rate_label.grid(column=0, row=2, padx=10, pady=10)
        self.rate_scale = ttk.Scale(root, from_=50, to=300, orient='horizontal')
        self.rate_scale.set(self.rate)
        self.rate_scale.grid(column=1, row=2, padx=10, pady=10)

        # Speak button
        self.speak_button = ttk.Button(root, text="Speak", command=self.speak)
        self.speak_button.grid(column=0, row=3, columnspan=2, pady=20)

    def speak(self):
        text = self.text_entry.get()
        selected_voice = self.voice_combobox.current()
        voice_id = self.voices[selected_voice].id
        rate = self.rate_scale.get()

        set_voice(self.engine, voice_id)
        set_rate(self.engine, rate)
        speak_text(self.engine, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
