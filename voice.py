import pyttsx3
engine = pyttsx3.init() 
       
engine.setProperty('rate', 125)     

engine.say("Hello World!")

engine.runAndWait()