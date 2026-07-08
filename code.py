import speech_recognition as sr
import pyttsx3
import ollama
import os
import sounddevice as sd
import numpy as np
import subprocess
import threading
import time

reco = sr.Recognizer()
voice = pyttsx3.init()



def chat_with_bmo(text):
    resp = ollama.chat(
        model = 'llava:7b-v1.5-q4_0',
        messages = [
            {'role': 'user', 'content': text}
        ]
    )
    return resp['message']['content']

def sy(text):
    
    voice.say(text)
    voice.runAndWait()

def wallpaper_change():
    subprocess.run([
                "gsettings",
                "set",
                "org.gnome.desktop.background",
                "picture-uri",
                "file:///home/nvidia/Pictures/bac_beran.jpg"
                ])
    time.sleep(1)
    subprocess.run([
                "gsettings",
                "set",
                "org.gnome.desktop.background",
                "picture-uri",
                "file:///home/nvidia/Pictures/pag_beran.jpg"
                ])
    time.sleep(1)

while True:
    try:
        timee = 1
        db = 16000
        audio_data = sd.rec(int(timee*db),samplerate=db,channels=1,dtype=np.int16)

        sd.wait()

        audio = sr.AudioData(audio_data.tobytes() , db,2)
        txt = reco.recognize_google(audio)
        if "hay bmo" in txt.lower():
            
            voice.say('yees')
            voice.runAndWait()
            timee = 5
            audio_data = sd.rec(int(timee*db),samplerate=db,channels=1,dtype=np.int16)
            sd.wait()
            audio = sr.AudioData(audio_data.tobytes() , db,2)
            
            txt = reco.recognize_google(audio)

            subprocess.run([
                "gsettings",
                "set",
                "org.gnome.desktop.background",
                "picture-uri",
                "file:///home/nvidia/Pictures/mtacox.jpg"
                ])
            text = chat_with_bmo(txt)
            t= threading.Thread(target= sy, args=(text,))
            t.start()
            while t.is_alive():
                
                wallpaper_change()
        
            

    except Exception as e:
        print("pizda",e)
        time.sleep(2)
