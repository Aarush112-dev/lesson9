from tkinter import *
from gtts import gTTS
import os
window=Tk()
window.title('Text to speech converter')
window.geometry("400x400")

def convert():
    language = "fr"
    text = enter.get()
    file = gTTS(text=text,lang=language,slow=True)
    path = "C:/Users/aarus/OneDrive/Desktop/Jetlearn/Build GUI/Lesson 9"
    os.chdir(path)
    file.save("audio.mp3")
    os.system("audio.mp3")

text_to_speech = Label(window,text="Text to Speech",font=12)
text_to_speech.pack(side=TOP)

enter = Entry(window,width=30)
enter.place(x=105,y=100,height=20)

submit = Button(window,text="Submit",width=20,command=convert)
submit.place(x=120,y=200,height=25)








window.mainloop()