import speech_recognition as sr
r = sr.Recognizer()
a = sr.Audiofile('file')
with a as source : 
    audio =r.record(source)
text = r.recognize_google(audio)

file1 = open(r"/j/Python_Tutorial/Project/AudioBook/Speech_to_text.txt","a")
file1 = writelines(text)
file1.close()
